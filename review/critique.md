# Red-team critique — circular concrete business case (Agent 9)

Date: 2026-10-22. Reviewer: Agent 9 (independent critic). I did not write any of the work reviewed. I did not change any project file. Re-running `run_all.py` rewrites `financial_model.xlsx`, so I restored the original copy afterwards.
Scope: `research/` (policy, market, technology, competitors, price_breakdown, viability_gate, viability_options, sources, assumptions), `model/` (inputs.csv, model_core.py, options.py, build_model.py, run_all.py, xlsx, model_summary, check_report, results*.json, all 7 charts). `research/value_proposition.md` did not exist when I finished, so I did not review it.

---

## 1. Summary

**What I did**
- Re-ran `python3 model/run_all.py`. All 18 Excel–Python cases match. The results did not change: base NPV −€4,481,665 and P2 NPV +€414.
- Recomputed the base NPV by hand from the yearly FCF: −€4,481,665, an exact match.
- Checked these identities in every year: revenue − opex = EBITDA, and FCF = NI + D&A − ΔWC − capex − sustaining capex + salvage. The difference is 0.
- Checked the IRR (NPV at the IRR = 0), the tax and loss carry-forward logic, depreciation timing and discounting (t = 0 is undiscounted, end-of-year convention). **No arithmetic or logic errors found.**
- Spot-checked 12 sources on the web or from the PDFs.
- Ran about 30 what-if cases on the base case and on P2.

**Main findings**
1. **The base-case verdict NOT VIABLE is robust.** The model has some conservative choices: 80% price pass-through, 25% salvage, no working-capital release and no tax loss on disposal. Undoing all of them together still leaves NPV at about −€2.7M. The optimistic biases I found (10 m³ truck loads, 3% public premium, sales from 2027, a premium-friendly price source) all push NPV further down. Under the fixed plan.md §2.1 rules, no plausible correction makes the base case BORDERLINE or VIABLE.
2. **The headline "P2 reaches break-even (+€414, IRR 8.0%)" is overstated. This is the most important problem in the work.**
   - P2 stacks favourable choices:
     - the "high" volume input of 90k m³;
     - the framework ramp-up (75/95%) overriding the slower ramp of an acquired plant;
     - a gate fee of €5/t, above the only bulk price evidence (€0/t for clean rubble);
     - a 3% steel yield (unverified) that stays with us;
     - sales from 1 Jan 2027, although the purchase gates only close in Q2 2027;
     - a delivery distance rounded down (22.7 → 22 km).
   - Each of these alone takes P2 below zero.
   - With evidence-consistent values (sales 2028, steel 1%, gate fee €1/t), P2 is about **−€1.2M**.
   - If we also add 9 m³ truck loads and no public premium, P2 is about **−€2.4M**.
   - P2's NPV lands within €414 of zero after about 17 discretionary round-number choices. I found no proof of tuning, but it should not be presented as "+€0.0M".
3. **The single most important number, the plant-average price of €135/m³, rests on a secondary supplier blog** (MKT-27, Dutch Fiber Trading). It is the #1 tornado driver: a swing of €14.5M. The same research cites a primary price list (GWL, MKT-20) that gives C20/25 €130 and C30/37 €139.5–144.5 delivered within 20 km. That is a retail list, so B2B project prices are likely *lower*. The figure needs triangulation, but the likely error points to "less viable", not "more viable".
4. **The green premium evidence is one-sided.** The research cites supplier surcharges for recycled aggregate (Heidelberg evoBuild R30/R50/R100: +€3.30/5.50/11.00, verified). It omits that the same GWL list it cites (MKT-20) sells **"Stortbeton recup" (recycled-aggregate concrete) about €20/m³ cheaper** than virgin concrete at equal cement content. Also, the modelled circular mix emits slightly *more* CO₂ than the standard CEM III/B mix (132 vs 129 kg/m³), so a 3% public premium is weakly supported.
5. **Double counting.**
   - The base model does not double count: `mki_value_to_supplier` is a memo row that `run()` does not use, and there is no gate fee in B1.
   - In O5, the +€1.5/m³ "MKI value" is added on top of a 3% public premium that A-MKT-25 already attributes to the MKI-driven public segment. This is a partial double count, but small, and O5 is negative anyway.
   - In O1/O2/P1/P2, the gate fee and the RCA credit are separate cash flows, not a double count. But the credit values mobile-crushed on-site RCA at the price of certified, washed, delivered RCA (€24.5/t), with no washing or screening cost.

**Issue count:** 5 High, 10 Medium, 9 Low.

---

## 2. Key-number check (the ~25 numbers that drive the verdict)

| # | Number (base) | In registers? | Label OK? | Source supports it? | Comment |
|---|---|---|---|---|---|
| 1 | Plant-average price €135/m³ delivered (115–155) | A-MKT-16, MKT-27 | Labelled M; should be L | **Partly.** I verified that the MKT-27 blog says C20/25 €110–130 and C30/37 €140–165. It is a fibre supplier's consumer page, not a primary source. GWL primary list: C20/25 €130, C30/37 €139.5–144.5 (retail, BE, ≤20 km). | Issue H1 |
| 2 | C30/37 project price €145 | A-MKT-18 | OK | As above | Memo only |
| 3 | List prices €203–212 (Holcim), "project ≈ 60–70% of list" | MKT-24 | – | The list prices are cited. **The 60–70% ratio has no source.** | M |
| 4 | CEM III/B €110/t delivered | A-CST-12, CST-14 | L, correct | Argus says EU cement is in the "mid-to-high US$100s/t". No NL list exists; the range 95–130 is honest. | OK |
| 5 | Gravel €32/t, sand €19/t delivered | A-MKT-11/12, MKT-20 | L, correct | GWL pick-up gravel 4/16 and sand 0/4 prices are cited (I could not read that page of the PDF; the ready-mix and rubble pages were readable). These are retail pick-up proxies. | OK as proxy |
| 6 | RCA €15/t ex-works, €24.5/t delivered | A-MKT-13, MKT-20 | L, correct | BE betongranulaat €9.5–18/t; the arithmetic 15 + 30×0.25 + 2 = 24.5 is correct | OK |
| 7 | Gate fee €5/t (−2 to 15) | A-MKT-15 | L | **No.** GWL (verified): "Zuiver betonpuin < 20% zand: 0 €/ton". Reinforced or large pieces cost the deliverer **+€3.5/t**. The NL €20/t counter tariff is for small, mixed loads. The bulk evidence points to €0–1/t. | Issue H3 |
| 8 | Steel yield 3%, €150/t | A-TEC-03, A-OPT-24, CST-16 | L; "domain knowledge, not verified" | **Not supported.** GWL charges *more* for reinforced rubble, so steel is not a free bonus. | Issue H3 |
| 9 | Contract crushing €7.5/t | A-OPT-05, OPT-04 | L | One UK contractor's web page (my fetch failed with HTTP 503). Weak anchor. | L5 |
| 10 | Capex €5.5M (4.0–8.0) | A-TEC-21, A-CST-02 | L, correct | No NL quote. The BE reference is €11M for >150k m³ including a builders' merchant. The range is plausible. | L |
| 11 | Plant purchase €2.5M (1.5–4.0) | A-OPT-06 | ESTIMATE, L | No transaction evidence. I could not confirm the OPT-01 "≈€18M" or the "€38.9M ready-mix EBITDA" in search. I did confirm that Cementir bought one plant plus a minority stake in April 2024. | M6 |
| 12 | Volume 70k m³ (50–90k) | A-TEC-24, A-MKT-32 | L | ERMCO verified: NL 6.0 Mm³, 178 plants, 33.7k m³/plant (2023). A-MKT-32 uses 37k (7.4 Mm³/200). Small inconsistency. | L7 |
| 13 | Ramp-up 50/79/100% | A-CST-01 | L | Judgement | OK |
| 14 | Delivery €9 + €0.5/km × 20 km = €19/m³ | A-TEC-28/29, A-CST-27 | M | The formula assumes **10 m³ loads**. ERMCO: 83% of truck mixers are 8 to <10 m³ and only 7% are ≥10 m³. Heidelberg's small-load surcharge applies below 9 m³. | M2 |
| 15 | Staff 7 + 3 FTE at €70k / €90k | A-CST-20/21, CST-06 | M | **Verified:** CAO wages €3,393.87–3,770, 8% holiday pay, 30% unsocial-hours bonus | OK |
| 16 | SG&A non-staff €300k | A-CST-25 | L, judgement | Plausible | OK |
| 17 | Green premium 3% public / 0% private | A-MKT-25/26 | L | Heidelberg surcharges verified, and PBL "~10% dearer, buys on lowest price" verified. **GWL "recup" concrete ~€20/m³ cheaper is omitted.** | M3 |
| 18 | MKI values (CEM III/B 8.6, circular 8.5 €/m³) | POL-01, A-CST-29 | – | Consistent with ProRail (verified: "Gunningsvoordeel ± 25% (factor 4 × MKI-referentiewaarde)"). MKI is not in the cash model, which is correct. | OK |
| 19 | ETS path and free-allocation phase-out | A-POL-01..08, POL-39 | M | The phase-out table (2.5%…100% by 2034) is current law. The 17 July 2026 proposal (end in 2038) is noted. EUA forecasts are probably nominal but are used as real. | L8 |
| 20 | Cement carbon pass-through 85% / concrete pass-through 80% | A-POL-09, A-CST-13 | L | No source. Together they build in a steady margin squeeze. | M4 |
| 21 | Discount rate 8% real | plan.md | OK | Client choice | OK |
| 22 | Vpb 19% / 25.8%, threshold €200k | A-CST-30 | M | Correct for 2024–2026 | OK |
| 23 | MIA 36% × 25.8% = 9.3% | A-POL-21, POL-68 | M | **Verified:** 2026 tiers 45/36/27%; codes A/D = 36% | OK |
| 24 | Working capital 60/10/30 days, not released | A-CST-07 | L | Judgement; conservative | L2 |
| 25 | Salvage 25% of plant + civil | A-CST-06, plan §2.1 | L | Plan-mandated "salvage value of equipment". Book value would be 60%. | L1 |
| 26 | Grant €0.4M | A-POL-24 | L | Uncertain. "No grant" already tested. | OK |

---

## 3. Issue table

| ID | Severity | File / location | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| H1 | High | `inputs.csv` price_plant_avg_all_classes; A-MKT-16; MKT-27 | The #1 value driver (€135/m³; tornado swing €14.5M) rests on a secondary supplier blog. Its confidence is labelled M. The "project ≈ 60–70% of list" ratio has no source. | I verified that MKT-27 is a Dutch Fiber Trading consumer page. The primary GWL list in the research's own MKT-20 gives retail delivered prices of C20/25 €130 and C30/37 €139.5–144.5 within 20 km. B2B contract prices are normally below retail. | Re-label as L. Triangulate with GWL stortbeton (primary), the Heidelberg list minus typical discounts, and CBS producer prices or ERMCO turnover/m³. Present €135 as "likely at or above the market average". State that this strengthens the NOT VIABLE verdict. |
| H2 | High | `viability_options.md` §0 item 4, §4 P2; `options_npv.png`; `results_options.json` | **P2 "break-even" (+€414, IRR 8.0%) is presented with false precision and is fragile. Any one of at least 8 evidence-based changes makes it negative.** The headline "integration brings it to break-even" is not robust. | My runs (base P2 = +€0.0M): sales 2028 −€0.24M; steel 1% −€0.43M; steel stays with partner −€0.64M; gate fee €0 −€0.71M; gate fee €1 −€0.57M; ramp 55/85 −€0.46M; 23 km −€0.22M; purchase €3.0M −€0.55M; no grant −€0.32M; 9 m³ loads −€0.96M. Stacked: delay + steel 1% + gate €1 = **−€1.23M**; plus 9 m³ loads and public premium 0 = **−€2.41M**. With sales from 2028 and 1% steel, P2 needs a gate fee of €9.7/t for NPV = 0. | Report P2 as "about −€1M (range −€2.4M to +€1.4M); break-even only if the gate fee is ≥ ~€10/t **and** the steel stays with us". Show the stacked downside next to the upside. Add "steel-scrap split" and "gate fee ≥ €10/t" as hard gates, not targets. |
| H3 | High | A-MKT-15, A-TEC-03, A-OPT-24; `options.py` CRUSH_PARTNER | The gate fee of €5/t and the 3% steel yield at €150/t (about €9.5/t of value combined, ~85% of the crushing line's net result together with the RCA credit spread) go against the bulk evidence in the research's own source. The partner deal is also internally odd: the partner pays us €5/t, leaves us the steel worth €4.5/t, and crushes for only €7.5/t. | GWL (MKT-20, verified): clean concrete rubble accepted at **€0/t**. Reinforced or large rubble costs the deliverer **+€3.5/t**, so steel removal is a cost the crusher charges for, not a windfall. The steel yield is labelled "domain knowledge, not verified". Steel = 41% of the crushing net result (182k of 446k €/yr), which I recomputed. | Base gate fee €0–1/t; steel 1% or split 50/50 with the partner. Keep €5/t and 3% as an upside case. Rerun P1/P2 and update §6 ("gate fee is the biggest lever"). |
| H4 | High | `options.py` P2 = merge(ACQ, CRUSH_PARTNER, OFFTAKE, SCALE90); viability_options §7 | **Timing and ramp inconsistency in P2.** The gates "before money is committed" target Q2 2027. Yet the model books the purchase in 2026 and full-year 2027 sales of **67.5k m³**: 75% of 90k, because the OFFTAKE ramp silently overrides the ACQ ramp (55/85). That is twice an average Dutch plant in the takeover year. A-OPT-08 also defines the acquired ramp as a % of **70k**, not 90k. | `mc.run(P2)['params']`: ramp 75/95. Volume 2027 = 67.5k. ERMCO average plant = 33.7k m³ (verified). | Model P2 with first sales in 2028, or mid-2027 at minimum, and with an acquisition-specific ramp of about 55/85% of 90k. Document the override order in options.py. |
| H5 | High | P2 selection; A-OPT-17; viability_options §0 item 4 ("We did not tune it") | **Cherry-picking and an appearance of tuning.** P2 combines the "high" utilisation input with the most favourable values of other discretionary inputs. 90k m³ = 2.7× the national average plant = 9% of all ready-mix in the radius, from an acquired plant. The delivery distance for 90k should be 20 × √(90/70) = 22.7 km but is rounded **down** to 22; O8 likewise uses 23.9 → 23. NPV landing within €414 of zero from round-number inputs is very unlikely by chance. | Recomputed: P2 at 22.7 km = −€0.15M; at 23 km = −€0.22M; 9 FTE instead of 8 = −€0.36M. P2 needs exactly 89,996 m³ for NPV = 0. | Remove the "+€414" wording. Use consistent rounding (or the exact 22.7 km). Present P2 as a scenario that combines favourable inputs, and say so explicitly to the jury. |
| M1 | Medium | `viability_gate.md`, model base timing | Sales from 2027 in the gated base case. This is acknowledged, and O0 corrects it. Fine for the verdict, but the deck must use O0 or show both. | O0 = −€4.38M | Use O0 as the reference in the deck. |
| M2 | Medium | A-TEC-28 delivery formula | Assumes 10 m³ per trip. Most truck mixers are 8 to <10 m³, and Heidelberg charges a small-load surcharge only below 9 m³, so the average real load is ≤9 m³. | ERMCO 2023 (verified): 9.9% ≤8 m³, 82.9% 8–<10 m³, 7.2% ≥10 m³. A 9 m³ load gives base −€5.36M (−€0.9M) and P2 −€0.96M. | Use a 9 m³ base load (8–10 range). Optionally add small-load surcharge revenue. |
| M3 | Medium | A-MKT-25; market.md §6; inputs green_premium_public | The green premium evidence is one-sided (surcharges only). The modelled circular mix has slightly *higher* CO₂ than the standard mix (132 vs 129 kg/m³), so a 3% *public* cash premium has no MKI basis. | GWL list (MKT-20, verified): "Stortbeton recup" 300 kg €109 vs virgin 300 kg €129 (−15%). PBL MKT-47 verified: "large part of the sector goes for the lowest price". Premium 0 gives base −€0.40M and P2 −€0.41M. | Set the public premium base to 0–1.5% (keep 3% as the high case), or justify it with tender evidence. Cite the GWL discount as counter-evidence. |
| M4 | Medium | A-POL-09 (85%), A-CST-13 (80%), slag uplift | The structural margin squeeze from 2030 (EBITDA €0.53M → €0.37M) comes entirely from two unsourced pass-through assumptions. Because all competitors use CEM III/B, long-run pass-through of an industry-wide cost is usually close to 100%. | Concrete pass-through 100% → base +€0.33M | Label both as key judgement calls. Show "100% pass-through" as a sensitivity in the summary. It does not change the verdict. |
| M5 | Medium | `model_core.py` crusher block, `cr_rca_credit` | Own mobile-crushed RCA is credited at the delivered price of *certified, washed* RCA (€24.5/t). No washing or extra screening cost is included, and the partner's €7.5/t covers crushing only. BRL 2506 certification (€25k/yr) is included. | Credit = 23.5 kt × €24.5 = €0.58M/yr | Add a washing/screening cost (€2–4/t) or credit at ex-works minus a quality discount. Test it in P2. |
| M6 | Medium | A-OPT-06, OPT-01, OPT-02 | Purchase price ≤ €2.5M has no Dutch transaction evidence. The OPT-01 and OPT-02 figures are "search excerpt read". I could not confirm the €18M Danish deal price, the €38.9M segment EBITDA or the 8% margin. Also, a plant priced on ~34k m³ EBITDA is then assumed to deliver 90k m³. | Cementir FY2024 release: plant + minority stake bought April 2024 (confirmed); price and margin not found in my search. Cemnet: 4K-Beton (18 plants, 0.6 Mm³) EBITDA €2.9M on €50.7M = 5.7%, which supports thin ready-mix margins. | Re-label OPT-01/02 as unverified, or fetch the full PDF. Add the 4K-Beton data point. State that €2.5M buys a ~35k m³ plant, and that the extra capacity and customers come at extra cost. |
| M7 | Medium | O5 / A-OPT-13 vs A-MKT-25 | Partial double count: the "MKI value captured in tenders" (+€1.5/m³) is added on top of a 3% public premium that is already justified as the MKI-driven segment. | A-MKT-25 text: "public/MKI-driven segment" | Net the two, or state that the 3% is not MKI-driven. O5 stays negative, so this is not verdict-relevant. |
| M8 | Medium | `model_summary.md` §2 "Plausible range −€16.0M to +€3.5M" | The root-sum-square of 21 drivers treats correlated drivers (price, cement, pass-through) as independent, and the result is not a probability interval. | – | Label it "indicative" or replace it with a small Monte Carlo. |
| M9 | Medium | Research overall: market size | Inconsistent market totals: ERMCO 6.0 Mm³ (2023), "~7.4 Mm³" (A-MKT-32), ACM ~8 Mm³ (2016), Betonhuis 14 Mm³ (all concrete). The SOM and "9–10% of ready-mix in radius" depend on which is used. | ERMCO verified 6.0 Mm³ / 178 plants / 33.7k | Use ERMCO 2023 everywhere for ready-mix. Explain that 14 Mm³ includes prefab and site concrete. |
| M10 | Medium | viability_options §7 "Recommended path" | Even if the numbers were right, the recommendation ("pursue P2 as a conditional acquisition play") is framed more positively than the criteria allow: P2 fails criterion 4 with 0/6 drivers and fails criterion 2. | §5 table | Frame it as "the only route that comes close; not investable on present evidence; worth a €50–100k diligence phase to test gates A–C". |
| L1 | Low | plan §2.1, A-CST-06 | The salvage-only terminal value (25%) values a 25-year asset at 25% after 10 years. The rule is plan-mandated and fine, but it is very strict for a jury. The tax loss on disposal (book value about €3.0M vs salvage €1.25M) is ignored, worth ~€0.2M PV. | Salvage at 60% (book) → base −€3.67M | Disclose. Show a memo with a going-concern TV. |
| L2 | Low | `model_core.py` WC | Working capital is not released in 2036 (memo +€0.6M). Conservative, and disclosed. | `npv_incl_wc_release_memo` −€3.89M | Keep it, and mention it with L1 as conservative choices worth about €1.4M together. |
| L3 | Low | `charts/ebitda_by_year.png` vs model_summary | The 2029 margin is shown as "6%" in the chart and "5.5%" in the text. | 0.53/9.57 = 5.5% | Show one decimal place. |
| L4 | Low | `charts/scenarios_npv.png` | The optimistic bound (+€30M, IRR 119%, payback 1.1 yr) invites misreading by a jury, even though it is labelled. | – | Drop it from the deck, or show the RSS / stacked-realistic range instead. |
| L5 | Low | OPT-04 | The contract-crushing anchor is one UK contractor's homepage. My fetch returned HTTP 503, so I could not verify it. | – | Mark it as an unverified anchor and look for an NL tariff. |
| L6 | Low | MKT-27 row in sources.md | It says "incl. regional transport". I could not see that wording in the page excerpt I fetched (the page mentions transport only as a cost driver). | Fetched page | Re-check the wording. |
| L7 | Low | A-MKT-32 vs CMP-43 | Average plant 37k (2016 basis) vs 33.7k (ERMCO 2023). | – | Align on 33.7k. |
| L8 | Low | inputs eua_price_* | EUA forecasts are typically nominal but are used as real 2026 €. This overstates the real carbon path by ~10–15% by 2034. Its effect on NPV is ≤€0.1M. | – | Deflate, or note it. |
| L9 | Low | `model_summary.md` §3 | The tornado omits the two combined "main driver" groups (transport, cement + ETS) that criterion 4 uses, so the reader cannot match the tables directly. | `SENSITIVITIES` list | Add a footnote. |

---

## 4. Model logic — what I checked and found correct

- **P&L and cash flow identities:** 0.0 difference in all years (my own recomputation from `run()` output).
- **NPV by hand:** sum(FCF_t / 1.08^t), t = 0..10, with t = 0 (2026) undiscounted = **−€4,481,665**. This equals the model. The yearly FCF is −5.48, −1.08, −0.27, +0.22, +0.45, +0.37, +0.37, +0.35, +0.32, +0.31, +1.55 €M (2036 includes €1.25M salvage).
- **IRR:** −7.06%. The NPV at that rate is about 0.
- **Tax:**
  - Losses are carried forward, so tax is first paid in 2035.
  - The grant is taxed as income, which is correct in NL.
  - The MIA is an extra deduction in the build year and enters the loss pool.
  - The two-bracket Vpb is correct.
  - Ignoring the 50% cap on loss relief above €1M is immaterial.
- **Depreciation:**
  - It starts in the first operating year.
  - Permits are written off over 10 years, plant and civil works over 25.
  - Sustaining capex is depreciated cumulatively.
  - Total D&A of €2.61M vs €5.5M capex is consistent with the lives.
- **Working capital:** receivables on revenue, inventory and payables on raw materials. Not released at the end (conservative).
- **Real vs nominal:** consistent: no inflation, 0.5% real wage growth, flat real prices. The only exception is L8.
- **Payback:** excludes salvage and is measured from 2026. That is a reasonable reading of the plan.
- **Excel = Python** in all 18 cases (`check_report.md`), confirmed by my re-run.
- **Criterion logic** in `viability()` applies plan §2.1 exactly, including the borderline OR-clause.

---

## 5. Source spot-checks (12)

| Source | Result |
|---|---|
| MKT-27 Dutch Fiber Trading | Exists. C20/25 €110–130 and C30/37 €140–165 confirmed. Secondary consumer blog (H1). |
| MKT-25 Heidelberg price list 2026 | Confirmed: base CEM III/B franco, full loads; C30/37 +€10.50; evoBuild R30/R50/R100 +€3.30/5.50/11.00; extra cement €0.20/kg, less cement €0.09/kg; CEM I +€22/m³; small load <9 m³ +€24/m³. |
| MKT-20 GWL price list | Confirmed: clean concrete rubble €0/t, reinforced +€3.5/t. **Not cited:** ready-mix C20/25 €130, C30/37 €139.5–144.5 delivered ≤20 km; "recup" concrete ~€20/m³ cheaper. |
| CMP-43 ERMCO 2023 | Confirmed: 6.0 Mm³, 178 plants, 33.7k m³/plant, 310 kg cement/m³. Also gives truck size shares (M2). |
| POL-24 ProRail MKI | Confirmed: "Gunningsvoordeel ± 25% (factor 4 x MKI-referentiewaarde)"; target 30% in 2025, 50% in 2030. |
| MKT-47 PBL Rutte | Confirmed: ~10% more expensive; lowest price; 400 kt; MRA ~2 Mt/yr. |
| CST-06 CAO Mortelbedrijven | Confirmed: €3,393.87–3,770; 8% holiday pay; 30% bonus. |
| POL-68 MIA 2026 | Confirmed: tiers 45/36/27%; A/D = 36%. |
| OPT-01 Cementir 2024 | Plant + minority stake bought in April 2024: confirmed. ≈€18M and €38.9M segment EBITDA: **not confirmed** (M6). |
| OPT-02 Cementir 8% ready-mix margin | **Not confirmed** in search. The 4K-Beton 5.7% data point is consistent with it. |
| OPT-04 SK Groundworks | HTTP 503: **unverifiable** (L5). |
| POL-01 / POL-39 | Not fetched; consistent with policy.md's internal tables. |

No fabricated URLs found among those checked.

---

## 6. Does the verdict hold?

- **Base case B1 (and O0): NOT VIABLE — holds, with high confidence.**
  - NPV is −€4.5M (−81% of capex), far outside the borderline band.
  - Undoing every conservative choice I found (100% pass-through, book-value salvage, WC release) still gives about −€2.7M.
  - Correcting the optimistic choices (truck load, premium, price source, timing) makes it worse.
  - Even 90k m³ plus all the conservative-choice reversals stays negative (−€1.1M; −€0.3M with WC release).
  - The diagnosis is sound: thin ready-mix margins (~€7.6/m³ EBITDA, consistent with the external 5.7–8% sector margins) cannot carry €5.5M of new capex. Selling price and volume dominate; "green" factors are small.
- **Options: "no option is VIABLE" — holds.** The verdict logic is applied correctly: P2 fails criteria 2 and 4, and P2 + subsidies → BORDERLINE is a correct reading of the rules.
- **"P2 reaches break-even" — does not hold as stated (H2–H5).**
  - On evidence-consistent inputs, P2 is about −€0.6M to −€1.2M, and down to −€2.4M if the delivery and premium corrections are added too.
  - It reaches zero only with a gate fee of about €10/t and our own steel recovery.
  - The jury message should be: *"The stand-alone circular plant is not viable. The best integrated route (acquire + crush + contracts) comes close to break-even only under favourable, still-unproven deal terms; it is not investable on present evidence."*
