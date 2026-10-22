# Plan — Circular concrete business case (Netherlands)

Status: **Phase 0 done. Waiting for the client to confirm the defaults (section 2) before Phase 1.**
Date: 2026-10-22

---

## 1. Scope

**Question:** Can a new circular concrete business in the Netherlands be financially viable from 2027–2036? If not, what would have to change to make it viable?

**In scope**
- Dutch market. EU policy where it affects Dutch prices (ETS, CBAM, CPR).
- A screening comparison of four archetypes (A–D, see 2.3).
- A detailed financial model for the chosen archetype. Variants are tested as scenarios.
- 10-year horizon (2027–2036). Prices in real 2026 euros.

**Out of scope**
- Engineering design of a plant (we use benchmark capex and capacity from literature and suppliers).
- Legal advice on permits (we describe the process and timeline only).
- Cement plant investments (CCS, kilns). We treat cement as a bought input.

---

## 2. Defaults for the `[FILL IN]` fields (please confirm or change)

| Field | Proposed default | Why |
|---|---|---|
| Intended use | **Academic business case (course assignment / thesis input), written so it can also work as an early startup pitch** | Most likely use for a first-year MSc student. Keeps the tone objective, not salesy. |
| Deck audience | **Professors and an early-stage investor / municipality panel** | One deck that works for both: method visible, verdict up front. |
| Archetype | **Compare A–D at screening level. Model A (recycling hub) in depth. Test A+B and A+C hybrids as viability options in Phase 3.** | A is the most data-rich (gate fees, aggregate prices, equipment costs are public) and is the base for B and C. D (platform) has little hard financial data, so it gets a qualitative screen plus a simple model. |
| Region | **Zuid-Holland (Rotterdam–The Hague–Delft), with the Randstad as the wider market** | Large demolition and construction volumes, port logistics, close to TU Delft research. Short transport distances matter a lot for a low-value bulk product. |
| Starting capital | **Unknown → the model calculates the capital needed and proposes a funding mix (equity, bank loan, subsidies)** | Avoids fixing a number that would bias the plant size. |
| Discount rate | **10% real (base); test 8% and 12%** | Typical for an industrial start-up with proven but niche technology. |

### 2.1 Viability criteria (fixed now, before any results)

The base case is **viable** only if **all** of these hold:
1. NPV > 0 at a 10% discount rate (10 years, with terminal value limited to the salvage value of the equipment — no growth perpetuity).
2. Payback period < 7 years.
3. EBITDA positive by year 3 at the latest.
4. Still NPV > 0 in the *low* scenario for at least two of the six main sensitivity drivers taken one at a time (robustness check).

**Borderline:** criteria 1–3 hold but 4 fails, OR NPV is between −10% and 0% of the initial capex.
**Not viable:** anything else.

If the result is borderline or not viable, Agent 7 (viability strategist) starts.

### 2.2 Units and conventions
- Mass: tonne (t). Volume: m³. Use 2.4 t/m³ for concrete and ~1.5 t/m³ for loose aggregate unless a source gives another value.
- Prices: € 2026, excluding VAT. Always say ex-works or delivered.
- Inflation conversion: CBS CPI (or a sector index such as CBS GWW input prices when available).
- Claim labels: **[VERIFIED]**, **[ESTIMATE]**, **[ASSUMPTION]**.

### 2.3 Archetypes
- **A. Recycling hub** — high-grade crushing/separation of demolition concrete into recycled coarse aggregate, sand and cement-rich fines.
- **B. Circular ready-mix / prefab** — uses recycled aggregates and low-clinker binders.
- **C. Element reuse** — deconstruction, testing, recertification and resale of whole elements.
- **D. Platform / chain orchestrator** — matching supply and demand, material passports.

---

## 3. Team, questions and outputs

Budget per agent: about 40–60 tool calls. Each agent writes to files and returns a short summary (max ~200 words + file paths).

### Phase 1 — Research (parallel)

**Agent 1 — Policy & regulation** → `research/policy.md`
1. What is the current status of the Betonakkoord targets (CO₂ −30% by 2021, −49% by 2030; high-grade reuse by 2030)? Latest progress report?
2. Current MPG limits (homes, offices) and the confirmed/planned tightening path with dates.
3. How do MKI/DuboCalc and EMVI/BPKV work in tenders of Rijkswaterstaat, ProRail and municipalities? How large is the fictive discount for a lower MKI (with real examples)?
4. Which norms govern recycled aggregate in structural concrete (NEN-EN 206, NEN 8005, NEN-EN 12620, BRL 2506) and what replacement percentages are allowed?
5. EU ETS free-allocation phase-out for cement and CBAM definitive phase from 2026: timeline and expected effect on cement/clinker price (€/t).
6. Dutch landfill tax and any (proposed) levy on primary raw materials.
7. Permits under the Omgevingswet for a crushing plant (environmental activity, noise, dust, timeline).
8. Subsidies: MIA/Vamil, DEI+, WBSO, regional funds, EU Innovation Fund — what fits and how much.
9. Timeline table 2026–2035 with a certainty rating per item.

**Agent 2 — Market & demand** → `research/market.md`
1. Concrete production in NL (m³/yr) and cement use (t/yr).
2. Concrete waste released per year (t/yr) and its current destinations (road base, high-grade reuse, landfill, export).
3. Demand for primary aggregates (gravel, sand) and their prices.
4. Public vs private share of concrete demand.
5. Customer segments and their buying drivers.
6. Evidence of willingness to pay / green premium (tenders, surveys, price data).
7. TAM / SAM / SOM for Zuid-Holland and NL.

**Agent 3 — Technology & supply chain** → `research/technology.md`
1. Process flow for A (and the extra steps for B and C).
2. Mass balance per tonne of input: coarse aggregate, sand, fines, residues — for conventional crushing vs advanced technologies (e.g. ADR, SmartCrusher-type, thermal/mechanical).
3. Quality issues and how they are tested (water absorption, adhered mortar, contamination, chlorides, ASR).
4. Equipment: capex, capacity (t/h), energy use (kWh/t), wear, staff, area needed.
5. Logistics: typical transport distances and modes (truck, inland ship).
6. Technology readiness level per technology.

**Agent 4 — Competitors & landscape** → `research/competitors.md`
1. Verify the listed players (SlimBreker / Smart Crusher, C2CA, New Horizon Urban Mining, Rutte Groep, Fieldlab Circulair Beton, prefab producers, cement producers with low-clinker products). What do they actually do today?
2. Other recyclers, demolition firms, ready-mix producers in Zuid-Holland.
3. Public prices, scale, capacity.
4. Positioning matrix + Porter's Five Forces + gaps in the market.

### Phase 2 — Economics (after Phase 1)

**Agent 5 — Cost & price** → `research/price_breakdown.md`, `model/inputs.csv`
- Unit cost breakdown (€/t and €/m³) for the circular product vs the conventional product: input/gate fee, transport, processing, testing/certification, binder (incl. ETS/CBAM), overhead, margin, by-product revenue.
- Every line: low / base / high + source or assumption ID.

**Agent 6 — Financial model** → `model/financial_model.xlsx` (with live formulas), `model/*.py`, `model/charts/`, `model/model_summary.md`
- Capex, opex, revenue, 10-year P&L and cash flow, NPV, IRR, payback, break-even volume, unit economics.
- Low / base / high scenarios. Tornado on: green premium, gate fee, transport distance, cement/ETS price, utilisation, capex.
- Scripts must run end-to-end and the totals must reconcile.

### Phase 3 — Viability gate (orchestrator)
- Apply the criteria from 2.1 (fixed above). If borderline/not viable → **Agent 7** tests ≥ 5 options in the model → `research/viability_options.md` + extra scenario sheets.

### Phase 4 — Value proposition & go-to-market
**Agent 8** → `research/value_proposition.md`: selling points per segment (with numbers), honest weak points, Business Model Canvas, pricing strategy, first 3 target customer *types*, 3-year roadmap.

### Phase 5 — Red team
**Agent 9 (independent critic)** → `review/critique.md`: check numbers vs sources, re-run model, flag issues (high/medium/low). Orchestrator fixes all high issues and answers the rest in `review/response.md`.

### Phase 6 — Deliverables
**Agent 10** → `report/business_plan.docx` + `.md`, `deck/pitch_deck.pptx` (12–15 slides, speaker notes, charts from `model/charts/`).

### Phase 7 — Final check (orchestrator)
- Cross-check numbers in report, deck and model. All charts render. No `[FILL IN]` left. Write `README.md` (contents, verdict in 3 sentences, top 3 uncertainties, what data would change the conclusion).

---

## 4. Shared files
- `research/sources.md` — every source: title, URL, date accessed, what it supports.
- `research/assumptions.md` — every assumption: ID, value, unit, reasoning, low/base/high, confidence.

## 5. Known limits of this setup (said up front)
- Agents can only use public web sources. Many real prices (gate fees, aggregate prices, tender scores) are not published or are only in trade press. Where this happens we use ranges and mark them **[ASSUMPTION]**.
- No interviews with industry experts. Some numbers that an expert could give in 5 minutes will stay uncertain. The README will list which interviews would reduce the uncertainty most.
