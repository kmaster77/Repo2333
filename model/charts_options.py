"""Chart: NPV per viability option vs the base case -> model/charts/options_npv.png (reads results_options.json)."""
from __future__ import annotations

import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "charts", "options_npv.png")

INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
BLUE, ORANGE, GREY = "#2a78d6", "#eb6834", "#a3a29e"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11, "axes.titlesize": 14, "axes.titleweight": "bold",
    "axes.labelcolor": INK2, "axes.edgecolor": GRID, "xtick.color": INK2, "ytick.color": INK2,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8, "axes.axisbelow": True,
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
    "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False,
})


def main():
    with open(os.path.join(HERE, "results_options.json")) as f:
        res = json.load(f)["options"]
    items = [(k, r) for k, r in res.items()]
    items.sort(key=lambda kr: kr[1]["kpis"]["npv"])
    labels = [f"{k}  {r['name']}" for k, r in items]
    vals = [r["kpis"]["npv"] / 1e6 for _, r in items]
    cols = [GREY if k in ("BASE", "O0") else ORANGE if k.startswith("P") else BLUE for k, _ in items]

    fig, ax = plt.subplots(figsize=(11, 7.2))
    y = range(len(items))
    ax.barh(list(y), vals, color=cols, height=0.62)
    ax.scatter(vals, list(y), color=cols, marker="D", s=28, zorder=3)
    ax.axvline(0, color=INK, linewidth=1.4)
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels, fontsize=10)
    ax.grid(axis="y", visible=False)
    lo = min(vals)
    for i, ((k, r), v) in enumerate(zip(items, vals)):
        c = r["criteria"]
        txt = f"{v:+.1f}  ({c['n_pass']}/4 criteria)"
        ax.text(v - 0.08 if v < 0 else v + 0.08, i, txt, va="center", ha="right" if v < 0 else "left", fontsize=9, color=INK2)
    ax.set_xlim(lo - 2.6, 1.6)
    ax.set_xlabel("NPV at 8% real, 2026-2036, EUR million (salvage-only terminal value)")
    ax.set_title("No single option makes the plant viable; the full package only reaches break-even", loc="left", pad=28)
    ax.text(0, 1.02, "Grey = base references, blue = single options, orange = combined packages. Label: NPV and plan.md criteria passed.",
            transform=ax.transAxes, color=INK2, fontsize=10, va="bottom")
    ax.text(0.0, -0.12, "NPV = 0 line: right of it the option earns more than 8% real. Criterion 4 (robustness) passes for no option.",
            transform=ax.transAxes, color=INK2, fontsize=9)
    fig.savefig(OUT, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("written", OUT)


if __name__ == "__main__":
    main()
