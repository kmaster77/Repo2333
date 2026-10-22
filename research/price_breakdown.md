# Unit cost and price breakdown — circular ready-mix (B1) vs conventional

Agent 5 (Cost & price analyst). Date: 2026-10-22. All money in **real 2026 €, excl. VAT**. Concrete prices are **delivered to site** unless stated.
Labels: **[VERIFIED]** = source read; **[ESTIMATE]** = calculated from sources (calculation shown); **[ASSUMPTION]** = no source, reasoning given.
IDs: Phase 1 sources (POL-, MKT-, TEC-, CMP-) and assumptions (A-POL-, A-MKT-, A-TEC-, A-CMP-) are reused. New: `research/sources_cost.md` (CST-xx), `research/assumptions_cost.md` (A-CST-xx). Machine-readable inputs: `model/inputs.csv`.

Words used once and explained:
- **RCA** = recycled concrete aggregate (*betongranulaat*), crushed old concrete used instead of gravel.
- **SSD** = saturated-surface-dry: aggregate that is wet inside but dry on the surface, so it does not take water from the mix.
- **EBIT** = profit before interest and tax; **EBITDA** = EBIT + depreciation.
- **Capital charge** = the yearly amount needed to pay back the capex with an 8% real return (an annuity). If EBIT is below it, the plant does not earn its cost of capital.

---

## 0. Summary

1. **C30/37 per m³ (steady state 70k m³/yr, 2026):** circular product costs **€133** and sells for **€147** → EBIT margin **€13.7/m³ (9.3%)**. The conventional CEM III/B reference costs **€136**, sells for **€145** → **€9.4/m³ (6.5%)**. A CEM I reference costs **€144** → **€1.0/m³**. [ESTIMATE, §9]
2. **The circular product is ~€2.5/m³ cheaper to make than the conventional one, not dearer**, because certified RCA delivered (~€24.5/t) is cheaper than barge gravel (~€32/t). Extra costs of the circular mix (+15 kg cement, +superplasticiser, lot testing, handling) are ~€3.8/m³. **Break-even RCA price ≈ €29/t delivered.** Above that, circular costs more. [ESTIMATE, §11]
3. **The premium is small:** base €1.7/m³ blended (3% on the 40% public share, 0% private). Incumbents' list surcharges (+€3.30 R30, +€5.50 R50) are evidence of *asking*, not of *getting*. [ASSUMPTION A-MKT-25/26; VERIFIED MKT-25]
4. **For the financial model use plant averages, not C30/37.** All strength classes together sell at ~€135/m³ with ~310 kg cement. Then the plant earns only **€4.4/m³ EBIT (3.2%) and €8.0/m³ EBITDA (≈€0.56M/yr)**. The capital charge at 8% is **€7.8/m³**. So in the base case the plant does **not** earn its cost of capital (−€3.4/m³ economic profit). [ESTIMATE, §10]
5. **Ranges are wide.** Margin of the circular C30/37: **−€17 to +€44/m³** (combined uncertainty, root-sum-square method, §9). The three inputs that matter most: **selling price** (±€15–20/m³), **volume/utilisation** (50k m³ → margin −€9/m³), and **delivery distance ≈ cement price** (each ±€6/m³). [ESTIMATE, §11]
6. **ETS/CBAM:** CEM III/B carbon cost rises from ~€4/t (2026) to €12/t (2030) and €26/t (2034); CEM I from €14 to €45 and €95/t (current law). That adds **+€2.3/m³ (2030) and +€6.1/m³ (2034)** to a CEM III/B mix but **+€8.3 and +€22/m³** to a CEM I mix. This hurts CEM I users, not Dutch CEM III/B competitors. [ESTIMATE, §3.2]
7. **MKI inconsistency resolved: it is method, not a mistake.** Betonakkoord values are A1–A3 only, product-specific data, no reinforcement. NMD values are generic category-3 data (×1.3 surcharge) and modules A1–D. Same A1 weighting set, same unit (€/m³). The model uses the **Betonakkoord basis**: circular **€8.5 MKI, 132 kg CO₂/m³**; CEM III/B reference **€8.6, 129 kg**; CEM I **€17.7, 286 kg**. Both CEM III/B mixes sit **between ceiling and front-runner** level. [ESTIMATE, §12]
8. **The circular mix is not lower-CO₂ than the Dutch standard** (it needs +15 kg cement). To reach front-runner values (≤119 kg CO₂/m³ "outside", 2026) the binder must change (e.g. ≤300 kg CEM III/B with more superplasticiser, CEM III/C or ~55 kg activated cement paste). [ESTIMATE, §12]

---

## 1. Products, basis and conventions

| Code | Product | Use |
|---|---|---|
| **CIRC** | C30/37, S3, Dmax 16–22, **50% of coarse aggregate replaced by RCA (V/V)**, CEM III/B binder | Circular product (base) |
| CONV | C30/37 CEM III/B, 100% primary gravel and sand | Conventional reference = Dutch standard (Heidelberg list base is CEM III/B, ~85% of Mebin products) [VERIFIED, MKT-25, CMP-27] |
| CEMI | C30/37 CEM I, primary aggregates | Second reference (prefab, early-strength buyers, importers) |

- Base plant: 120 m³/h, **70,000 m³/yr** at steady state, 1.5 ha waterside site, Zuid-Holland (Rotterdam area); 60% of volume circular, 40% CONV [ASSUMPTION, A-TEC-24, A-TEC-44].
- Fixed costs are spread over all 70,000 m³. Extra circular costs go only to CIRC.
- **Low / base / high** per line: low = cheapest plausible value of that line; high = dearest. In the low column fixed costs use 90k m³, in the high column 50k m³.
- **Totals:** adding all "high" lines gives an extreme case nobody expects. So the total range uses the **root-sum-square (RSS)** of the line deviations, which assumes the lines vary independently. The all-low / all-high "stress" totals are shown too.
- Calculation script (for audit): `/tmp/claude-0/-home-user-Repo2333/4db0c959-97fb-5db0-bba8-60ffc6756c32/scratchpad/calc.py` (scratch copy; the model agent should rebuild from `model/inputs.csv`).

---

## 2. Mix designs per m³ (the recipes used)

| kg/m³ | CIRC (base) | CIRC low variant (30% RCA) | CIRC high variant (+fine RCA) | CONV CEM III/B | CEMI |
|---|---|---|---|---|---|
| Cement | **345 CEM III/B** | 330 | 360 | **330 CEM III/B** | **320 CEM I** |
| Water (effective) | 165 | 165 | 165 | 165 | 165 |
| Extra absorption water (pre-wetting, not in w/c) | 28 | ~15 | 40 | 0 | 0 |
| Gravel 4/16–4/32 | **620** | 870 | 620 | **1,241** | **1,241** |
| Coarse RCA 4/16–4/22, Type A1 | **560** | 330 | 560 | 0 | 0 |
| Sand 0/4 | **630** | 630 | 480 | 639 | 639 |
| Recycled sand 0/4 | 0 | 0 | 150 | 0 | 0 |
| Superplasticiser (liquid PCE, % of binder) | **0.9% (3.1 kg)** | 0.7% | 1.2% | 0.7% (2.3 kg) | 0.7% (2.2 kg) |
| Label | ESTIMATE (A-CST-09, from TEC §4.3 mix C2) | VERIFIED (NMD C1, TEC-04) | ESTIMATE (TEC C2) | VERIFIED (NMD R2, TEC-04) | VERIFIED (NMD R1, TEC-04) |

Why these choices:
- 50% coarse RCA is allowed in X0 by NEN 8005 and in other classes under CUR-Aanbeveling 112 without changing design rules [VERIFIED, POL-30]. For most reinforced outdoor work without client acceptance of CUR 112, **30% is the fallback** (low variant).
- +15 kg cement compensates the ~−9.5% strength loss at 50% coarse RCA [ESTIMATE, A-TEC-11].
- Fine RCA is left out of the base: no easy norm route (CROW-CUR 127 only) [VERIFIED, POL-30].
- Superplasticiser +0.2 pt keeps slump with RCA's higher water demand [ASSUMPTION, A-TEC-13, A-CST-10].

---

## 3. Raw materials (€/t and €/m³)

### 3.1 Prices, 2026, delivered to the plant

| Material | Low | Base | High | Unit | Label / ID | Note |
|---|---|---|---|---|---|---|
| CEM III/B 42.5 N, bulk | 95 | **110** | 130 | €/t | ESTIMATE, A-CST-12 (CST-14, CST-11, MKT-25) | Market agent had €105; raised (Argus: EU cement mid-to-high US$100s/t ex-works, +10–15% in 2026) |
| CEM I 52.5 R, bulk | 120 | **140** | 165 | €/t | ESTIMATE, A-CST-12 | Market agent had €125; Sika uses ~€150/t CEM I |
| Gravel 4/16–4/32, by barge | 25 | **32** | 40 | €/t | ASSUMPTION, A-MKT-11 | Only Belgian lists public (~€36–37 pick-up, MKT-20) |
| Sand 0/4, by barge | 14 | **19** | 25 | €/t | ASSUMPTION, A-MKT-12 | |
| RCA coarse, ex-works crusher | 10 | **15** | 25 | €/t | ASSUMPTION, A-MKT-13 | BE COPRO €9.5–18/t (MKT-20–22) |
| RCA coarse, **delivered** (see 3.3) | 14.2 | **24.5** | 45.5 | €/t | ESTIMATE | |
| Recycled sand 0/4, ex-works | 3 | 8 | 15 | €/t | ASSUMPTION, A-CST-15 | Only in high variant |
| Superplasticiser (liquid PCE) | 1.0 | **1.4** | 2.0 | €/kg | ASSUMPTION, A-CST-10 (CST-11–13) | |
| Water | 0.8 | 1.2 | 2.0 | €/m³ | ASSUMPTION, A-CST-16 | |

Note on cement: the 2026 price already contains the 2026 carbon cost (~€4/t CEM III/B, ~€14/t CEM I). Later years add only the *increase* (§3.2).

### 3.2 Cement carbon cost (ETS / CBAM) by year

Formula from policy.md §5: net carbon cost per t cement = (clinker CO₂ intensity − 0.656 × CBAM factor) × EUA × clinker share. Base: intensity 0.82 t/t, clinker share CEM I 0.93, CEM III/B 0.25, current law (free allocation 97.5% in 2026 → 0% in 2034) [ESTIMATE, POL-39, POL-41, A-POL-05–08]. Price uplift vs 2026 = 85% of the increase (pass-through, A-POL-09).

| Year | EUA base (€/t CO₂) | CEM I carbon €/t (low / **base** / high) | CEM III/B carbon €/t (low / **base** / high) | CEM I price, base | CEM III/B price, base | Binder €/m³ CONV / CIRC / CEMI |
|---|---|---|---|---|---|---|
| 2026 | 85 | 10.7 / **14.3** / 17.8 | 2.4 / **3.8** / 5.6 | €140 | €110 | 36.3 / 38.0 / 44.8 |
| 2030 | 100 | 24.8 / **44.8** / 64.5 | 5.5 / **12.1** / 20.4 | €166 (+26) | €117 (+7) | 38.6 / 40.4 / 53.1 |
| 2034 | 125 | 51.1 / **95.3** / 147.1 | 11.4 / **25.6** / 46.4 | €209 (+69) | €128.5 (+18.5) | 42.4 / 44.3 / 66.9 |

- Low = July 2026 Commission proposal (free allocation ends 2038) + low EUA, intensity 0.78, low clinker shares. High = current law + high EUA (€130 in 2030, €180 in 2034), intensity 0.86. All years 2026–2036 are in `model/inputs.csv` (`carbon_cost_*_YYYY`, `eua_price_YYYY`). [ESTIMATE]
- Base matches policy.md (A-POL-07/08) within €0.5/t. The policy low case for CEM I in 2030 (€31) is a bit higher than mine (€24.8) because I use a lower EUA path; both are labelled estimates.
- Not in the table: **slag scarcity** after Tata Steel's blast furnace 7 closes: +10% (0–25%) on CEM III/B from 2031 ≈ +€11/t ≈ **+€3.7/m³** [ASSUMPTION, A-POL-28]. It hits all Dutch CEM III/B producers.
- Effect on competition: every Dutch competitor using CEM III/B pays the same increase, so it is mostly passed on in prices (base 80%, A-CST-13). The real winners are CEM III/B and low-clinker users **vs CEM I users**: the gap grows from €8.5/m³ (2026) to €14.5 (2030) and €24.5/m³ (2034) in binder cost.

### 3.3 RCA delivered — build-up per tonne

| Step | Low | Base | High | Label |
|---|---|---|---|---|
| Ex-works crusher price | 10 | 15 | 25 | ASSUMPTION, A-MKT-13 |
| Truck transport, km × €/t·km | 15 × 0.18 = 2.7 | 30 × 0.25 = **7.5** | 50 × 0.35 = 17.5 | ESTIMATE, A-TEC-32, A-CST-14 (TEC-41) |
| Handling/loading | 1.5 | 2.0 | 3.0 | ESTIMATE, A-TEC-32 |
| **Delivered price** | **14.2** | **24.5** | **45.5** | ESTIMATE |
| At-plant lot testing + handling/pre-wetting | 1.0 | 1.8 | 3.5 | ASSUMPTION, A-CST-17/18 |
| **Effective cost in the mix** | 15.2 | **26.3** | 49.0 | ESTIMATE |
| Compare: gravel by barge, delivered | 25 | 32 | 40 | ASSUMPTION, A-MKT-11 |

Option: RCA from a **waterside crusher by barge**: 50 km × €0.03 + €2.5 transshipment ≈ €4/t → ~€19/t delivered [ESTIMATE, A-TEC-33]. This is a real lever in the Rotterdam port area and should be a supplier-selection criterion.

---

## 4. Inbound transport

| Flow | Mode | Rate | Typical distance | €/t | Label |
|---|---|---|---|---|---|
| Gravel, sand | Inland ship (waterside plant) | €0.015–0.05/t·km + €1.5–4/t transshipment | 100–250 km (Rhine/Maas sources; ~75% of coarse aggregate imported, MKT-17) | ~€4.5–10, inside the delivered price | ESTIMATE, A-TEC-33 |
| Gravel, sand | Truck (if not waterside) | €0.25/t·km + €2/t | 40 km | ~€12 → **+€5–8/t vs barge** → +€9–14/m³ | ESTIMATE, TEC §6 |
| RCA | Truck | €0.25/t·km + €2/t | 30 km | €9.5 | ESTIMATE |
| Cement | Bulk truck/ship from grinding plants (ENCI Rotterdam 0.6 Mt/yr, IJmuiden 1.4 Mt/yr; Ecocem Moerdijk) | in delivered price | 30–300 km (NMD assumes 300 km) | in price | VERIFIED locations, CMP-58, CMP-61; TEC-04 |

Implied ex-quarry gravel price: €32 − barge €4.5–7.5 − transshipment €2.5 ≈ **€22–25/t** [ESTIMATE]. A waterside site is worth **~€9–14/m³** against a truck-fed site. This is bigger than any green premium.

---

## 5. Processing costs (per m³, 70k m³/yr)

| Line | Calculation (base) | Low | Base | High | Label / ID |
|---|---|---|---|---|---|
| Energy | 3.6 kWh × €0.20 + 0.12 l × €1.55 | 0.69 | **0.91** | 1.62 | VERIFIED use (TEC-04, A-TEC-38); price ESTIMATE (CST-04: €0.245 incl. VAT → ~€0.20 excl.); A-CST-19 |
| Production labour | 7 FTE × €70k ÷ 70k m³ | 4.13 | **7.00** | 14.04 | ESTIMATE, A-CST-20/21 (CAO Mortelbedrijven, CST-06) |
| Maintenance & wear | 2.5% × €5.0M (plant + civil) ÷ 70k | 0.60 | **1.79** | 5.84 | ASSUMPTION, A-CST-22 |
| Certification & testing, fixed (KOMO BRL 1801, CSC, NMD, external tests) | €50k ÷ 70k | 0.33 | **0.71** | 1.60 | ASSUMPTION, A-CST-23 (CST-20, CST-03, CST-21) |
| Extra RCA testing + handling (CIRC only) | 0.56 t × (€0.8 + €1.0) | 0.56 | **1.01** | 1.96 | ASSUMPTION, A-CST-17/18 |
| Site lease | 15,000 m² × €10 ÷ 70k | 0.67 | **2.14** | 7.50 | ESTIMATE, A-CST-24 (CST-09) |
| Depreciation | (€5.0M ÷ 25 yr + €0.5M ÷ 10 yr) ÷ 70k | 1.78 | **3.57** | 8.70 | ESTIMATE, A-CST-02, A-TEC-39 |
| *Memo: capital charge at 8% real* | €5.0M × annuity(8%, 25 yr) + €0.5M × annuity(8%, 10 yr) ÷ 70k | – | *7.76* | – | ESTIMATE |

Capex items used (`model/inputs.csv`): plant equipment €4.0M (3.0–5.5), site prep/civil €1.0M (0.6–1.8), permits/engineering €0.5M (0.4–0.7) → **€5.5M (4.0–8.0)** as decided; plus LCA/EPDs €80k, pre-opening €300k; working capital 60 days receivables, 30 days payables, 10 days stock [ASSUMPTION, A-CST-02–07].

---

## 6. Delivery to site

Formula from technology.md: **€9 + €0.5 × one-way km per m³** [ESTIMATE, A-TEC-28].
**Check:** truck mixer €110/h all-in, 10 m³ per trip, 50 min fixed (load, wait, unload, wash), 45 km/h. At 20 km: (50 + 2 × 20 ÷ 45 × 60) min = 103 min = 1.72 h × €110 = €189 ÷ 10 m³ = **€18.9/m³**. The formula gives €19.0. ✔ [ESTIMATE]
**Distance:** a 30 km delivery radius with evenly spread demand gives an average distance of 2/3 × 30 = **20 km** [ESTIMATE, A-CST-27]. Range 10–35 km → **€11 / €19 / €32 per m³** (low/base/high, incl. formula ranges).
Caution: waiting time on site (pumps, slow pours) and part loads are the main reasons real costs exceed the formula. Holcim's list charges €18/m³ for under-loads <7.5 m³ [VERIFIED, CMP-35] — a sign of how much part loads cost.

---

## 7. Overheads (SG&A)

| Line | Base | Low | High | Label |
|---|---|---|---|---|
| SG&A staff: 3 FTE × €90k (manager, sales, planner/admin) | €270k | €160k | €440k | ASSUMPTION, A-CST-20/21 |
| Non-staff (insurance, ERP/dispatch, audit, legal, marketing, cars) | €300k | €200k | €450k | ASSUMPTION, A-CST-25 |
| Bad debt | 0.5% of revenue | 0.3% | 1.0% | ASSUMPTION, A-CST-26 |
| **Per m³** | **€8.9** | €4.4 | €19.3 | ESTIMATE |

SG&A ≈ 6% of revenue in the base case.

---

## 8. Revenue side

| Item | Low | Base | High | Label / ID | How used |
|---|---|---|---|---|---|
| C30/37 project price, delivered (CEM III/B standard) | 130 | **145** | 165 | ESTIMATE, A-MKT-18 (MKT-27) | Price for CONV and base for CIRC |
| List price C30/37 (for reference) | 195 | 212 | 225 | VERIFIED, MKT-24, A-CMP-16 | Project ≈ 68% of list |
| **Plant average, all classes** | 115 | **135** | 155 | ESTIMATE, A-MKT-16 | **Use in the P&L** |
| Green premium, public (40% of sales) | 0% | **3%** | 8% | ASSUMPTION, A-MKT-25 | **Only premium line that is added** |
| Green premium, private (60%) | −2% | **0%** | +3% | ASSUMPTION, A-MKT-26 | |
| → Blended premium on CIRC, C30/37 | −€1.8 | **+€1.74** | +€9.1 | ESTIMATE: 145 × (0.4 × 3% + 0.6 × 0%) | |
| Recycled-content list surcharges (Heidelberg R30/R50/R100; Holcim ≤30%) | €3.30 | €5.50 | €11.00 (Holcim €4) | VERIFIED, MKT-25, MKT-24 | Cross-check only. Shows the ceiling of what incumbents ask; not additive |
| MKI tender value reaching the supplier | €0 | €0.5 | €3.4 | ESTIMATE, A-CST-28 (POL §3) | Inside the public premium; not additive |

Why the MKI value is low: policy.md's €3.4/m³ assumes our mix beats a **ceiling-level** mix by the ceiling–front-runner gap (~€2.8 MKI). But the Dutch standard is already CEM III/B, and our circular mix has almost the **same MKI** as that standard (§12). Against a typical Dutch competitor ΔMKI ≈ €0–0.3/m³ → value ≈ €0–1/m³. The €3.4 only applies against CEM I / CEM III/A competitors. **Double-counting warning for the model:** add only `green_premium_public/private`; treat the recycled surcharge and MKI value as evidence.

Price evolution: market price rises with 80% of the *market-wide* CEM III/B carbon cost increase (+€1.7–1.9/m³ in 2030, +€4.6–4.9/m³ in 2034 on a 310–330 kg mix) [ASSUMPTION, A-CST-13]. No other real price growth (A-MKT-34 says volume flat to −0.5%/yr after 2030).

---

## 9. Stacked breakdown — C30/37, €/m³, 2026, steady state

| Line (€/m³) | CIRC low | **CIRC base** | CIRC high | CONV low | **CONV base** | CONV high | CEMI low | **CEMI base** | CEMI high |
|---|---|---|---|---|---|---|---|---|---|
| Cement / binder | 32.8 | **38.0** | 44.9 | 31.4 | **36.3** | 42.9 | 38.4 | **44.8** | 52.8 |
| Gravel | 15.5 | **19.8** | 24.8 | 31.0 | **39.7** | 49.6 | 31.0 | **39.7** | 49.6 |
| Recycled coarse aggregate (delivered) | 8.0 | **13.7** | 25.5 | – | – | – | – | – | – |
| Sand | 8.8 | **12.0** | 15.8 | 9.0 | **12.1** | 16.0 | 9.0 | **12.1** | 16.0 |
| Admixtures | 3.1 | **4.4** | 6.2 | 2.3 | **3.2** | 4.6 | 2.2 | **3.1** | 4.5 |
| Water | 0.2 | **0.2** | 0.4 | 0.1 | **0.2** | 0.3 | 0.1 | **0.2** | 0.3 |
| **Subtotal materials** | 68.3 | **88.1** | 117.5 | 73.8 | **91.6** | 113.5 | 80.8 | **100.0** | 123.2 |
| Energy | 0.7 | **0.9** | 1.6 | 0.7 | **0.9** | 1.6 | 0.7 | **0.9** | 1.6 |
| Production labour | 4.1 | **7.0** | 14.0 | 4.1 | **7.0** | 14.0 | 4.1 | **7.0** | 14.0 |
| Maintenance & wear | 0.6 | **1.8** | 5.8 | 0.6 | **1.8** | 5.8 | 0.6 | **1.8** | 5.8 |
| Certification & testing (fixed) | 0.3 | **0.7** | 1.6 | 0.3 | **0.7** | 1.6 | 0.3 | **0.7** | 1.6 |
| RCA testing + handling | 0.6 | **1.0** | 2.0 | – | – | – | – | – | – |
| Site lease | 0.7 | **2.1** | 7.5 | 0.7 | **2.1** | 7.5 | 0.7 | **2.1** | 7.5 |
| Depreciation | 1.8 | **3.6** | 8.7 | 1.8 | **3.6** | 8.7 | 1.8 | **3.6** | 8.7 |
| **Ex-works cost** | 77.1 | **105.2** | 158.7 | 82.0 | **107.7** | 152.8 | 89.0 | **116.1** | 162.5 |
| Delivery (truck mixer) | 11.0 | **19.0** | 32.0 | 11.0 | **19.0** | 32.0 | 11.0 | **19.0** | 32.0 |
| SG&A incl. bad debt | 4.4 | **8.9** | 19.3 | 4.4 | **8.9** | 19.2 | 4.4 | **8.9** | 19.2 |
| **Total cost** — RSS range | 119.4 | **133.1** | 157.8 | 121.2 | **135.6** | 158.9 | 129.0 | **144.0** | 167.7 |
| *Total cost — stress (all lines low / high)* | *92.5* | | *210.0* | *97.4* | | *204.0* | *104.4* | | *213.8* |
| **Price** (CIRC incl. blended premium) | 128.2 | **146.7** | 174.1 | 130.0 | **145.0** | 165.0 | 130.0 | **145.0** | 165.0 |
| **EBIT margin** (RSS of cost and price) | −17.3 | **13.7** | 44.2 | −18.3 | **9.4** | 34.1 | −27.1 | **1.0** | 26.0 |
| EBIT margin % of price | | **9.3%** | | | **6.5%** | | | **0.7%** | |
| EBITDA margin | | **17.2** | | | **13.0** | | | **4.6** | |
| *Memo: capital charge (8%)* | | *7.8* | | | *7.8* | | | *7.8* | |

All lines [ESTIMATE] from §2–§8. Columns may not add exactly because of rounding.

Reading the table:
- **Where the circular advantage comes from:** gravel saving €19.9 minus RCA €13.7 = **+€6.2**; minus extra cement €1.7, extra admixture €1.1, RCA QC/handling €1.0 + sand €0.2 = **net +€2.5/m³ cost advantage**, plus **€1.7 premium** → CIRC margin €4.3/m³ above CONV.
- **CEM I:** priced here at the CEM III/B market price. On Heidelberg's list CEM I costs +€22/m³ extra [VERIFIED, MKT-25]; if ~68% of that is realised on project prices (+€15/m³), CEMI margin is ~€16/m³. So CEM I is a niche *upsell*, not a cheaper route.
- **Delivery is the second-largest cost line** after aggregates + cement. Average distance matters as much as the cement price.

---

## 10. Plant-average economics (what the financial model should use)

The plant sells all strength classes (C20/25 to C35/45), not only C30/37. Average price ~€135/m³ [A-MKT-16]; average cement ~310 kg/m³ [VERIFIED, CMP-43 ERMCO 2023]. Recipe otherwise as §2; circular +15 kg (325 kg). 60% CIRC / 40% CONV. Base values.

| €/m³, steady state 70k m³ | 2026 | 2030 | 2034 |
|---|---|---|---|
| Average price (incl. 1.2% blended premium on CIRC; + 80% of market binder carbon cost) | 135.97 | 137.72 | 140.60 |
| Average total cost | 131.59 | 133.83 | 137.52 |
| — of which CIRC / CONV | 130.56 / 133.13 | 132.84 / 135.30 | 136.60 / 138.89 |
| **EBIT** | **4.38 (3.2%)** | 3.89 | 3.08 |
| **EBITDA** | **7.96** | 7.46 | 6.65 |
| EBITDA per year (× 70,000) | **€0.56M** | €0.52M | €0.47M |
| Capital charge 8% (€5.5M capex) | 7.76 | 7.76 | 7.76 |
| Economic profit (EBIT − capital charge) | **−3.38** | −3.87 | −4.68 |

[ESTIMATE] (2030/2034 excl. the slag-scarcity uplift, which would be largely passed on.)

Benchmark: Heidelberg Materials' European EBITDA margin is 17.9–19.9%, but that includes cement and aggregates, where margins are highest [VERIFIED, CST-19]. A non-integrated newcomer that buys cement and subcontracts trucks earning ~6% EBITDA (7.96 ÷ 135.97) is plausible, not pessimistic [ESTIMATE].

**Message for Agent 6:** with these inputs, simple payback ≈ €5.5M ÷ €0.56M ≈ 10 years before tax and working capital. The plan's viability criteria (payback < 7 years, NPV > 0 at 8%) look hard to meet in the base case. The case needs a higher price (+€4–5/m³ ≈ +3%), higher volume (≥90k m³), cheaper RCA (barge), or a lower capex. Using C30/37 economics for the whole plant would **overstate EBIT by ~€7.6/m³** (blended C30/37 EBIT €12.0 vs plant average €4.4) — please do not.

---

## 11. Sensitivities (one at a time, CIRC C30/37 EBIT, base €13.7/m³)

| Input | Low value → margin | High value → margin | Swing |
|---|---|---|---|
| **Selling price** (130 / 165 €/m³) | −1.5 | 33.9 | **35.4** |
| **Volume** (90k / 50k m³/yr) | 18.9 | 4.3 | **14.5** |
| **Delivery distance** (10 / 35 km) | 18.7 | 6.2 | **12.5** |
| **CEM III/B price** (95 / 130 €/t) | 18.9 | 6.8 | **12.1** |
| Gravel price (25 / 40 €/t) | 18.0 | 8.7 | 9.3 |
| RCA ex-works (10 / 25 €/t) | 16.5 | 8.1 | 8.4 |
| Sand price (14 / 25 €/t) | 16.8 | 9.9 | 6.9 |
| Green premium public (0% / 8%) | 11.9 | 16.6 | 4.6 |
| RCA distance (15 / 50 km) | 15.8 | 10.9 | 4.9 |
| Equipment capex (3.0 / 5.5 M€) | 14.6 | 12.3 | 2.3 |
| Site lease (6 / 15 €/m²) | 14.5 | 12.6 | 1.9 |
| Cost per FTE (62k / 78k) | 14.5 | 12.9 | 1.6 |

[ESTIMATE]

**Break-even RCA price:** the circular mix saves 0.621 t gravel × €32 + 0.009 t sand × €19 = €20.0 and pays 0.56 t × P(RCA) + €3.8 extra costs. Cost-neutral at **P ≈ €29/t delivered**; with the €1.7 premium, margin-neutral at ~€32/t. [ESTIMATE]

---

## 12. CO₂ and MKI per m³, and the reconciliation

### 12.1 What looked inconsistent

| Set | MKI €/m³ | CO₂ kg/m³ | Where |
|---|---|---|---|
| Betonakkoord 2026 front-runner → ceiling (unreinforced → aggressive) | 7.1–8.8 → 9.5–11.9 | 103–131 → 145–186 | policy.md §1 [VERIFIED, POL-01] |
| NMD cat. 3, C30/37: CEM III/B → CEM I | 26.01 → 34.59 | 126 → 276 (CO₂ is TEC's own estimate) | technology.md §4.4 [VERIFIED MKI, TEC-04] |

### 12.2 Explanation — method, not a mistake

| Factor | Betonakkoord | NMD (technology.md) | Effect |
|---|---|---|---|
| LCA modules | **A1–A3 only** (raw materials to plant gate, "until the concrete is in the truck mixer"), reinforcement excluded [VERIFIED, POL-01 §5.1] | **A1–D** total (adds transport to site A4, construction A5, end of life C, credits D) | CEM III/B: €26.01 total vs €18.51 for A1–A3 → **A4–D add €7.50 (29%)** [VERIFIED, TEC-04] |
| Data quality | Product-specific: reference mixes calculated with the Betonhuis **Ontwerptool Groen Beton V7**, without PCR cement/concrete [VERIFIED, POL-01 §5.3] | **Category 3 generic data with a 30% markup factor (×1.3)** [VERIFIED, CST-01, CST-02] | €18.51 ÷ 1.3 = €14.24 |
| Background data for cement | Dutch product data (tool) | Generic NMD process database profiles | Remaining factor 14.24 ÷ ~8.6 ≈ **1.65** — generic cement profiles carry more non-CO₂ impacts (e.g. toxicity) than Dutch cement EPDs [ESTIMATE] |
| Weighting set | A1 set (11 indicators) | A1 set | **Same** — not the cause. (A2 set from mid-2026/2027 roughly doubles both: ×2.15, TEC-05) |
| Unit | €/m³ concrete | €/m³ concrete | **Same** |
| CO₂ | A1–A3 | TEC's 126/276 are own A1–A3 estimates, not NMD | **Consistent**: CEM III/B 126–129 is between front-runner (119 "outside") and ceiling (169); CEM I 276–286 is far above the ceiling — exactly what POL-01 says ("ceiling ≈ CEM III/A, front-runner ≈ CEM III/B") |

So **only the MKI numbers differ**, and the difference is fully explained by scope (A1–A3 vs A1–D), the ×1.3 cat-3 markup and generic vs product-specific cement data. Neither file is wrong; they measure different things. A third ruler exists too: Rijkswaterstaat RTD 1033 caps C30/37 at €16.1/m³ (2025–26) [VERIFIED, TEC-06] — producers meet it with product-specific data.

### 12.3 Values the model uses (Betonakkoord basis: A1–A3, A1 set, product-specific)

The Betonakkoord tables show MKI is almost a straight line in CO₂: **MKI ≈ €1.10 + €0.058 × kg CO₂/m³** (fits all 24 published values within ±€0.1) [ESTIMATE, A-CST-29]. CO₂ = cement × GWP + other. GWP: CEM III/B **300 kg/t** (270–360; Mebin's table implies 290, TEC base 320), CEM I **800 kg/t** (700–900); "other" (aggregates, transport, plant) **30 kg/m³** (Betonakkoord worked example), 28 for CIRC [ESTIMATE, A-TEC-14/15, CMP-27, POL-01].

| Product | CO₂ kg/m³ (low–base–high) | MKI €/m³ A1-set (Betonakkoord basis) | MKI A2-set (×2.15, 2027+) | NMD cat-3 A1–D (if no own LCA) | vs 2026 "outside" ceiling 169 kg / €10.9 | vs front-runner 119 kg / €8.0 |
|---|---|---|---|---|---|---|
| CIRC (345 kg CEM III/B, 50% RCA) | 111 – **132** – 157 | **8.5** (7.1–10.0) | ~18.3 | ~26.4 (TEC) | below ✔ | **above** ✘ |
| CONV CEM III/B (330 kg) | 109 – **129** – 154 | **8.6** (7.4–10.0) | ~18.5 | 26.01 | below ✔ | above ✘ |
| CEMI (320 kg) | 244 – **286** – 323 | **17.7** (15.2–19.8) | ~38 | 34.59 | far above ✘ | ✘ |
| Option: CIRC + 55 kg activated cement paste (290 kg CEM III/B) | ~116 | ~7.6 | ~16.4 | ~23.9 (TEC) | ✔ | ✔ ("outside"), ✘ ("inside" 111) |

[ESTIMATE] (CIRC MKI includes a −€0.2 credit for less gravel extraction; NMD shows RCA cuts MKI by only ~2%, TEC-04.)

Implications:
- **CO₂ and MKI cannot be the selling point of the base circular mix vs the Dutch standard** — both are ~130 kg/m³. The circular claim is recycled content (Betonakkoord recycling targets, municipal "% circular" specs).
- **Get product-specific (cat. 1) LCAs.** With generic cat-3 data a product looks ~30% worse in tenders (×1.3) [VERIFIED, CST-01].
- To reach front-runner values, design the binder: cut CEM III/B to ≤~300 kg with superplasticiser, use CEM III/C (NMD C30/37 €23.64 vs €26.01, TEC-04) or certified activated cement paste (2027–28+).

---

## 13. Gate fees and by-products (inputs for the A+B hybrid option)

In B1 the plant does **not** receive rubble. For a later "own crushing" option (A+B):

| Input | Low | Base | High | Label / ID |
|---|---|---|---|---|
| Gate fee received for clean concrete rubble (bulk) | −€2/t | **€5/t** | €15/t | ASSUMPTION, A-MKT-15 (BE €0–1/t, MKT-20–22; NL counter tariff ~€20/t small loads, MKT-23) |
| Yields per t input: coarse / 0/4 sand / steel / contaminants | 50 / 30 / 1 / 0.5% | **58 / 38 / 3 / 1%** | 65 / 45 / 5 / 2% | ESTIMATE, A-TEC-01–04 |
| Value of coarse RCA used in own plant | €14.2/t | **€24.5/t** (avoided delivered price) | €45.5/t | ESTIMATE |
| Crusher sand 0/4 outlet | €0/t | **€3/t** | €8/t | ASSUMPTION, A-CST-31 |
| Steel scrap | €100/t | **€150/t** | €220/t | ESTIMATE, A-CST-32 (yard HMS €150–240/t, CST-16/17; HMS 1/2 ~US$370–400/t CFR Turkey, CST-18) |
| Contaminant disposal | −€90/t | **−€120/t** | −€160/t | ASSUMPTION, A-CST-33 (landfill tax €40.85 → €81/t, POL-50/51) |
| Crusher capex: mobile / stationary high-grade / advanced | 1.0 / 6 / 8 | **1.6 / 10 / 15** | 2.5 / 15 / 30 M€ | A-TEC-40/41/42 |
| Crusher opex: diesel / wear / staff / maintenance / BRL 2506 | 0.15 l, €0.2/t, 2 FTE, 2%, €15k | **0.3 l/t, €0.4/t, 3 FTE, 3%, €25k/yr** | 0.6 l, €0.8/t, 4 FTE, 5%, €40k | A-TEC-08, A-TEC-43, A-CST-34 |
| Permit lead time | 9 | **18** | 36 months | A-POL-20 |

**Indicative per-tonne economics, sized to own need** (plant needs 0.56 t × 42k m³ ≈ 23.5 kt RCA → **~40.5 kt rubble/yr**) [ESTIMATE]:
- Value per t rubble: gate fee 5.00 + coarse 0.58 × 24.5 = 14.21 + sand 0.38 × 3 = 1.14 + steel 0.03 × 150 = 4.50 − contaminants 0.01 × 120 = 1.20 → **€23.65/t**.
- Cost per t (mobile line €1.6M): diesel 0.47 + wear 0.40 + labour 5.19 + maintenance 1.19 + certification 0.62 + land (1 ha × €10/m²) 2.47 + depreciation 3.29 → **€13.6/t**.
- Net ≈ **€10/t ≈ €0.4M/yr EBIT** (≈ €0.53M EBITDA) for ~€1.6M capex + permit. On paper attractive, but it rests on three weak inputs: the gate fee (±€8/t ≈ ±€0.3M/yr), the 38% sand fraction with almost no outlet, and an 18-month permit. Labour at 40 kt is heavy (a 300 t/h crusher would run ~135 h/yr); hiring campaign crushing may be cheaper — no price found. Agent 7 should test this.

---

## 14. Inconsistent numbers between the Phase 1 files — and what I chose

| # | Topic | Values found | Chosen | Why |
|---|---|---|---|---|
| 1 | MKI per m³ | Betonakkoord €7–12 (POL-01) vs NMD €26–35 (TEC-04) | Betonakkoord basis €8.5/8.6/17.7 | Method difference, see §12 |
| 2 | CO₂ per m³ CEM III/B | Mebin 87 kg @300 kg cement, excl. transport (CMP-27); TEC 126 (330 kg × 0.32 + 20); Betonakkoord example 115 + 30 | 129 kg (330 × 0.300 + 30) | Middle GWP; Betonakkoord's own 30 kg "other" |
| 3 | Cement prices | A-MKT-19/20 €105 / €125 | €110 / €140 | Argus and Sika evidence (CST-14, CST-11); still no Dutch list |
| 4 | CEM I–CEM III/B spread | €20/t (MKT) vs Heidelberg +€22/m³ ≈ €70/t (list, MKT-25) | €30/t | List surcharge includes margin and option pricing |
| 5 | Green premium | A-MKT-25/26: 3% public / 0% private vs A-CMP-04: €5/m³ (0–12) | Market's 3% / 0% (→ €1.7/m³ blended) | CMP's €5 is a list premium of ECOPact, a *binder* product our reference also matches |
| 6 | MKI tender value | Policy €3.4/m³ supplier share; market ΔMKI €5 × factor 4 = €20 fictive | €0.5 (0–3.4), not additive | Our ΔMKI vs a Dutch CEM III/B competitor is ~0 (§12) |
| 7 | Fictive discount factor | A-POL-10 base 3 vs A-MKT-27 base 4 | Not used directly | Only matters vs ceiling-level competitors |
| 8 | RCA per m³ | A-MKT-29 0.40 t vs A-TEC-45 0.71 t (incl. fines) vs NMD C1 0.33 t | 0.56 t coarse (50%), no fines | Brief's 30–50%; fines need CUR 127 |
| 9 | Allowed coarse RCA | Policy base 30% (A-POL-25) vs TEC mix C2 50% | 50% base, 30% as low variant | 50% needs CUR 112 acceptance outside X0 — a sales risk |
| 10 | CBAM path in base | A-POL-04 base = 50/50 blend with July-2026 proposal from 2028; A-POL-07/08 and policy §5 table = current law | Current law in base; proposal as low | It is the law today; brief and policy table use it |
| 11 | Project price vs list | MKT: project €145 ≈ 68% of list €212; A-CMP-01: −20% (→ ~€170) | €145 (130–165) | MKT-27 is an observed trade indication; −20% is a guess |
| 12 | Ready-mix market size | MKT 7.4 Mm³ (~200 plants, 2016) vs CMP 6.0 Mm³ at 178 plants (ERMCO 2023, avg 33.7k m³/plant) | Not used in unit cost | Flag for Agent 6: our 70k m³ is 2× the 2023 average plant |
| 13 | Steady-state output | TEC 70k (brief) vs MKT SOM base 60k | 70k base; **test 60k** | At 60k, fixed costs rise by ~€3.9/m³ |
| 14 | NMD A1-set C30/37 CEM I | €34.59 (TEC-04) vs €32.48 (TEC-05) | €34.59 (TEC-04) | Different card versions; TEC-04 has the module split |
| 15 | CPI factors | MKT 2021→2026 ×1.27; TEC ×1.26; A-CMP-15 placeholder 1.03 (2025→26) | 1.022 for 2025→2026 (CBS Jan values, MKT-54) | Immaterial (<1%) |
| 16 | Delivery radius | Plan 25–50 km; TEC average 20 km; CMP effective radius 35 km | 20 km average (10–35) | Mean distance = 2/3 of radius |

---

## 15. Biggest data gaps (what an interview would fix)

1. **Real project prices and realised green premiums** by strength class (2–3 contractor buyers). Price is the #1 driver.
2. **Delivered prices for gravel, sand, RCA and cement** in Zuid-Holland (one buyer at a ready-mix plant). Only Belgian lists and trade press exist.
3. **Truck-mixer subcontract rates** and real average distance/waiting time (one haulier).
4. **KOMO/CSC certification and lab costs** (Kiwa or SKG-IKOB quotation).
5. **Port land lease rates** (Havenbedrijf Rotterdam or Drechtsteden municipalities).
6. **Gate fees for clean rubble** in bulk (2 demolition firms) — needed for A+B.

## Files written

- `/home/user/Repo2333/research/price_breakdown.md` (this file)
- `/home/user/Repo2333/model/inputs.csv` (174 parameters, `parameter,unit,low,base,high,source_ids,label,notes`)
- `/home/user/Repo2333/research/sources_cost.md` (CST-01 … CST-21)
- `/home/user/Repo2333/research/assumptions_cost.md` (A-CST-01 … A-CST-34)
