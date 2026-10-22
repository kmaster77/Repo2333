"""Viability options (Agent 7) on top of model_core.py.

    python3 model/options.py          # prints the option table, writes model/results_options.json

Every option is a set of overrides for model_core.run() (all live in the Excel workbook through the
option selector Inputs!I3 and the Opt_Overview sheet), except O6 (asset-light), which is a small
separate model: run_asset_light() here and the live sheet Opt_AssetLight in the workbook.

Assumption IDs (A-OPT-xx) and sources (OPT-xx) are in research/assumptions_options.md and
research/sources_options.md. The base case (no overrides) is NOT changed by anything in this file.
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import model_core as mc  # noqa: E402

OUT_JSON = os.path.join(HERE, "results_options.json")

DELAY = {"opt_start_delay": 1}                                   # A-OPT-01

# On-site crushing, partner variant (contract crushing on our site)  A-OPT-02/03/05
CRUSH_PARTNER = {"opt_crusher_on": 1, "opt_crusher_start_year": 2029, "opt_rubble_intake_tpy": 40500,
                 "opt_crusher_capex": 400000, "opt_crusher_salvage_pct": 10, "opt_crusher_mia_share_pct": 0,
                 "opt_crusher_contract_rate": 7.5, "hybrid_crusher_diesel": 0, "hybrid_crusher_wear": 0,
                 "hybrid_crusher_staff_fte": 1}
# On-site crushing, own mobile line                                  A-OPT-02/03/04
CRUSH_OWN = {"opt_crusher_on": 1, "opt_crusher_start_year": 2029, "opt_rubble_intake_tpy": 40500,
             "opt_crusher_capex": 2000000, "opt_crusher_salvage_pct": 10, "opt_crusher_mia_share_pct": 100}
# Acquisition of an existing plant                                   A-OPT-06..10
ACQ = {"capex_plant_equipment": 3.3, "capex_site_prep_civil": 0.2, "capex_permits_engineering": 0.2,
       "capex_preopening_costs": 100000, "ramp_year1_pct_of_steady": 55, "ramp_year2_pct_of_steady": 85,
       "maintenance_pct_of_capex": 3.5, "salvage_value_yr10_pct_of_plant_civil_capex": 15}
OFFTAKE = {"ramp_year1_pct_of_steady": 75, "ramp_year2_pct_of_steady": 95, "opt_price_delta_per_m3": -1.0}   # A-OPT-11/12
BINDER = {"opt_circ_price_delta_per_m3": 1.5, "opt_circ_cost_delta_per_m3": 1.5, "opt_circ_delta_start_year": 2029,
          "opt_extra_capex_y0": 150000, "opt_extra_opex_per_yr": 40000}                                      # A-OPT-13..15
SUBSIDY = {"grant_dei_veki_first_plant": 1.0, "mia_eligible_share_of_capex": 50}                               # A-OPT-16
SCALE90 = {"output_steady_state": 90000, "staff_production_fte": 8, "delivery_avg_distance_oneway": 22}       # A-OPT-17
SCALE100 = {"output_steady_state": 100000, "staff_production_fte": 9, "delivery_avg_distance_oneway": 23}     # A-OPT-17
URBAN = {"delivery_avg_distance_oneway": 15, "site_lease_rate": 15, "price_gravel_delivered": 37}             # A-OPT-18


def merge(*ds):
    out = {}
    for d in ds:
        out.update(d)
    return out


# key, short name, description, overrides (None = separate model), who must act, feasibility 1-5
OPTIONS = [
    ("O0", "Corrected base: first sales 2028",
     "Same plant, but permit + build take until end 2027; first sales 2028 (9 operating years to 2036).",
     merge(DELAY), "Founders (planning)", 5),
    ("O1", "A+B own mobile crushing line",
     "O0 + own mobile crusher on a 1 ha extension: takes 40.5 kt/yr clean rubble for a gate fee, makes own RCA, sells sand and steel. Crushing from 2029 (waste permit).",
     merge(DELAY, CRUSH_OWN), "Founders + province (waste permit) + demolition suppliers", 3),
    ("O2", "A+B with demolition partner (contract crushing)",
     "O0 + a demolition firm delivers rubble (gate fee by contract) and crushes it on our site in campaigns at a fixed rate per tonne. Little own capex.",
     merge(DELAY, CRUSH_PARTNER), "Demolition partner + province (waste permit)", 3),
    ("O3", "Acquire and convert an existing plant",
     "Buy a running ready-mix plant (permit, customers, staff) in Zuid-Holland and convert it (RCA bins, covered store, probes). Sales from 2027.",
     merge(ACQ), "Founders + seller (independent or divesting group) + bank", 3),
    ("O4", "Offtake / framework contracts (MKI tenders)",
     "O0 + framework contracts with a public client / GWW contractor before the plant opens: faster ramp-up (75%/95%) at a ~3% framework discount on that volume.",
     merge(DELAY, OFFTAKE), "Contractors, Rijkswaterstaat / municipalities", 3),
    ("O5", "Lower-CO2 binder product (from 2029)",
     "O0 + circular mix with a lower-CO2 binder (activated cement paste / ACT-type, ~-30% CO2 vs CEM III/B). Earns MKI value in tenders, but costs more and needs certification.",
     merge(DELAY, BINDER), "Binder supplier (everox, Ecocem, ENCI) + certification body", 2),
    ("O6", "Asset-light: licence + RCA service (archetype D)",
     "No plant. Sell certified circular mix designs, RCA supply and MKI/EPD documentation to 2-8 existing plants for a fee per m3.",
     None, "Founders + licensee plants", 2),
    ("O7", "Maximum realistic subsidies",
     "O0 + DEI+ grant EUR 1.0M (instead of 0.4M) + 50% of plant capex eligible for MIA.",
     merge(DELAY, SUBSIDY), "RVO", 2),
    ("O8", "Bigger plant: 100k m3/yr",
     "O0 at 100k m3/yr (market SOM high case): +2 production FTE, larger delivery radius (23 km average).",
     merge(DELAY, SCALE100), "Founders + anchor customers", 2),
    ("O9", "Urban site closer to demand (truck-fed)",
     "O0 on an inland site in the city: shorter delivery (15 km) but higher lease and gravel by truck (+EUR 5/t).",
     merge(DELAY, URBAN), "Founders + municipality", 3),
    ("P1", "Package 1: acquire + partner crushing + frameworks",
     "O3 + O2 crushing from 2029 + O4 framework contracts (ramp 75%/95%, -EUR 1/m3).",
     merge(ACQ, CRUSH_PARTNER, OFFTAKE), "Founders, seller, demolition partner, contractors", 3),
    ("P2", "Package 2: P1 + scale to 90k m3/yr",
     "P1 with a second framework contract: 90k m3/yr, +1 production FTE, 22 km average delivery.",
     merge(ACQ, CRUSH_PARTNER, OFFTAKE, SCALE90), "As P1 + second anchor customer", 2),
]
OPT_BY_KEY = {o[0]: o for o in OPTIONS}
MODEL_OPTIONS = [o for o in OPTIONS if o[3] is not None]          # in the workbook selector (1..N)


# ---------------------------------------------------------------------------
# O6 asset-light sub-model (same conventions: real 2026 EUR, t = 0..10, Vpb, salvage only)
# ---------------------------------------------------------------------------
AL_INPUTS = [
    # key, label, unit, low, base, high, ID
    ("al_licensees_max", "Licensee plants at maturity (+1 per year from 2027)", "plants", 2, 4, 8, "A-OPT-19"),
    ("al_circ_volume_per_licensee", "Circular volume per licensee plant", "m3/yr", 8000, 15000, 25000, "A-OPT-19"),
    ("al_fee_per_m3", "Licence / service fee", "EUR/m3", 1.0, 2.0, 3.5, "A-OPT-20"),
    ("al_rca_t_per_m3", "RCA supplied per m3", "t/m3", 0.33, 0.56, 0.56, "inputs mix_circ_rca_coarse"),
    ("al_rca_margin_per_t", "Brokerage margin on RCA", "EUR/t", 0.5, 1.5, 3.0, "A-OPT-21"),
    ("al_services_rev", "LCA/EPD/MKI project services (from 2028)", "EUR/yr", 0, 100000, 200000, "A-OPT-22"),
    ("al_fte", "Team (technologist, LCA, sales, logistics)", "FTE", 3, 4, 5, "A-OPT-23"),
    ("al_cost_per_fte", "Cost per FTE", "EUR/yr", 80000, 90000, 110000, "inputs cost_per_fte_sga"),
    ("al_overhead", "Other overhead (office, IT, insurance, LCA software)", "EUR/yr", 100000, 150000, 200000, "A-OPT-23"),
    ("al_startup_t0", "Mix development, trial mixes, EPDs, contracts (2026, expensed)", "EUR", 250000, 350000, 500000, "A-OPT-23"),
    ("al_capex_t0", "Lab equipment, software (2026)", "EUR", 100000, 200000, 300000, "A-OPT-23"),
    ("al_capex_life", "Depreciation life", "yr", 5, 5, 5, "ASSUMPTION"),
    ("al_receivable_days", "Receivable days", "d", 45, 60, 75, "inputs working_capital_receivable_days"),
]
AL_BASE = {k: b for k, _, _, _, b, _, _ in AL_INPUTS}


def run_asset_light(over=None, table=None):
    a = dict(AL_BASE)
    a.update(over or {})
    tab = table or mc.load_inputs()
    p = mc.resolve(tab)
    r = p["discount_rate_real"] / 100
    T = mc.T
    lic = [0.0 if t == 0 else min(a["al_licensees_max"], t) for t in T]
    vol = [lic[t] * a["al_circ_volume_per_licensee"] for t in T]
    rev_fee = [vol[t] * a["al_fee_per_m3"] for t in T]
    rev_rca = [vol[t] * a["al_rca_t_per_m3"] * a["al_rca_margin_per_t"] for t in T]
    rev_srv = [a["al_services_rev"] if t >= 2 else 0.0 for t in T]
    revenue = [rev_fee[t] + rev_rca[t] + rev_srv[t] for t in T]
    staff = [a["al_fte"] * a["al_cost_per_fte"] if t >= 1 else 0.0 for t in T]
    over_ = [a["al_overhead"] if t >= 1 else 0.0 for t in T]
    startup = [a["al_startup_t0"] if t == 0 else 0.0 for t in T]
    ebitda = [revenue[t] - staff[t] - over_[t] - startup[t] for t in T]
    capex = [a["al_capex_t0"] if t == 0 else 0.0 for t in T]
    dep = [a["al_capex_t0"] / a["al_capex_life"] if 1 <= t <= a["al_capex_life"] else 0.0 for t in T]
    ebit = [ebitda[t] - dep[t] for t in T]
    lim, rl, rh = p["tax_vpb_low_bracket_limit"], p["tax_rate_vpb_low_bracket"] / 100, p["tax_rate_vpb_high_bracket"] / 100
    tax, prev = [], 0.0
    for t in T:
        taxable = max(0.0, ebit[t] - prev)
        prev = max(0.0, prev - ebit[t])
        tax.append(min(taxable, lim) * rl + max(0.0, taxable - lim) * rh)
    wc = [revenue[t] * a["al_receivable_days"] / 365 for t in T]
    dwc = [wc[t] - (wc[t - 1] if t else 0.0) for t in T]
    fcf = [ebitda[t] - tax[t] - dwc[t] - capex[t] for t in T]
    df = [1 / (1 + r) ** t for t in T]
    cum = [sum(fcf[: t + 1]) for t in T]
    npv = sum(fcf[t] * df[t] for t in T)
    k = {"npv": npv, "irr": mc._irr(fcf), "payback": mc._payback(cum), "discounted_payback":
         mc._payback([sum(fcf[i] * df[i] for i in range(t + 1)) for t in T]),
         "ebitda_y3": ebitda[3], "ebitda_y3_year": 2029, "funding_need": max(0.0, -min(cum)),
         "capex_initial": a["al_capex_t0"], "npv_pct_of_capex": npv / a["al_capex_t0"], "revenue_y3": revenue[3]}
    years = {"year": mc.YEARS, "licensees": lic, "volume": vol, "rev_fee": rev_fee, "rev_rca": rev_rca, "rev_services": rev_srv,
             "revenue": revenue, "staff": staff, "overhead": over_, "startup": startup, "ebitda": ebitda, "dep": dep,
             "ebit": ebit, "tax": tax, "wc": wc, "delta_wc": dwc, "capex": capex, "fcf": fcf, "cum_fcf": cum, "df": df}
    return {"kpis": k, "years": years, "params": a}


def al_breakeven_licensees(table=None):
    """Licensee plants at maturity needed for NPV = 0 (other AL inputs at base)."""
    for n in range(1, 41):
        if run_asset_light({"al_licensees_max": n}, table)["kpis"]["npv"] > 0:
            return n
    return None


# ---------------------------------------------------------------------------
# Criterion 4 for an option: the 6 main drivers at their pessimistic value, one at a time.
# A parameter the option overrides is moved by the same RATIO (pessimistic / base input) as in the
# base test, so the stress is relative to the option's own value. For options with on-site crushing
# the "RCA price" driver is replaced by its A+B analogue, the gate fee (low = -2 EUR/t), as plan.md
# names the gate fee as a main driver.
# ---------------------------------------------------------------------------
def criterion4_option(table, ov):
    out = []
    for name, params, main in mc.SENSITIVITIES:
        if not main:
            continue
        if ov.get("opt_crusher_on") and params == ["price_rca_coarse_exworks"]:
            name, params = "Gate fee received (A+B analogue of RCA price)", ["hybrid_gate_fee_received"]
        d = mc.DIRECTION.get(params[0], "fixed")
        col = "high" if d == "cost" else "low"
        if params == ["hybrid_gate_fee_received"]:
            col = "low"
        o = dict(ov)
        for q in params:
            b, x = table[q]["base"], table[q][col]
            o[q] = ov[q] * x / b if (q in ov and b) else x
        if params[0] == "capex_plant_equipment" and ov.get("opt_crusher_capex"):
            o["opt_crusher_capex"] = ov["opt_crusher_capex"] * table["capex_plant_equipment"]["high"] / table["capex_plant_equipment"]["base"]
        npv = mc.run(table, o)["kpis"]["npv"]
        out.append({"name": name, "params": params, "pessimistic_column": col, "npv_pessimistic": npv})
    return out


def criteria(k, c4):
    c1 = k["npv"] > 0
    c2 = k["payback"] is not None and k["payback"] < 7
    c3 = k["ebitda_y3"] > 0
    n4 = sum(1 for s in c4 if s["npv_pessimistic"] > 0) if c4 is not None else None
    c4ok = (n4 or 0) >= 2
    if c1 and c2 and c3 and c4ok:
        v = "VIABLE"
    elif (c1 and c2 and c3) or (-0.10 * k["capex_initial"] <= k["npv"] <= 0):
        v = "BORDERLINE"
    else:
        v = "NOT VIABLE"
    return {"c1": c1, "c2": c2, "c3": c3, "c4_n_pass": n4, "c4": c4ok, "n_pass": sum([c1, c2, c3, c4ok]), "verdict": v}


def al_criterion4(table):
    """Asset-light robustness: 6 own drivers at their pessimistic value (the plant drivers do not apply)."""
    drivers = [("Licensee plants (2)", {"al_licensees_max": 2}), ("Volume per licensee (8k m3)", {"al_circ_volume_per_licensee": 8000}),
               ("Fee (EUR 1/m3)", {"al_fee_per_m3": 1.0}), ("RCA margin (EUR 0.5/t)", {"al_rca_margin_per_t": 0.5}),
               ("Services revenue (0)", {"al_services_rev": 0}), ("Team cost (5 FTE x 110k)", {"al_fte": 5, "al_cost_per_fte": 110000})]
    return [{"name": n, "params": list(o), "pessimistic_column": "low/high", "npv_pessimistic": run_asset_light(o, table)["kpis"]["npv"]}
            for n, o in drivers]


# ---------------------------------------------------------------------------
# Policy dependence
# ---------------------------------------------------------------------------
STD_AGG_T_PER_M3 = None  # set from inputs (gravel + sand of the standard mix, t/m3)


def levy_overrides(table, ov, L):
    """Levy L EUR/t on primary gravel and sand for ALL producers. Our costs rise by L per t used;
    the market price rises by the pass-through share x the standard mix's extra cost."""
    p = mc.resolve(table, overrides=ov)
    std_t = (p["mix_conv_cem3b_gravel"] + p["mix_conv_cem3b_sand"]) / 1000
    o = dict(ov)
    o["price_gravel_delivered"] = p["price_gravel_delivered"] + L
    o["price_sand_delivered"] = p["price_sand_delivered"] + L
    o["opt_price_delta_per_m3"] = p["opt_price_delta_per_m3"] + p["concrete_price_passthrough_of_market_binder_cost"] / 100 * std_t * L
    return o


def solve_fn(f, lo, hi):
    flo, fhi = f(lo), f(hi)
    if flo * fhi > 0:
        return None
    for _ in range(80):
        m = (lo + hi) / 2
        fm = f(m)
        if flo * fm <= 0:
            hi = m
        else:
            lo, flo = m, fm
    return (lo + hi) / 2


def policy_tests(table, key, ov):
    npv = lambda o: mc.run(table, o)["kpis"]["npv"]
    res = {"option": key}
    res["levy_for_npv0_eur_per_t"] = solve_fn(lambda L: npv(levy_overrides(table, ov, L)), 0, 300)
    res["npv_levy_5"] = npv(levy_overrides(table, ov, 5))
    res["public_premium_for_npv0_pct"] = solve_fn(lambda x: npv(dict(ov, green_premium_public=x)), -20, 300)
    res["circ_mki_value_for_npv0_eur_m3"] = solve_fn(
        lambda x: npv(dict(ov, opt_circ_price_delta_per_m3=x, opt_circ_delta_start_year=ov.get("opt_circ_delta_start_year", 2028))), 0, 100)
    hi_c = {f"carbon_cost_cem3b_{y}": table[f"carbon_cost_cem3b_{y}"]["high"] for y in mc.YEARS}
    res["npv_high_ets_path"] = npv(dict(ov, **hi_c))
    res["npv_landfill_81"] = npv(dict(ov, hybrid_cost_contaminant_disposal=160))
    res["npv_gate_fee_15"] = npv(dict(ov, hybrid_gate_fee_received=15))
    res["price_for_npv0_eur_m3"] = solve_fn(lambda x: npv(dict(ov, price_plant_avg_all_classes=x)), 80, 250)
    res["volume_for_npv0_m3"] = solve_fn(lambda x: npv(dict(ov, output_steady_state=x)), 20000, 240000)
    return res


def kfmt(k):
    return {a: k.get(a) for a in ("npv", "irr", "payback", "discounted_payback", "ebitda_y3", "ebitda_y3_year",
                                  "funding_need", "capex_initial", "npv_pct_of_capex")}


def evaluate(table=None):
    table = table or mc.load_inputs()
    rows = {}
    base_k = mc.run(table)["kpis"]
    rows["BASE"] = {"name": "Base case as gated (sales 2027)", "overrides": {}, "kpis": kfmt(base_k),
                    "c4": [{"name": s["name"], "npv_pessimistic": s["npv_pessimistic"]} for s in mc.criterion4(table)]}
    rows["BASE"]["criteria"] = criteria(base_k, rows["BASE"]["c4"])
    for key, name, desc, ov, who, feas in OPTIONS:
        if ov is None:
            r = run_asset_light(table=table)
            c4 = al_criterion4(table)
        else:
            r = mc.run(table, ov)
            c4 = criterion4_option(table, ov)
        k = r["kpis"]
        rows[key] = {"name": name, "description": desc, "overrides": ov, "who": who, "feasibility": feas,
                     "kpis": kfmt(k), "c4": c4, "criteria": criteria(k, c4),
                     "ebitda_by_year": r["years"]["ebitda"], "fcf_by_year": r["years"]["fcf"]}
        if ov is not None:
            y = r["years"]
            rows[key]["crusher_net_y5"] = y["crusher_net"][5]
            rows[key]["volume_y5"] = y["volume"][5]
    rows["O6"]["breakeven_licensees"] = al_breakeven_licensees(table)
    # low / high range per option for the most uncertain option-specific inputs (one at a time)
    ranges = {
        "O1": [("gate fee -2 / 15", {"hybrid_gate_fee_received": -2}, {"hybrid_gate_fee_received": 15}),
               ("steel yield 1% / 5%", {"hybrid_yield_steel": 1}, {"hybrid_yield_steel": 5}),
               ("crusher capex 2.5M / 1.4M", {"opt_crusher_capex": 2.9e6}, {"opt_crusher_capex": 1.4e6})],
        "O2": [("gate fee -2 / 15", {"hybrid_gate_fee_received": -2}, {"hybrid_gate_fee_received": 15}),
               ("contract rate 10 / 5 EUR/t", {"opt_crusher_contract_rate": 10}, {"opt_crusher_contract_rate": 5}),
               ("steel yield 1% / 5%", {"hybrid_yield_steel": 1}, {"hybrid_yield_steel": 5})],
        "O3": [("purchase price 4.0M / 1.5M", {"capex_plant_equipment": 4.8}, {"capex_plant_equipment": 2.3}),
               ("ramp as greenfield 50/79 / 65/90", {"ramp_year1_pct_of_steady": 50, "ramp_year2_pct_of_steady": 79},
                {"ramp_year1_pct_of_steady": 65, "ramp_year2_pct_of_steady": 90}),
               ("truck-fed site gravel +5 / waterside", {"price_gravel_delivered": 37}, {})],
        "O4": [("framework discount -2 / 0 EUR/m3", {"opt_price_delta_per_m3": -2}, {"opt_price_delta_per_m3": 0})],
        "O5": [("MKI value 0 / 4.5, cost +4 / 0", {"opt_circ_price_delta_per_m3": 0, "opt_circ_cost_delta_per_m3": 4},
                {"opt_circ_price_delta_per_m3": 4.5, "opt_circ_cost_delta_per_m3": 0})],
        "P1": [("gate fee -2 / 15", {"hybrid_gate_fee_received": -2}, {"hybrid_gate_fee_received": 15}),
               ("purchase price 4.0M / 1.5M", {"capex_plant_equipment": 4.8}, {"capex_plant_equipment": 2.3}),
               ("ramp 55/85 (no framework) / 85/100", {"ramp_year1_pct_of_steady": 55, "ramp_year2_pct_of_steady": 85, "opt_price_delta_per_m3": 0},
                {"ramp_year1_pct_of_steady": 85, "ramp_year2_pct_of_steady": 100})],
        "P2": [("gate fee -2 / 15", {"hybrid_gate_fee_received": -2}, {"hybrid_gate_fee_received": 15}),
               ("purchase price 4.0M / 1.5M", {"capex_plant_equipment": 4.8}, {"capex_plant_equipment": 2.3}),
               ("volume 75k / 100k", {"output_steady_state": 75000}, {"output_steady_state": 100000})],
    }
    for key, lst in ranges.items():
        ov = OPT_BY_KEY[key][3]
        rows[key]["ranges"] = [{"case": c, "npv_low_case": mc.run(table, dict(ov, **lo))["kpis"]["npv"],
                                "npv_high_case": mc.run(table, dict(ov, **hi))["kpis"]["npv"]} for c, lo, hi in ranges[key]]
    al_r = []
    for k_, lab, unit, lo, b, hi, _ in AL_INPUTS:
        if lo != hi:
            al_r.append({"case": f"{lab} {lo} / {hi}", "npv_low_case": run_asset_light({k_: lo}, table)["kpis"]["npv"],
                         "npv_high_case": run_asset_light({k_: hi}, table)["kpis"]["npv"]})
    rows["O6"]["ranges"] = al_r
    policy = [policy_tests(table, "O0", OPT_BY_KEY["O0"][3]), policy_tests(table, "P1", OPT_BY_KEY["P1"][3]),
              policy_tests(table, "P2", OPT_BY_KEY["P2"][3])]
    return {"options": rows, "policy": policy,
            "notes": "NPV at 8% real, 2026-2036, salvage-only terminal value. Criterion 3 uses the third operating year "
                     "(2029 if sales start 2027, 2030 if 2028). Criterion 4: option-relative stress (see options.py)."}


def main():
    table = mc.load_inputs()
    res = evaluate(table)
    with open(OUT_JSON, "w") as f:
        json.dump(res, f, indent=1, default=str)
    f_ = lambda v, s=1e6, d=2: "-" if v is None else f"{v / s:,.{d}f}"
    print(f"{'key':4s} {'name':52s} {'NPV':>7s} {'IRR':>6s} {'PB':>5s} {'EBITDA3':>8s} {'fund':>6s} crit verdict")
    for key, r in res["options"].items():
        k, c = r["kpis"], r["criteria"]
        irr = "-" if k["irr"] is None else f"{k['irr'] * 100:.1f}%"
        print(f"{key:4s} {r['name'][:52]:52s} {f_(k['npv']):>7s} {irr:>6s} {f_(k['payback'], 1, 1):>5s} {f_(k['ebitda_y3']):>8s} "
              f"{f_(k['funding_need']):>6s} {c['n_pass']}/4 (c4 {c['c4_n_pass']}/6) {c['verdict']}")
    for pt in res["policy"]:
        print(pt)
    print("asset-light break-even licensees:", res["options"]["O6"]["breakeven_licensees"])
    print("written", OUT_JSON)


if __name__ == "__main__":
    main()
