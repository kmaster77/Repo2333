# Excel vs Python check - 2026-10-22

Method: `check_model.py` builds a copy of `financial_model.xlsx` per test case (scenario selector and/or values in the Override column), recalculates it with LibreOffice headless (`soffice --headless --convert-to xlsx`), reads the values with openpyxl (`data_only=True`) and compares them with `model_core.run()`. Tolerance: EUR 0.5 or relative 1e-07. Text results ('not reached', 'n/a') must match a Python `None`.

**Overall result: ALL CASES MATCH**

| Case | Result | NPV Python | NPV Excel | IRR Python | IRR Excel | max abs diff yearly lines (EUR) | max abs check row (EUR) | errors |
|---|---|---|---|---|---|---|---|---|
| Base (selector 2) | OK | -5,326,984 | -5,326,984 | -0.1390 | -0.1390 | 9.31e-09 | 6.98e-10 | 0 |
| Pessimistic (selector 1) | OK | -35,548,096 | -35,548,096 | - | - | 4.84e-08 | 0.00e+00 | 0 |
| Optimistic (selector 3) | OK | 24,535,641 | 24,535,641 | 1.0365 | 1.0365 | 4.28e-08 | 0.00e+00 | 0 |
| Override: 60k m3/yr | OK | -6,416,672 | -6,416,672 | -0.2120 | -0.2120 | 6.52e-09 | 1.34e-09 | 0 |
| Override: discount rate 10% | OK | -5,352,664 | -5,352,664 | -0.1390 | -0.1390 | 9.31e-09 | 6.98e-10 | 0 |
| Override: option hooks all non-zero | OK | -4,470,798 | -4,470,798 | -0.0728 | -0.0728 | 4.66e-09 | 1.16e-09 | 0 |
| Option O0 via selector (1) | OK | -5,326,984 | -5,326,984 | -0.1390 | -0.1390 | 9.31e-09 | 6.98e-10 | 0 |
| Option O1 via selector (2) | OK | -6,241,925 | -6,241,925 | -0.1225 | -0.1225 | 6.52e-09 | 1.40e-09 | 0 |
| Option O2 via selector (3) | OK | -5,415,793 | -5,415,793 | -0.1289 | -0.1289 | 4.89e-09 | 1.34e-09 | 0 |
| Option O3 via selector (4) | OK | -3,537,420 | -3,537,420 | -0.1438 | -0.1438 | 8.38e-09 | 6.98e-10 | 0 |
| Option O4 via selector (5) | OK | -5,137,258 | -5,137,258 | -0.1455 | -0.1455 | 1.12e-08 | 1.16e-09 | 0 |
| Option O5 via selector (6) | OK | -5,863,590 | -5,863,590 | -0.1635 | -0.1635 | 1.30e-08 | 1.46e-09 | 0 |
| Option O7 via selector (7) | OK | -4,771,428 | -4,771,428 | -0.1297 | -0.1297 | 9.31e-09 | 6.98e-10 | 0 |
| Option O8 via selector (8) | OK | -4,147,283 | -4,147,283 | -0.0726 | -0.0726 | 6.98e-09 | 1.40e-09 | 0 |
| Option O9 via selector (9) | OK | -6,315,400 | -6,315,400 | -0.1980 | -0.1980 | 6.52e-09 | 1.05e-09 | 0 |
| Option P1 via selector (10) | OK | -3,973,035 | -3,973,035 | -0.1569 | -0.1569 | 1.02e-08 | 1.22e-09 | 0 |
| Option P2 via selector (11) | OK | -4,013,320 | -4,013,320 | -0.1061 | -0.1061 | 8.38e-09 | 2.33e-09 | 0 |
| Option O_orig via selector (12) | OK | -4,481,665 | -4,481,665 | -0.0706 | -0.0706 | 1.02e-08 | 6.40e-10 | 0 |
| Pessimistic scenario + option P1 via selector | OK | -30,569,134 | -30,569,134 | - | - | 5.22e-08 | 0.00e+00 | 0 |
| Override: first sales 2027 + 8 m3 loads | OK | -6,687,595 | -6,687,595 | -0.1772 | -0.1772 | 1.02e-08 | 1.51e-09 | 0 |
| Override: first sales 2029 (delay 2) | OK | -5,094,556 | -5,094,556 | -0.1643 | -0.1643 | 1.02e-08 | 1.34e-09 | 0 |
| Option P2 downside stack (selector + overrides) | OK | -6,772,314 | -6,772,314 | -0.2589 | -0.2589 | 7.45e-09 | 2.39e-09 | 0 |
| Option P2 upside stack (selector + overrides) | OK | -1,417,869 | -1,417,869 | 0.0192 | 0.0192 | 6.87e-09 | 0.00e+00 | 0 |

## Detail per case

### Base (selector 2) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -5,326,983.5067 | -5,326,983.5067 | yes |
| irr | -0.1390 | -0.1390 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 324,745.5225 | 324,745.5225 | yes |
| funding | 7,085,186.0050 | 7,085,186.0050 | yes |
| be_vol | 56,822.3784 | 56,822.3784 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| asset-light npv | -2,512,811.1532 | -2,512,811.1532 | yes |
| asset-light irr | None | None | yes |
| asset-light payback | None | None | yes |
| asset-light ebitda_y3 | -282,200.0000 | -282,200.0000 | yes |
| asset-light funding | 3,346,049.3151 | 3,346,049.3151 | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 6.98e-10 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | -1.80e-09 | | yes |

### Pessimistic (selector 1) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -35,548,095.5053 | -35,548,095.5053 | yes |
| irr | None | None | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | -4,540,402.0609 | -4,540,402.0609 | yes |
| funding | 52,033,454.2635 | 52,033,454.2635 | yes |
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
| npv | 24,535,641.3184 | 24,535,641.3184 | yes |
| irr | 1.0365 | 1.0365 | yes |
| payback | 2.1469 | 2.1469 | yes |
| dpayback | 2.2272 | 2.2272 | yes |
| ebitda_y3 | 6,741,954.5760 | 6,741,954.5760 | yes |
| funding | 2,842,680.0000 | 2,842,680.0000 | yes |
| be_vol | 10,349.2347 | 10,349.2347 | yes |
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
| npv | -6,416,672.0312 | -6,416,672.0312 | yes |
| irr | -0.2120 | -0.2120 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 78,308.3935 | 78,308.3935 | yes |
| funding | 7,814,786.9688 | 7,814,786.9688 | yes |
| be_vol | 56,822.3784 | 56,822.3784 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 1.34e-09 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | -7.42e-10 | | yes |

### Override: discount rate 10% - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -5,352,664.2121 | -5,352,664.2121 | yes |
| irr | -0.1390 | -0.1390 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 324,745.5225 | 324,745.5225 | yes |
| funding | 7,085,186.0050 | 7,085,186.0050 | yes |
| be_vol | 56,822.3784 | 56,822.3784 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 6.98e-10 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | -1.80e-09 | | yes |

### Override: option hooks all non-zero - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -4,470,798.1021 | -4,470,798.1021 | yes |
| irr | -0.0728 | -0.0728 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 683,547.0025 | 683,547.0025 | yes |
| funding | 7,567,665.0810 | 7,567,665.0810 | yes |
| be_vol | 45,257.6423 | 45,257.6423 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 1.16e-09 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 1.00e+03 | | n/a (hook revenue) |

### Option O0 via selector (1) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -5,326,983.5067 | -5,326,983.5067 | yes |
| irr | -0.1390 | -0.1390 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 324,745.5225 | 324,745.5225 | yes |
| funding | 7,085,186.0050 | 7,085,186.0050 | yes |
| be_vol | 56,822.3784 | 56,822.3784 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 6.98e-10 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | -1.80e-09 | | yes |

### Option O1 via selector (2) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -6,241,924.8861 | -6,241,924.8861 | yes |
| irr | -0.1225 | -0.1225 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 493,599.3173 | 493,599.3173 | yes |
| funding | 9,053,708.7208 | 9,053,708.7208 | yes |
| be_vol | 66,169.0817 | 66,169.0817 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 1.40e-09 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | -1.92e-09 | | yes |

### Option O2 via selector (3) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -5,415,793.0268 | -5,415,793.0268 | yes |
| irr | -0.1289 | -0.1289 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 385,479.7624 | 385,479.7624 | yes |
| funding | 7,495,816.7080 | 7,495,816.7080 | yes |
| be_vol | 62,812.3932 | 62,812.3932 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 1.34e-09 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | -2.27e-09 | | yes |

### Option O3 via selector (4) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -3,537,420.1354 | -3,537,420.1354 | yes |
| irr | -0.1438 | -0.1438 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 327,245.5225 | 327,245.5225 | yes |
| funding | 4,931,578.7113 | 4,931,578.7113 | yes |
| be_vol | 56,720.9327 | 56,720.9327 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 6.98e-10 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | -2.39e-09 | | yes |

### Option O4 via selector (5) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -5,137,258.2685 | -5,137,258.2685 | yes |
| irr | -0.1455 | -0.1455 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 254,844.7825 | 254,844.7825 | yes |
| funding | 6,672,085.7312 | 6,672,085.7312 | yes |
| be_vol | 59,222.1031 | 59,222.1031 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 1.16e-09 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Option O5 via selector (6) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -5,863,590.2210 | -5,863,590.2210 | yes |
| irr | -0.1635 | -0.1635 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 250,580.6225 | 250,580.6225 | yes |
| funding | 7,411,252.0460 | 7,411,252.0460 | yes |
| be_vol | 59,626.4147 | 59,626.4147 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 1.46e-09 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Option O7 via selector (7) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -4,771,427.9511 | -4,771,427.9511 | yes |
| irr | -0.1297 | -0.1297 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 324,745.5225 | 324,745.5225 | yes |
| funding | 6,485,186.0050 | 6,485,186.0050 | yes |
| be_vol | 56,822.3784 | 56,822.3784 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 6.98e-10 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | -1.80e-09 | | yes |

### Option O8 via selector (8) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -4,147,282.5735 | -4,147,282.5735 | yes |
| irr | -0.0726 | -0.0726 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 704,315.1623 | 704,315.1623 | yes |
| funding | 7,098,289.0859 | 7,098,289.0859 | yes |
| be_vol | 68,661.5956 | 68,661.5956 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 1.40e-09 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Option O9 via selector (9) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -6,315,399.8074 | -6,315,399.8074 | yes |
| irr | -0.1980 | -0.1980 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 140,249.9669 | 140,249.9669 | yes |
| funding | 7,643,903.1386 | 7,643,903.1386 | yes |
| be_vol | 63,923.1776 | 63,923.1776 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 1.05e-09 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | -2.04e-09 | | yes |

### Option P1 via selector (10) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -3,973,034.7430 | -3,973,034.7430 | yes |
| irr | -0.1569 | -0.1569 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 318,079.0224 | 318,079.0224 | yes |
| funding | 5,415,260.1473 | 5,415,260.1473 | yes |
| be_vol | 65,360.2593 | 65,360.2593 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 1.22e-09 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 1.22e-09 | | yes |

### Option P2 via selector (11) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -4,013,320.2459 | -4,013,320.2459 | yes |
| irr | -0.1061 | -0.1061 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 585,677.6864 | 585,677.6864 | yes |
| funding | 6,368,910.1197 | 6,368,910.1197 | yes |
| be_vol | 72,968.3333 | 72,968.3333 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 2.33e-09 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Option O_orig via selector (12) - OK

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

### Pessimistic scenario + option P1 via selector - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -30,569,133.6894 | -30,569,133.6894 | yes |
| irr | None | None | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | -4,250,101.3112 | -4,250,101.3112 | yes |
| funding | 45,918,436.0180 | 45,918,436.0180 | yes |
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

### Override: first sales 2027 + 8 m3 loads - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -6,687,595.1187 | -6,687,595.1187 | yes |
| irr | -0.1772 | -0.1772 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 163,834.0786 | 163,834.0786 | yes |
| funding | 7,478,179.6239 | 7,478,179.6239 | yes |
| be_vol | 62,649.8427 | 62,649.8427 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 1.51e-09 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Override: first sales 2029 (delay 2) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -5,094,556.0798 | -5,094,556.0798 | yes |
| irr | -0.1643 | -0.1643 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 254,465.5245 | 254,465.5245 | yes |
| funding | 7,195,550.8986 | 7,195,550.8986 | yes |
| be_vol | 59,260.8343 | 59,260.8343 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 1.34e-09 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

### Option P2 downside stack (selector + overrides) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -6,772,314.2927 | -6,772,314.2927 | yes |
| irr | -0.2589 | -0.2589 | yes |
| payback | None | None | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 208,778.9775 | 208,778.9775 | yes |
| funding | 7,908,816.2215 | 7,908,816.2215 | yes |
| be_vol | 89,980.4466 | 89,980.4466 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 2.39e-09 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | -2.36e-09 | | yes |

### Option P2 upside stack (selector + overrides) - OK

| Item | Python | Excel (LibreOffice) | Match |
|---|---|---|---|
| npv | -1,417,868.8324 | -1,417,868.8324 | yes |
| irr | 0.0192 | 0.0192 | yes |
| payback | 9.8861 | 9.8861 | yes |
| dpayback | None | None | yes |
| ebitda_y3 | 1,168,625.6222 | 1,168,625.6222 | yes |
| funding | 5,486,153.5193 | 5,486,153.5193 | yes |
| be_vol | 51,405.5613 | 51,405.5613 | yes |
| revenue (11 years, max abs diff) | 0.0000 |  | yes |
| ebitda (11 years, max abs diff) | 0.0000 |  | yes |
| ebit (11 years, max abs diff) | 0.0000 |  | yes |
| tax (11 years, max abs diff) | 0.0000 |  | yes |
| net_income (11 years, max abs diff) | 0.0000 |  | yes |
| fcf (11 years, max abs diff) | 0.0000 |  | yes |
| cum (11 years, max abs diff) | 0.0000 |  | yes |
| Reconciliation rows (P&L sums, EBITDA, FCF = NI + D&A + dWC - capex + salvage), max abs | 0.00e+00 | | yes |
| UnitEconomics: avg EBITDA/m3 x volume - P&L EBITDA | 0.00e+00 | | yes |

## Python-internal reconciliation (base case)

- FCF vs (net income + D&A - change in WC - capex - sustaining capex + salvage): max abs diff 0.00e+00 EUR
- EBITDA vs (revenue - total opex): max abs diff 0.00e+00 EUR

## What is and is not checked

- Checked: every KPI on the Valuation sheet that drives the criteria, 7 yearly lines x 11 years, all check rows, for 3 scenarios, 3 override cases (incl. all original option hooks), every Agent-7 option through the live option selector (Inputs!I3) incl. the memo case O_orig (original base), one pessimistic-scenario + package P1 case, two timing / truck-load override cases, the P2 downside and upside stacks (selector + Override column), and the asset-light sheet (O6) KPIs.
- Not checked by recalculation: the Scenarios, Sensitivity, criterion-4 and Opt_Overview results values, because they are pasted from model_core.py / options.py (same code path as the cases above).
