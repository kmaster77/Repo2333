# Excel vs Python check - 2026-10-22

Method: `check_model.py` builds a copy of `financial_model.xlsx` per test case (scenario selector and/or values in the Override column), recalculates it with LibreOffice headless (`soffice --headless --convert-to xlsx`), reads the values with openpyxl (`data_only=True`) and compares them with `model_core.run()`. Tolerance: EUR 0.5 or relative 1e-07. Text results ('not reached', 'n/a') must match a Python `None`.

**Overall result: ALL CASES MATCH**

| Case | Result | NPV Python | NPV Excel | IRR Python | IRR Excel | max abs diff yearly lines (EUR) | max abs check row (EUR) | errors |
|---|---|---|---|---|---|---|---|---|
| Base (selector 2) | OK | -4,481,665 | -4,481,665 | -0.0706 | -0.0706 | 1.02e-08 | 6.40e-10 | 0 |
| Pessimistic (selector 1) | OK | -38,250,548 | -38,250,548 | - | - | 4.84e-08 | 0.00e+00 | 0 |
| Optimistic (selector 3) | OK | 29,963,057 | 29,963,057 | 1.1938 | 1.1938 | 4.66e-08 | 0.00e+00 | 0 |
| Override: 60k m3/yr | OK | -5,920,016 | -5,920,016 | -0.1389 | -0.1389 | 4.66e-09 | 8.15e-10 | 0 |
| Override: discount rate 10% | OK | -4,726,018 | -4,726,018 | -0.0706 | -0.0706 | 1.02e-08 | 6.40e-10 | 0 |
| Override: option hooks all non-zero | OK | -3,681,687 | -3,681,687 | -0.0252 | -0.0252 | 5.59e-09 | 0.00e+00 | 0 |

## Detail per case

### Base (selector 2) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -4,481,665.3956 | -4,481,665.3956 | yes |
| irr | -0.0706 | -0.0706 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 530,374.2601 | 530,374.2601 | yes |
| funding | 6,835,872.7648 | 6,835,872.7648 | yes |
| be_vol | 50,731.9939 | 50,731.9939 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 6.40e-10 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Pessimistic (selector 1) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -38,250,548.1817 | -38,250,548.1817 | yes |
| irr | None | None | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | -4,109,613.6761 | -4,109,613.6761 | yes |
| funding | 53,454,568.9718 | 53,454,568.9718 | yes |
| be_vol | None | None | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 0.00e+00 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Optimistic (selector 3) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | 29,963,056.8777 | 29,963,056.8777 | yes |
| irr | 1.1938 | 1.1938 | yes |
| payback | 1.1227 | 1.1227 | yes |
| dpayback | 1.1901 | 1.1901 | yes |
| ebitda_y3 | 6,952,848.3796 | 6,952,848.3796 | yes |
| funding | 2,842,680.0000 | 2,842,680.0000 | yes |
| be_vol | 10,070.4467 | 10,070.4467 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 0.00e+00 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Override: 60k m3/yr - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -5,920,016.2445 | -5,920,016.2445 | yes |
| irr | -0.1389 | -0.1389 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 255,112.6380 | 255,112.6380 | yes |
| funding | 7,073,231.3003 | 7,073,231.3003 | yes |
| be_vol | 50,731.9939 | 50,731.9939 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 8.15e-10 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Override: discount rate 10% - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -4,726,018.2467 | -4,726,018.2467 | yes |
| irr | -0.0706 | -0.0706 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 530,374.2601 | 530,374.2601 | yes |
| funding | 6,835,872.7648 | 6,835,872.7648 | yes |
| be_vol | 50,731.9939 | 50,731.9939 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 6.40e-10 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Override: option hooks all non-zero - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -3,681,687.3454 | -3,681,687.3454 | yes |
| irr | -0.0252 | -0.0252 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 889,677.2201 | 889,677.2201 | yes |
| funding | 7,354,931.0172 | 7,354,931.0172 | yes |
| be_vol | 40,845.7446 | 40,845.7446 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 0.00e+00 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 1.00e+03 | | n/a (hook revenue) |

## Python-internal reconciliation (base case)

- FCF vs (net income + D&A - change in WC - capex - sustaining capex + salvage): max abs diff 0.00e+00 EUR
- EBITDA vs (revenue - total opex): max abs diff 0.00e+00 EUR

## What is and is not checked

- Checked: every KPI on the Valuation sheet that drives the criteria, 7 yearly lines x 11 years, all check rows, for 3 scenarios and 3 override cases (incl. all option hooks).
- Not checked by recalculation: the Scenarios, Sensitivity and criterion-4 values, because they are pasted from model_core.py (same code path as the cases above).
