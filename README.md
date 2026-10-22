# Circular concrete business case — Netherlands (2026)

An objective business case for a **circular ready-mix concrete plant** in the Netherlands, made with recycled concrete aggregate and low-clinker cement. It was produced by a multi-agent research team: research → cost model → viability gate → options → red-team review → report and deck. Prices are in real 2026 €, excl. VAT. Discount rate: 8% real.

## Verdict in three sentences

1. A stand-alone circular ready-mix plant is **NOT VIABLE**. NPV is **−€5.33M** at 8% real, IRR −13.9%, there is no payback within 10 years, and it needs **€7.09M** of funding. It fails 3 of the 4 viability tests that were fixed *before* modelling (`plan.md` §2.1).
2. The circular product itself is not the problem. It is about **€2.5/m³ cheaper** to make than the Dutch standard mix. The plant is the problem: in a mature, consolidating market it earns about **€4.6/m³ EBITDA**, but it needs about **€11.7/m³** to repay its capital. "Green" levers (green premium, ETS, MKI) barely move the result, because Dutch competitors already use low-CO₂ CEM III/B cement.
3. None of the 10 options and 2 packages tested reaches NPV ≥ 0. The best plant route, buying an existing plant, gives −€3.5M. The integrated package P2 ranges from −€6.8M to −€1.4M. **Recommendation: no investment.** At most, run a €50–100k due-diligence phase with hard stop rules (gates A–C in the deck, slide 14).

## What is where

| Folder / file | Contents |
|---|---|
| `plan.md` | Scope, client choices (archetype B, national scope, 8% rate, investor/jury audience), viability criteria fixed in advance, team and phases |
| `research/policy.md` | Dutch and EU policy: Betonakkoord, MPG/MKI, GWW decree, norms (NEN 8005, CUR 112), ETS/CBAM, landfill tax, permits, subsidies, timeline 2026–2035 |
| `research/market.md` | Market size (ERMCO 2023: 6.0 Mm³ ready-mix), rubble flows, prices, customer segments, green premium evidence, TAM/SAM/SOM, regions |
| `research/technology.md` | Process flow, mass balance, mix designs, CO₂/MKI, plant capex, logistics, TRL; why ready-mix (B1) and not prefab (B2) |
| `research/competitors.md` | Players (SL Materials, everox, Heidelberg, Holcim, …), positioning, Five Forces, gaps, partners |
| `research/price_breakdown.md` | Unit cost and price breakdown €/m³, circular vs conventional; MKI method reconciliation |
| `research/viability_gate.md` | Phase 3 gate result (and the re-run after the critique) |
| `research/viability_options.md` | 10 options + 2 packages tested in the model; what the business depends on |
| `research/value_proposition.md` | Selling points per segment, honest weak points, Business Model Canvas, pricing, roadmap with go/no-go gates |
| `research/sources.md`, `research/assumptions.md` | Merged registers of all sources (IDs POL/MKT/TEC/CMP/CST/OPT/FIX) and assumptions (low/base/high, confidence) |
| `model/` | `inputs.csv` (all inputs), `model_core.py` + `options.py` (Python model), `build_model.py` (Excel with live formulas), `financial_model.xlsx`, `check_report.md` (Excel = Python in 23 cases), `model_summary.md`, `results*.json`, `charts/` |
| `review/critique.md`, `review/response.md` | Independent red-team review (24 issues) and how each one was handled, with before/after KPIs |
| `report/business_plan.docx` (+ `.md`) | Full business plan, 11 sections + appendices, ~30 pages |
| `deck/pitch_deck.pptx` | 15-slide pitch deck with speaker notes on every slide |

**Re-run everything:** `python3 model/run_all.py` (model, Excel, checks, charts), then `python3 report/build_report.py` and `python3 deck/build_deck.py`. LibreOffice is needed for the Excel recalculation check.

## Top 3 uncertainties

1. **Selling price (€135/m³ plant average, confidence low).** This is the biggest driver: from €115 to €155/m³ the NPV swings by about €14.5M. The price rests on a secondary source plus a Belgian retail price list. Real Dutch B2B project prices are not public and are probably lower, which would make the verdict stronger.
2. **Capex and plant purchase price.** There is no public Dutch quote for a new plant (€5.5M, range €4–8M) and no transaction evidence for buying one (about €2.5M for a ~35k m³ plant). Both are estimates.
3. **Gate fee and by-product values for own crushing.** The evidence says clean rubble is accepted at €0–1/t. The integrated route would need about €30/t to break even. Steel yield and how the steel value is split with a partner are not verified.

## What data would most change the conclusion

- **Real B2B ready-mix prices and margins in the chosen region**, from 3–5 contractor quotes or a producer's accounts. The base case needs about €154/m³ (+€19, +14%) to reach NPV = 0, so only a large price error would change the verdict.
- **Signed deal terms:** an existing plant offered for ≤ €2.5M, a long rubble contract with a gate fee far above today's €0–1/t, and framework contracts for ≥ 40k m³/yr. These are gates A–C. Without them, no route is viable.
- **Evidence that public clients pay in cash for low MKI**, not only as a fictive tender discount to the contractor. This only matters if the product becomes clearly lower-CO₂ than CEM III/B, for example with a recycled cement paste binder.
- **Expert interviews** (none were done) with a ready-mix plant manager, a demolition/recycling firm and a Rijkswaterstaat tender manager. These would reduce the three uncertainties above fastest.

## Method notes and honest limits

- Every number is labelled **[VERIFIED]**, **[ESTIMATE]** or **[ASSUMPTION]**, with a source or assumption ID.
- The verdict is robust against the model's conservative choices. With 100% cost pass-through, book-value salvage and working-capital release all applied, NPV is still −€3.4M.
- The pessimistic and optimistic scenarios move all inputs together. Treat them as stress bounds, not likely cases.
- Only public web sources were used. Several important prices (gate fees, B2B concrete prices, plant transaction prices) are not published. For these, Belgian or international proxies were used and marked.
