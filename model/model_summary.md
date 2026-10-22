# Financial model summary: B1 circular ready-mix plant (base case)

Agent 6 (Financial modeller). Date: 2026-10-22. All money is in **real 2026 €, excl. VAT**. Discount rate **8% real**. Horizon **2027–2036**.
Model files: `model/financial_model.xlsx` (live formulas), `model/model_core.py` (same model in Python), `model/build_model.py`, `model/charts.py`, `model/check_model.py`, `model/run_all.py` (runs the full pipeline). Inputs: `model/inputs.csv` (Agent 5), not changed.

**Preliminary verdict (plan.md 2.1): NOT VIABLE.** In the base case the plant makes a small operating profit (EBITDA about €0.4–0.5M a year). That is far too little to pay back €5.5M of capex in 10 years. Criteria 1, 2 and 4 fail. Only criterion 3 (EBITDA positive by year 3) passes. NPV is −€4.5M, which is −81% of capex. That is far outside the −10% to 0% "borderline" band.

---

## 1. Key assumptions (base case)

| Topic | Assumption | Source |
|---|---|---|
| Plant | One ready-mix plant (B1), 120 m³/h, waterside site in Zuid-Holland (Rotterdam–Drechtsteden), 1.5 ha leased. Recycled aggregate (RCA) is bought, not crushed in-house. | inputs.csv, technology.md |
| Timing | **2026 = year 0**: permit and construction. All capex (€5.5M), start-up costs (€0.38M) and the grant (€0.4M) fall in 2026. Sales run 2027–2036. | Agent 6 decision |
| Volume | 35,000 → 55,300 → **70,000 m³/yr** from 2029 (50% / 79% / 100% of steady state). 60% circular mixes, 40% standard CEM III/B. | A-CST-01, A-TEC-44 |
| Price | **Plant average over all strength classes: €135/m³ delivered**, not C30/37. Green premium only on circular volume: 3% public (40% of sales), 0% private, which gives a 1.2% blended premium. The price passes on 80% of the market-wide rise in CEM III/B carbon and slag costs. No other real price growth. | A-MKT-16, A-MKT-25/26, A-CST-13 |
| Recipe | Plant-average cement 325 kg/m³ (circular) and 310 kg/m³ (standard). The circular mix has 50% coarse RCA (560 kg). | A-CST-09/11 |
| Costs | Cement €110/t, plus 85% of the extra ETS/CBAM cost each year after 2026, plus 10% slag uplift from 2031. Gravel €32/t. Sand €19/t. RCA delivered €24.5/t (€15 ex-works + 30 km × €0.25 + €2). Subcontracted delivery €9 + €0.5/km at 20 km average = €19/m³. 7 production FTE, 3 SG&A FTE, €300k other overheads, €150k lease, 2.5% maintenance. | price_breakdown.md |
| Capex | Plant €4.0M + civil €1.0M + permits/engineering €0.5M = **€5.5M**. LCA/EPD (€80k) and pre-opening (€300k) are expensed in 2026. Sustaining capex is 1%/yr. | A-CST-02–08 |
| Tax | Vpb 19% up to €200k and 25.8% above. Losses are carried forward. MIA (9.3% net on 20% of capex) and the grant are both in 2026. Unlevered (no debt). | A-CST-30, A-POL-21/22/24 |
| Working capital | 60 days receivables, 10 days inventory, 30 days payables. Not released at the end. | A-CST-07 |
| Terminal value | **Salvage only**: 25% of plant + civil capex in 2036 (€1.25M), tax-neutral. No perpetuity. | plan.md 2.1 |
| Payback | Measured from 2026. Uses cumulative free cash flow **excluding** salvage, interpolated within the year. | Agent 6 |

Check against Agent 5: at 2026 prices and 70k m³, the model gives the same plant-average numbers as price_breakdown.md §10: €135.97/m³ price, €131.59/m³ cost, €7.96/m³ EBITDA.

## 2. Results

| KPI | Pessimistic | **Base** | Optimistic |
|---|---|---|---|
| NPV @ 8% real | −€38.3M | **−€4.48M** | +€30.0M |
| IRR (real) | n/a (all negative) | **−7.1%** | 119% |
| Payback (simple) | not reached | **not reached in 10 yr** | 1.1 yr |
| Discounted payback | not reached | **not reached** | 1.2 yr |
| EBITDA year 3 (2029) | −€4.1M | **+€0.53M** (5.5% margin) | +€6.95M |
| Funding need (peak cumulative negative FCF) | €53.5M | **€6.84M** (lowest point 2028) | €2.84M |
| Initial capex | €8.0M | €5.5M | €4.0M |

- **How the scenarios are built.** Every input goes to its "bad" column (pessimistic) or its "good" column (optimistic) at the same time. For a cost input, bad = high column. For a revenue input, bad = low column. Some inputs stay at base in all scenarios: discount rate, tax rates, asset lifetimes, C30/37 recipe variants, and CO₂/MKI memo rows. Inputs!F/G and Inputs!N in the workbook show which column each input takes. These two scenarios are **stress bounds, not likely cases**. All inputs will not go wrong (or right) together.
- **Plausible range.** Base NPV ± the root-sum-square of the one-at-a-time NPV changes of 21 independent drivers gives **−€16.0M to +€3.5M**. Most of this range is below zero.
- **Base case per year.** EBITDA is −€0.42M (2027), +€0.14M (2028), +€0.53M (2029), then falls to €0.37M (2036). It falls because cement carbon and slag costs rise faster than the 80% that is passed on in prices. Cumulative FCF excluding salvage is still −€4.15M in 2036 (−€2.90M with salvage).
- **Unit economics, 2029, €/m³** (UnitEconomics sheet):

| €/m³ | Circular | Standard | Plant average |
|---|---|---|---|
| Price | 137.4 | 135.8 | 136.7 |
| Cash cost | 128.2 | 130.7 | 129.2 |
| EBITDA | 9.2 | 5.1 | 7.6 |
| EBIT | 5.6 | 1.4 | 3.9 |

  The circular mix is **€2.5/m³ cheaper** to make than the standard mix: RCA at €24.5/t is cheaper than gravel at €32/t. It also earns €1.6/m³ premium. But the whole plant earns only €7.6/m³ EBITDA. The plant needs €11.7/m³ to recover its capex over 10 years at 8%. **The gap is about €4/m³ (3%).**
- **Break-even (other inputs at base):**
  - EBITDA = 0 at **50.7k m³/yr**.
  - NPV = 0 needs any one of:
    - **112k m³/yr** steady-state volume (+60%, about 3× the Dutch plant average of ~34–37k m³), or
    - a plant-average price of **€149.2/m³** (+€14.2, +10.5%), or
    - a public green premium of 46% (not realistic).
  - Even free plant equipment (−€4M capex) does not reach NPV = 0.
- **Other checks:**

| Case | NPV |
|---|---|
| 60k m³/yr (market SOM) | −€5.9M |
| 6% discount rate | −€4.2M |
| 10% discount rate | −€4.7M |
| No grant | −€4.9M |
| Working capital released in 2036 (memo) | −€3.9M |

## 3. Sensitivity (tornado, NPV @ 8%, one input group at a time)

| Rank | Driver (low / high input) | NPV at low input | NPV at high input | Swing |
|---|---|---|---|---|
| 1 | **Average selling price** (€115 / €155 per m³) | −€12.8M | **+€1.8M** | €14.5M |
| 2 | **Plant utilisation** (50k / 90k m³/yr) | −€7.4M | −€2.3M | €5.1M |
| 3 | **Gravel price** (€25 / €40 per t) | −€2.5M | −€7.4M | €4.9M |
| 4 | Concrete delivery distance (10 / 35 km) | −€2.8M | −€7.7M | €4.8M |
| 5 | Cement price 2026 (€95 / €130 per t) | −€2.9M | −€7.2M | €4.3M |
| 6 | Capex (€4.0M / €8.0M) | −€3.0M | −€7.2M | €4.3M |
| 7 | SG&A | −€3.3M | −€6.6M | €3.3M |
| 8 | Delivery cost rates | −€3.1M | −€6.2M | €3.0M |
| 9 | Sand price | −€3.4M | −€6.1M | €2.7M |
| 10 | Ramp-up speed | −€6.2M | −€4.1M | €2.1M |
| … | RCA ex-works price (€10 / €25 per t) | −€3.9M | −€5.9M | €2.0M |
| … | Green premium (0%/−2% / 8%/+3%) | −€5.3M | −€3.4M | €1.9M |
| … | Discount rate (6% / 10%) | −€4.2M | −€4.7M | €0.5M |
| … | ETS/CBAM carbon path only | −€4.3M | −€4.7M | €0.4M |

The full list (24 groups) is in the Sensitivity sheet and `charts/tornado_npv.png`.

**Only one single change lifts NPV above zero: the high selling price.** The green premium and the RCA price, the two "circular" levers, matter little. ETS/CBAM hardly matters for a CEM III/B producer, because competitors face the same cost and most of it is passed on in prices.

## 4. Viability criteria (plan.md 2.1, not changed)

| # | Criterion | Base case value | Result |
|---|---|---|---|
| 1 | NPV > 0 at 8% real, salvage-only terminal value | −€4.48M | **FAIL** |
| 2 | Payback < 7 years | not reached in 10 years | **FAIL** |
| 3 | EBITDA positive by year 3 | +€0.53M in 2029 (already positive in 2028) | **PASS** |
| 4 | NPV > 0 with each of the 6 main drivers at its pessimistic value, at least 2 of 6 | **0 of 6** (see below) | **FAIL** |
| – | Borderline band: NPV between −10% and 0% of capex | −81% | no |

Criterion 4 detail. Each driver is set to its pessimistic value, one at a time:

| Driver | Values used | NPV |
|---|---|---|
| Green premium | 0% public / −2% private | −€5.3M |
| RCA price (the B1 analogue of the gate fee) | €25/t ex-works | −€5.9M |
| Transport distance | delivery 35 km + RCA haul 50 km | −€8.4M |
| Cement / ETS | €130/t + high carbon path | −€7.5M |
| Utilisation | 50k m³/yr | −€7.4M |
| Capex | €8.0M | −€7.2M |

No gate fee is used: in B1 the plant buys RCA and does not receive rubble.

**Verdict: NOT VIABLE.** The Excel Viability sheet and `model_core.viability()` give the same result. Agent 7 should start.

## 5. What this means (for Agent 7 and the deck)

- **The weak point is not the circular product.** The circular mix is cheaper than the standard mix and earns a small premium. The weak point is a **stand-alone, non-integrated ready-mix plant**. It buys cement, subcontracts trucks and sells at plant-average prices. Its EBITDA margin of ~5.5% does not carry €5.5M of capex.
- **Levers with enough size:**
  - price/mix: +€14/m³ on the average, for example more high-strength and specification work, or long contracts with anchor clients;
  - volume above ~110k m³/yr, for example a second shift or a framework contract;
  - lower capex, for example by taking over or sharing an existing plant;
  - cheaper aggregates and short delivery distances: each of these is worth €2–5M of NPV;
  - integration, for example own crushing (option A+B) or own trucks.
- **Things that could make the base case worse than shown:**
  - Sales in 2027 are optimistic, because the permit and build take 12–18 months from late 2026.
  - The 0.4M grant is uncertain.
  - The concrete price may not follow cement carbon costs at 80%.

## 6. Model integrity

- The Excel workbook and the Python model give **the same numbers to < €0.0001**. This was checked after a LibreOffice headless recalculation in 6 cases: base, pessimistic, optimistic, and 3 override cases including all option hooks. Details are in `model/check_report.md`.
- All P&L sums, the EBITDA identity and the cash-flow reconciliation (FCF = net income + D&A − ΔWC − capex − sustaining capex + salvage) are 0 in every year.
- **Extension points:**
  - Inputs!I "Override" column;
  - option hooks `opt_*` (extra capex, extra revenue, extra opex, price or cost change per m³);
  - `model_core.run(table, overrides={...})`;
  - `build_model.build_workbook(path, overrides={...})`.
