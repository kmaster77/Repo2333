"""Pitch-deck charts from model_core.py results -> model/charts/*.png (200 dpi)."""
from __future__ import annotations

import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import model_core as mc  # noqa: E402

OUT = os.path.join(HERE, "charts")
os.makedirs(OUT, exist_ok=True)

# Validated categorical palette (fixed order) + neutral inks
C = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11, "axes.titlesize": 14, "axes.titleweight": "bold",
    "axes.labelcolor": INK2, "axes.edgecolor": GRID, "xtick.color": INK2, "ytick.color": INK2,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8, "axes.axisbelow": True,
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
    "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False,
})
MEUR = FuncFormatter(lambda v, _: f"{v / 1e6:,.1f}")


def save(fig, name):
    p = os.path.join(OUT, name)
    fig.savefig(p, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return p


def subtitle(ax, text):
    ax.text(0, 1.02, text, transform=ax.transAxes, color=INK2, fontsize=10, va="bottom")


def unit_cost_stack(tab):
    r = mc.run(tab)
    y, u = r["years"], r["unit"]
    t = 3 + int(round(r["params"]["first_sales_delay_yr"]))     # third operating year = first full-output year
    vol = y["volume"][t]
    fixed_m3 = lambda k: y[f"opex_{k}"][t] / vol
    share = y["volume_circ"][t] / vol

    def stack(prod):
        m = u["m_circ"] if prod == "circ" else u["m_conv"]
        price = y["price_circ"][t] if prod == "circ" else y["price_conv"][t]
        return price, {
            "Cement": m["cement"][t],
            "Aggregates (gravel, sand, recycled)": m["gravel"][t] + m["sand"][t] + m["rca"][t],
            "Admixture, water, RCA testing": m["admix"][t] + m["water"][t] + (u["rca_qc_m3"] if prod == "circ" else 0),
            "Delivery by truck mixer": u["delivery_m3"],
            "Plant staff, maintenance, energy, certification": fixed_m3("staff_prod") + fixed_m3("maintenance")
            + fixed_m3("certification") + u["energy_m3"],
            "Site lease, overheads, bad debt": fixed_m3("site_lease") + fixed_m3("staff_sga") + fixed_m3("sga_other")
            + price * r["params"]["bad_debt_pct_revenue"] / 100,
            "Depreciation": y["da"][t] / vol,
        }
    pc, sc = stack("circ")
    pv, sv = stack("conv")
    pa = share * pc + (1 - share) * pv
    sa = {k: share * sc[k] + (1 - share) * sv[k] for k in sc}
    bars = [("Circular mix\n(50% recycled coarse)", pc, sc), ("Standard mix\n(CEM III/B, gravel)", pv, sv), ("Plant average\n(60% circular)", pa, sa)]
    fig, ax = plt.subplots(figsize=(10, 6.2))
    x = range(len(bars))
    for i, (lab, price, s) in enumerate(bars):
        bottom = 0
        for j, (k, v) in enumerate(s.items()):
            ax.bar(i, v, bottom=bottom, color=C[j], width=0.55, edgecolor=SURF, linewidth=1.5, label=k if i == 0 else None)
            if v > 6:
                ax.text(i, bottom + v / 2, f"{v:.0f}", ha="center", va="center", color="white", fontsize=9, fontweight="bold")
            bottom += v
        ax.plot([i - 0.34, i + 0.34], [price, price], color=INK, linewidth=2.2)
        ax.text(i + 0.36, price, f"price {price:.0f}", va="center", color=INK, fontsize=10)
        ax.text(i, max(price, bottom) + 4, f"cost {bottom:.0f}\nmargin {price - bottom:+.1f}", ha="center", va="bottom", color=INK2, fontsize=10)
    ax.set_xticks(list(x), [b[0] for b in bars])
    ax.set_ylabel("EUR per m³ delivered (real 2026 €)")
    ax.set_ylim(0, 180)
    ax.grid(axis="x", visible=False)
    ax.set_title("Circular concrete costs about the same as standard concrete", loc="left", pad=28)
    subtitle(ax, f"Cost per m³ in {mc.YEARS[t]} (first full year, {vol:,.0f} m³), base case. Black line = selling price.")
    ax.legend(loc="upper left", bbox_to_anchor=(1.12, 1), fontsize=9.5)
    return save(fig, "unit_cost_stack.png")


def tornado(tab):
    sens = mc.sensitivity(tab)
    base = sens[0]["npv_base"]
    skip = {"Transport distance (delivery 10-35 km + RCA haul 15-50 km)", "Cement price + ETS/CBAM path"}
    s = sorted([x for x in sens if x["name"] not in skip], key=lambda x: x["swing"])[-15:]
    fig, ax = plt.subplots(figsize=(11, 7.5))
    for i, d in enumerate(s):
        lo, hi = d["npv_low_input"] - base, d["npv_high_input"] - base
        ax.barh(i, lo, left=base, color=C[0], height=0.62, edgecolor=SURF, label="Input at LOW value" if i == 0 else None)
        ax.barh(i, hi, left=base, color=C[1], height=0.62, edgecolor=SURF, label="Input at HIGH value" if i == 0 else None)
    ax.axvline(base, color=INK, linewidth=1.5)
    ax.axvline(0, color=INK2, linewidth=1, linestyle="--")
    ax.text(0, len(s) - 0.3, " NPV = 0", color=INK2, fontsize=9, va="bottom")
    ax.text(base - 0.1e6, -1.0, f"base NPV {base / 1e6:.1f}M ", ha="right", va="center", color=INK, fontsize=9.5)
    ax.set_yticks(range(len(s)), [d["name"] for d in s], fontsize=9.5)
    ax.xaxis.set_major_formatter(MEUR)
    ax.set_xlabel("NPV at 8% real (EUR million)")
    ax.grid(axis="y", visible=False)
    ax.set_ylim(-1.4, len(s))
    ax.set_title("Selling price moves NPV far more than any other input", loc="left", pad=28)
    subtitle(ax, "One input at a time to its low / high value. Only the high selling price lifts NPV above zero.")
    ax.legend(loc="lower right", fontsize=9.5)
    return save(fig, "tornado_npv.png")


def cashflow(tab):
    y = mc.run(tab)["years"]
    fig, ax = plt.subplots(figsize=(10.5, 5.8))
    yrs = y["year"]
    ax.bar(yrs, y["fcf"], color=C[0], width=0.6, label="Free cash flow in the year")
    ax.plot(yrs, y["cum_fcf"], color=C[1], linewidth=2.2, marker="o", markersize=7, markeredgecolor=SURF, markeredgewidth=2,
            label="Cumulative free cash flow")
    ax.axhline(0, color=INK2, linewidth=1)
    m = min(y["cum_fcf"])
    tm = y["cum_fcf"].index(m)
    ax.annotate(f"funding need {-m / 1e6:.1f}M", (yrs[tm], m), xytext=(yrs[tm] + 0.6, m - 0.9e6), color=INK, fontsize=10,
                arrowprops=dict(arrowstyle="-", color=INK2))
    ax.annotate(f"2036 incl. salvage: {y['cum_fcf'][-1] / 1e6:.1f}M", (yrs[-1], y["cum_fcf"][-1]), xytext=(yrs[-1] - 2.6, y["cum_fcf"][-1] + 0.9e6),
                color=INK, fontsize=10, arrowprops=dict(arrowstyle="-", color=INK2))
    ax.set_ylim(m - 1.5e6, max(y["fcf"]) + 1.2e6)
    ax.yaxis.set_major_formatter(MEUR)
    ax.set_ylabel("EUR million (real 2026 €)")
    ax.set_xticks(yrs, [str(v) for v in yrs])
    ax.grid(axis="x", visible=False)
    ax.set_title("The plant does not earn back its investment within 10 years", loc="left", pad=28)
    d = int(round(mc.run(tab)["params"]["first_sales_delay_yr"]))
    subtitle(ax, f"Base case. Permits 2026, build {mc.YEARS[d]} (capex EUR 5.5M + start-up costs); first sales {mc.YEARS[d + 1]}.")
    ax.legend(loc="lower right")
    return save(fig, "cashflow_10yr.png")


def scenarios(tab):
    res = {s: mc.run(tab, scenario=s)["kpis"] for s in mc.SCENARIOS}
    fig, ax = plt.subplots(figsize=(9, 5.8))
    labs = ["Pessimistic\n(all inputs bad)", "Base", "Optimistic\n(all inputs good)"]
    vals = [res[s]["npv"] for s in mc.SCENARIOS]
    ax.bar(labs, vals, color=[C[1], C[0], C[2]], width=0.55, edgecolor=SURF)
    for i, s in enumerate(mc.SCENARIOS):
        k = res[s]
        irr = "n/a" if k["irr"] is None else f"{k['irr'] * 100:.1f}%"
        pb = "not reached" if k["payback"] is None else f"{k['payback']:.1f} yr"
        txt = f"NPV {k['npv'] / 1e6:+.1f}M\nIRR {irr}\npayback {pb}"
        yv = vals[i]
        ax.text(i, yv + (1.5e6 if yv >= 0 else -1.5e6), txt, ha="center", va="bottom" if yv >= 0 else "top", fontsize=10, color=INK)
    ax.axhline(0, color=INK2, linewidth=1)
    ax.yaxis.set_major_formatter(MEUR)
    ax.set_ylabel("NPV at 8% real (EUR million)")
    ax.set_ylim(min(vals) * 1.45, max(vals) * 1.5)
    ax.grid(axis="x", visible=False)
    ax.set_title("Base case NPV is negative; the outcome range is very wide", loc="left", pad=28)
    subtitle(ax, "Pessimistic / optimistic move ALL inputs together: stress bounds, not likely cases.")
    return save(fig, "scenarios_npv.png")


def ebitda(tab):
    r_ = mc.run(tab)
    y = r_["years"]
    d = int(round(r_["params"]["first_sales_delay_yr"]))
    yrs, e = y["year"][1 + d:], y["ebitda"][1 + d:]
    fig, ax = plt.subplots(figsize=(10, 5.6))
    ax.bar(yrs, e, color=[C[1] if v < 0 else C[0] for v in e], width=0.6, edgecolor=SURF)
    for x_, v, rv in zip(yrs, e, y["revenue"][1 + d:]):
        ax.text(x_, v + (0.02e6 if v >= 0 else -0.02e6), f"{v / 1e6:.2f}\n({v / rv * 100:.1f}%)", ha="center",
                va="bottom" if v >= 0 else "top", fontsize=9, color=INK)
    ax.axhline(0, color=INK2, linewidth=1)
    ax.yaxis.set_major_formatter(MEUR)
    ax.set_ylabel("EBITDA, EUR million (margin % of revenue)")
    ax.set_xticks(yrs, [str(v) for v in yrs])
    ax.set_ylim(min(e) * 1.6, max(e) * 1.5)
    ax.grid(axis="x", visible=False)
    first_pos = next((i + 1 for i, v in enumerate(e) if v > 0), None)
    pos = [v for v in e[2:]]
    ax.set_title(f"EBITDA turns positive in operating year {first_pos}, but stays at EUR {min(pos) / 1e6:.1f}-{max(pos) / 1e6:.1f}M a year",
                 loc="left", pad=28)
    v_ = y["volume"][1 + d:]
    subtitle(ax, f"Base case, {v_[0] / 1e3:.0f}k / {v_[1] / 1e3:.0f}k / {v_[2] / 1e3:.0f}k m³ in {yrs[0]} / {yrs[1]} / {yrs[2]}+. "
                 "Margin % of revenue in brackets; it shrinks as carbon costs rise faster than prices.")
    return save(fig, "ebitda_by_year.png")


def breakeven(tab):
    vols = list(range(40000, 160001, 5000))
    npv_v = [mc.run(tab, {"output_steady_state": v})["kpis"]["npv"] for v in vols]
    prices = [115 + i for i in range(0, 51)]
    npv_p = [mc.run(tab, {"price_plant_avg_all_classes": p})["kpis"]["npv"] for p in prices]
    bv = mc.solve(tab, "output_steady_state", lo=20000, hi=240000)
    bp = mc.solve(tab, "price_plant_avg_all_classes", lo=80, hi=250)
    fig, axs = plt.subplots(1, 2, figsize=(12, 5.4), sharey=True)
    for ax, xs, ys, base, be, xl, fmt in (
        (axs[0], [v / 1000 for v in vols], npv_v, 70, bv / 1000, "Steady-state volume (thousand m³ per year)", "{:.0f}k m³"),
        (axs[1], prices, npv_p, 135, bp, "Plant-average selling price (EUR per m³, 2026)", "EUR {:.0f}/m³")):
        ax.plot(xs, ys, color=C[0], linewidth=2.2)
        ax.axhline(0, color=INK2, linewidth=1)
        bn = ys[min(range(len(xs)), key=lambda i: abs(xs[i] - base))]
        ax.plot([base], [bn], "o", color=C[1], markersize=9, markeredgecolor=SURF, markeredgewidth=2)
        ax.annotate("base " + fmt.format(base), (base, bn), xytext=(10, -18), textcoords="offset points", color=INK, fontsize=10)
        ax.plot([be], [0], "o", color=INK, markersize=8, markeredgecolor=SURF, markeredgewidth=2)
        ax.annotate("NPV = 0 at " + fmt.format(be), (be, 0), xytext=(-150, 22), textcoords="offset points", color=INK, fontsize=10,
                    arrowprops=dict(arrowstyle="-", color=INK2))
        ax.set_xlabel(xl)
        ax.yaxis.set_major_formatter(MEUR)
    axs[0].set_ylabel("NPV at 8% real (EUR million)")
    axs[0].set_title(f"Break-even needs ~{bv / 1000:.0f}k m³ a year ...", loc="left", pad=10)
    axs[1].set_title(f"... or a ~{(bp / 135 - 1) * 100:.1f}% higher average price", loc="left", pad=10)
    fig.suptitle("What it takes to reach NPV = 0 (other inputs at base)", x=0.07, ha="left", fontsize=15, fontweight="bold", y=1.03)
    return save(fig, "breakeven.png")


def main():
    tab = mc.load_inputs()
    for f in (unit_cost_stack, tornado, cashflow, scenarios, ebitda, breakeven):
        print("written", f(tab))


if __name__ == "__main__":
    main()
