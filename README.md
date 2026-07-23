# Worship Music School

Source and web page for a weekly discipleship & development group for young musicians at **North Metro Church** (Kennesaw, GA) — Bible study, real musician skills, and playing together as a band. First-terms plan, **Sept 2026 – Feb 2027**.

The plan lives as markdown in `content/` and tabular data in `data/`. A single self-contained web page is generated into `docs/index.html`, and polished Word/Excel versions into `deliverables/`.

## Quick start
```bash
pip install markdown openpyxl
python3 build/build_site.py     # regenerate docs/index.html
# then open docs/index.html in a browser
```

## Layout
- `content/` — the plan (markdown). Source of truth, except `01-*` and `04-*` which are generated.
- `data/` — `rollout_schedule.csv` (22-week grid) and `song_library.csv` (45 songs, difficulty per instrument).
- `build/` — generators. `build_site.py` is the main one.
- `docs/` — the public web page (`index.html`) + `PUBLISH.md` (GitHub Pages steps).
- `deliverables/` — generated Word/PDF/Excel versions.

See **`CLAUDE.md`** for the full map: the source-of-truth rule, all build commands, and the visual/brand conventions. See **`docs/PUBLISH.md`** to put the page live on GitHub Pages.

## Using Claude Code
Open this folder in a new Claude Code session and paste **`PROMPT.md`** as your first message — it briefs the assistant on the project and what to do first (publish it, keep it in sync, work the open decisions, and grow it into a per-week song-resource hub).

---
*Non-denominational, NIV, discipleship-first. Brand: pine-teal `#123a40` + amber `#dc9a34`; Fraunces / Figtree / IBM Plex Mono.*
