# Worship Music School — project context

*This file is auto-loaded by Claude Code. It's the map of the project. Read it fully before making changes.*

## What this is
A weekly discipleship & development group for young musicians at **North Metro Church** (Kennesaw, GA). Every meeting has the same three parts, in order:
1. **Discipleship** (~25 min) — a short, discussion-driven Bible study (NIV).
2. **Musicianship** (~30 min) — the craft around the notes: gear/signal flow, in-ears, playing to a click, charts, rehearsing, the music director, planning a set, production.
3. **Playing together** (~35 min) — learn and work a song as a band, and play it.

~60-minute meetings, **confirmed Sunday evenings**, launching **Sept 6, 2026**. Two terms are planned week-by-week (Fall + Winter, **Sept 2026 – Feb 2027, 22 meetings**), ending in a **Fall Showcase** (Dec 13) and a **full-set milestone** (Feb 28). Leaders: **Evan** (former touring/session bassist; works at Planning Center), a **music-teacher co-leader** (piano/guitar), and a **professional vocalist**.

This repo holds the plan as source-of-truth content and generates a public web page (and polished documents) from it.

## Repository layout
- `content/` — the plan, in markdown.
  - Hand-written (edit these): `00-program-overview.md`, `02-discipleship-track.md`, `03-musicianship-track.md`, `05-planning-center-setup.md`, `06-promotion-communication.md`, `07-logistics-safety.md`, `README.md`.
  - `site-copy.md` — **all editable copy** for both generated pages (hero, section headings/ledes, the three cards, team bios, open-questions lists, footer, meta tags, plus the leader-page hero). Hand-written. Slots are `## key` blocks; `build/build_site.py` reads them, so the page's *words* are edited here while its *structure* (layout, CSS, tables) stays in the build script. Not every string is here — table column headers and section chrome stay in the build script.
  - `04-song-library.md` — hand-written **TBD stub** (the song list is deferred until the roster settles; an earlier ~45-song draft is in git history).
  - **Generated** (do not hand-edit): `01-weekly-rhythm-schedule.md` — built from `data/rollout_schedule.csv` by `build/build_markdown_docs.py`.
- `data/` — tabular source of truth.
  - `rollout_schedule.csv` — **the calendar.** One row per Sunday: `Date, Term, Status, Discipleship (~15 min), Passage (NIV), Musicianship (~20 min), Note`. `Status` is `meeting` or `off` — that's how you turn a date on/off (holidays, school breaks). **Week numbers are computed by the build** (meetings counted in order), so toggling a date needs no renumbering. `Note` labels off-weeks. Songs aren't programmed here (chosen weekly to fit who attends).
- `docs/` — the public site (GitHub Pages ready). Both pages are **generated** by `build/build_site.py` (single self-contained files; inline CSS/JS; Google Fonts via CDN).
  - `index.html` — the landing page (for families/students).
  - `leader.html` — the leader page (Planning Center setup, promotion, logistics, open decisions). Not linked from the landing nav; public URL (can't be password-protected on a static host).
  - `PUBLISH.md` — how to publish on GitHub Pages. `.nojekyll` — disables Jekyll processing.
- `build/` — generators (see **Build**).
- `deliverables/` — **generated** polished outputs (Program Plan `.docx`/`.pdf`, Rollout Schedule `.xlsx`) for sharing/printing.

## Source-of-truth rule (important)
- **Edit by hand:** `content/00,02,03,04,05,06,07`, `content/site-copy.md`, and `data/rollout_schedule.csv`.
- **Regenerate, never hand-edit:** `content/01`, `docs/index.html`, `docs/leader.html`, `deliverables/*`.

To change the calendar (which dates are on/off) or the weekly Bible-study/musicianship topics, edit `data/rollout_schedule.csv`, then rebuild. To change deep-content prose (studies, musicianship topics, setup/promo/logistics), edit the relevant `content/*.md`. To change page copy (hero, section intros, cards, team, open questions, leader-page text), edit `content/site-copy.md`. Either way, rebuild the site after. Note: the Studies/Musicianship week headers intentionally carry **no dates** — the schedule owns dates, so calendar shifts never touch that prose.

## Build
Scripts resolve their own paths, so they can be run from anywhere. **Dependencies:** `pip install markdown openpyxl`; for the Word doc, Node with `npm i docx`; LibreOffice is optional (used to render PDFs).

Regenerate after editing content or data:
```bash
python3 build/build_markdown_docs.py   # content/01 (from data/rollout_schedule.csv)
python3 build/build_site.py            # docs/index.html + docs/leader.html   <- the important one
```
Regenerate the polished deliverables (optional):
```bash
python3 build/build_xlsx.py            # deliverables/Rollout Schedule.xlsx
node    build/build_plan_docx.js       # deliverables/Program Plan.docx   (needs `npm i docx`)
```
Preview: open `docs/index.html` (or `docs/leader.html`) in a browser.

## Conventions / brand
- **Content:** NIV; non-denominational, Christ-centered; worship-leaning repertoire with occasional secular change-ups; discipleship-first tone.
- **Song difficulty (deferred):** the plan is per-instrument 1 (very easy) → 5 (a feature part) so a beginner and an advanced player can share a song. Songs are currently TBD; the "input-level meter" motif and per-song resources come back when a repertoire settles (both preserved in git history).
- **Visual identity:** deep pine-teal `#123a40` (with darker `#0d262b`, brand `#1a4b51`) + warm amber `#dc9a34`; fonts **Fraunces** (display), **Figtree** (body), **IBM Plex Mono** (labels/data). Keep both pages self-contained.
- **Dates** key off a confirmed Sunday-evening start, Sep 6, 2026, and are owned entirely by `data/rollout_schedule.csv` — change a `Status` cell to toggle a date on/off, then rebuild.

## Current state
**Live:** https://evanlemmons.github.io/worship-music-school/ (repo: github.com/evanlemmons/worship-music-school, public). Published via GitHub Pages, deploying from `main` / `/docs`. Meeting night/time is confirmed (Sunday evenings, ~60 min, from Sep 6, 2026); other assumptions and open decisions below are still being worked.

## Assumptions to confirm with Evan
Meeting night/time: **confirmed** — Sunday evenings, ~60 min, from Sep 6, 2026. Still open: ages (assumed middle + high, ~12–18) · experience (assumed a wide mix — hence tiered parts) · group size (one band of ~5–12; splits into two).

## Roadmap / next
1. **Change → rebuild → publish workflow:** use `/session-end` at the close of a working session — it logs decisions, rebuilds `docs/index.html` (and `deliverables/` if relevant), commits, and merges so the live page stays current.
2. **Work the open decisions** in `content/07-logistics-safety.md` (also shown in the page's "Open questions" section); update content as they're settled.
3. **Grow the page into a per-week resource hub** — per-song charts, chord sheets, and reference-track links organized by week (the "students download this week's songs" idea). The song and schedule data are structured to support this.
