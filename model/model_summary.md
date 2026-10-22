# Financial model summary: B1 circular ready-mix plant (base case)

Agent 6 (Financial modeller). Date: 2026-10-22. **Re-run after the red-team critique** (`review/critique.md`, decisions in `review/response.md`). All money is in **real 2026 €, excl. VAT**. Discount rate **8% real**. Horizon 2026–2036 (permits 2026, build 2027, **sales 2028–2036**).
Model files: `model/financial_model.xlsx` (live formulas), `model/model_core.py` (same model in Python), `model/build_model.py`, `model/charts.py`, `model/check_model.py`, `model/run_all.py` (runs the full pipeline). Inputs: `model/inputs.csv`.

**Verdict (plan.md 2.1, criteria not changed): NOT VIABLE.** In the base case the plant makes a very small operating profit (EBITDA €0.2–0.3M a year from 2030). That is far too little to pay back €5.5M of capex. Criteria 1, 2 and 4 fail. Only criterion 3 (EBITDA positive by the 3rd operating year) passes, just (+€0.32M in 2030). NPV is −€5.33M, which is −97% of capex, far outside the −10% to 0% "borderline" band.

**What changed after the critique (base case):** first sales 2028 instead of 2027 (M1), average truck load 9 m³ instead of 10 m³ (M2), public green premium 1.5% instead of 3% (M3). Step by step: original base −€4.48M → sales 2028 −€4.38M → 9 m³ loads −€5.15M → 1.5% public premium **−€5.33M**. The original base is kept as memo case `O_orig` (Excel option selector, `results_options.json`) and still gives −€4,481,665 to the euro.

---

## 1. Key assumptions (base case)

| Topic | Assumption | Source |
|---|---|---|
| Plant | One ready-mix plant (B1), 120 m³/h, waterside site in Zuid-Holland (Rotterdam–Drechtsteden), 1.5 ha leased. Recycled aggregate (RCA) is bought, not crushed in-house. | inputs.csv, technology.md |
| Timing | **2026 = permits** (permits/engineering €0.5M). **2027 = build**: plant + civil capex (€5.0M), start-up costs (€0.38M), grant (€0.4M) and MIA. **First sales 2028** (9 operating years). Input `first_sales_delay_yr` = 1. | A-FIX-01 (critique M1), A-OPT-01 |
| Volume | 35,000 → 55,300 → **70,000 m³/yr** in 2028 / 2029 / 2030+ (50% / 79% / 100%). 60% circular mixes, 40% standard CEM III/B. | A-CST-01, A-TEC-44 |
| Price | **Plant average over all strength classes: €135/m³ delivered** (confidence **L**, critique H1; likely at or above the market average, see market.md §9). Green premium only on circular volume: **1.5% public** (40% of sales), 0% private, which gives a 0.6% blended premium (€0.8/m³ circular). The price passes on 80% of the market-wide rise in CEM III/B carbon and slag costs. No other real price growth. | A-MKT-16, A-MKT-25/26, A-FIX-03, A-CST-13 |
| Recipe | Plant-average cement 325 kg/m³ (circular) and 310 kg/m³ (standard). The circular mix has 50% coarse RCA (560 kg). | A-CST-09/11 |
| Costs | Cement €110/t, plus 85% of the extra ETS/CBAM cost each year after 2026, plus 10% slag uplift from 2031. Gravel €32/t. Sand €19/t. RCA delivered €24.5/t (€15 ex-works + 30 km × €0.25 + €2). Subcontracted delivery (€9 + €0.5/km at 20 km) × 10/9 for the **9 m³ average load = €21.1/m³** (was €19.0 at 10 m³). 7 production FTE, 3 SG&A FTE, €300k other overheads, €150k lease, 2.5% maintenance. | price_breakdown.md, A-TEC-28, A-FIX-02 |
| Capex | Plant €4.0M + civil €1.0M + permits/engineering €0.5M = **€5.5M**. LCA/EPD (€80k) and pre-opening (€300k) are expensed in the build year. Sustaining capex is 1%/yr. | A-CST-02–08 |
| Tax | Vpb 19% up to €200k and 25.8% above. Losses are carried forward. MIA (9.3% net on 20% of capex) and the grant fall in the build year. Unlevered (no debt). | A-CST-30, A-POL-21/22/24 |
| Working capital | 60 days receivables, 10 days inventory, 30 days payables. Not released at the end (conservative, see §2). | A-CST-07 |
| Terminal value | **Salvage only**: 25% of plant + civil capex in 2036 (€1.25M), tax-neutral. No perpetuity (conservative, see §2). | plan.md 2.1 |
| Payback | Measured from 2026. Uses cumulative free cash flow **excluding** salvage, interpolated within the year. | Agent 6 |
| **Key judgement calls** (critique M4) | Cement carbon pass-through **85%** (A-POL-09) and concrete price pass-through of the market binder cost **80%** (A-CST-13). Neither has a source. Together they create the slow margin squeeze after 2030. A 100% line is shown in §2. | A-POL-09, A-CST-13 |

## 2. Results

| KPI | Pessimistic | **Base** | Optimistic |
|---|---|---|---|
| NPV @ 8% real | −€35.5M | **−€5.33M** | +€24.5M |
| IRR (real) | n/a (all negative) | **−13.9%** | 103.7% |
| Payback (simple) | not reached | **not reached in 10 yr** | 2.1 yr |
| Discounted payback | not reached | **not reached** | 2.2 yr |
| EBITDA 3rd operating year (2030) | −€4.5M | **+€0.32M** (3.4% margin) | +€6.74M |
| Funding need (peak cumulative negative FCF) | €52.0M | **€7.09M** (lowest point 2029) | €2.84M |
| Initial capex | €8.0M | €5.5M | €4.0M |

- **How the scenarios are built.** Every input goes to its "bad" column (pessimistic) or its "good" column (optimistic) at the same time. For a cost input, bad = high column. For a revenue input, bad = low column. Some inputs stay at base in all scenarios: discount rate, tax rates, asset lifetimes, timing (`first_sales_delay_yr`), C30/37 recipe variants, and CO₂/MKI memo rows. These two scenarios are **stress bounds, not likely cases**. All inputs will not go wrong (or right) together. The deck should not show the all-optimistic bar (critique L4); the model keeps it.
- **Indicative range (not a probability interval, critique M8).** Base NPV ± the root-sum-square of the one-at-a-time NPV changes of 22 drivers gives **−€15.3M to +€2.1M**. The method treats correlated drivers (price, cement, pass-through) as independent, so it is only a rough indication of spread. Most of the range is below zero.
- **Base case per year.** EBITDA is −€0.38M in 2027 (start-up costs in the build year), −€0.52M (2028), −€0.02M (2029), **+€0.32M (2030)**, then falls to €0.19M (2036). It falls because cement carbon and slag costs rise faster than the 80% that is passed on in prices. Cumulative FCF excluding salvage is still −€6.12M in 2036 (−€4.87M with salvage).
- **Unit economics, 2030 (first full-output year), €/m³** (UnitEconomics sheet):

| €/m³ | Circular | Standard | Plant average |
|---|---|---|---|
| Price | 137.6 | 136.7 | 137.2 |
| Cash cost | 131.6 | 134.1 | 132.6 |
| EBITDA | 6.0 | 2.7 | 4.6 |
| EBIT | 2.3 | −1.0 | 1.0 |

  The circular mix is **€2.5/m³ cheaper** to make than the standard mix: RCA at €24.5/t is cheaper than gravel at €32/t. It also earns €0.8/m³ premium. But the whole plant earns only €4.6/m³ EBITDA. The plant needs €11.7/m³ to recover its capex over 10 years at 8%. **The gap is about €7/m³ (5% of price).**
- **Break-even (other inputs at base):**
  - EBITDA = 0 at **56.8k m³/yr**.
  - NPV = 0 needs any one of:
    - **134k m³/yr** steady-state volume (+92%, about 4× the Dutch average plant of 33.7k m³, ERMCO 2023), or
    - a plant-average price of **€154.0/m³** (+€19.0, +14.1%), or
    - a public green premium of 58.5% (not realistic).
  - Even free plant equipment (−€4M capex) does not reach NPV = 0.
- **Other checks and memo values:**

| Case | NPV |
|---|---|
| 60k m³/yr (market SOM) | −€6.4M |
| 6% discount rate | −€5.3M |
| 10% discount rate | −€5.4M |
| No grant | −€5.7M |
| First sales 2027 (all other new inputs) | −€5.6M |
| Truck load 8 m³ / 10 m³ | −€6.3M / −€4.6M |
| Public green premium 0% / 3% | −€5.5M / −€5.2M |
| **100% concrete price pass-through of the binder cost** (critique M4) | **−€4.93M** (+€0.40M) |
| 100% cement carbon pass-through **and** 100% concrete pass-through | −€4.94M |
| Memo L2: working capital released in 2036 (not allowed by plan 2.1) | −€4.74M (+€0.59M) |
| Memo L1: salvage at book value of plant + civil (64% in 2036; not allowed by plan 2.1) | −€4.42M (+€0.90M) |
| Memo: L1 + L2 + 100% concrete pass-through together (all conservative choices undone) | −€3.42M |

  **Conservative choices disclosed (critique L1, L2):** the salvage-only terminal value (25%, set by plan.md §2.1) and the missing working-capital release together cost about €1.5M of NPV against a going-concern view. The tax loss on disposal (book value above salvage) is also ignored (~€0.2M PV). Undoing all of them still leaves NPV at −€3.4M, so they do not change the verdict.
- **Carbon prices (critique L8):** the EUA forecasts are probably nominal but are used as real 2026 €. This overstates the real carbon path by ~10–15% by 2034. The whole ETS/CBAM path only moves NPV by €0.45M (tornado), so the effect is ≤ €0.1M.

## 3. Sensitivity (tornado, NPV @ 8%, one input group at a time)

| Rank | Driver (low / high input) | NPV at low input | NPV at high input | Swing |
|---|---|---|---|---|
| 1 | **Average selling price** (€115 / €155 per m³) | −€12.4M | **+€0.25M** | €12.6M |
| 2 | Concrete delivery distance (10 / 35 km) | −€3.5M | −€8.4M | €4.9M |
| 3 | Gravel price (€25 / €40 per t) | −€3.4M | −€7.8M | €4.5M |
| 4 | Plant utilisation (50k / 90k m³/yr) | −€7.5M | −€3.4M | €4.1M |
| 5 | Capex (€4.0M / €8.0M) | −€3.8M | −€7.9M | €4.1M |
| 6 | Cement price 2026 (€95 / €130 per t) | −€3.7M | −€7.7M | €4.0M |
| 7 | Delivery cost rates | −€3.8M | −€6.9M | €3.1M |
| 8 | SG&A | −€4.1M | −€7.2M | €3.1M |
| 9 | Sand price | −€4.2M | −€6.7M | €2.5M |
| 10 | Production staff | −€4.6M | −€6.6M | €2.0M |
| … | RCA ex-works price (€10 / €25 per t) | −€4.7M | −€6.5M | €1.8M |
| … | **Truck-mixer load (8 / 10 m³)** (new, critique M2) | −€6.3M | −€4.6M | €1.7M |
| … | Ramp-up speed | −€6.7M | −€5.0M | €1.7M |
| … | Green premium (0%/−2% / 3%/+3%) | −€5.9M | −€4.6M | €1.2M |
| … | ETS/CBAM carbon path only | −€5.2M | −€5.6M | €0.45M |
| … | Discount rate (6% / 10%) | −€5.3M | −€5.4M | €0.08M |

The full list (25 groups) is in the Sensitivity sheet and `charts/tornado_npv.png`.

**Footnote (critique L9):** the tornado shows single input groups. Criterion 4 (§4) uses six "main drivers", two of which are **combined** groups that the tornado chart shows only as their parts: "Transport distance" = concrete delivery distance + RCA haul distance; "Cement / ETS" = cement price 2026 + ETS/CBAM path. Both combined groups are in the Sensitivity sheet (−€9.0M and −€7.9M at their pessimistic values).

**Only one single change lifts NPV above zero: the high selling price (+€0.25M at €155/m³).** The green premium and the RCA price, the two "circular" levers, matter little. ETS/CBAM hardly matters for a CEM III/B producer, because competitors face the same cost and most of it is passed on in prices.

## 4. Viability criteria (plan.md 2.1, not changed)

| # | Criterion | Base case value | Result |
|---|---|---|---|
| 1 | NPV > 0 at 8% real, salvage-only terminal value | −€5.33M | **FAIL** |
| 2 | Payback < 7 years | not reached in 10 years | **FAIL** |
| 3 | EBITDA positive by year 3 (3rd operating year = 2030) | +€0.32M in 2030 (2029: −€0.02M) | **PASS** (narrowly) |
| 4 | NPV > 0 with each of the 6 main drivers at its pessimistic value, at least 2 of 6 | **0 of 6** (see below) | **FAIL** |
| – | Borderline band: NPV between −10% and 0% of capex | −97% | no |

Criterion 4 detail. Each driver is set to its pessimistic value, one at a time:

| Driver | Values used | NPV |
|---|---|---|
| Green premium | 0% public / −2% private | −€5.9M |
| RCA price (the B1 analogue of the gate fee) | €25/t ex-works | −€6.5M |
| Transport distance | delivery 35 km + RCA haul 50 km | −€9.0M |
| Cement / ETS | €130/t + high carbon path | −€7.9M |
| Utilisation | 50k m³/yr | −€7.5M |
| Capex | €8.0M | −€7.9M |

No gate fee is used: in B1 the plant buys RCA and does not receive rubble.

**Verdict: NOT VIABLE.** The Excel Viability sheet and `model_core.viability()` give the same result. The original base (memo `O_orig`) is also NOT VIABLE (−€4.48M, 1/4 criteria, 0/6).

## 5. What this means (for the options and the deck)

- **The weak point is not the circular product.** The circular mix is cheaper than the standard mix and earns a small premium. The weak point is a **stand-alone, non-integrated ready-mix plant**. It buys cement, subcontracts trucks and sells at plant-average prices. Its EBITDA margin of ~3.4% does not carry €5.5M of capex.
- **Levers with enough size:** price/mix (+€19/m³ on the average needed), volume above ~130k m³/yr, lower capex (taking over an existing plant), cheaper aggregates and short delivery distances (each worth €2–5M of NPV). None of these alone reaches NPV = 0 except a +14% price. See `research/viability_options.md`.
- **The price risk points down, not up:** the €135/m³ base rests on a secondary source (H1). The primary GWL retail list gives C20/25 €130 and C30/37 €139.5–144.5 delivered ≤ 20 km; B2B project prices are normally at or below retail. At €130/m³ NPV would be −€7.1M. So the likely error in the #1 driver strengthens NOT VIABLE.

## 6. Model integrity

- The Excel workbook and the Python model give **the same numbers to < €0.0001**. Checked after a LibreOffice headless recalculation in **23 cases**: base, pessimistic, optimistic, 3 override cases (incl. all option hooks), every plant option through the live selector (incl. the memo case `O_orig`), pessimistic + P1, first sales 2027 + 8 m³ loads, first sales 2029, and the P2 downside and upside stacks. Details: `model/check_report.md`.
- All P&L sums, the EBITDA identity and the cash-flow reconciliation (FCF = net income + D&A − ΔWC − capex − sustaining capex + salvage) are 0 in every year.
- The workbook IRR formula now accepts only a root above −99% (with the 2027 build year the cash-flow series also has a meaningless root below −100% that LibreOffice found from guess 10%).
- **Extension points:** Inputs!I "Override" column; option hooks `opt_*`; `model_core.run(table, overrides={...})`; `build_model.build_workbook(path, overrides={...})`.

## 7. Viability options

- Live logic: input `first_sales_delay_yr` (timing; now an input with base 1), on-site crushing block (`opt_crusher_*` + `hybrid_*` inputs, incl. the new steel-value share and RCA washing/screening cost), circular-only price and cost deltas.
- Option selector `Inputs!I3`, with the option matrix on sheet `Opt_Overview` (also shows the P2 range and the gate fee for NPV = 0). Asset-light option on the live sheet `Opt_AssetLight`.
- Definitions and tests are in `model/options.py`. Results: `model/results_options.json`. Chart: `model/charts/options_npv.png`. Write-up: `research/viability_options.md`.
