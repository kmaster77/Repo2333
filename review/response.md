# Orchestrator response to the red-team critique

Date: 2026-10-22. Responds to `review/critique.md` (24 issues: 5 High, 10 Medium, 9 Low).
Rule from plan.md: all High issues are fixed; all others get a response.

## Decisions (made by the orchestrator before re-running the model)

### Base case changes (apply to `inputs.csv` base column; the old base stays reported as "original base" for traceability)
| Issue | Decision |
|---|---|
| M1 | **First sales in 2028** (build/permit 2026–2027). Becomes the new base. The 2027-start result is kept as a memo. |
| M2 | **Average truck load 9 m³** (range 8–10) in the delivery cost formula. |
| M3 | **Public green premium base 1.5%** (low 0%, high 3%). Add the GWL "recup" concrete discount as counter-evidence in market.md. |
| H1 | Keep €135/m³ as base, but re-label **confidence L**, add GWL primary list (C20/25 €130, C30/37 €139.5–144.5 retail, delivered ≤20 km) as triangulation, remove the unsourced "project ≈ 60–70% of list" claim or mark it [ASSUMPTION]. State that the price is more likely at/above the B2B average, so the error direction strengthens NOT VIABLE. |
| M9/L7 | Use ERMCO 2023 everywhere for ready-mix (6.0 Mm³, 178 plants, 33.7k m³/plant); explain that 14 Mm³ includes prefab and other concrete. |

### P2 and option fixes
| Issue | Decision |
|---|---|
| H3 | **Gate fee base €1/t** (low €0, high €10). **Steel yield 1%** base (low 0.5%, high 3%), and steel value **split 50/50 with the partner** in the base. €5/t and 3% move to the upside case. |
| M5 | Add **RCA washing/screening cost €3/t** (range 2–4) to own-crushed RCA. |
| H4 | P2 inherits first sales 2028 and uses an **acquisition ramp of 55% / 85% / 100%** of target volume. The override order is documented in `options.py` (later merge wins, explicit). |
| H5 | Use the exact formula for delivery distance (no rounding: 22.7 km at 90k, 23.9 km at 100k). Remove the "+€414" and "break-even" wording. Present P2 explicitly as a combination of favourable inputs. |
| M6 | Re-label OPT-01/OPT-02 as unverified. Add the 4K-Beton 5.7% EBITDA margin data point (from critique). State that ~€2.5M buys a ~35k m³ plant; reaching 90k needs extra capex. Add **+€1.0M** expansion capex to P2 (range 0.5–2.0), labelled [ASSUMPTION]. |
| H2 | Report P2 as a **range** (stacked downside / base / upside) and add the gate-fee-for-NPV=0 figure. Gates for "go": gate fee and steel split become hard gates. |
| M7 | O5: net the MKI value against the public premium (no double count). |
| M10 | Re-frame the recommendation: "No route is investable on present evidence. The integrated acquisition route is the only one that comes close; it is worth a small (€50–100k) due-diligence phase to test gates A–C, not an investment." |

### Presentation fixes
| Issue | Decision |
|---|---|
| M4 | Label both pass-through rates as key judgement calls; add a "100% pass-through" sensitivity line in model_summary.md. |
| M8 | Label the RSS range "indicative, not a probability interval". |
| L1, L2 | Disclose in model_summary.md: salvage-only terminal value and no WC release are conservative (memo values given). |
| L3 | Chart shows one decimal place. |
| L4 | Deck does not show the all-optimistic +€30M bar; it shows the realistic range instead. The model keeps it. |
| L5, L6 | Mark OPT-04 unverified; correct MKT-27 wording. |
| L8 | Note that EUA forecasts are probably nominal; effect ≤ €0.1M NPV. |
| L9 | Footnote in model_summary.md linking tornado and criterion-4 drivers. |

## Status
The table above records the decisions. Results after implementation are in section "Results after fixes" below (filled after re-running the model).

---

## Results after fixes

Implemented by the fix engineer on 2026-10-22. `python3 model/run_all.py` re-run; **Excel–Python check: ALL 23 CASES MATCH** (`model/check_report.md`; was 18 cases — added: memo case `O_orig` via the option selector, first sales 2027 + 8 m³ loads, first sales 2029, P2 downside and upside stacks). plan.md §2.1 criteria not changed. Nothing was tuned toward a result: every new value is the one decided above; ranges are the ones stated above.

### Per issue

| ID | What was changed (file) | Result |
|---|---|---|
| M1 | New input `first_sales_delay_yr` (base 1, low 0, high 2; fixed in scenario stacks) replaces the option hook `opt_start_delay` in `inputs.csv`, `model_core.py`, `build_model.py` (live formulas), `options.py`. A-FIX-01. | Base = permits 2026, build 2027, first sales 2028. Alone worth +€0.10M vs the original base (deferred capex ≈ lost first-year margin). |
| M2 | New inputs `delivery_truck_load_avg` (8/9/10 m³, revenue-type driver, in tornado) and `delivery_rates_reference_load` (10 m³); delivery €/m³ = (fixed + per-km × distance) × 10 / load (`inputs.csv`, `model_core.py`, `build_model.py`). A-FIX-02. | Delivery €19.0 → €21.1/m³. −€0.77M NPV. Tornado: 8 / 10 m³ → −€6.3M / −€4.6M. |
| M3 | `green_premium_public` 0 / **1.5** / 3% (`inputs.csv`); GWL "recup" counter-evidence in `market.md` §4 and §7, A-MKT-25, MKT-20. A-FIX-03. | −€0.18M NPV. Premium 0% / 3% → −€5.5M / −€5.2M. |
| H1 | €135/m³ kept; A-MKT-16 confidence M → **L**; GWL triangulation table and withdrawal of the "60–70% of list" claim in `market.md` §4; notes in `inputs.csv`, `price_breakdown.md`, `sources*.md` (MKT-20, MKT-27). | Text only. Error direction stated: at €130/m³ NPV −€7.1M → strengthens NOT VIABLE. |
| M9 / L7 | ERMCO 2023 (6.0 Mm³, 178 plants, 33.7k m³/plant) used for ready-mix in `market.md` §1, §5, §8 (TAM €2.7bn → €2.5bn; ready-mix SAM €0.43bn → €0.35bn; regional SAM 0.45 → 0.36 Mm³; SOM shares), A-MKT-32, A-OPT-17. 14 Mm³ explained as all concrete incl. prefab and other. | Text only; no model input uses the market size. |
| H3 | `hybrid_gate_fee_received` 0 / **1** / 10 €/t; `hybrid_yield_steel` 0.5 / **1** / 3%; new `hybrid_steel_value_share_retained` 0 / **50** / 100% (own line O1 = 100%). `inputs.csv`, `model_core.py`, `build_model.py`, `options.py`. A-FIX-04–06. | Crushing net (partner, full output) €0.45M → **€0.06M/yr**; O2 −€3.09M → −€5.42M (now −€0.09M vs base). |
| M5 | New input `hybrid_rca_washing_screening` 2 / **3** / 4 €/t on all coarse RCA produced (live row `o_cr_wash`). A-FIX-07. | −€0.26M on P2. |
| H4 | `options.py`: override order documented (later merge wins); `ACQ_RAMP` (55/85) listed last in **P1 and P2**; packages inherit first sales 2028. A-FIX-09. Note: also applied to P1 (same package logic; leaving P1 at 75/95 would make "P2 = P1 + scale" false). | P2 ramp −€0.40M; P2 volume 49.5k / 76.5k / 90k m³ in 2028/29/30. |
| H5 | Exact distance 20 × √(V/70k): 22.68 km (P2), 23.90 km (O8) in `options.py`; "+€414"/"break-even" wording removed from `viability_options.md`, `value_proposition.md`, `charts_options.py` (new title "No route is investable on present evidence…"); P2 described as a combination of favourable inputs. | −€0.14M on P2. Old P2 definition reproduced as a memo: +€414 (traceability, `results_options.json` → P2.stack). |
| M6 | OPT-01/OPT-02 marked UNVERIFIED (`sources.md`, `sources_options.md`); 4K-Beton 5.7% added (FIX-S01, A-OPT-06); "€2.5M buys a ~35k m³ plant" stated; **+€1.0M expansion capex** (range 0.5–2.0) in P2 via `opt_extra_capex_y0`. A-FIX-10. | −€0.88M on P2 (range €2.0M / €0.5M → −€4.90M / −€3.57M). |
| H2 | `options.p2_stack()`: stacked downside / base / upside + gate fee for NPV = 0 (base terms, steel 3% kept, other inputs at downside/upside); shown in `results_options.json`, Opt_Overview sheet, options chart (whisker), `viability_options.md` §4. Gate fee and steel split are **hard gates** (§7). A-FIX-12. | **P2 range −€6.77M / −€4.01M / −€1.42M.** Gate fee for NPV = 0: **€29.7/t** (base terms), €25.9/t (steel 3% kept 100%), €15.2/t (others at upside), €45.3/t (others at downside). |
| M7 | O5 MKI value netted against the public premium: +€1.5 − €0.81 = **+€0.69** per circular m³, computed from inputs in `options.py`. A-FIX-11. | O5 −€5.86M (−€0.53M vs base). |
| M10 | `viability_options.md` §0 and §7, `value_proposition.md` §0, §6, §7, `viability_gate.md`: "No route is investable on present evidence. The integrated acquisition route is the only one that comes close; it is worth a small (€50–100k) due-diligence phase to test gates A–C, not an investment." A-VP-05 marked superseded. | Honest nuance added: on the fixed inputs the acquisition alone (O3, −€3.54M) is as close as P1/P2; integration helps only if gate B is far better than the evidence. |
| M4 | Both pass-through rates labelled KEY JUDGEMENT CALL (`inputs.csv`, A-POL-09, A-CST-13, `model_summary.md` §1); "100% pass-through" lines in `model_summary.md` §2 and the Valuation sheet. | Concrete 100%: **−€4.93M** (+€0.40M); cement and concrete 100%: −€4.94M; P2 + 100%: −€3.63M. Verdict unchanged. |
| M8 | RSS range labelled "indicative, not a probability interval" (`model_summary.md`, Scenarios sheet). | −€15.3M to +€2.1M. |
| L1, L2 | Disclosed in `model_summary.md` §2 with memo values (also on the Valuation sheet). | Salvage at book value (64%): −€4.42M; WC release: −€4.74M; both + 100% pass-through: −€3.42M. |
| L3 | `charts.py`: margin labels and IRR labels with one decimal; all titles computed from results. | Checked: `ebitda_by_year.png` shows 3.4%, 2.6%, …; `scenarios_npv.png` IRR −13.9% / 103.7%. |
| L4 | No deck exists yet; the model and `scenarios_npv.png` keep the optimistic bar; `model_summary.md` §2 states the deck must show the realistic range (P2 range, indicative RSS range) instead. | For Agent 10. |
| L5, L6 | OPT-04 marked unverified (`sources*.md`, A-OPT-05, `viability_options.md` O2); MKT-27 wording corrected (no claim that prices include transport) in `sources.md`, `sources_market.md`, `market.md`. | Text only. |
| L8 | Note in `inputs.csv` (EUA rows) and `model_summary.md` §2. | Effect ≤ €0.1M NPV (whole ETS path swing €0.45M). |
| L9 | Footnote under the tornado table in `model_summary.md` §3 linking the combined criterion-4 drivers to their parts. | – |
| (other) | Workbook IRR formula now accepts only a root above −99% (the 2027 build year creates a second, meaningless root below −100% that LibreOffice found from guess 10%). UnitEconomics default year = 3rd operating year. | Needed for the Excel = Python check to pass. |

### Key KPIs before / after

| KPI | Before (original base, sales 2027) | After (new base, sales 2028) |
|---|---|---|
| NPV @ 8% real | −€4.48M (−81% of capex) | **−€5.33M (−97% of capex)** |
| IRR (real) | −7.1% | **−13.9%** |
| Payback | not reached | **not reached** |
| EBITDA 3rd operating year | +€0.53M (2029) | **+€0.32M (2030)** |
| Funding need | €6.84M | **€7.09M** |
| Criteria 1 / 2 / 3 / 4 | FAIL / FAIL / PASS / FAIL (0 of 6) | **FAIL / FAIL / PASS (narrowly) / FAIL (0 of 6)** |
| Verdict | NOT VIABLE | **NOT VIABLE** |
| NPV = 0 needs | 112k m³/yr or €149.2/m³ | 134k m³/yr or €154.0/m³ |
| Pessimistic / optimistic scenario NPV | −€38.3M / +€30.0M | −€35.5M / +€24.5M |
| Indicative RSS range | −€16.0M to +€3.5M | −€15.3M to +€2.1M |
| Best single plant option (O3 acquisition) | −€2.71M | −€3.54M |
| P1 | −€1.36M (IRR 2.1%, payback 9.8 yr) | −€3.97M (IRR −15.7%, not reached) |
| **P2** | **+€0.0M (+€414), IRR 8.0%, payback 7.3 yr, 2/4 criteria** | **−€4.01M, IRR −10.6%, not reached, 1/4 criteria, 0/6; range −€6.77M (downside) to −€1.42M (upside)** |
| Gate fee for P2 NPV = 0 | (≈ €5/t sufficed) | €29.7/t base terms; €15.2/t with all other inputs at upside |
| Options passing criterion 4 | none | none |

**Verdict after fixes:** base case **NOT VIABLE** (further from the borderline band than before). **No option or package is investable on present evidence**; every NPV is negative (−€2.5M to −€6.3M), none is BORDERLINE. The original base is kept as memo case `O_orig` (−€4,481,665, reproduced to the euro).
