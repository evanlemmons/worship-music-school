# Worship Music School

Source and web page for a weekly discipleship & development group for young musicians at **North Metro Church** (Kennesaw, GA) — Bible study, real musician skills, and playing together as a band. First-terms plan, **Sept 2026 – Feb 2027**.

The plan lives as markdown in `content/` and tabular data in `data/`. Two self-contained pages are generated into `docs/` (`index.html` + `leader.html`), and polished Word/Excel versions into `deliverables/`.

## Quick start
```bash
pip install markdown openpyxl
python3 build/build_site.py     # regenerate docs/index.html + docs/leader.html
# then open docs/index.html in a browser
```

## Layout
- `content/` — the plan (markdown) + `site-copy.md` (page copy). Source of truth, except `01-*` which is generated.
- `data/` — `rollout_schedule.csv`, the calendar (one row per Sunday; a `Status` column toggles dates on/off; week numbers are computed at build time).
- `build/` — generators. `build_site.py` is the main one.
- `docs/` — the public site: `index.html` (landing) + `leader.html` (leaders) + `PUBLISH.md` (GitHub Pages steps).
- `deliverables/` — generated Word/PDF/Excel versions.

See **`CLAUDE.md`** for the full map: the source-of-truth rule, all build commands, and the visual/brand conventions. See **`docs/PUBLISH.md`** to put the page live on GitHub Pages.

## Using Claude Code
Open this folder in a new Claude Code session and paste **`PROMPT.md`** as your first message — it briefs the assistant on the project and what to do first. Close each working session with `/session-end` to log decisions, rebuild, and ship.

---
*Non-denominational, NIV, discipleship-first. Brand: pine-teal `#123a40` + amber `#dc9a34`; Fraunces / Figtree / IBM Plex Mono.*
