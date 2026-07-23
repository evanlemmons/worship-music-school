# Session Log

Working notes from each session on Worship Music School — decisions and why, not a diff dump (see `git log` for that).

## 2026-07-23

**Decided:**
- Meeting night/length: **Sunday evenings, ~60 min** (not the drafted Wednesday/90-min assumption) — launch shifted to **Sep 6, 2026** and every date in the 22-week schedule moved with it (same weekly cadence, 3 days earlier).
- Repo/URL: public repo `evanlemmons/worship-music-school`, live at `https://evanlemmons.github.io/worship-music-school/`.
- Name **"Worship Music School" is final**, not a working title.
- Grade range **confirmed**: middle + high school (~12–18), all levels, no floor.
- Cost **confirmed**: free to families.
- Showcase format (standalone vs. folded into a service): still undecided — left open.

**Changed:**
- Flattened the unzipped bundle into the project root and initialized git.
- Published to GitHub Pages. GitHub Pages branch deploys only support `/` or `/docs` as the source folder, so the generated site moved from `site/` to `docs/` (updated `build_site.py` and all doc references accordingly).
- Applied the Sunday/60-min decision across `data/rollout_schedule.csv`, all of `content/`, `CLAUDE.md`, `README.md`, `PROMPT.md`, and every build script (`build_site.py`, `build_markdown_docs.py`, `build_xlsx.py`, `build_plan_docx.js`, `build_schedule.py`).
- Applied the name/grade/cost decisions to `content/00`, `content/07`, `content/README.md`, and the site's "Open questions" section — moved them from "assumed" to "confirmed."
- Built `/session-end` — a project skill (`.claude/skills/session-end/`) that applies session decisions to source, rebuilds, logs here, and ships via branch + PR + merge.
- Built v1 of the per-week resource hub: added `Chart URL` / `Chord Chart URL` / `Reference Track URL` columns to `data/song_library.csv`, and a `Song Title` join column to `data/rollout_schedule.csv` (semicolon-separated, exact match against Song Library titles — verified programmatically). The public site's Schedule and Song Library tables both now render a **Resources** column: link pills when a URL is filled in, a muted "Coming soon" otherwise. All 45 songs currently have empty URLs — the plumbing is live, content gets filled in incrementally.

**Open:**
- Showcase format (standalone vs. folded into a service).
- Room on the church calendar for Sunday evenings.
- Budget figure for gear/consumables.
- Who owns Planning Center admin & parent communication.
- Existing gear inventory (so we only buy the gaps).
- Whether we want a simple logo/brand.
- Assumptions still unconfirmed: experience mix, group size.
- Possible future Planning Center Services integration to source/sync resource links instead of hand-filling the CSV (Evan can provide a PAT if we go this route).
- `deliverables/Worship Music School - Program Plan.pdf` is now stale relative to the `.docx` — no LibreOffice on this machine to regenerate it. Re-export from Word/`soffice` when needed.
