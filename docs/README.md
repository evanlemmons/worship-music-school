# Worship Music School

A weekly discipleship & development group for young musicians at **North Metro Church** (Kennesaw, GA) — Bible study, real musician skills, and playing together as a band.

This folder holds two self-contained pages presenting the plan for the first two terms (Sept 2026 – Feb 2027). No build step, no dependencies — just HTML.

- **`index.html`** — the landing page (families/students). **Live:** https://evanlemmons.github.io/worship-music-school/
- **`leader.html`** — a separate leader page (setup, promotion, logistics, open decisions). Not linked from the landing nav; reach it at `…/leader.html`. Public URL — a static site can't password-protect it.

## What's on the landing page
- The vision and the three-part weekly meeting (discipleship → musicianship → playing together)
- The two-term arc and milestones (including a Fall Showcase)
- The 22-week Bible-study + musicianship rollout schedule
- The discipleship / Bible-study arc and the musicianship topic arc
- A song section (TBD — repertoire chosen once the roster settles)

## Editing
Both pages are generated — don't hand-edit `index.html` / `leader.html`. Source lives at the repo root: page copy (hero, section intros, cards, team, open questions, leader-page text) in `content/site-copy.md`; deep-content prose in `content/*.md`; the calendar in `data/rollout_schedule.csv`. Edit those, then run `python3 build/build_site.py` from the repo root. See `CLAUDE.md` at the repo root for the full map.
