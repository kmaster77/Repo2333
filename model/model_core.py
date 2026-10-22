"""Pure-Python financial model for the B1 circular ready-mix plant.

This is the SAME model as the live-formula workbook written by build_model.py.
check_model.py recalculates the workbook with LibreOffice and compares both.

Usage
-----
    from model_core import load_inputs, run
    table = load_inputs()                       # {param: {"low":..,"base":..,"high":..,...}}
    res = run(table)                            # base case
    res = run(table, scenario="pessimistic")    # all inputs at their pessimistic column
    res = run(table, overrides={"output_steady_state": 60000})

`inputs` may be either the table returned by load_inputs() (then `scenario`
selects the column per parameter, see DIRECTION) or a flat {param: value} dict.
`overrides` is a flat {param: value} dict applied last (same as the "Override"
column on the Inputs sheet of the workbook).

Conventions (identical in the workbook)
--------------------------------------
* Real 2026 EUR, excl. VAT. Year index t = 0..10, calendar year = 2026 + t.
* t = 0 (2026): permitting year; permits/engineering capex always fall in t = 0. Plant and
  civil capex, the one-off start-up costs (pre-opening, LCA/EPD), the grant and the MIA fall
  in the build year t = first_sales_delay_yr (base: 2027). Cash flow of t = 0 is not
  discounted; year t is discounted with 1/(1+r)^t.
* t = 1..10 (2027-2036): possible operating years. First sales in t = 1 + first_sales_delay_yr
  (base: delay 1 -> build 2026-2027, first sales 2028, 9 operating years). Ramp-up: first
  operating year ramp1, second ramp2, then ramp3.
* Percent inputs are stored as numbers (8 = 8 %) and divided by 100 in formulas.
* Unlevered model (no debt, no interest). Tax = Dutch Vpb, two brackets, losses
  carried forward without time limit (the 50 % cap above EUR 1M is ignored; taxable
  profits stay far below that). MIA is modelled as an extra tax deduction in t=0
  whose size gives the stated net value at the top rate.
* Terminal value = salvage value only (plan.md 2.1), as a tax-neutral cash inflow in
  t = 10. Working capital is NOT released at the end (shown as a memo only).
* Payback (simple and discounted) uses cumulative free cash flow EXCLUDING the
  salvage value, interpolated linearly within the year.
"""
from __future__ import annotations

import csv
import math
import os
from typing import Dict, Optional

HERE = os.path.dirname(os.path.abspath(__file__))
INPUTS_CSV = os.path.join(HERE, "inputs.csv")

BASE_YEAR = 2026
N_YEARS = 10                     # operating years
YEARS = list(range(BASE_YEAR, BASE_YEAR + N_YEARS + 1))   # 2026..2036 (t = 0..10)
T = list(range(N_YEARS + 1))

SCENARIOS = ("pessimistic", "base", "optimistic")
COLS = ("low", "base", "high")

# ---------------------------------------------------------------------------
# Scenario direction per parameter.
#   "cost": higher value is worse  -> pessimistic = high, optimistic = low
#   "rev" : higher value is better -> pessimistic = low,  optimistic = high
#   anything not listed            -> "fixed": base value in all three scenarios
# Fixed on purpose: discount rate (client choice; tested separately), tax rates,
# asset lifetimes (only shift tax timing), C30/37 recipe rows (the low/high columns
# are recipe VARIANTS, not uncertainty), CO2/MKI memo rows, hybrid-option rows.
# ---------------------------------------------------------------------------
_COST = """
capex_plant_equipment capex_site_prep_civil capex_permits_engineering capex_lca_epd_one_off
capex_preopening_costs working_capital_receivable_days working_capital_inventory_days
sustaining_capex_pct_of_capex mix_circ_water_absorption mix_circ_superplasticiser_pct_binder
mix_conv_cem3b_superplasticiser_pct_binder mix_plant_avg_binder_conv mix_plant_avg_binder_circ
price_cem3b_2026_delivered cement_carbon_passthrough cem3b_slag_scarcity_uplift_2031plus
price_gravel_delivered price_sand_delivered price_rca_coarse_exworks rca_transport_distance
road_haulage_rate road_handling_per_t price_rca_fine_exworks price_superplasticiser price_water
rca_lot_testing rca_handling_prewetting electricity_use price_electricity diesel_use_plant
price_diesel staff_production_fte cost_per_fte_production staff_sga_fte cost_per_fte_sga
real_wage_growth maintenance_pct_of_capex certification_testing_fixed site_area site_lease_rate
sga_fixed_non_staff bad_debt_pct_revenue delivery_fixed_per_m3 delivery_variable_per_km_oneway
delivery_avg_distance_oneway
""".split() + [f"carbon_cost_cem3b_{y}" for y in YEARS]

_REV = """
mia_net_value_pct_eligible_capex mia_eligible_share_of_capex grant_dei_veki_first_plant
output_steady_state ramp_year1_pct_of_steady ramp_year2_pct_of_steady ramp_year3plus_pct_of_steady
circular_share_of_volume public_share_of_sales salvage_value_yr10_pct_of_plant_civil_capex
working_capital_payable_days concrete_price_passthrough_of_market_binder_cost
price_plant_avg_all_classes green_premium_public green_premium_private price_real_escalation
delivery_truck_load_avg
""".split()

DIRECTION: Dict[str, str] = {p: "cost" for p in _COST}
DIRECTION.update({p: "rev" for p in _REV})

# Column index (1=low, 2=base, 3=high) per scenario and direction
_COLMAP = {
    "cost": {"pessimistic": 3, "base": 2, "optimistic": 1},
    "rev": {"pessimistic": 1, "base": 2, "optimistic": 3},
    "fixed": {"pessimistic": 2, "base": 2, "optimistic": 2},
}


def scenario_col(param: str, scenario: str) -> int:
    return _COLMAP[DIRECTION.get(param, "fixed")][scenario]


# Option hooks: not in inputs.csv; zero by default. For Agent 7 / option sheets.
HOOKS = {
    "opt_extra_capex_y0": ("EUR", "Extra initial capex in 2026 (depreciated over plant-equipment life; no salvage)"),
    "opt_extra_revenue_per_yr": ("EUR/yr", "Extra revenue every operating year (e.g. by-product sales)"),
    "opt_extra_opex_per_yr": ("EUR/yr", "Extra fixed opex every operating year"),
    "opt_price_delta_per_m3": ("EUR/m3", "Price change on ALL concrete sold (e.g. extra premium)"),
    "opt_cost_delta_per_m3": ("EUR/m3", "Variable cost change on ALL concrete sold (negative = saving)"),
    # --- added by Agent 7 (viability options); all 0 = base case unchanged -------------
    "opt_crusher_on": ("0/1", "Option A+B: on-site rubble acceptance + crushing line (uses the hybrid_* inputs)"),
    "opt_crusher_start_year": ("year", "First calendar year of crushing (waste-processing permit)"),
    "opt_rubble_intake_tpy": ("t/yr", "Rubble intake at full plant output (scales with the ramp-up)"),
    "opt_crusher_capex": ("EUR", "Crushing-line capex, spent the year before crushing starts; depreciated over hybrid_crusher_lifetime"),
    "opt_crusher_contract_rate": ("EUR/t", "Contract (campaign) crushing rate per t rubble, when crushing is outsourced"),
    "opt_crusher_salvage_pct": ("%", "Salvage value of the crushing-line capex in 2036"),
    "opt_crusher_mia_share_pct": ("%", "Share of crushing-line capex eligible for MIA (A 1401 recycling equipment)"),
    "opt_circ_price_delta_per_m3": ("EUR/m3", "Extra price on CIRCULAR volume only, from opt_circ_delta_start_year (e.g. MKI value of a lower-CO2 binder)"),
    "opt_circ_cost_delta_per_m3": ("EUR/m3", "Extra variable cost on CIRCULAR volume only, from opt_circ_delta_start_year"),
    "opt_circ_delta_start_year": ("year", "First calendar year of the two circular-only deltas"),
}


# ---------------------------------------------------------------------------
def load_inputs(path: str = INPUTS_CSV) -> Dict[str, dict]:
    table: Dict[str, dict] = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rec = dict(row)
            for c in COLS:
                try:
                    rec[c] = float(row[c])
                except (TypeError, ValueError):
                    rec[c] = row[c]
            table[row["parameter"]] = rec
    return table


def resolve(inputs: dict, scenario: str = "base", overrides: Optional[dict] = None) -> Dict[str, float]:
    """Flat {param: value} for a scenario, with hooks and overrides applied."""
    flat: Dict[str, float] = {}
    for k, v in inputs.items():
        if isinstance(v, dict) and "base" in v:
            flat[k] = v[COLS[scenario_col(k, scenario) - 1]]
        else:
            flat[k] = v
    for h in HOOKS:
        flat.setdefault(h, 0.0)
    if overrides:
        unknown = [k for k in overrides if k not in flat]
        if unknown:
            raise KeyError(f"Unknown override parameter(s): {unknown}")
        flat.update(overrides)
    return flat


def _irr(cfs, lo=-0.99, hi=20.0, tol=1e-10):
    def npv(r):
        return sum(cf / (1 + r) ** i for i, cf in enumerate(cfs))
    f_lo, f_hi = npv(lo), npv(hi)
    if f_lo * f_hi > 0:
        return None
    for _ in range(300):
        mid = (lo + hi) / 2
        f_mid = npv(mid)
        if abs(f_mid) < tol:
            break
        if f_lo * f_mid < 0:
            hi, f_hi = mid, f_mid
        else:
            lo, f_lo = mid, f_mid
    return (lo + hi) / 2


def _payback(cum):
    """First year in which cumulative cash flow turns >= 0, interpolated."""
    for t in range(1, len(cum)):
        if cum[t - 1] < 0 <= cum[t]:
            return (t - 1) + (-cum[t - 1]) / (cum[t] - cum[t - 1])
    return None


# ---------------------------------------------------------------------------
def run(inputs: dict, overrides: Optional[dict] = None, scenario: str = "base") -> dict:
    p = resolve(inputs, scenario, overrides)
    pct = lambda k: p[k] / 100.0
    n = len(T)
    r = pct("discount_rate_real")

    # ---------------- Timing (input first_sales_delay_yr; base 1 = first sales 2028, critique M1) ---
    d = int(round(p["first_sales_delay_yr"]))     # build year index (0 = 2026)
    s0 = 1 + d                                     # first operating year index
    op = [1.0 if t >= s0 else 0.0 for t in T]
    t3 = 2 + s0                                    # third operating year (criterion 3)

    # ---------------- Capex -------------------------------------------------
    capex_plant = p["capex_plant_equipment"] * 1e6
    capex_civil = p["capex_site_prep_civil"] * 1e6
    capex_permits = p["capex_permits_engineering"] * 1e6
    capex_extra = p["opt_extra_capex_y0"]
    capex_land = p["land_purchase"] * 1e6
    capex_crusher = p["opt_crusher_capex"]
    crush_t0 = p["opt_crusher_start_year"] - BASE_YEAR           # t of first crushing year
    crush_capex_t = min(N_YEARS, max(0, int(round(crush_t0)) - 1))
    capex_initial = capex_plant + capex_civil + capex_permits + capex_extra + capex_land + capex_crusher
    physical = capex_plant + capex_civil
    startup_oneoff = p["capex_lca_epd_one_off"] + p["capex_preopening_costs"]
    grant = p["grant_dei_veki_first_plant"] * 1e6
    mia_deduction = pct("mia_eligible_share_of_capex") * physical * pct("mia_net_value_pct_eligible_capex") / pct("tax_rate_vpb_high_bracket")
    mia_crusher = pct("opt_crusher_mia_share_pct") * capex_crusher * pct("mia_net_value_pct_eligible_capex") / pct("tax_rate_vpb_high_bracket")

    # ---------------- Volume ------------------------------------------------
    ramp = [0.0] * n
    for t in T:
        if t >= s0:
            ramp[t] = pct("ramp_year1_pct_of_steady") if t == s0 else pct("ramp_year2_pct_of_steady") if t == s0 + 1 else pct("ramp_year3plus_pct_of_steady")
    vol = [p["output_steady_state"] * ramp[t] for t in T]
    vol_circ = [v * pct("circular_share_of_volume") for v in vol]
    vol_conv = [vol[t] - vol_circ[t] for t in T]

    # ---------------- Prices ------------------------------------------------
    cc = [p[f"carbon_cost_cem3b_{y}"] for y in YEARS]
    slag = [(pct("cem3b_slag_scarcity_uplift_2031plus") * p["price_cem3b_2026_delivered"] if YEARS[t] >= 2031 else 0.0) for t in T]
    cem_price = [p["price_cem3b_2026_delivered"] + pct("cement_carbon_passthrough") * (cc[t] - cc[0]) + slag[t] for t in T]
    mkt_binder_incr = [p["mix_plant_avg_binder_conv"] / 1000 * (cem_price[t] - p["price_cem3b_2026_delivered"]) for t in T]
    price_market = [p["price_plant_avg_all_classes"] * (1 + pct("price_real_escalation")) ** t
                    + pct("concrete_price_passthrough_of_market_binder_cost") * mkt_binder_incr[t]
                    + p["opt_price_delta_per_m3"] for t in T]
    premium = pct("public_share_of_sales") * pct("green_premium_public") + (1 - pct("public_share_of_sales")) * pct("green_premium_private")
    circ_flag = [1.0 if YEARS[t] >= p["opt_circ_delta_start_year"] else 0.0 for t in T]
    price_circ = [price_market[t] * (1 + premium) + circ_flag[t] * p["opt_circ_price_delta_per_m3"] for t in T]
    price_conv = list(price_market)
    rev_circ = [vol_circ[t] * price_circ[t] for t in T]
    rev_conv = [vol_conv[t] * price_conv[t] for t in T]
    rev_extra = [p["opt_extra_revenue_per_yr"] * op[t] for t in T]

    # ---------------- On-site crushing (option A+B) -------------------------
    rca_deliv = p["price_rca_coarse_exworks"] + p["rca_transport_distance"] * p["road_haulage_rate"] + p["road_handling_per_t"]
    cflag = [p["opt_crusher_on"] * op[t] * (1.0 if YEARS[t] >= p["opt_crusher_start_year"] else 0.0) for t in T]
    intake = [p["opt_rubble_intake_tpy"] * ramp[t] * cflag[t] for t in T]
    coarse_prod = [intake[t] * pct("hybrid_yield_coarse") for t in T]
    rca_need = [vol_circ[t] * p["mix_circ_rca_coarse"] / 1000 + vol_conv[t] * p["mix_conv_cem3b_rca_coarse"] / 1000 for t in T]
    rca_own = [min(coarse_prod[t], rca_need[t]) for t in T]
    rca_surplus = [coarse_prod[t] - rca_own[t] for t in T]
    cr_rev = {
        "gate_fee": [intake[t] * p["hybrid_gate_fee_received"] for t in T],
        "sand": [intake[t] * pct("hybrid_yield_sand_0_4") * p["hybrid_price_crusher_sand"] for t in T],
        "steel": [intake[t] * pct("hybrid_yield_steel") * p["hybrid_price_steel_scrap"] * pct("hybrid_steel_value_share_retained") for t in T],
        "surplus_rca": [rca_surplus[t] * p["price_rca_coarse_exworks"] for t in T],
    }
    rev_crusher = [sum(cr_rev[k][t] for k in cr_rev) for t in T]
    revenue = [rev_circ[t] + rev_conv[t] + rev_extra[t] + rev_crusher[t] for t in T]

    # ---------------- Material cost per m3 ---------------------------------
    m_circ = {
        "cement": [p["mix_plant_avg_binder_circ"] / 1000 * cem_price[t] for t in T],
        "gravel": [p["mix_circ_gravel"] / 1000 * p["price_gravel_delivered"]] * n,
        "rca": [p["mix_circ_rca_coarse"] / 1000 * rca_deliv + p["mix_circ_rca_fine"] / 1000 * p["price_rca_fine_exworks"]] * n,
        "sand": [p["mix_circ_sand"] / 1000 * p["price_sand_delivered"]] * n,
        "admix": [p["mix_plant_avg_binder_circ"] * pct("mix_circ_superplasticiser_pct_binder") * p["price_superplasticiser"]] * n,
        "water": [(p["mix_circ_water_effective"] + p["mix_circ_water_absorption"]) / 1000 * p["price_water"]] * n,
    }
    m_conv = {
        "cement": [p["mix_plant_avg_binder_conv"] / 1000 * cem_price[t] for t in T],
        "gravel": [p["mix_conv_cem3b_gravel"] / 1000 * p["price_gravel_delivered"]] * n,
        "rca": [p["mix_conv_cem3b_rca_coarse"] / 1000 * rca_deliv] * n,
        "sand": [p["mix_conv_cem3b_sand"] / 1000 * p["price_sand_delivered"]] * n,
        "admix": [p["mix_plant_avg_binder_conv"] * pct("mix_conv_cem3b_superplasticiser_pct_binder") * p["price_superplasticiser"]] * n,
        "water": [(p["mix_conv_cem3b_water_effective"] + p["mix_conv_cem3b_water_absorption"]) / 1000 * p["price_water"]] * n,
    }
    mat_circ_m3 = [sum(m_circ[k][t] for k in m_circ) for t in T]
    mat_conv_m3 = [sum(m_conv[k][t] for k in m_conv) for t in T]
    rca_qc_m3 = p["mix_circ_rca_coarse"] / 1000 * (p["rca_lot_testing"] + p["rca_handling_prewetting"])
    energy_m3 = p["electricity_use"] * p["price_electricity"] + p["diesel_use_plant"] * p["price_diesel"]
    # rates are calibrated at the reference load (10 m3); cost per m3 scales with reference / actual load (critique M2)
    delivery_m3 = ((p["delivery_fixed_per_m3"] + p["delivery_variable_per_km_oneway"] * p["delivery_avg_distance_oneway"])
                   * p["delivery_rates_reference_load"] / p["delivery_truck_load_avg"])

    # ---------------- Opex (EUR/yr) ----------------------------------------
    wage_idx = [(1 + pct("real_wage_growth")) ** t for t in T]
    opex = {
        "raw_materials": [vol_circ[t] * mat_circ_m3[t] + vol_conv[t] * mat_conv_m3[t] for t in T],
        "rca_qc": [vol_circ[t] * rca_qc_m3 for t in T],
        "energy": [vol[t] * energy_m3 for t in T],
        "delivery": [vol[t] * delivery_m3 for t in T],
        "var_delta": [vol[t] * p["opt_cost_delta_per_m3"] for t in T],
        "circ_delta": [vol_circ[t] * circ_flag[t] * p["opt_circ_cost_delta_per_m3"] for t in T],
        "cr_rca_credit": [-rca_own[t] * rca_deliv for t in T],
        "cr_contaminants": [intake[t] * pct("hybrid_yield_contaminants") * p["hybrid_cost_contaminant_disposal"] for t in T],
        "cr_diesel": [intake[t] * p["hybrid_crusher_diesel"] * p["price_diesel"] for t in T],
        "cr_wear": [intake[t] * p["hybrid_crusher_wear"] for t in T],
        "cr_washing": [coarse_prod[t] * p["hybrid_rca_washing_screening"] for t in T],
        "cr_contract": [intake[t] * p["opt_crusher_contract_rate"] for t in T],
        "bad_debt": [revenue[t] * pct("bad_debt_pct_revenue") for t in T],
        "staff_prod": [op[t] * p["staff_production_fte"] * p["cost_per_fte_production"] * wage_idx[t] for t in T],
        "maintenance": [op[t] * pct("maintenance_pct_of_capex") * physical for t in T],
        "certification": [op[t] * p["certification_testing_fixed"] for t in T],
        "site_lease": [op[t] * p["site_area"] * p["site_lease_rate"] for t in T],
        "staff_sga": [op[t] * p["staff_sga_fte"] * p["cost_per_fte_sga"] * wage_idx[t] for t in T],
        "sga_other": [op[t] * p["sga_fixed_non_staff"] for t in T],
        "extra_fixed": [op[t] * p["opt_extra_opex_per_yr"] for t in T],
        "cr_staff": [cflag[t] * p["hybrid_crusher_staff_fte"] * p["cost_per_fte_production"] * wage_idx[t] for t in T],
        "cr_maintenance": [cflag[t] * pct("hybrid_crusher_maintenance_pct_capex") * capex_crusher for t in T],
        "cr_certification": [cflag[t] * p["hybrid_brl2506_certification"] for t in T],
        "cr_site": [cflag[t] * p["hybrid_extra_site_area"] * p["site_lease_rate"] for t in T],
        "startup_oneoff": [startup_oneoff if t == d else 0.0 for t in T],
    }
    VARIABLE = ("raw_materials", "rca_qc", "energy", "delivery", "var_delta", "circ_delta", "cr_rca_credit",
                "cr_contaminants", "cr_diesel", "cr_wear", "cr_washing", "cr_contract", "bad_debt")
    FIXED = ("staff_prod", "maintenance", "certification", "site_lease", "staff_sga", "sga_other", "extra_fixed",
             "cr_staff", "cr_maintenance", "cr_certification", "cr_site")
    CR_VAR = ("cr_rca_credit", "cr_contaminants", "cr_diesel", "cr_wear", "cr_washing", "cr_contract")
    CR_FIX = ("cr_staff", "cr_maintenance", "cr_certification", "cr_site")
    opex_var = [sum(opex[k][t] for k in VARIABLE) for t in T]
    opex_fixed = [sum(opex[k][t] for k in FIXED) for t in T]
    opex_total = [opex_var[t] + opex_fixed[t] + opex["startup_oneoff"][t] for t in T]
    ebitda = [revenue[t] - opex_total[t] for t in T]
    crusher_net = [rev_crusher[t] - sum(opex[k][t] for k in CR_VAR) - sum(opex[k][t] for k in CR_FIX) for t in T]

    # ---------------- Depreciation -----------------------------------------
    def sl(amount, life, start):
        return [amount / life if start <= t < start + life else 0.0 for t in T]
    dep_plant = sl(capex_plant + capex_extra, p["lifetime_plant_equipment"], s0)
    dep_civil = sl(capex_civil, p["lifetime_civil_works"], s0)
    dep_permits = sl(capex_permits, p["lifetime_permits_engineering"], s0)
    dep_crusher = sl(capex_crusher, p["hybrid_crusher_lifetime"], crush_capex_t + 1)
    sust = [op[t] * pct("sustaining_capex_pct_of_capex") * physical for t in T]
    dep_sust = [sum(sust[: t + 1]) / p["lifetime_plant_equipment"] for t in T]
    da = [dep_plant[t] + dep_civil[t] + dep_permits[t] + dep_crusher[t] + dep_sust[t] for t in T]
    ebit = [ebitda[t] - da[t] for t in T]
    grant_inc = [grant if t == d else 0.0 for t in T]
    pbt = [ebit[t] + grant_inc[t] for t in T]

    # ---------------- Tax ---------------------------------------------------
    mia = [(mia_deduction if t == d else 0.0) + (mia_crusher if t == crush_capex_t else 0.0) for t in T]
    ti = [pbt[t] - mia[t] for t in T]
    pool, taxable, tax = [0.0] * n, [0.0] * n, [0.0] * n
    prev = 0.0
    lim, rl, rh = p["tax_vpb_low_bracket_limit"], pct("tax_rate_vpb_low_bracket"), pct("tax_rate_vpb_high_bracket")
    for t in T:
        taxable[t] = max(0.0, ti[t] - prev)
        pool[t] = max(0.0, prev - ti[t])
        tax[t] = min(taxable[t], lim) * rl + max(0.0, taxable[t] - lim) * rh
        prev = pool[t]
    net_income = [pbt[t] - tax[t] for t in T]

    # ---------------- Working capital & cash flow --------------------------
    wc_rec = [revenue[t] * p["working_capital_receivable_days"] / 365 for t in T]
    wc_inv = [opex["raw_materials"][t] * p["working_capital_inventory_days"] / 365 for t in T]
    wc_pay = [opex["raw_materials"][t] * p["working_capital_payable_days"] / 365 for t in T]
    wc = [wc_rec[t] + wc_inv[t] - wc_pay[t] for t in T]
    d_wc = [wc[t] - (wc[t - 1] if t > 0 else 0.0) for t in T]
    capex_cf = [(capex_permits if t == 0 else 0.0) + (capex_plant + capex_civil + capex_extra + capex_land if t == d else 0.0)
                + (capex_crusher if t == crush_capex_t else 0.0) for t in T]
    salvage = [(pct("salvage_value_yr10_pct_of_plant_civil_capex") * physical + pct("opt_crusher_salvage_pct") * capex_crusher)
               if t == N_YEARS else 0.0 for t in T]
    fcf = [ebitda[t] + grant_inc[t] - tax[t] - d_wc[t] - capex_cf[t] - sust[t] + salvage[t] for t in T]
    fcf_x = [fcf[t] - salvage[t] for t in T]
    df = [1 / (1 + r) ** t for t in T]
    dcf = [fcf[t] * df[t] for t in T]
    cum = [sum(fcf[: t + 1]) for t in T]
    cum_x = [sum(fcf_x[: t + 1]) for t in T]
    cum_dx = [sum(fcf_x[i] * df[i] for i in range(t + 1)) for t in T]

    npv = sum(dcf)
    irr = _irr(fcf)
    payback = _payback(cum_x)
    dpayback = _payback(cum_dx)
    funding_need = max(0.0, -min(cum))
    npv_wc_memo = npv + wc[-1] * df[-1]

    # Break-even steady-state volume (EBITDA = 0) in the third operating year.
    # Crusher net result and hook revenue are treated as fixed amounts (memo KPI).
    cr_var3 = sum(opex[k][t3] for k in CR_VAR)
    conc_rev3 = revenue[t3] - rev_extra[t3] - rev_crusher[t3]
    unit_contrib = conc_rev3 / vol[t3] - (opex_var[t3] - cr_var3) / vol[t3] if vol[t3] else float("nan")
    be_vol_ebitda = (opex_fixed[t3] - rev_extra[t3] - crusher_net[t3]) / unit_contrib if unit_contrib > 0 else None

    kpis = {
        "npv": npv, "irr": irr, "payback": payback, "discounted_payback": dpayback,
        "ebitda_y3": ebitda[t3], "ebitda_y3_year": YEARS[t3], "funding_need": funding_need, "capex_initial": capex_initial,
        "npv_pct_of_capex": npv / capex_initial if capex_initial else None,
        "npv_incl_wc_release_memo": npv_wc_memo, "be_volume_ebitda_y3": be_vol_ebitda,
        "unit_contribution_y3": unit_contrib, "revenue_y3": revenue[t3],
    }
    years = {
        "year": YEARS, "t": T, "ramp": ramp, "volume": vol, "volume_circ": vol_circ, "volume_conv": vol_conv,
        "carbon_cost_cem3b": cc, "slag_uplift": slag, "cement_price": cem_price, "market_binder_increase_m3": mkt_binder_incr,
        "price_market": price_market, "price_circ": price_circ, "price_conv": price_conv,
        "revenue_circ": rev_circ, "revenue_conv": rev_conv, "revenue_extra": rev_extra,
        "revenue_crusher": rev_crusher, **{f"crusher_rev_{k}": v for k, v in cr_rev.items()},
        "rubble_intake": intake, "rca_own": rca_own, "rca_surplus": rca_surplus, "crusher_net": crusher_net,
        "revenue": revenue,
        "mat_circ_m3": mat_circ_m3, "mat_conv_m3": mat_conv_m3,
        **{f"opex_{k}": v for k, v in opex.items()},
        "opex_variable": opex_var, "opex_fixed": opex_fixed, "opex_total": opex_total, "ebitda": ebitda,
        "dep_plant": dep_plant, "dep_civil": dep_civil, "dep_permits": dep_permits, "dep_crusher": dep_crusher,
        "dep_sustaining": dep_sust, "da": da,
        "ebit": ebit, "grant_income": grant_inc, "pbt": pbt, "mia_deduction": mia, "taxable_before_losses": ti,
        "loss_pool": pool, "taxable": taxable, "tax": tax, "net_income": net_income,
        "wc_receivables": wc_rec, "wc_inventory": wc_inv, "wc_payables": wc_pay, "wc": wc, "delta_wc": d_wc,
        "capex": capex_cf, "sustaining_capex": sust, "salvage": salvage, "fcf": fcf, "cum_fcf": cum,
        "discount_factor": df, "dcf": dcf, "cum_fcf_excl_salvage": cum_x, "cum_dcf_excl_salvage": cum_dx,
    }
    unit = {
        "m_circ": m_circ, "m_conv": m_conv, "rca_delivered_per_t": rca_deliv, "rca_qc_m3": rca_qc_m3,
        "energy_m3": energy_m3, "delivery_m3": delivery_m3, "premium_blended": premium,
    }
    return {"kpis": kpis, "years": years, "unit": unit, "params": p}


# ---------------------------------------------------------------------------
# Sensitivity definitions (one at a time). Each driver = a GROUP of parameters
# moved together to their low or high input column.
# ---------------------------------------------------------------------------
CARBON = [f"carbon_cost_cem3b_{y}" for y in YEARS]
SENSITIVITIES = [
    # name, params, is a "main driver" for criterion 4
    ("Green premium (public & private)", ["green_premium_public", "green_premium_private"], True),
    ("Average selling price (EUR 115-155/m3)", ["price_plant_avg_all_classes"], False),
    ("Recycled aggregate price, ex-works (EUR 10-25/t)", ["price_rca_coarse_exworks"], True),
    ("Transport distance (delivery 10-35 km + RCA haul 15-50 km)", ["delivery_avg_distance_oneway", "rca_transport_distance"], True),
    ("Concrete delivery distance (10-35 km)", ["delivery_avg_distance_oneway"], False),
    ("RCA haul distance (15-50 km)", ["rca_transport_distance"], False),
    ("Cement price + ETS/CBAM path", ["price_cem3b_2026_delivered"] + CARBON, True),
    ("Cement price 2026 (EUR 95-130/t)", ["price_cem3b_2026_delivered"], False),
    ("ETS/CBAM carbon cost path only", CARBON, False),
    ("Plant utilisation (50k-90k m3/yr)", ["output_steady_state"], True),
    ("Ramp-up speed (yr1-3)", ["ramp_year1_pct_of_steady", "ramp_year2_pct_of_steady", "ramp_year3plus_pct_of_steady"], False),
    ("Capex (plant, civil, permits)", ["capex_plant_equipment", "capex_site_prep_civil", "capex_permits_engineering"], True),
    ("Discount rate (6-10%)", ["discount_rate_real"], False),
    ("Gravel price (EUR 25-40/t)", ["price_gravel_delivered"], False),
    ("Sand price (EUR 14-25/t)", ["price_sand_delivered"], False),
    ("Delivery cost rates (fixed + per km)", ["delivery_fixed_per_m3", "delivery_variable_per_km_oneway"], False),
    ("Truck-mixer load (8-10 m3 per trip)", ["delivery_truck_load_avg"], False),
    ("Production staff (FTE x cost)", ["staff_production_fte", "cost_per_fte_production"], False),
    ("SG&A (staff + non-staff)", ["staff_sga_fte", "cost_per_fte_sga", "sga_fixed_non_staff"], False),
    ("Site lease (area x rate)", ["site_area", "site_lease_rate"], False),
    ("Circular share of volume (40-80%)", ["circular_share_of_volume"], False),
    ("Grant DEI+/VEKI (EUR 0-1.5M)", ["grant_dei_veki_first_plant"], False),
    ("Working capital days", ["working_capital_receivable_days", "working_capital_payable_days", "working_capital_inventory_days"], False),
    ("Salvage value (10-40% of capex)", ["salvage_value_yr10_pct_of_plant_civil_capex"], False),
    ("Maintenance (1.5-4% of capex)", ["maintenance_pct_of_capex"], False),
]


def _col_overrides(table, params, col):
    return {k: table[k][col] for k in params}


def sensitivity(table: dict, base_overrides: Optional[dict] = None) -> list:
    """One-at-a-time: each group set to its LOW and HIGH input column. Returns NPVs."""
    base = run(table, base_overrides)["kpis"]["npv"]
    out = []
    for name, params, main in SENSITIVITIES:
        res = {}
        for col in ("low", "high"):
            ov = dict(base_overrides or {})
            ov.update(_col_overrides(table, params, col))
            res[col] = run(table, ov)["kpis"]["npv"]
        # pessimistic column for this group (by DIRECTION of first param; discount rate: high is worse)
        d = DIRECTION.get(params[0], "cost" if params[0] == "discount_rate_real" else "fixed")
        pess_col = "high" if d == "cost" else "low"
        out.append({"name": name, "params": params, "main_driver": main, "npv_base": base,
                    "npv_low_input": res["low"], "npv_high_input": res["high"],
                    "npv_pessimistic": res[pess_col], "pessimistic_column": pess_col,
                    "swing": abs(res["high"] - res["low"])})
    return out


def criterion4(table: dict) -> list:
    return [s for s in sensitivity(table) if s["main_driver"]]


def solve(table: dict, param: str, target_npv: float = 0.0, lo: float = None, hi: float = None,
          overrides: Optional[dict] = None, scenario: str = "base"):
    """Bisection: value of `param` that gives NPV = target (None if not bracketed)."""
    def f(x):
        ov = dict(overrides or {}); ov[param] = x
        return run(table, ov, scenario)["kpis"]["npv"] - target_npv
    flo, fhi = f(lo), f(hi)
    if flo * fhi > 0:
        return None
    for _ in range(100):
        mid = (lo + hi) / 2
        fm = f(mid)
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def viability(table: dict, scenario: str = "base") -> dict:
    k = run(table, scenario=scenario)["kpis"]
    c4 = criterion4(table)
    n_pass4 = sum(1 for s in c4 if s["npv_pessimistic"] > 0)
    c1 = k["npv"] > 0
    c2 = k["payback"] is not None and k["payback"] < 7
    c3 = k["ebitda_y3"] > 0
    c4ok = n_pass4 >= 2
    if c1 and c2 and c3 and c4ok:
        verdict = "VIABLE"
    elif (c1 and c2 and c3 and not c4ok) or (-0.10 * k["capex_initial"] <= k["npv"] <= 0):
        verdict = "BORDERLINE"
    else:
        verdict = "NOT VIABLE"
    return {"c1_npv_pos": c1, "c2_payback_lt7": c2, "c3_ebitda_y3_pos": c3, "c4_n_pass": n_pass4,
            "c4_pass": c4ok, "verdict": verdict, "kpis": k, "c4_detail": c4}


if __name__ == "__main__":
    tab = load_inputs()
    for sc in SCENARIOS:
        k = run(tab, scenario=sc)["kpis"]
        print(sc, {a: (round(b, 4) if isinstance(b, float) else b) for a, b in k.items()})
    v = viability(tab)
    print(v["verdict"], v["c1_npv_pos"], v["c2_payback_lt7"], v["c3_ebitda_y3_pos"], v["c4_n_pass"])
