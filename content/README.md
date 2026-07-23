# Worship Music School — Repository Index

**North Metro Church · Kennesaw, GA · Launching Sun Sept 6, 2026**

This is the home base for everything about the group. Start with the Program Overview; the rest are the working pieces.

| Doc | What's in it |
| --- | --- |
| **00 — Program Overview & Plan** | The vision, the 3-part weekly model, the team, terms, milestones, rollout timeline, and the admin-facing plan. Start here. |
| **01 — Weekly Rhythm & Rollout Schedule** | The week-by-week Bible-study + musicianship map (Sep 2026–Feb 2027). Also delivered as a spreadsheet. Generated from `data/rollout_schedule.csv`. |
| **02 — Discipleship Track (Bible Studies)** | The worship-themed study arc: passages, big ideas, discussion questions, NIV. |
| **03 — Musicianship Track (Topics)** | The sequenced craft topics, each with a hands-on demo. |
| **04 — Song Library & Difficulty Guide** | **TBD** — songs picked once we see who shows up and can gauge skill levels. (An earlier ~45-song draft is in git history.) |
| **05 — Planning Center Setup** | How to wire Registrations, People, Groups, and Services for this group. |
| **06 — Promotion & Communication Kit** | Parent email, student invite, announcement script, slide copy, FAQ, weekly cadence. |
| **07 — Logistics, Safety & Open Questions** | Room/gear/budget, child safety, roles, contingencies, the "didn't-think-of-that" list, and open decisions. |

## Confirmed & working assumptions
**Confirmed:** name (Worship Music School, final) · meeting **Sunday evenings, ~60 min**, starting **Sep 6, 2026** · grade range **middle + high school (~12–18), all levels** · **free** to families. Still assumed: a **wide mix** of experience (hence per-instrument difficulty tiers); one band of ~5–12 (splits into two cleanly). None of these change the structure — only the specifics.

## Deliverables generated alongside this repository
- **Program Plan** (Word + PDF) — the polished, admin-facing version of doc 00.
- **Rollout Schedule** (Excel) — doc 01 as a sortable grid.

## The public site
Two pages are generated into `docs/`:
- **`index.html`** — the landing page for families and students (overview, the three-part night, terms, schedule, studies, musicianship, and a TBD song section).
- **`leader.html`** — a separate leader page (Planning Center setup, promotion, logistics, and the open decisions). Not linked from the landing nav; reach it directly at `…/leader.html`. It's a public URL — a static site can't password-protect it.

Songs are chosen week to week to fit who's in the room, so they aren't programmed into the schedule. When a fixed repertoire settles, per-song charts and reference tracks can come back (they live in git history from an earlier draft).
