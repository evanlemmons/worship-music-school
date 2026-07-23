# Worship Music School

A weekly discipleship & development group for young musicians at **North Metro Church** (Kennesaw, GA) — Bible study, real musician skills, and playing together as a band.

This repo is a single, self-contained web page (`index.html`) that presents the first-draft plan for the first two terms (Sept 2026 – Feb 2027). It's meant to be shared publicly so leaders, parents, and students can look it over and talk about next steps. There's no build step and no dependencies — it's one HTML file.

**Live page:** https://evanlemmons.github.io/worship-music-school/

## What's on the page
- The vision and the three-part weekly meeting (discipleship → musicianship → playing together)
- The two-term arc and milestones (including a Fall Showcase)
- The full 22-week rollout schedule
- The discipleship / Bible-study arc and the musicianship topic arc
- A 45-song library with difficulty rated per instrument
- Planning Center setup, a promotion & communication kit, and logistics
- Open questions we're deciding together

## Editing
This `index.html` is generated — don't hand-edit it. The source lives at the repo root: landing-page copy (hero, section intros, cards, team, open questions) in `content/site-copy.md`, deep-content prose in `content/*.md`, tabular data in `data/*.csv`. Edit those, then run `python3 build/build_site.py` from the repo root to regenerate this file. See `CLAUDE.md` at the repo root for the full map.
