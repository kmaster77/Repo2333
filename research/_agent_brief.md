# Shared brief for all agents (read this first)

Project: objective business case for a **circular concrete business in the Netherlands**.
Base case = **archetype B: circular ready-mix / prefab producer** using recycled aggregates and low-clinker binders. Archetypes A (recycling hub), C (element reuse), D (platform) are screened and used as viability options.
Region: **national** (first-plant location is an output). Audience: **investors / competition jury**. Discount rate **8% real**. Horizon 2027–2036, prices in **2026 €, excl. VAT**. Today is 2026-10-22.
Full plan: `/home/user/Repo2333/plan.md`.

## Working rules
- **Sources:** prefer primary sources: Rijksoverheid, RVO, CBS, Rijkswaterstaat, PBL, TNO, Betonakkoord / MVO Nederland, NEN/BRL norms, NMD (Nationale Milieudatabase), EU (ETS, CBAM, CPR), company annual reports, peer-reviewed papers (incl. TU Delft research on recycled concrete). Trade press (Cobouw, Betoniek, Bouwmachines, etc.) only as a secondary source.
- Mark every claim **[VERIFIED]** (source found and read), **[ESTIMATE]** (derived from sources — show the calculation) or **[ASSUMPTION]** (no source — give reasoning).
- Prices: state the year, unit (€/t or €/m³), and ex-works or delivered. Convert older prices to 2026 € (state the index used, e.g. CBS CPI or CBS GWW input price index) and show the factor.
- **Do not invent** companies, quotes, people, numbers or URLs. If data is missing, say so and give a low/base/high range. A cited URL must be one you actually opened or saw in search results.
- When a "domain anchor" given to you turns out wrong or outdated, say so clearly and give the corrected fact.
- Plain English. Short sentences. Explain each technical term once. The client's English is a second language.

## Logging (to avoid write conflicts, each agent has its OWN log files)
- Sources → `research/sources_<agentname>.md` as a table: `| ID | Title | Publisher | URL | Date published | Date accessed | Supports |`. Use IDs with your prefix (e.g. `POL-01`, `MKT-01`, `TEC-01`, `CMP-01`, `CST-01`).
- Assumptions → `research/assumptions_<agentname>.md` as a table: `| ID | Description | Low | Base | High | Unit | Reasoning / source IDs | Confidence (L/M/H) |`. Same prefixes (`A-POL-01` etc.).
- In your main file, cite by ID, e.g. "[VERIFIED, POL-03]".
- The orchestrator merges the logs into `research/sources.md` and `research/assumptions.md`. Do not edit those two files.

## Final message to the orchestrator
Max ~250 words: the 5–8 most important findings (with numbers), the biggest data gaps, any anchor you corrected, and the paths of the files you wrote. Do NOT commit to git.
