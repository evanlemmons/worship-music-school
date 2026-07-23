# Site copy — the words on the public page

This file holds all the landing-page text for the public site (docs/index.html).
Edit the words here, then rebuild with `python3 build/build_site.py` and open
docs/index.html to preview. The page's structure — layout, colors, tables — lives
in build/build_site.py; this file is just copy.

How it's organized: each `## something` below is one slot on the page, and the
text under it is what shows there. Two kinds of slot:

- **Plain text** — just write the sentence. Markdown works: `**bold**`, `*italic*`.
- **Bulleted** (facts, the three cards, the "open questions" lists) — one item per
  `- ` line. When a line has parts separated by ` | `, keep the same number of
  parts (that's what lines the columns up), and don't type a `|` inside the words.

Everything above the first `## ` (this intro) is ignored by the build.

## meta_title
Worship Music School — North Metro Church

## meta_description
A weekly discipleship & development group for young musicians at North Metro Church: Bible study, real musician skills, and playing together as a band. First-terms plan, Sept 2026–Feb 2027.

## og_title
Worship Music School — North Metro Church

## og_description
Discipleship, musicianship, and playing together — a weekly group for young musicians. The first-terms plan, open for discussion.

## nav_brand
Worship Music School

## nav_links
- overview | Overview
- rhythm | The Night
- schedule | Schedule
- studies | Studies
- musicianship | Musicianship
- songs | Songs
- behind | Setup
- discuss | Discuss

## hero_eyebrow
North Metro Church · Kennesaw, GA

## hero_title
Worship Music School

## hero_subtitle
Discipleship & development for young musicians

## hero_vision
Forming young musicians into worshipers first and skilled, stage-ready band members second — growing them in Christ, in craft, and in the real-world skills of playing music together.

## hero_facts
- launch | Sun · Sep 6, 2026
- rhythm | Weekly · ~60 min
- a night | 3 sections
- first terms | 22 meetings · Sep–Feb
- draft v1 | for discussion

## overview_eyebrow
The idea

## overview_heading
Discipleship, taught through music

## overview_lede
Most churches can teach a teenager to play an instrument, and many can run a Bible study. Very few do both in the same room, on purpose, led by people who have done it professionally. This group closes that gap.

## overview_body
We want students to leave able to explain what worship really is and live like it, to understand the whole ecosystem of being a working musician — not just the notes, but the gear, the team, and the preparation — and to sit in with a band and confidently hold their part on a real stage. The heart of it is discipleship through music.

## rhythm_eyebrow
Every week, the same shape

## rhythm_heading
The three-part night

## rhythm_lede
Ground, sharpen, play — in that order, so that playing together is the celebration the rest of the night points toward.

## rhythm_cards
- 01 | Discipleship | ~15 minutes | A short, discussion-driven Bible study (NIV). The first term explores worship as a whole life, not just singing — and we get to know each other.
- 02 | Musicianship | ~20 minutes | The craft nobody teaches you: signal flow and gear, in-ears, playing to a click, charts, rehearsing, the music director, planning a set, and production.
- 03 | Playing together | ~25 minutes | We learn and work a song as a band and actually play it. Repertoire leans worship, with the occasional secular song for range and fun.

## rhythm_note
Timing assumes a ~60-minute meeting. If we stretch to 90 minutes, expand to roughly 25 / 30 / 35; for a full two hours, the extra time goes to hands-on gear and a longer band run-through.

## terms_eyebrow
The arc

## terms_heading
Two terms, one break at Christmas

## terms_list
- Fall | Sep 6 – Dec 13 | 14 weeks | “What Is Worship?” | Foundations. A biblical theology of worship-as-life; the ecosystem of playing (gear, signal flow, in-ears, click, charts, rehearsing); accessible worship songs that grow in difficulty.
- Winter | Jan 3 – Feb 21 | 8 weeks | “The Worshiping Life” | Deepening. The Psalms and the character of a worship leader; gear deep-dives, set planning, leading vs. playing, and self-review; the band works toward a full, connected set.

## terms_milestones
- Fall Showcase — Dec 13 · the term’s repertoire performed for families / a service
- A full connected set — Feb 21 · planned, flowing, with transitions; then plan spring

## team_eyebrow
Who leads

## team_members
- Lead | Evan Lemmons | Former touring & session musician — bass professionally, drums at an intermediate level, functional piano & guitar. Plays and leads at North Metro. Anchors the rhythm section and the “life of a working musician” teaching.
- Co-lead | Music educator | A full-time music teacher, strong on piano and guitar. Anchors instrument instruction and theory fundamentals.
- Vocals | Professional vocalist | A professional vocalist who leads on the North Metro team. Anchors vocal coaching, harmony, and leading a congregation.

## schedule_eyebrow
Week by week

## schedule_heading
The rollout schedule

## schedule_lede
All 22 meetings, with each week’s Bible study, musicianship topic, and song lined up together. Dates run Sunday evenings from Sep 6. Tap a week’s **Resources** for that song’s chart, chords, and reference track as they’re added.

## studies_eyebrow
Section 01 · the full arc

## studies_heading
Discipleship & Bible studies

## music_eyebrow
Section 02 · the full arc

## music_heading
Musicianship topics

## songs_eyebrow
Section 03 · the backlog

## songs_heading
Song library

## songs_lede
45 songs — mostly worship, a Christmas set for the Showcase, and secular change-ups for range. Difficulty is rated 1–5 *per instrument*, shown as input-level meters, so a beginner and an advanced player can take the same song and both be challenged.

## songs_legend_easier
easier

## songs_legend_harder
harder

## songs_legend_scale
**1** very easy · **3** intermediate · **5** a feature part

## songs_filters
- all | All
- worship | Worship
- christmas | Christmas
- secular | Secular

## behind_eyebrow
Making it run

## behind_heading
Setup, promotion & logistics

## behind_lede
The operational side — how we sign people up, spread the word, and cover the practical bases. Expand any section for the full detail.

## behind_cards
- 05-planning-center-setup.md | Planning Center setup — the full guide | Registrations is the front door, People is the roster, Groups is the week-to-week home base, and Services is both the teaching tool and the real thing we’re preparing them for.
- 06-promotion-communication.md | Promotion & communication kit — emails, scripts, FAQ | Ready-to-adapt templates: a parent email, a student invite, an on-stage announcement, promo slide copy, an FAQ, and the weekly-communication cadence that keeps a group alive.
- 07-logistics-safety.md | Logistics, safety & the didn’t-think-of-that list | Room and gear, a starter budget, child-safety essentials, leader roles, contingencies, and a running list of ideas worth deciding on early.

## discuss_eyebrow
Let’s decide together

## discuss_heading
Open questions & next steps

## discuss_lede
This is a first draft meant to start the conversation. A few things are confirmed, a few are still assumptions, and a few decisions are still genuinely open — that’s where your input comes in.

## discuss_col_confirmed
Confirmed

## discuss_confirmed
- Name | Worship Music School — final
- Meeting night & length | Sunday evenings, ~60 min, launching Sep 6, 2026
- Grade range | middle + high school (~12–18), all levels — no floor
- Cost | free to families

## discuss_col_assumptions
Assumptions to confirm

## discuss_assumptions
- Experience mix | assumed a wide range — hence tiered, per-instrument song parts
- Group size | designed for one band of ~5–12; splits cleanly into two

## discuss_col_open
Decisions still open

## discuss_open
- Whether we want a simple logo/brand
- Room on the church calendar for Sunday evenings
- The budget figure for gear/consumables
- Showcase format — standalone, or folded into a service
- Who owns Planning Center admin & parent communication
- What existing gear we can use so we only buy the gaps

## discuss_closing
Have a reaction, a name idea, or a student in mind? That’s exactly what this page is for — bring it to Evan and the team.

## footer_left
**Worship Music School** · North Metro Church, Kennesaw GA

## footer_right
Draft v1 · July 2026 · for discussion
