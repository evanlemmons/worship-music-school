# Session Log

Working notes from each session on Worship Music School — decisions and why, not a diff dump (see `git log` for that).

## 2026-07-23 (session 2)

**Decided:**
- Evan wants to make many copy edits himself, locally. Chose to move all landing-page copy out of the Python build script into plain markdown so every visible word is editable without touching code.

**Changed:**
- Created `content/site-copy.md` — a "copy deck" holding all landing-page text (hero, section headings/ledes, the three cards, term blurbs, team bios, open-questions lists, footer, and the `<title>`/meta tags). Slots are `## key` blocks; plain sections are prose, tabular bits (facts, cards, lists) are `- ` bullets with ` | ` field separators. Markdown (`**bold**`/`*italic*`) works.
- Rewired `build/build_site.py` to read from the copy deck (parser + `ci()`/`cattr()`/`crows()` helpers). The page's structure/CSS/tables stay in the script; only the words moved out. Verified via a visible-text diff that this is a pure refactor — the only content changes are intended: dropped the stale "the name is a working title" line, and fixed a pre-existing double-escape bug where two "Setup" section summaries rendered literal `&amp;`/`&rsquo;`.
- Bonus: the song-library filter counts (All 45 / Worship 29 / …) are now computed from the CSV instead of hardcoded, so they can't drift.
- Documented the new file in `CLAUDE.md` (layout + source-of-truth rule), `docs/README.md`, and the `/session-end` skill.

**Open:** (unchanged from session 1 below) — Showcase format, room, budget figure, PC admin owner, gear inventory, logo/brand, experience-mix & group-size assumptions, possible Planning Center Services integration for resource links. Note: `Program Plan.pdf` still stale vs `.docx` (no LibreOffice locally).

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
