# Viability options — what would make the circular concrete business viable?

Agent 7 (Viability strategist). Date: 2026-10-22. All money is in **real 2026 €, excl. VAT**. NPV at **8% real**, 2026–2036, terminal value = salvage only (plan.md §2.1, not changed).
Model: `model/model_core.py` (new option logic) + `model/options.py` (option definitions, asset-light model, robustness test, policy tests) + `model/financial_model.xlsx` (live option selector `Inputs!I3`, sheets `Opt_Overview` and `Opt_AssetLight`). Results: `model/results_options.json`. Chart: `model/charts/options_npv.png`.
New sources: `research/sources_options.md` (OPT-xx). New assumptions: `research/assumptions_options.md` (A-OPT-xx).

---

## 0. Summary

1. **No single option makes the plant viable.** We tested 10 single options and 2 packages in the financial model. Every single option still has a negative NPV, between −€2.5M and −€5.5M (see §2).
2. **Corrected base reference (O0): first sales in 2028, not 2027.** NPV is −€4.38M, almost the same as the gated base (−€4.48M). The year without sales costs about as much as the year of later capex saves, because the plant earns so little each year. **Verdict: still NOT VIABLE.**
3. **The three levers that matter are about plant economics, not "green":**
   - **buy an existing plant instead of building one** (O3): +€1.7M NPV vs O0;
   - **on-site crushing with a demolition partner**, earning gate fees and getting own recycled aggregate (O2): +€1.3M;
   - **more volume** (O8, 100k m³/yr): +€1.5M.
   
   The green levers add little or even lose money: a lower-CO₂ binder (O5) is −€0.4M, extra subsidies (O7) +€0.6M, framework contracts (O4) +€0.2M.
4. **Package P1** (buy and convert an existing plant + partner crushing + framework contracts) gives NPV **−€1.36M**, IRR 2.1% and payback 9.8 years. **Package P2** (P1 at 90k m³/yr with a second framework contract) gives NPV **+€0.0M** (+€414), IRR 8.0% and payback 7.3 years. P2 is exactly at break-even. We did not tune it: 90k m³ is the existing "high" utilisation input.
5. **Robustness (criterion 4) fails for every option, P2 included: 0 of 6 drivers.** Even P2 turns negative if any one main driver moves to its pessimistic value. Under the fixed plan.md rules **no option is VIABLE, and none is even BORDERLINE.** P2 passes criteria 1 and 3, but its payback of 7.3 years misses the 7-year limit. With the maximum realistic subsidies P2 would reach NPV +€0.56M and a 6.6-year payback, which is BORDERLINE. But a €1.0M DEI+ grant is unlikely for a plant takeover that is not innovative.
6. **Policy cannot rescue the stand-alone plant.**
   - **Primary aggregate levy:** no levy level helps. It even hurts slightly, because our mixes still contain 1.25–1.9 t primary sand and gravel per m³.
   - **Faster ETS phase-out:** hurts by −€0.2–0.3M, because CEM III/B is also our binder.
   - **Landfill tax at €81/t:** ≈ €0.
   - **Green premium for public clients:** to reach NPV = 0 it would need to be 52% (O0) or 15.6% (P1), against 3% today.
   - **What does help:** the GWW MKI ceilings from 2028, but only with a truly lower-CO₂ product. P1 needs about €7.8 of captured value per circular m³, and our estimate is €1.5.
7. **Recommended path:** do not build a greenfield plant. Pursue P2 as a **staged, conditional acquisition play**. Go ahead only if, before money is committed, three things are signed:
   - **(a)** a plant purchase at ≤ €2.5M, preferably ≤ €2.0M;
   - **(b)** a 7+ year rubble contract with a demolition partner, with a gate fee of ≥ €5/t and contract crushing at ≤ €7.5/t;
   - **(c)** framework contracts for ≥ 40k m³/yr.
   
   Even then the case is break-even, not robust. Present it to the jury honestly as "investable only under these conditions".

---

## 1. Method

- **Criteria** (plan.md §2.1, unchanged):
  1. NPV > 0;
  2. payback < 7 years;
  3. EBITDA > 0 in the 3rd operating year (2029, or 2030 if sales start in 2028);
  4. NPV > 0 with at least 2 of the 6 main drivers at their pessimistic value, one at a time.
- **Criterion 4 for options** is relative to each option:
  - If the option itself sets a driver (for example utilisation at 90k), that value is stressed by the same ratio as in the base test (for example ×50/70).
  - For options with on-site crushing, the "RCA price" driver is replaced by its A+B analogue, the **gate fee** (low = −€2/t). plan.md names the gate fee as a main driver.
  - For the asset-light option (O6) the plant drivers do not apply. Its own 6 drivers are used instead.
- **New model logic** in `model_core.py` and the workbook (live formulas, all 0 = off, base case unchanged to the euro):
  - `opt_start_delay`: first sales later. Permits stay in 2026. Plant capex, start-up costs, grant and MIA move to the build year. Depreciation starts in the first operating year.
  - **On-site crushing block** (`opt_crusher_*`, using the existing `hybrid_*` inputs):
    - rubble intake follows the ramp-up;
    - the coarse yield replaces purchased RCA (credited at the delivered price, €24.5/t);
    - surplus coarse RCA is sold ex-works;
    - gate fee, sand and steel revenue;
    - costs: contaminant disposal, diesel, wear, contract crushing, staff, maintenance, BRL 2506 certification and extra site lease;
    - own crusher capex, MIA, depreciation and salvage.
  - **Circular-only price and cost deltas** from a start year (for the binder option).
  - **O6 asset-light** is a separate small model (`options.run_asset_light`, live sheet `Opt_AssetLight`).
- **Excel–Python check** (`model/check_report.md`): **ALL CASES MATCH**. 18 recalculated cases: the 6 original cases, all 11 plant options through the live selector, and pessimistic scenario + P1. The asset-light KPIs are checked as well. The base case gives the same NPV as before (−€4,481,665).

---

## 2. Option table

The KPIs come from `model/results_options.json`. Payback is counted from 2026. "Funding need" is the lowest point of cumulative free cash flow, before financing. Feasibility runs from 1 (hard) to 5 (easy).

| # | Option | NPV €M | IRR | Payback | EBITDA 3rd yr €M | Funding €M | Capex €M | Criteria passed | Crit. 4 | Feas. | Who must act |
|---|---|---|---|---|---|---|---|---|---|---|---|
| – | Base as gated (sales 2027) | −4.48 | −7.1% | not reached | 0.53 (2029) | 6.84 | 5.50 | 1/4 | 0/6 | – | – |
| **O0** | **Corrected base: sales 2028** | **−4.38** | −9.0% | not reached | 0.51 (2030) | 6.86 | 5.50 | 1/4 | 0/6 | 5 | Founders |
| O1 | A+B own mobile crushing line | −3.87 | −3.4% | not reached | 1.03 (2030) | 8.58 | 7.50 | 1/4 | 0/6 | 3 | Founders, province (waste permit), demolition suppliers |
| O2 | A+B with demolition partner (contract crushing) | −3.09 | −2.6% | not reached | 0.95 (2030) | 7.00 | 5.90 | 1/4 | 0/6 | 3 | Demolition partner, province |
| O3 | Acquire and convert an existing plant | −2.71 | −5.7% | not reached | 0.53 (2029) | 4.66 | 3.70 | 1/4 | 0/6 | 3 | Founders, seller, bank |
| O4 | Offtake / framework contracts | −4.14 | −9.2% | not reached | 0.44 (2030) | 6.44 | 5.50 | 1/4 | 0/6 | 3 | Contractors, RWS, municipalities |
| O5 | Lower-CO₂ binder product (from 2029) | −4.76 | −10.4% | not reached | 0.47 (2030) | 7.09 | 5.65 | 1/4 | 0/6 | 2 | Binder supplier, certification body |
| O6 | Asset-light licence + RCA service (D) | −2.51 | n/a | not reached | −0.28 (2029) | 3.35 | 0.20 | 0/4 | 0/6 | 2 | Founders, licensee plants |
| O7 | Maximum realistic subsidies | −3.83 | −7.9% | not reached | 0.51 (2030) | 6.26 | 5.50 | 1/4 | 0/6 | 2 | RVO |
| O8 | Bigger plant 100k m³/yr | −2.85 | −2.0% | not reached | 1.03 (2030) | 6.68 | 5.50 | 1/4 | 0/6 | 2 | Founders, anchor customers |
| O9 | Urban site closer to demand | −5.47 | −14.6% | not reached | 0.30 (2030) | 7.17 | 5.50 | 1/4 | 0/6 | 3 | Founders, municipality |
| **P1** | **Acquire + partner crushing + frameworks** | **−1.36** | 2.1% | 9.8 yr | 0.91 (2029) | 4.72 | 4.10 | 1/4 | 0/6 | 3 | Founders, seller, demolition partner, contractors |
| **P2** | **P1 + scale to 90k m³/yr** | **+0.00** | 8.0% | 7.3 yr | 1.28 (2029) | 4.58 | 4.10 | 2/4 | 0/6 | 2 | As P1 + a second anchor customer |

Every option's verdict is **NOT VIABLE**. Ranking by NPV: P2 > P1 > O6 > O3 > O8 > O2 > O7 > O1 > O4 > O0 > base > O5 > O9. Ranking by **value per unit of risk and effort**, which is the order we would pursue: **O3, O2, O4**, together as P1, then P2. O8 only works with contracts (P2). O6 is a fallback.

![NPV per option](../model/charts/options_npv.png)

---

## 3. Per-option detail

### O0 — Corrected base: first sales 2028 (timing realism)
- **Change:** `opt_start_delay = 1` [A-OPT-01]. Permits and engineering (€0.5M) stay in 2026. Plant capex (€5.0M), start-up costs, the grant and MIA move to 2027. Ramp-up is 50/79/100% in 2028/29/30. Only 9 operating years remain.
- **Result:** NPV −€4.38M. EBITDA is +€0.51M in 2030. Funding need is €6.86M. 1/4 criteria pass.
- **Why it barely changes:** the year of delay removes about −€0.4M of FCF in the first sales year. It also defers €5M of capex by one year, which is worth about +€0.4M at 8%. So it is neutral. **The lesson is that time is not the problem. The plant's margin is.**
- **Use:** this is the honest reference for all greenfield options (O1, O2, O4, O5, O7–O9).

### O1 — A+B own mobile crushing line
- **Changes:**
  - O0 + `opt_crusher_on = 1`;
  - crushing from 2029 (waste permit about 18 months) [A-OPT-02];
  - intake 40.5 kt/yr (sized to own RCA need) [inputs `hybrid_rubble_needed`];
  - capex €2.0M (mobile crusher €1.6M, A-TEC-40, + site works €0.4M, A-OPT-03), 100% MIA-eligible (A 1401), 10% salvage [A-OPT-04];
  - 3 crushing FTE, diesel 0.3 l/t, wear €0.4/t, maintenance 3%, BRL 2506 €25k/yr, extra 1 ha leased;
  - gate fee €5/t (A-MKT-15), yields 58/38/3/1% (A-TEC-01–04), sand €3/t, steel €150/t.
- **Crushing line at full output (2031):** net result about +€0.52M/yr EBITDA. Own RCA replaces purchases worth €0.58M. Gate fee €0.20M, steel €0.18M, sand €0.05M.
- **Result:** NPV −€3.87M. EBITDA 2030 €1.03M. Funding need €8.58M (the highest).
- **Ranges:**
  - gate fee −€2 / €15 per t → NPV −€4.96M / −€2.46M;
  - steel yield 1% / 5% → −€4.31M / −€3.44M;
  - crusher capex +45% / −30% → −€4.59M / −€3.40M.
- **Risks:**
  - The waste permit (9–36 months, A-POL-20).
  - Rubble supply: demolition firms are building their own high-grade lines (competitors.md §11).
  - 3 FTE are heavy for 40 kt. A 300 t/h crusher would only run ~135 h/yr.
  - Sand outlet is almost nil (€3/t).
- **Feasibility 3.** O2 is the better form of the same idea.

### O2 — A+B with a demolition partner (contract crushing on our site)
- **Changes:**
  - as O1, but the partner crushes in campaigns at **€7.5/t** (machine, operator, diesel and wear included) [A-OPT-05, OPT-04: UK £7/t];
  - our capex is only €0.4M of site works;
  - 1 FTE for acceptance and loader work;
  - the gate fee (€5/t) is fixed in a long-term supply contract.
- **Crushing line at full output:** net result ≈ **+€0.45M/yr**.
  - Revenue and avoided cost: gate fee €0.20M, RCA credit €0.58M, steel €0.18M, sand €0.05M.
  - Costs: contract crushing €0.30M, extra site lease €0.10M, staff €0.07M, contaminants €0.05M, BRL 2506 certification €0.03M.
- **Result:** NPV −€3.09M (+€1.30M vs O0). Funding need €7.00M.
- **Ranges:**
  - gate fee −€2 / €15 per t → −€4.08M / −€1.70M;
  - contract rate €10 / €5 per t → −€3.45M / −€2.73M;
  - steel yield 1% / 5% → −€3.51M / −€2.67M.
- **Risks:**
  - **About 40% of the net result is steel scrap at an assumed 3% yield** [A-OPT-24]. In clean rubble much rebar may already have been removed.
  - The partner's bargaining power: the gate fee could turn into a price we pay for rubble.
  - The same permit risk as O1.
- **What the partner gains:** a high-grade outlet as road-base demand falls (competitors.md §10), circular credentials in tenders, and its crushing crew is used.
- **Feasibility 3.** Who must act: a demolition firm (examples in competitors.md §12: New Horizon, Vlasman, Adex, GP Groot, Van Werven, Circulair Mineraal members) and the province (permit).

### O3 — Acquire and convert an existing ready-mix plant
- **Changes:**
  - purchase price **€2.5M** (€1.5–4.0M) [A-OPT-06] + conversion €0.8M [A-OPT-07] → `capex_plant_equipment` 3.3;
  - civil €0.2M; permit change and transaction €0.2M; pre-opening €100k;
  - ramp-up 55/85/100% [A-OPT-08];
  - maintenance 3.5% [A-OPT-09]; salvage 15% [A-OPT-10];
  - sales start in 2027: the plant is already permitted and running.
- **Result:** NPV −€2.71M (+€1.67M vs O0). Capex €3.7M. **Funding need €4.66M (−€2.2M).**
- **Ranges:**
  - purchase price €4.0M / €1.5M → −€4.39M / −€1.61M;
  - greenfield-like ramp vs a fast one → −€2.85M / −€2.50M;
  - truck-fed site (gravel +€5/t) → −€4.36M.
- **NPV = 0 alone** would need about 95k m³/yr.
- **Why it makes sense:**
  - The market has ~178 plants for 6.0 Mm³, with spare capacity (CMP-43).
  - Groups are exiting or consolidating (Cementbouw sold its ready-mix; Heidelberg bought Kalle en Bakker's customers; CMP-33, CMP-38).
  - Buying a plant adds **no new capacity**, so incumbents have less reason to fight on price.
  - It removes the 12–18-month permit-and-build delay.
- **Risks:**
  - Older equipment.
  - The site may not be waterside or may lack space for RCA storage and crushing.
  - Customers may leave after the change of owner.
  - A good plant costs far more: Cementir paid ≈ €18M for one Danish plant + a minority stake (OPT-01).
  - No Dutch transaction prices were found. This is a data gap.
- **Feasibility 3.** Who must act: the founders, a seller (independent family plant or a divesting group) and the bank (the plant is collateral).

### O4 — Offtake / framework contracts (MKI-based tenders)
- **Change:** O0 + ramp-up 75/95/100% [A-OPT-11] at a framework discount of −€1.0/m³ on all volume (~3% on one third) [A-OPT-12].
- **Result:** NPV −€4.14M (+€0.24M vs O0). Discount −€2 / €0 → −€4.51M / −€3.83M.
- **Why so small:** a faster ramp-up only brings forward the margin of 2 years of volume, and that margin is thin (~€7.6/m³ EBITDA). Contracts mainly **reduce volume risk**: the "utilisation 50k" stress is the second-worst driver. They are a precondition for P2, not a lever on their own.
- **Who must act:** GWW contractors, Rijkswaterstaat, municipalities, housing corporations. From 2028 the GWW decree makes MKI ceilings compulsory (POL-17), which helps tender access but not price (our MKI ≈ CEM III/B standard).
- **Feasibility 3.**

### O5 — A genuinely lower-CO₂ binder (from 2029)
- **Product:** a circular mix with a binder that is ~30% lower in CO₂ than CEM III/B. Options include activated cement paste from everox (TRL 6–7, certification via EN 197-6/ETA pending) or an Ecocem ACT-type low-clinker cement (company claim: −70% vs average cement at "minimal" extra cost, OPT-05/06).
- **Changes:**
  - from 2029, +€1.5/m³ price on circular volume [A-OPT-13: MKI value captured in tenders + a small private premium];
  - +€1.5/m³ cost on circular volume [A-OPT-14];
  - €150k certification/EPD one-off + €40k/yr [A-OPT-15].
- **Result:** NPV −€4.76M (−€0.38M vs O0). Best/worst case → −€3.98M / −€5.55M.
- **Why it earns so little:**
  - −40 kg CO₂/m³ is worth ≈ €5 MKI/m³ (A2 set).
  - The contractor gets a fictive advantage of ~€15/m³, but that is only in MKI tenders (≈20% of our volume), and the supplier keeps ~30% of it.
  - Spread over all circular volume this is ≈ €1.5/m³.
  - To reach NPV = 0 on P1, the captured value would need to be **€7.8 per circular m³**.
- **Strategic value:** a **hedge** against CEM III/B slag scarcity after Tata's blast-furnace replacement (~2028–30, A-POL-28). It also gives a real CO₂ story: recycled aggregate alone cuts only 8–12%. **It is not a profit driver.**
- **Feasibility 2:** the technology risk is TRL 6–7 and certification is pending. Who must act: binder supplier (everox, Ecocem, ENCI/Heidelberg) and the certification body (KOMO, NEN 8005 assessment).

### O6 — Asset-light: licence + RCA service (archetype D platform)
- **Model:** a separate model, live in `Opt_AssetLight`. No plant.
- **Revenue streams:**
  - a fee of **€2/m³** [A-OPT-20] for certified circular mix designs and MKI/EPD documentation;
  - RCA brokerage at €1.5/t [A-OPT-21];
  - project LCA services, €100k/yr [A-OPT-22].
- **Licensees:** 4 at maturity, +1 per year, 15k circular m³ each [A-OPT-19].
- **Costs:** team 4 FTE, €150k overhead, €350k start-up, €200k capex [A-OPT-23].
- **Result:** NPV −€2.51M. EBITDA stays negative (−€0.28M in 2029). Funding need €3.35M. **0/4 criteria.**
- **Break-even:** each licensee brings only €42.6k/yr. EBITDA breaks even at ≈ **10 licensee plants**, which is not reachable by 2036 at +1 plant per year.
- **Why:** the margin pool per circular m³ is only ~€4 (cost saving + premium). The licensee keeps most of it. Incumbents have their own lines, and SL Materials, everox and SQAPE already license. The downside is capped and small, so it remains a **fallback** or a later add-on (selling mix know-how from the P2 plant).
- **Feasibility 2.**

### O7 — Maximum realistic subsidies
- **Change:** O0 + DEI+ grant €1.0M (instead of €0.4M) + 50% of plant capex MIA-eligible [A-OPT-16].
- **Result:** NPV −€3.83M (+€0.56M vs O0).
- **What does not fit:**
  - **VEKI:** it pays at most €80/t CO₂ avoided, and our circular mix avoids ~0 CO₂ vs CEM III/B.
  - **EU Innovation Fund:** it is for large binder projects.
  - **WBSO (36–50% of R&D wages):** only for mix R&D, worth ~€0.1M.
- **Effect on the best package:** on P2 these subsidies add +€0.56M. But a €1.0M DEI+ grant needs an innovative element (for example O5 or recycled sand), not a plant takeover.
- **Feasibility 2.** Who must act: RVO (competitive, first come, first served).

### O8 — Bigger plant: 100k m³/yr
- **Change:** O0 + 100k m³/yr, +2 production FTE, average delivery 23 km [A-OPT-17]. One shift can make ~240k m³, so no extra plant capex is needed.
- **Result:** NPV −€2.85M (+€1.53M). NPV = 0 for the corrected base needs **~119k m³/yr**.
- **Market check:**
  - 100k m³ = the SOM **high** case. That is ≈ 22% of the regional circular SAM (0.45 Mm³) and ≈ 10% of **all** ready-mix in the delivery radius (MKT §8).
  - It is about 3× the average Dutch plant (34k m³).
  - 119k m³ is above anything market.md supports for a newcomer.
- **Feasibility 2.** Scale only works when it is sold before the plant opens (P2).

### O9 — Urban site closer to demand (truck-fed)
- **Change:** O0 + delivery 15 km, lease €15/m², gravel by truck +€5/t [A-OPT-18].
- **Result:** NPV −€5.47M (−€1.09M). Waterside supply of gravel, sand and RCA (by barge, technology.md) beats proximity.
- **Location advice:** stay **waterside** in Zuid-Holland (Rotterdam–Drechtsteden). Choose a site that can also take rubble by water, which supports P1 and P2.

### C — Element reuse add-on (screening only, not modelled)
- There are no public prices for tested and recertified elements, and market.md / competitors.md give no volumes.
- Element reuse needs deconstruction contracts, testing and a different customer (project developers). It shares little with a ready-mix plant except the demolition partner.
- **Not recommended as a viability lever** for this case. It is better left to a later platform role (O6) or to partners such as New Horizon.

---

## 4. Packages

### P1 — Acquire + partner crushing + framework contracts
- **Changes:**
  - O3 (acquisition, €3.7M);
  - + O2 (partner crushing from 2029, +€0.4M site works);
  - + O4 (ramp-up 75/95/100%, −€1/m³);
  - sales from 2027.
- **Result:** NPV **−€1.36M**, IRR 2.1%, payback 9.8 years. EBITDA 2029 €0.91M. Funding need €4.72M. Capex €4.10M. 1/4 criteria.
- **Ranges:**
  - gate fee −€2 / €15 per t → −€2.35M / +€0.06M;
  - purchase price €4.0M / €1.5M → −€2.99M / −€0.26M;
  - ramp without frameworks / very fast → −€1.41M / −€1.17M.
- **NPV = 0 needs any one of:**
  - a gate fee of **€14.6/t**;
  - a purchase price of **≤ €1.26M**;
  - **82.6k m³/yr**;
  - an average price of **€139.1/m³** (+3%).
- **At other discount rates:** 6% → −€0.97M; 10% → −€1.69M.

### P2 — P1 + scale to 90k m³/yr (second framework contract)
- **Change:** P1 at 90k m³/yr (the "high" utilisation input), +1 production FTE, average delivery 22 km. That is 9% of all ready-mix in the radius, above the SOM base of 60k.
- **Result:** NPV **+€0.0M (+€414)**, IRR 8.0%, payback **7.3 years** (fails the < 7 rule).
  - EBITDA: 2027 €0.28M; 2029 €1.28M; 2036 €1.08M.
  - Funding need €4.58M.
  - **2/4 criteria. NOT VIABLE.** It is not borderline either, because borderline needs criteria 1–3 to pass or NPV between −10% of capex and 0.
- **Ranges:**
  - gate fee −€2 / €15 per t → −€0.99M / +€1.42M;
  - purchase price €4.0M / €1.5M → −€1.63M / +€1.09M;
  - volume 75k / 100k → −€1.54M / +€1.02M;
  - discount rate 6% / 10% → +€0.54M / −€0.46M.
- **Fragile by-products:**
  - no grant → −€0.31M;
  - steel yield 1% → −€0.43M;
  - sand outlet €0 → −€0.16M.
- **Upsides:**
  - P2 + gate fee €10/t → NPV +€0.71M, payback 6.5 years (criteria 1–3 pass), still 0/6 on criterion 4 → BORDERLINE.
  - P2 + O7 subsidies → NPV +€0.56M, payback 6.6 years → BORDERLINE.
  - P2 + O5 binder → −€0.35M.

---

## 5. Robustness test (criterion 4) on the best options

NPV in €M when one main driver is set to its pessimistic value (option-relative, see §1):

| Driver (pessimistic) | O0 | O2 | O3 | P1 | P2 |
|---|---|---|---|---|---|
| Green premium 0% public / −2% private | −5.09 | −3.63 | −3.38 | −2.00 | −0.83 |
| RCA price €25/t (O0, O3) / gate fee −€2/t (O2, P1, P2) | −5.59 | −4.08 | −3.94 | −2.35 | −0.99 |
| Transport distance (delivery ×1.75, RCA haul 50 km) | −7.71 | −5.46 | −6.46 | −4.19 | −3.94 |
| Cement €130/t + high ETS/CBAM path | −6.98 | −5.29 | −5.54 | −3.81 | −3.05 |
| Utilisation ×50/70 | −6.83 | −5.46 | −5.47 | −3.95 | −2.73 |
| Capex ×1.45 (incl. purchase price and crushing works) | −6.91 | −5.49 | −4.35 | −3.07 | −1.71 |
| **Drivers with NPV > 0** | **0/6** | **0/6** | **0/6** | **0/6** | **0/6** |

The asset-light option (O6) is 0/6 on its own drivers too (−€2.7M to −€3.8M). **Conclusion: no option is robust.** P2's NPV of zero leaves no buffer. The two most dangerous drivers are **transport distance** (delivery cost is ~14% of price) and **cement/ETS** (we buy cement; we do not make it).

---

## 6. What the business depends on (policy and market)

The policy tests come from `options.policy_tests`. The levy is applied to all producers, and 80% of the standard mix's extra cost is passed into concrete prices.

| Change | O0 (corrected base) | P1 | P2 |
|---|---|---|---|
| Primary aggregate levy (gravel + sand) | **no level gives NPV = 0**; €5/t → −€4.42M | no level; €5/t → −€1.40M | €5/t → −€0.06M (hurts) |
| Public green premium needed for NPV = 0 (today 3%) | 52% | 15.6% | 3.0% |
| MKI value per circular m³ needed for NPV = 0 (estimate with low-CO₂ binder: €1.5) | €27.3 | €7.8 | €0 |
| High ETS/CBAM path ("faster phase-out of free allocation") | −€4.65M | −€1.57M | −€0.27M |
| Landfill tax €81/t (2030), via contaminant disposal | no effect (no crushing) | −€0.06M vs P1 | −€0.06M vs P2 |
| Gate fee €15/t (rubble pushed out of road base) | n/a | +€0.06M | +€1.42M |
| Average concrete price for NPV = 0 (today €135/m³) | €151.3 | €139.1 | €135.0 |
| Steady volume for NPV = 0 | 119k m³ | 83k m³ | 90k m³ |

**Reading the table:**
1. **A levy on primary aggregates does not help this business model.** Our circular mix still uses 620 kg gravel + 630 kg sand per m³, and 40% of our volume is standard mix. The levy raises our cost about as much as the market price. It helps only a producer with very high recycled content, including recycled sand (CUR 127), which is not certifiable at scale today.
2. **A faster ETS phase-out hurts.** We buy CEM III/B. Competitors use the same binder, so there is no relative gain, and the market passes on only 80%.
3. **The market changes that matter are:**
   - **(a) gate fees for clean rubble.** They rise if road-base outlets shrink (RAW no longer specifies concrete granulate, CMP-91) or if high-grade-reuse targets become binding (NPCE, Betonakkoord). This is the single biggest P2 lever: €15/t adds +€1.4M.
   - **(b) MKI ceilings at front-runner level** in the GWW decree (base 1 Jan 2028, levels not yet set, POL-17). These would turn our CO₂ advantage into a price only if we also have a lower-CO₂ binder (O5). The value needed (€7.8/m³ on P1) is about 5× our estimate.
   - **(c) plant prices staying low** as the market consolidates.
4. **What the business really depends on:**
   - buying capacity cheaply (≤ €2.5M);
   - a long rubble contract with a positive gate fee;
   - ~90k m³ sold under contract, with deliveries kept short (≤ 22 km);
   - a stable average price of €135/m³.
   
   None of this is a "green" factor. The circular content makes these deals possible (partner, tenders), but it does not pay for itself.

---

## 7. Recommended path

1. **Stop the greenfield plan (base and O0).** It cannot reach NPV = 0 with any realistic single change.
2. **Pursue P2 as a conditional acquisition play,** with three gates before any money is committed (target Q2 2027):
   - **Gate A — plant:** an LOI on a waterside ready-mix plant in Zuid-Holland at **≤ €2.5M** (target ≤ €2.0M; P1 needs ≤ €1.26M on its own), with 1 ha of space and a permit route for rubble acceptance.
   - **Gate B — rubble:** a 7–10-year contract with a demolition firm: **gate fee ≥ €5/t (target €10/t), contract crushing ≤ €7.5/t**, and a steel-scrap split agreed in writing.
   - **Gate C — volume:** framework or offtake contracts for **≥ 40k m³/yr** with GWW contractors or public clients, so that 90k m³ is reachable by year 3.
   
   If any gate fails, do not invest. The fallback is the asset-light service (O6): capex €0.2M, but expected losses of ~€0.3–0.5M/yr, so only as a small pilot.
3. **Use O5 (lower-CO₂ binder) as a hedge from ~2029,** not as a profit line: run trials with everox/Ecocem/ENCI and an ETA/EN 197-6 route, financed with WBSO/DEI+. It protects against slag scarcity and supports the GWW MKI story.
4. **Funding:** ~€4.6M peak need for P2, against €6.9M for O0. Part of this could be debt secured on the acquired plant. The demolition partner could take equity, which aligns its incentives on the gate fee.
5. **For the jury:**
   - "The stand-alone circular plant is not viable."
   - "Integration (acquire + crush + contracts) brings it to break-even."
   - "It is investable only if three named contracts are signed."
   
   Show criterion 4 failing openly.

---

## 8. Data gaps (what would change the conclusion fastest)

1. **Dutch gate fees for clean concrete rubble (bulk, multi-year).** These are worth ±€1.2M on P2. Interview 2 demolition firms.
2. **Prices paid for small Dutch ready-mix plants** (asset deals 2022–2026). Worth ±€1.3M.
3. **Contract-crushing rates in NL** (only a UK price was found) and the **real steel content** of clean rubble.
4. **ACP / ACT binder price and certification date.** This decides whether O5 is a cost or a margin.
5. **GWW decree ceiling levels (2028) and award factors** (how much MKI value reaches the supplier).
