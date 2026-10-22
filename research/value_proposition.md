# Value proposition & go-to-market — circular ready-mix, package P2

Agent 8 (Value proposition & go-to-market). Date: 2026-10-22. All money is in **real 2026 €, excl. VAT**. Concrete prices are **delivered to site**.
Labels: **[VERIFIED]** = source read by an earlier agent; **[ESTIMATE]** = calculated (calculation shown or model run named); **[ASSUMPTION]** = no source, reasoning given.
IDs: sources POL-, MKT-, TEC-, CMP-, CST-, OPT- and assumptions A-xxx- come from the earlier files. My own assumptions are in `research/assumptions_vp.md` (A-VP-01 … A-VP-10). My model runs (R-01 … R-20) are listed in **Appendix A**. No new web research was done.

**Numbers updated after the red-team critique (Phase 5).** The model now uses first sales in 2028, 9 m³ truck loads, a 1.5% public premium, a €1/t gate fee, 1% steel split 50/50 with the partner, €3/t RCA washing, the acquired-plant ramp and +€1.0M expansion capex for P2 (`review/response.md`). All P2 numbers and the runs in Appendix A were re-run on that basis. The structure and the selling points are unchanged; the conclusion is not: **P2 is no longer break-even (NPV −€4.0M, range −€6.8M to −€1.4M)**, so this go-to-market plan describes what a small due-diligence phase would test, not an investment plan.

Words used once and explained:
- **P2** = the closest (but not investable) concept: buy an existing ready-mix plant, let a demolition partner crush rubble on our site (we receive a gate fee), and sell 90k m³/yr, partly under framework contracts (viability_options.md §4).
- **RCA** = recycled concrete aggregate (crushed old concrete used instead of gravel).
- **Gate fee** = the price a demolition firm pays us to take its rubble.
- **MKI** = the Dutch environmental cost score in € per m³, used in public tenders. **MPG** = the legal environmental limit for new buildings, in € per m² floor area per year.
- **Framework contract** = a multi-year agreement on volume and price formula with one buyer.
- **CEM III/B** = blast-furnace slag cement, the Dutch standard binder. **CEM I** = ordinary Portland cement, high in CO₂.

---

## 0. Summary

1. **The honest core message.** Our circular mix is **cheaper to make** than the Dutch standard (−€2.5/m³) and has **31% recycled content**. But its **CO₂ is about the same** as the Dutch CEM III/B standard (132 vs 129 kg/m³). The big CO₂ gap exists only against CEM I (286 kg/m³), and CEM I is rare in Dutch ready-mix [ESTIMATE, price_breakdown.md §9, §12; VERIFIED, CMP-27].
2. **So we sell "circular at the standard price, with supply security", not "low-CO₂ at a premium".** Incumbents charge +€3.30 to +€5.50/m³ for 30–50% recycled content and +€5–9/m³ for low-CO₂ ECOPact [VERIFIED, MKT-25, CMP-35]. We can price circular at parity and still keep a €2.5/m³ cost edge.
3. **The strongest pitch is to the supply side, not the buyer side.** Demolition firms are losing their road-base outlet (concrete cap in mixed granulate 30% → 15% → 5% in 2025/2027/2030, MKT-11). We offer them a 7–10-year outlet plus paid crushing work. Owners of small, under-used ready-mix plants (178 plants, average 33.7k m³, market −20% in 2023, CMP-43) get an exit.
4. **Buyers to target first:** (1) mid-size GWW contractors with public framework or maintenance work in Zuid-Holland, (2) municipalities that must set MKI ceilings in every GWW tender from ~2028 (POL-17), (3) housing corporations with multi-year building programmes. Developers come later: their cash premium is ~0% (A-MKT-26).
5. **Pricing:** parity on private work, a small premium (≤3%, ≈€4/m³) only where MKI or circularity is scored, framework discount capped at −€1/m³ on average, cement-cost indexation, delivery-zone pricing and an under-load surcharge. On the supply side, P2 would need a gate fee of **≈ €30/t** for NPV = 0 (R-19), against €0–1/t in the bulk market (MKT-20). The gate fee and the steel split are **hard gates**.
6. **P2 is not investable on present evidence.** NPV **−€4.01M** (stacked range −€6.77M to −€1.42M), IRR −10.6%, payback not reached, 0 of 6 robustness tests passed [model, P2]. Even with the target terms (plant €2.0M, gate fee €10/t) it stays **NOT VIABLE**: NPV −€2.24M, 0 of 6 robustness tests (R-17).
7. **Roadmap:** a **€50–100k due-diligence phase** (critique M10) tests three gates by end of Q2 2027 (plant, rubble, frameworks). It is a test, not an investment: on today's evidence gate B fails. If any gate fails, **stop**. Asset-light licensing is a capped pilot at most, because it also loses money in the model (O6: NPV −€2.51M).

---

## 1. Selling points per customer segment

### 1.1 Facts the selling points rest on

| Metric (C30/37, per m³, 2026) | Our circular mix (50% coarse RCA, 345 kg CEM III/B) | Dutch standard (CEM III/B, 330 kg) | CEM I mix (320 kg) | Source |
|---|---|---|---|---|
| CO₂, A1–A3 (kg/m³) | **132** (111–157) | 129 (109–154) | 286 (244–323) | ESTIMATE, price_breakdown.md §12.3 |
| Difference vs our mix | – | **+3 kg (+2%) for us = no real gain** | **−154 kg (−54%) for us** | ESTIMATE |
| MKI, A1 set, Betonakkoord basis (€/m³) | **8.5** | 8.6 | 17.7 | ESTIMATE, price_breakdown.md §12.3 |
| MKI difference | – | **−€0.1 (≈0)** | **−€9.2** | ESTIMATE |
| MKI, generic NMD cat-3 data, A1–D (€/m³) | ~26.4 | 26.01 | 34.59 | VERIFIED NMD cards / TEC estimate, TEC-04 |
| Total cost, delivered (€/m³) | **133.1** | 135.6 | 144.0 | ESTIMATE, price_breakdown.md §9 |
| Cost difference | – | **−€2.5 for us** | **−€10.9 for us** | ESTIMATE |
| Recycled concrete in total aggregate | **31%** (560 / 1,810 kg) | 0% | 0% | ESTIMATE from the recipe, price_breakdown.md §2 |
| Gravel saved | **621 kg/m³** | – | – | ESTIMATE (1,241 − 620 kg) |
| Option: + 55 kg activated cement paste (from ~2028–29, if certified) | ~116 kg CO₂, MKI ~7.6 | −13 kg (−10%) | – | ESTIMATE, price_breakdown.md §12.3; TEC-25 |

Notes:
- Recycled aggregate gives **circularity, not CO₂**. In NMD data, 30% RCA lowers MKI by only €0.49/m³ (−2%) [VERIFIED, TEC-04]. The binder is the CO₂ lever.
- With generic NMD data our mix even looks slightly **worse** than the standard (+€0.4/m³), because it needs +15 kg cement. A **product-specific EPD** is required. It removes the 30% markup on generic category-3 data [VERIFIED, CST-01].
- With the 30% RCA fallback mix (for reinforced outdoor work without CUR 112 acceptance), recycled content in total aggregate is **18%** (330 / 1,830 kg) [ESTIMATE, price_breakdown.md §2].

**At P2 scale (54k circular m³/yr of 90k):** about **33 kt/yr less primary gravel** (54k × 0.621 t) and **40.5 kt/yr rubble** moved from road base into new concrete [ESTIMATE, A-OPT inputs; model P2]. CO₂ saved vs the Dutch standard: **≈0**. Only against CEM I would it be ≈8 kt/yr (54k × 154 kg), and that comparison is not honest for most Dutch buyers.

### 1.2 Rijkswaterstaat, ProRail and their GWW contractors

Who buys: the contractor's buyer and concrete technologist, inside the client's MKI rules (market.md §6).

| Selling point | Number | Honest limit |
|---|---|---|
| **Tender access under the coming GWW decree.** Maximum MKI values become compulsory in all public GWW tenders; MKI becomes an award criterion above the EU threshold. Base start 1 Jan 2028 [VERIFIED, POL-17, POL-18; A-POL-13]. | Our mix: 132 kg CO₂ / €8.5 MKI, below the 2027 "outside" ceiling of 155 kg / €10.1 [VERIFIED ceiling, POL-01]. | It meets the **ceiling, not the front-runner value** (2027 "outside": 112 kg / €7.6). If ceilings keep falling 7.5%/yr, our mix hits the "outside" ceiling in **~2029** and fails it in **~2030**; the "inside" ceiling already in **~2029** [ESTIMATE, A-VP-03]. The Dutch standard has the same problem. A lower-CO₂ binder (O5) is needed by ~2029. |
| **Fictive tender discount.** RWS adds MKI × €2 to the bid; ProRail gives up to ±25% award advantage (factor 4) [VERIFIED, POL-23, POL-24]. | vs a CEM I competitor: ΔMKI €9.2 → €18–37/m³ fictive advantage for the contractor [ESTIMATE: 9.2 × 2 to 9.2 × 4]. | vs a CEM III/B competitor: ΔMKI ≈ €0.1 → **€0.2–0.5/m³ only**. Most Dutch rivals use CEM III/B (~85% of Mebin products, CMP-27). Do not promise a tender win from CO₂. |
| **Recycled content for circular specs.** NPCE: ≥80% high-grade recycling of non-reused material from concrete bridges and viaducts by 2030 [VERIFIED, POL-55]. RWS aims to halve primary raw materials [VERIFIED, POL-27]. | 31% recycled concrete in total aggregate; 621 kg gravel saved per m³. | Norms: 30% coarse RCA in most exposure classes, 50% only in X0 or with CUR 112 acceptance [VERIFIED, POL-30]. Heavy bridge classes may need the 30% fallback. |
| **Same price as standard.** | Parity with CEM III/B project price (C30/37 €145, plant average €135) [ESTIMATE, A-MKT-16/18]. Incumbents ask +€3.30 (R30) to +€5.50 (R50) for recycled content [VERIFIED, MKT-25]. | The premium is worth little: full parity costs P2 only −€0.19M and a 5% public premium adds +€0.41M (R-02, R-03); neither moves P2 near NPV 0. |
| **Supply security.** ~75% of coarse aggregate is imported; the last big Dutch Maas gravel project ends in late 2026 [VERIFIED, MKT-17, MKT-18]. Own RCA from the partner's rubble: ~23.5 kt/yr [ESTIMATE, 40.5 kt × 58%]. | Waterside plant; volume reserved in a framework. | The government expects **no gravel shortage for 10 years** [VERIFIED, MKT-16]. Supply security is a "nice to have", not a pain today. |
| **Steady public demand.** Civil-structure renewal €2.4bn/yr (2021–30) → €2.9bn/yr (2031–40); ~€18bn extra for maintenance and renewal to 2041 [VERIFIED, MKT-40, MKT-41]. Zuid-Holland has the biggest RWS bridge cluster (market.md §9). | – | Large contractors often have captive suppliers (Dura Vermeer–everox JV; Ballast Nedam–Haitsma) [VERIFIED, CMP-16, CMP-54]. Target mid-size contractors. |

### 1.3 Municipalities (and provinces, water boards)

| Selling point | Number | Honest limit |
|---|---|---|
| **They must set MKI ceilings soon.** Municipalities are **30%** of GWW turnover; about half of the GWW market (mid/small municipalities, water boards, regional grid operators) rarely uses MKI today [VERIFIED, POL-20]. The decree forces them from ~2028. | We deliver a product-specific EPD and an MKI statement per project. This saves the municipality and its contractor work. | Ceilings are set at peloton level, which incumbents also meet (policy.md §3). The help is **paperwork and certainty**, not a price premium. |
| **Simple, low-risk first uses.** X0 / unreinforced work (foundations, lean concrete, kerb and street-furniture foundations) allows **50%** coarse RCA without discussion [VERIFIED, POL-30]. | 31% recycled content. For unreinforced work this beats the Betonakkoord **target** (25%) but not the **limit value** (35%). For "inside" and "outside" it beats both (15% / 25% and 5% / 15%) [VERIFIED targets, POL-01; ESTIMATE ours]. | Indicative circularity requirements are "not yet introduced" [VERIFIED, POL-02]. Today they are a spec option, not a rule. |
| **Local loop story.** Rubble from local demolition comes back in local works (via the demolition partner). | ~2.7 Mt/yr concrete rubble in Zuid-Holland; we use 40.5 kt (1.5%) [ESTIMATE, market.md §9]. | Matching one project's rubble to another project's concrete is hard to plan. Offer it as traceability (batch records), not as a promise per project. |
| **Price.** Municipalities buy mostly on lowest price (market.md §6). | Parity price. | 0–3% premium at most (A-MKT-25). |

### 1.4 Housing corporations (and their main contractors in bouwteams)

| Selling point | Number | Honest limit |
|---|---|---|
| **Long building programmes = framework volume.** Corporations built 31% of new homes in 2025 [VERIFIED, MKT-30]. Zuid-Holland has 25% of all woondeal homes, 84% apartments (concrete-heavy) [VERIFIED, MKT-39]. | A 3–5-year framework with volume reservation. | Housing permits fell 8.6% in 2025 [VERIFIED, MKT-35]; the 100k homes/yr target will not be met (MKT-37). |
| **Own CO₂ and circular targets, Betonakkoord.** | 31% recycled content; meets Betonakkoord "inside" target and limit (15% / 25%) [ESTIMATE vs POL-01]. | No real CO₂ gain vs the standard. Say so. |
| **MPG effect.** | vs CEM I: ≈ −€0.12/m² floor area/yr ≈ **7% of the homes limit (1.6)**. vs CEM III/B: **≈ €0/m²/yr** (slightly worse with generic data). A product-specific EPD alone is worth ≈ −€0.06/m²/yr (≈4% of the limit) [ESTIMATE: ΔMKI × 2.15 (A2 set, TEC-05) × 0.5 m³/m² (A-VP-01) ÷ 75 yr (A-VP-02)]. | MPG for homes was **not tightened** (0.8 → 0.5 cancelled June 2025); the new 1.6 is the same strictness; the old 0.8 "is usually easily met" [VERIFIED, POL-10, POL-13]. **MPG is not a selling point** for homes before ~2030. |
| **Same price.** Total cost per home is the main driver (market.md §6). | Parity price; circular mix is €2.5/m³ cheaper for us to make. | The corporation's contractor makes the buying choice. |

### 1.5 Developers and investors (private B&U)

| Selling point | Number | Honest limit |
|---|---|---|
| **Disclosure is coming.** Life-cycle GWP on the energy label from 1 Jan 2028 for new buildings >1,000 m² [VERIFIED, POL-14]. 21 developers and builders signed a Betonakkoord intent declaration (June 2026) [VERIFIED, POL-06]. | Product-specific EPD; recycled content for BREEAM/ESG reporting. | Disclosure is not a limit. Dutch limit values come at the earliest in 2030 (base 2032, A-POL-16). The declaration asks for ceiling or front-runner values: we meet the ceiling only. |
| **Offices.** The office MPG limit is 15% stricter since 1 July 2026 (1.55) [VERIFIED, POL-08, POL-09]. | Small pull. | The binder, not the aggregate, is the cheap MPG lever (market.md §6). |
| **Price parity.** | Parity. | Private cash premium ≈ 0% (−2% to +3%) [ASSUMPTION, A-MKT-26]. PBL: "a large part of the sector still goes for the lowest price" [VERIFIED, MKT-47]. **Not a first segment.** |

### 1.6 Demolition firms (suppliers and partners)

This is the segment where our offer is strongest.

| Selling point | Number | Honest limit |
|---|---|---|
| **Their outlet is shrinking.** Betonakkoord cap on concrete in mixed granulate: **30% (2025) → 15% (2027) → 5% (2030)** [VERIFIED, MKT-11]. RAW no longer specifies concrete granulate for road base [VERIFIED, CMP-91]. Betonakkoord path for rubble back into concrete: <15% (2025) → >60% (2030) [VERIFIED, POL-01]. | We take **40.5 kt/yr for 7–10 years** under contract. | The cap is a Betonakkoord rule, not law. The national Circulair Materialenplan still counts road base as recycling [VERIFIED, POL-55]. The push is real only where clients apply Betonakkoord rules. |
| **Paid work for their crushing crew.** | Contract crushing at €7.5/t × 40.5 kt = **€0.30M/yr** to the partner [model P2; A-OPT-05]. | The rate comes from one UK contractor page (OPT-04) that the red team could not re-open (**unverified**). No Dutch tariff was found. |
| **Better than their road-base route.** | At the new base gate fee (€1/t) with half the steel, the offer clearly beats the partner's road-base route (≈ €0/t, A-VP-06, which used 3% steel). | Belgian/GWL bulk prices: clean concrete €0–1/t, reinforced rubble costs the deliverer +€3.5/t [VERIFIED, MKT-20–22]. The gate fee P2 needs (≈ €30/t) is far above both the partner's alternative and the market. This is the biggest data gap and a hard gate (viability_options.md §7–8). |
| **Circular credentials in their own demolition tenders.** NPCE asks for circular demolition of concrete bridges and viaducts [VERIFIED, POL-55]. | Documented high-grade destination per tonne. | Rivals for clean rubble: everox ('s-Gravendeel, 100 kt/yr permitted), Renewi, Circulair Mineraal [VERIFIED, CMP-17, CMP-67, CMP-75]. |
| **Option of equity.** | A stake in P2 aligns the gate fee with shared upside (viability_options.md §7). | There is no upside to share on present numbers (P2 NPV −€4.0M). |

### 1.7 Owners of existing ready-mix plants (sellers)

| Selling point | Number | Honest limit |
|---|---|---|
| **An exit in a shrinking market.** Ready-mix fell from 7.5 Mm³ (2022) to 6.0 Mm³ (2023); 178 plants, average 33.7k m³ [VERIFIED, CMP-43]. Groups are exiting or consolidating (Cementbouw sold its ready-mix; Kalle en Bakker closes Maastricht) [VERIFIED, CMP-33, CMP-38]. | Our offer: **€2.0–2.5M** for equipment, site rights, permit and customer book [ESTIMATE, A-OPT-06: EBITDA €0.2–0.3M × 5–8 + assets]. | €2.5M buys a ~35k m³ plant (an average plant); 90k m³ needs extra capex (+€1.0M modelled) and customers. No Dutch transaction prices were found (data gap). A good plant may cost much more: Cementir reportedly paid ≈€18M for one Danish plant + a minority stake [OPT-01, search excerpt; **not confirmed** by the red team]. |
| **Jobs and name stay.** | Staff kept (7–8 production FTE in P2); brand and customers kept. | Customers may leave after the change of owner (viability_options.md §3, O3). |
| **No closure costs** (site clean-up, social plan). | – | Not quantified. |
| **Option: earn-out or vendor loan.** | Lowers our upfront cash (funding need €6.37M in P2). | Not modelled. |

---

## 2. Honest weak points and how we answer each

| # | Weak point | Evidence | How we address it | What remains |
|---|---|---|---|---|
| 1 | **Quality perception and liability.** Contractors carry liability for structural concrete; trust is built through pilots. | VolkerWessels' granulate use **fell** in 2024 because of availability and client requirements [VERIFIED, MKT-51]. Pilots go via RWS programmes first [VERIFIED, CMP-15]. | Start with X0 / unreinforced / inside work (50% RCA allowed). Use 30% RCA for reinforced outdoor work unless CUR 112 is accepted. Lot testing on every RCA delivery (density, water absorption, constituents). Publish strength and durability data per mix. Most Dutch granulate meets Type A1 [VERIFIED, POL-35]. | Each project with >30% RCA outdoors needs client acceptance. |
| 2 | **Price: buyers buy on price.** | Cash premium 0–3% (A-MKT-25/26); German study: clients pay below producers' premiums [VERIFIED, MKT-48]. | Price parity on private work. The circular mix is €2.5/m³ cheaper to make, so parity is affordable. | At full parity (0%/0%) P2 NPV is **−€4.20M** (R-02), against −€4.01M at the 1.5% public base. The premium is not the problem. |
| 3 | **Certification time and cost.** | KOMO product certificate, NEN-EN 206 / NEN 8005, BRL 2506 for crushed output, EPD in the NMD; 6–18 months [ASSUMPTION, A-CMP-10]. Generic data looks ~30% worse [VERIFIED, CST-01]. | Buy a plant that already has KOMO / CSC. Initial type testing of circular mixes in 2027. Budget EPDs (€80k one-off in the base, A-CST-05). BRL 2506 for the on-site crushing (€25k/yr in the model). | The crushing permit takes ~18 months (9–36) [A-POL-20]. One year late changes NPV by < €0.01M (R-16), because crushing earns almost nothing on evidence-consistent terms. |
| 4 | **Slag supply risk for CEM III/B.** | Tata Steel replaces blast furnace 7 by DRI + EAF, first DRI 2028–2030 [VERIFIED, TEC-70, TEC-71]. Model: +10% (0–25%) on CEM III/B from 2031 ≈ +€3.7/m³ [ASSUMPTION, A-POL-28]. | All Dutch CEM III/B producers face it, so most is passed on. Hedge: binder trials (activated cement paste, Ecocem ACT, CEM VI) from 2028, financed with WBSO/DEI+. Index the framework price to binder cost (A-VP-10). | Cement + ETS stress is the second-worst driver for P2: −€7.30M [model P2, criterion 4]. Full indexation helps only +€0.38M and does not cover a higher starting cement price (R-15b: −€6.48M). |
| 5 | **Small CO₂ advantage vs CEM III/B.** | 132 vs 129 kg/m³; MKI 8.5 vs 8.6 [ESTIMATE, price_breakdown.md §12]. RCA alone cuts only 8–12% CO₂ in EPDs [VERIFIED, CMP-27, CMP-41]. | **Do not claim low-CO₂.** Sell recycled content, gravel saved and rubble diverted. Show the CEM III/B comparison openly. Add a lower-CO₂ binder when certified (−13 to −40 kg/m³; price_breakdown.md §12.3, A-OPT-13). | The binder option loses money in the model (O5: −€0.53M vs the base, with the MKI value netted against the public premium). It is a hedge for tender access around 2029–2030 (A-VP-03), not a profit line. |
| 6 | **Incumbents already sell green lines at a small surcharge.** | Holcim ECOPact +€5–9/m³; Holcim ≤30% granulate +€4/m³; Heidelberg EcoCrete / evoBuild R30 +€3.30, R50 +€5.50; Heidelberg has ~30 plants and owns ENCI cement [VERIFIED, CMP-35, MKT-25, CMP-28]. | Our parity price undercuts their circular surcharge by €3–5.50/m³. Integration (gate fee, own RCA) is now worth only ≈ €0.7/m³ across the plant (crushing net €0.06M/yr ÷ 90k m³) [ESTIMATE, model P2], so the cost edge is the €2.5/m³ of the mix itself. | Incumbents can drop the surcharge any day. Heidelberg can integrate crushing too. Buyer and supplier power are both 4/5 [CMP §9]. |
| 7 | **SL Materials has €100m.** | Initial €100m commitment from Aviva Investors and ABN AMRO (Oct 2026) to expand Zaandam and build new NL and EU sites. It recycles sand, gravel and cement and claims up to 90% CO₂ cut and price parity [VERIFIED claims, CMP-04, CMP-05]. | Our level-2 product (coarse RCA only) cannot win on "most circular". Stay in Zuid-Holland and on volume work. Consider buying their Freement or recycled sand later, or hosting a licensed line on our site (they seek sites and partners, CMP-06). | If they open in the Rotterdam region, our circular claim looks ordinary. |
| 8 | **everox is in our region.** | First plant in 's-Gravendeel (Hoeksche Waard) with Dura Vermeer, 100 kt/yr permitted, delayed, still under construction Sept 2026 [VERIFIED, CMP-16, CMP-17]. | everox is a possible **supplier** of activated cement paste for our binder hedge (O5). Our rubble need (40.5 kt/yr) is small next to ~2.7 Mt/yr regional rubble. | Dura Vermeer is a captive buyer for everox. everox competes with us for clean rubble. |
| 9 | **The economics do not work.** | P2: NPV −€4.01M (range −€6.77M to −€1.42M), IRR −10.6%, payback not reached, 0/6 robustness; transport stress −€8.62M; plant at €4.0M −€5.58M; volume 75k −€5.37M [model P2]. | A €50–100k diligence phase to test three gates (§6). Delivery-zone pricing. Cement indexation. Target terms (plant €2.0M, gate fee €10/t) → NPV −€2.24M (R-17). | Even at target terms the case is NOT VIABLE (0 of 6 robustness tests). |
| 10 | **The crushing line hardly pays.** | At gate fee €1/t, 1% steel split 50/50 and €3/t washing, the crushing net is only €0.06M/yr; P2 without crushing is −€3.92M, slightly *better* than with it (R-14) [viability_options.md §3–4]. | Agree the steel split and rubble quality in writing (hard gate). If the partner keeps all steel, NPV = 0 needs a gate fee of ≈ €30/t (R-19). | Real steel content of clean rubble is unknown (data gap). |
| 11 | **90k m³ is a big plant.** | 2.7× the average Dutch plant; 11% of all ready-mix in the delivery radius (ERMCO 2023 basis); above SOM base 60k [CMP-43; viability_options.md §4]. | Sell it before buying: frameworks ≥ 40k m³/yr (gate C) + the existing book (~35k) + ~15k new sales (A-VP-04). | At 80k m³ NPV is −€4.88M (R-11). |

---

## 3. Business Model Canvas — P2 (acquired plant + partner crushing + frameworks, 90k m³/yr)

Numbers are for 2030, the first year at 90k m³ with crushing at full output [model P2, R-20].

| Block | Content |
|---|---|
| **1. Customer segments** | (a) Mid-size GWW contractors with public framework or maintenance contracts in Zuid-Holland. (b) Municipalities, province, water boards (as clients who set the specs). (c) Housing corporations and their bouwteam contractors. Later: B&U contractors and developers. Supply side: demolition firms (they pay a gate fee, so they are also customers). |
| **2. Value propositions** | **Buyers:** certified circular ready-mix (31% recycled content, 621 kg gravel saved per m³) at the **standard CEM III/B price**; a product-specific EPD and MKI statement per project; volume reserved in a framework; one supplier for standard and circular mixes. **Demolition partner:** a 7–10-year outlet for 40.5 kt/yr of clean rubble as road-base demand is capped, plus €0.30M/yr of paid crushing work. **Plant seller:** a cash exit of €2.0–2.5M, staff and name kept. |
| **3. Channels** | Direct sales to contractors' buyers and concrete technologists. Framework tenders of public clients and corporations. Betonakkoord tender coalitions and circular deals (e.g. Cirkelstad network, CMP-23). The demolition partner's client network (clients who demolish and then build). |
| **4. Customer relationships** | Multi-year frameworks with a price formula. Technical support in bouwteams (mix choice, CUR 112 acceptance). Open test data per mix. Monthly MKI/recycled-content report per client. |
| **5. Revenue streams** | Concrete sales ≈ **€12.26M/yr** (90k m³ × ~€136.2 average realised price incl. −€1 framework discount). Gate fees **€0.04M** (40.5 kt × €1/t). Steel scrap **€0.03M** (1% yield, our 50% share). Crusher sand **€0.05M**. Total revenue **€12.38M**. Later and small: MKI/EPD services or mix-design licences (O6 logic). |
| **6. Key resources** | Permitted waterside plant with ≥1 ha extra space for rubble (Zuid-Holland, Rotterdam–Drechtsteden). KOMO/CSC certificates, BRL 2506 for crushed output, product-specific EPDs. The rubble contract. The framework contracts. A concrete technologist and the existing plant staff (8 production + 3 SG&A + 1 crushing FTE). |
| **7. Key activities** | Buy and convert the plant (€0.8M: RCA bins, covered store, moisture probes) and expand it to 90k m³ (+€1.0M, A-FIX-10). Certified mix design and lot testing. Campaign crushing on site by the partner, plus washing/screening of own RCA. Dispatch and short delivery (average 22.7 km). Binder trials from 2028 (hedge). Tender support for clients. |
| **8. Key partners** | Demolition firm (rubble + contract crushing, possibly equity). Plant seller (possibly earn-out). Cement supplier for CEM III/B (ENCI/Heidelberg, Holcim, Ecocem — note that two are also rivals, CMP §5). Truck-mixer hauliers (subcontracted delivery). Certification body (KOMO, BRL 2506) and LCA consultant (EPD in the NMD). Binder innovators for the hedge (everox, Ecocem ACT). Bank (debt on the plant) and impact investors. Province (crushing permit). |
| **9. Cost structure** | Materials ≈ €85–90/m³ (C30/37 circular €88; cement €36–45/m³, rising with carbon cost; gravel, sand, RCA) [price_breakdown.md §9; model P2]. Delivery ≈ €22.6/m³ ((€9 + €0.5 × 22.7 km) × 10/9 for 9 m³ loads). Staff, lease, maintenance (3.5% of capex), SG&A. Crushing line: contract crushing €0.30M, extra lease €0.10M, washing €0.07M, staff €0.07M, contaminants €0.05M, BRL €0.03M per year, against an RCA credit of €0.58M. Capex **€5.1M** (plant €2.5M + conversion €0.8M + civil €0.2M + permits/transaction €0.2M + rubble site works €0.4M + expansion €1.0M). Peak funding need **€6.37M**. EBITDA 2030 **€0.59M (4.7%)**. |

---

## 4. Pricing strategy

### 4.1 Three options for the concrete price

| Option | What it means | Evidence | Effect on P2 (NPV @ 8%) | Verdict |
|---|---|---|---|---|
| **A. Price parity everywhere** | Circular = CEM III/B standard price, also in public work | Buyers buy on price (MKT-47) | **−€4.20M** (−€0.19M vs P2 base, R-02) | Wins volume, loses a little value |
| **B. Small surcharge like incumbents** | +€3.30–5.50/m³ (R30–R50 level) on all circular volume | Incumbents *ask* this; whether they *get* it is not proven (price_breakdown.md §0) | Not modelled as a base. Public 5% → +€0.41M vs P2 base (R-03) | Head-to-head with Heidelberg at lower scale: weak (CMP §8) |
| **C. Premium (ECOPact level, +€9 or more)** | Sell as "green" | Our CO₂ is the same as the standard | – | **Not credible.** Rejected. |
| **Recommended: "parity-plus where it is scored"** | Parity on private work; ≤3% (≈€4/m³) only on public/MKI-tender circular volume, always below the incumbents' circular surcharge | Model base: 1.5% public, 0% private (A-MKT-25/26, A-FIX-03); counter-evidence: GWL sells recycled-aggregate concrete ~€20/m³ cheaper (MKT-20) | **−€4.01M** (R-01) | Honest and defensible; pricing alone cannot make P2 viable |

Rule of thumb from the model: **each €1/m³ on the average realised price is worth about €0.36M NPV** in P2 (R-05 vs R-01). A €5/m³ lower average price (€130, about the GWL C20/25 retail list) gives −€6.21M (R-13, −€2.2M). Price discipline matters more than any green story.

### 4.2 Framework contract pricing

| Clause | Proposal | Why (number) |
|---|---|---|
| Discount | At most −€3/m³ on framework volume, which is ≈ −€1/m³ on all volume (A-OPT-12) | −€2/m³ on all volume → −€0.38M vs P2 base (R-06). No discount at all → +€0.35M (R-05). |
| Trade-off for the buyer | Offer **either** the framework discount **or** the public circular premium, not both. Parity price with no discount gives −€3.83M, slightly better than the base (R-07). | Simple to explain: "standard price, circular for free, volume reserved". |
| Volume | ≥ 40k m³/yr in total over 2 contracts (gate C); take-or-pay band ±20% | Volume 80k → −€4.88M (R-11). Utilisation is a top-3 risk. |
| Duration | 3–5 years | Covers the 7-year payback only with renewals; flag this to the jury. |
| Binder indexation | Pass binder cost changes (CEM III/B carbon cost and slag uplift) 100% into the price (A-VP-10) | 100% instead of the market's 80% (a key judgement call, critique M4) → +€0.38M (R-15). Pair with a multi-year cement supply contract, because a higher starting cement price is not covered (R-15b: −€6.48M). |
| Delivery zones | Price includes delivery up to ~22–25 km; above that +€0.5/m³ per extra km; under-load surcharge for loads below 9 m³ (Heidelberg +€24/m³ below 9 m³, MKT-25; Holcim €18/m³ below 7.5 m³, CMP-35) | Transport distance is P2's worst driver: −€8.62M if delivery costs ×1.75 [model P2]. Formula (€9 + €0.5 × km) at a 10 m³ reference load, ×10/9 for the 9 m³ average load (A-TEC-28, A-FIX-02, A-VP-08). |
| Documentation | EPD + MKI statement + recycled content per delivery, included in the price | This is the service clients need under the GWW decree. |

### 4.3 Gate-fee pricing for demolition partners

| Element | Proposal | Why (number) |
|---|---|---|
| Gate fee, clean concrete rubble (A1-type) | **Hard gate:** the level needed for NPV = 0 is **≈ €30/t** on P2 base terms (€15/t only if every other input is at its upside). Model base €1/t (A-FIX-04), upside €5/t. Fixed for 7–10 years, indexed to the landfill tax path | Each €1/t ≈ €0.15M NPV (R-08, R-09: €0 → −€0.15M; €10 → +€1.27M vs P2 base). |
| Tiers (A-VP-07) | Clean €5–10/t; reinforced €3–7.5/t; mixed or out of spec: rejected or ≥ €20/t | NL small-load counter tariff ~€20/t (MKT-23); contaminant disposal €120/t (A-CST-33), landfill tax €40.85 → €81/t by 2030 (proposal, POL-51). |
| Steel | **Hard gate:** split agreed in writing. Model base 1% yield split 50/50 (A-FIX-05/06) | Partner keeps all steel: gate fee €1 / €5 / €10 → −€4.13M / −€3.55M / −€2.84M; NPV = 0 at ≈ €30/t (R-19). |
| Contract crushing rate (we pay) | **≤ €7.5/t**, campaign crushing, machine + operator + diesel + wear included (unverified UK anchor) | €10/t → −€0.40M; €5/t → +€0.37M vs P2 base (R-10). |
| Net for the partner | At the base terms (gate fee €1, crushing €7.5, half the steel) the partner is clearly better off than on its road-base route (≈ €0/t, A-VP-06). | But at the ≈ €30/t that P2 needs, no partner would sign while its alternative is ≈ €0/t. |
| Volume | 40.5 kt/yr, take-or-pay band | Sized to our own RCA need (A-OPT inputs). |
| Contamination | Acceptance protocol; contaminants charged back at disposal cost | Contaminant share 1% (0.5–2%) in the model (A-TEC-04). |

Honest note: Belgian crushers take clean concrete for **€0–1/t** and charge **+€3.5/t** for reinforced rubble [VERIFIED, MKT-20–22]. If clean rubble becomes a wanted raw material, the gate fee could even turn negative (we pay for rubble). At €0/t P2 NPV is −€4.16M [model P2]. This is why gate B is a hard gate that must be tested before any plant is bought.

---

## 5. First three target customer types, and partner types for the pre-conditions

### 5.1 First three customer types

| # | Customer type | Why first | What we offer | Size signal |
|---|---|---|---|---|
| 1 | **Mid-size GWW contractors** (no captive concrete supplier) with RWS, ProRail, province or municipal maintenance and renewal work in Zuid-Holland | Hardest demand driver: GWW decree (~2028) + MKI award (POL-17); biggest RWS bridge cluster in ZH (market.md §9); frameworks are normal in this segment | Framework with reserved volume, parity price, EPD/MKI per project | GWW ≈ 95% public; ~0.96 Mm³ ready-mix nationally (market.md §5) |
| 2 | **Municipalities, the province and water boards** (as spec-setters; we sell via their contractors) | 30% of GWW turnover; half rarely uses MKI today and must start (POL-20); X0/unreinforced work allows 50% RCA | Spec support: ready-made MKI ceilings and recycled-content clauses; low-risk first uses | GWW market ≈ €22bn/yr (POL-22) |
| 3 | **Housing corporations** with multi-year building programmes, and their bouwteam contractors | 31% of new homes (MKT-30); ZH 25% of woondeal homes, 84% apartments (MKT-39); long programmes give framework volume; own circular targets | 3–5-year framework, parity price, recycled-content reporting | ~0.94 Mm³ public housing ready-mix nationally (market.md §5) |

Not first: **developers** (cash premium ≈ 0%, MPG gives no pull for homes before 2030) and **agriculture** (price only).

### 5.2 Partner types needed for the three pre-conditions

| Pre-condition | Partner type | What we need from them | What they get |
|---|---|---|---|
| **(a) Plant ≤ €2.5M** | Owner of an independent (family) ready-mix plant, or a group divesting a plant, **waterside** in Zuid-Holland, with ≥1 ha extra space | LOI at ≤ €2.5M (target ≤ €2.0M → +€0.50M vs P2 base, R-12), permit route for rubble acceptance, customer book, expansion quote for 90k m³ | Exit, staff kept, no closure cost |
| | Bank (debt secured on the plant); M&A adviser | Part of the €6.37M funding need | Collateral, fees |
| **(b) Rubble contract** | Regional demolition / urban-mining firm with ≥ 40 kt/yr clean concrete rubble in Zuid-Holland and a mobile crusher (types as in CMP §12: demolition families, urban-mining networks) | 7–10-year contract; gate fee and steel split as hard gates (NPV = 0 needs ≈ €30/t); crushing ≤ €7.5/t | Outlet, paid crushing, optional equity |
| | Province (permit authority); certification body (BRL 2506) | Waste-processing permit (~18 months), certified RCA | – |
| **(c) Frameworks ≥ 40k m³/yr** | 2 anchor customers: a GWW contractor framework and a corporation (or municipal) framework | Signed volume, not only a letter of intent | Price certainty, volume reserved, MKI paperwork |
| **Supporting** | Cement supplier (multi-year CEM III/B contract); truck-mixer haulier; LCA consultant; binder innovator for trials (everox / Ecocem type) | Supply and cost certainty; EPDs; binder hedge | Volume; a trial site |

---

## 6. Three-year roadmap 2027–2029 with go/no-go gates

Model reference (after the critique fixes): P2 buys the plant in 2027 and sells under our name from 2028 (49.5k m³), 76.5k m³ in 2029 and 90k m³ from 2030 (acquired-plant ramp 55/85/100%); crushing from 2029 [model P2]. On present evidence the gates below are expected to **fail** (mainly gate B), so the realistic first step is a **€50–100k due-diligence phase** (critique M10; this replaces the earlier ~€0.25M pre-gate budget of A-VP-05), not an investment.

| When | Step | Gate and pass test | If it fails |
|---|---|---|---|
| **Q4 2026 – Q1 2027** | Due diligence (€50–100k): screen waterside plants in Zuid-Holland; talks with 2–3 demolition firms and 3–4 anchor customers; expansion quote for 90k m³. | **Gate A — plant:** signed LOI at **≤ €2.5M** (target ≤ €2.0M), ≥1 ha extra space, rubble acceptance possible under the permit; expansion to 90k m³ ≤ €1.0M. | Price €3.0M → NPV −€4.53M; €4.0M → −€5.58M (R-12). **Stop the plant route.** |
| **Q1 – Q2 2027** | Test rubble and crushing terms; steel ownership. | **Gate B — rubble (hard gate):** signed **7–10-year** contract with a **gate fee and steel split that bring P2 to NPV ≥ 0** (≈ €30/t on base terms; ≈ €15/t only if every other input is at its upside), **crushing ≤ €7.5/t**, 40.5 kt/yr. | Bulk evidence today is €0–1/t (MKT-20). Without crushing P2 is −€3.92M (R-14). **Stop.** |
| **Q1 – Q2 2027** | Test anchor-customer demand. | **Gate C — volume:** frameworks for **≥ 40k m³/yr** signed (with the existing ~35k book this makes 90k reachable, A-VP-04). | Volume 80k → −€4.88M; 75k → −€5.37M (R-11). **Stop.** |
| **Q2 2027 — decision** | Investment decision only if A + B + C are all signed **and** the re-run model with the signed terms passes plan.md §2.1. | Even at the target terms (€2.0M plant, €10/t gate fee): NPV −€2.24M, IRR −2.1%, payback not reached, 0/6 robustness (R-17) — **NOT VIABLE**. | Do not invest. Stopping loses only the diligence budget. |
| **H2 2027** (only if invested) | Close the purchase; convert and expand the plant (€0.8M + €1.0M); initial type testing of circular mixes; product-specific EPDs; file the crushing permit. | KPI: circular mixes certified; first framework deliveries signed for 2028. | Delay → shift the plan; recheck NPV. |
| **2028** | First sales year (model: 49.5k m³, EBITDA −€0.34M). GWW decree expected (1 Jan 2028, A-POL-13). Start binder trials (WBSO/DEI+). | **Gate D (end 2028):** ≥ 75k m³ run-rate; crushing permit granted. | Permit late → keep buying RCA (crushing adds almost nothing anyway, R-16). Volume short → no extra spend on site works (€0.4M). |
| **2029–2030** | Crushing starts 2029. 2029: 76.5k m³, EBITDA €0.27M; 2030: 90k m³, EBITDA €0.59M (model). | **Gate E (end 2030):** EBITDA ≥ €0.6M; decide on the lower-CO₂ binder for ~2030 MKI ceilings (A-VP-03); decide on selling mix know-how as a licence (O6 add-on). | Renegotiate the steel split or gate fee. |

**If a gate fails: the default is to stop.** Stopping loses only the diligence budget (€50–100k). The **asset-light licence + RCA service (O6)** is not a rescue: in the model it has NPV −€2.51M, EBITDA −€0.28M in 2029 and needs ≈10 licensee plants to break even (viability_options.md §3). Run it only as a capped pilot: max €0.5M over 2 years, continue only with ≥3 paying licensee plants signed by end-2028 (A-VP-09).

---

## 7. Honest pitch (slide 1)

1. A stand-alone circular concrete plant in the Netherlands does not pay: our greenfield case loses €5.3M (NPV at 8%, first sales 2028).
2. The product is not the problem: our circular mix is €2.5/m³ cheaper to make than the Dutch standard, but its CO₂ is about the same.
3. No route is investable on present evidence. The integrated acquisition route (buy a plant, crush rubble on site, sell 90k m³ under contracts) comes closest, but even its favourable-input stack stays below zero (NPV −€4.0M; range −€6.8M to −€1.4M).
4. Break-even would need a gate fee of ~€15–30/t for clean rubble, against €0–1/t in the bulk market today.
5. We ask for a €50–100k due-diligence phase to test three named contracts (plant, rubble, volume), not for an investment. If a gate fails, we stop.

---

## Appendix A — model runs by Agent 8 (re-run after the critique fixes)

All runs use `model/model_core.py` with the P2 overrides from `model/options.py` (after the critique fixes) plus the change shown. NPV at 8% real, 2026–2036, salvage-only terminal value. P2 base: NPV −€4.01M, IRR −10.6%, payback not reached.

| Run | Change vs P2 | NPV €M | IRR | Payback (yr) |
|---|---|---|---|---|
| R-01 | P2 base (1.5% public premium, 0% private, −€1/m³ framework discount, gate fee €1/t, steel 1% split 50/50) | −4.01 | −10.6% | not reached |
| R-02 | Premium 0% public / 0% private (full parity) | −4.20 | −11.8% | not reached |
| R-03 | Public premium 5% | −3.60 | −8.2% | not reached |
| R-04 | Public 1.5% + private 1% | −3.83 | −9.5% | not reached |
| R-05 | No framework discount (0 €/m³) | −3.66 | −8.6% | not reached |
| R-06 | Framework discount −€2/m³ on all volume | −4.39 | −12.9% | not reached |
| R-07 | Full parity (0%/0%) and no framework discount | −3.83 | −9.6% | not reached |
| R-08 | Gate fee €0/t | −4.16 | −11.6% | not reached |
| R-09 | Gate fee €10/t | −2.74 | −3.5% | not reached |
| R-10 | Contract crushing €10/t / €5/t | −4.41 / −3.64 | −13.2% / −8.4% | not reached |
| R-11 | Volume 80k m³/yr (75k: −5.37) | −4.88 | −16.7% | not reached |
| R-12 | Plant purchase €2.0M / €3.0M / €4.0M | −3.51 / −4.53 / −5.58 | −9.5% / −11.6% / −13.3% | not reached |
| R-13 | Plant-average price €130/m³ (instead of €135) | −6.21 | −29.1% | not reached |
| R-14 | No on-site crushing (gate B fails) | −3.92 | −11.6% | not reached |
| R-15 | Binder cost pass-through 100% (instead of 80%) | −3.63 | −7.9% | not reached |
| R-15b | R-15 + cement €130/t and high carbon path | −6.48 | −29.0% | not reached |
| R-16 | Crushing starts 2030 instead of 2029 | −4.01 | −10.8% | not reached |
| R-17 | Target terms: plant €2.0M + gate fee €10/t | −2.24 | −2.1% | not reached |
| | → criterion 4 (6 drivers at pessimistic value): green premium −2.75; gate fee −3.65; transport −6.36; cement/ETS −5.05; utilisation −4.26; capex −3.64 → **0 of 6 → NOT VIABLE** (1 of 4 criteria) | | | |
| R-18 | R-17 + crushing €6.5/t | −2.10 | −1.3% | not reached |
| R-19 | Steel all to partner, gate fee €1 / €5 / €10 per t; gate fee for NPV = 0 ≈ €30.4/t (€29.7/t with the 50/50 split) | −4.13 / −3.55 / −2.84 | – | – |
| R-20 | P2 year 2030 detail: revenue €12.38M (crushing €0.12M: gate fee €0.04M, steel €0.03M, sand €0.05M); RCA credit €0.58M; contract crushing €0.30M; washing €0.07M; crushing net €0.06M/yr; EBITDA €0.59M | – | – | – |

## Appendix B — data gaps that would change this go-to-market most

1. **Dutch gate fees for clean rubble, bulk, multi-year, and steel ownership** (gate fee €0 → €10/t = €1.4M NPV on P2; NPV = 0 needs ≈ €30/t). Interview 2 demolition firms before Gate B.
2. **Prices paid for small Dutch ready-mix plants and the cost of expanding one to 90k m³** (purchase €1.5–4.0M = €2.6M NPV range; expansion €0.5–2.0M = €1.3M). Ask 1–2 M&A advisers before Gate A.
3. **Realised (not list) premiums for recycled content** in public frameworks. Ask 2–3 contractor buyers.
4. **The real GWW-decree ceiling levels and their tightening path.** They decide when the binder hedge becomes necessary (A-VP-03).
5. **Steel content of clean rubble** and the Dutch campaign-crushing rate.
