# Worship Music School — project context

*This file is auto-loaded by Claude Code. It's the map of the project. Read it fully before making changes.*

## What this is
A weekly discipleship & development group for young musicians at **North Metro Church** (Kennesaw, GA). Every meeting has the same three parts, in order:
1. **Discipleship** (~25 min) — a short, discussion-driven Bible study (NIV).
2. **Musicianship** (~30 min) — the craft around the notes: gear/signal flow, in-ears, playing to a click, charts, rehearsing, the music director, planning a set, production.
3. **Playing together** (~35 min) — learn and work a song as a band, and play it.

~60-minute meetings, **confirmed Sunday evenings**, launching **Sept 6, 2026**. Two terms are planned week-by-week (Fall + Winter, **Sept 2026 – Feb 2027, 22 meetings**), ending in a **Fall Showcase** (Dec 13) and a **full-set milestone** (Feb 21). Leaders: **Evan** (former touring/session bassist; works at Planning Center), a **music-teacher co-leader** (piano/guitar), and a **professional vocalist**.

This repo holds the plan as source-of-truth content and generates a public web page (and polished documents) from it.

## Repository layout
- `content/` — the plan, in markdown.
  - Hand-written (edit these): `00-program-overview.md`, `02-discipleship-track.md`, `03-musicianship-track.md`, `05-planning-center-setup.md`, `06-promotion-communication.md`, `07-logistics-safety.md`, `README.md`.
  - **Generated** (do not hand-edit): `01-weekly-rhythm-schedule.md`, `04-song-library.md` — built from `data/` by `build/build_markdown_docs.py`.
- `data/` — tabular source of truth.
  - `rollout_schedule.csv` — the 22-meeting grid: Week, Date, Term, Discipleship, Passage, Musicianship, Playing Together, Notes.
  - `song_library.csv` — 45 songs: Title, Artist, Type, Key, BPM, Feel, Drums, Bass, Guitar, Keys, Vocals, Overall, Best For, Teaching Focus, Notes. Difficulty columns are 1–5.
- `site/` — the public web page (GitHub Pages ready).
  - `index.html` — **generated** by `build/build_site.py` from `content/` + `data/`. A single self-contained file (inline CSS/JS; Google Fonts via CDN). Opens with no server.
  - `PUBLISH.md` — how to publish on GitHub Pages. `.nojekyll` — disables Jekyll processing.
- `build/` — generators (see **Build**).
- `deliverables/` — **generated** polished outputs (Program Plan `.docx`/`.pdf`, Rollout Schedule `.xlsx`, Song Library `.xlsx`) for sharing/printing.

## Source-of-truth rule (important)
- **Edit by hand:** `content/00,02,03,05,06,07` and `data/*.csv`.
- **Regenerate, never hand-edit:** `content/01`, `content/04`, `site/index.html`, `deliverables/*`.

To change the schedule or songs, edit the CSV in `data/`, then rebuild. To change prose, edit the relevant `content/*.md`, then rebuild the site.

## Build
Scripts resolve their own paths, so they can be run from anywhere. **Dependencies:** `pip install markdown openpyxl`; for the Word doc, Node with `npm i docx`; LibreOffice is optional (used to render PDFs).

Regenerate the site after editing content or data:
```bash
python3 build/build_markdown_docs.py   # content/01 + content/04 (from data/*.csv)
python3 build/build_site.py            # site/index.html   <- the important one
```
Regenerate the polished deliverables (optional):
```bash
python3 build/build_xlsx.py            # deliverables/*.xlsx
node    build/build_plan_docx.js       # deliverables/*.docx   (needs `npm i docx`)
```
Preview the page: open `site/index.html` in a browser.

**Seed generators (optional / provenance):** `build/build_songs.py` and `build/build_schedule.py` recreate `data/*.csv` from Python literals inside them. ⚠️ Running them **overwrites** the CSVs — only use them to reset from seed (or keep the literals in sync with the CSVs). For normal work, edit the CSVs directly and skip these.

## Conventions / brand
- **Content:** NIV; non-denominational, Christ-centered; worship-leaning repertoire with occasional secular change-ups; discipleship-first tone.
- **Song difficulty:** 1 (very easy) → 5 (a feature part), rated **per instrument** so a beginner and an advanced player can share a song.
- **Visual identity:** deep pine-teal `#123a40` (with darker `#0d262b`, brand `#1a4b51`) + warm amber `#dc9a34`; fonts **Fraunces** (display), **Figtree** (body), **IBM Plex Mono** (labels/data); signature motif = song difficulty shown as audio **input-level meters**. Keep `index.html` self-contained.
- **Dates** key off a confirmed Sunday-evening start, Sep 6, 2026 — if the meeting night ever changes, update `data/rollout_schedule.csv` and rebuild.

## Current state
Complete first draft. The page is built and was shared for discussion. It is **not yet published** to a permanent public URL — that's the immediate next step.

## Assumptions to confirm with Evan
Meeting night/time: **confirmed** — Sunday evenings, ~60 min, from Sep 6, 2026. Still open: ages (assumed middle + high, ~12–18) · experience (assumed a wide mix — hence tiered parts) · group size (one band of ~5–12; splits into two).

## Roadmap / next
1. **Publish** `site/` to GitHub Pages under Evan's account (see `site/PUBLISH.md`); set up a change → rebuild → push loop so the live page stays current.
2. **Work the open decisions** in `content/07-logistics-safety.md` (also shown in the page's "Open questions" section); update content as they're settled.
3. **Grow the page into a per-week resource hub** — per-song charts, chord sheets, and reference-track links organized by week (the "students download this week's songs" idea). The song and schedule data are structured to support this.
