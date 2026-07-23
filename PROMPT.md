# Kickoff prompt

*Paste everything below as your first message in a new Claude Code session opened in this folder.*

---

I'm handing you an established project to own going forward. Everything you need is already in this folder (unzipped from a bundle).

**What this is:** **Worship Music School** — a weekly discipleship-and-development group for young musicians at North Metro Church (Kennesaw, GA). The format is a three-part weekly meeting: (1) Discipleship — a short NIV Bible study; (2) Musicianship — the real craft around playing (gear, in-ears, click, charts, rehearsing, the band, running a set, production); (3) Playing together — learning and playing songs as a band. Meetings are ~60 minutes, Sunday evenings, launching September 6, 2026. There's a detailed week-by-week plan for two terms (Fall + Winter, Sept 2026 – Feb 2027, 22 meetings) that ends in a Fall Showcase and a full-set milestone. Leaders: me (Evan — a former touring/session bassist, and I work at Planning Center), a music-teacher co-leader, and a professional vocalist.

**Do this first — get oriented before acting:**
1. Read `CLAUDE.md` — it's the project context, the repo layout, the build commands, and the conventions.
2. Read `content/README.md`, then skim `content/` and `data/`. That's the whole plan.
3. Run the build to confirm the toolchain works: `python3 build/build_site.py` should regenerate `docs/index.html`. Dependencies: `pip install markdown openpyxl` (and `npm i docx` if you regenerate the Word doc). Tell me if anything doesn't run.

**The golden rule:** `docs/index.html` and `content/01-*.md` and `content/04-*.md` are **generated**. Never hand-edit them — edit the source (`content/*.md` prose and `data/*.csv`), then rebuild. Full details are in `CLAUDE.md`.

**What I need from you, in order:**

1. **Publish the page publicly on GitHub Pages under my personal GitHub account.** Ask me for my GitHub username and the repo name I want. Then initialize git here, help me create the repo — use the `gh` CLI if I have it authenticated (`gh auth status`), otherwise give me exact click-by-click steps — push, enable Pages, and confirm the live URL. `docs/PUBLISH.md` has a manual walkthrough you can follow or improve.

2. **Set up a tight change → rebuild → publish workflow.** Whenever we change anything (a study, a song, the schedule, the design), you edit the source, rebuild `docs/index.html`, and push so the live page updates. Regenerate the files in `deliverables/` too when it's relevant.

3. **Help me resolve the open decisions.** They're listed in `content/07-logistics-safety.md` and in the page's "Open questions" section: the name/brand, meeting night, age range, free-vs-materials-fee & budget, showcase format, Planning Center ownership, and gear. Ask me about a few at a time; as we decide, update the content and rebuild.

4. **Grow the site into a per-week resource hub** — the "students can pull this week's songs" idea: per-song charts, chord sheets, and reference-track links, organized by week. Propose a simple structure and build it incrementally. The song library and schedule data are already structured to support this.

**Conventions to preserve:** NIV; non-denominational, Christ-centered; worship-leaning repertoire with occasional secular change-ups; discipleship-first tone. Visual brand: deep pine-teal `#123a40` + warm amber `#dc9a34`; fonts Fraunces (display), Figtree (body), IBM Plex Mono (labels/data); song difficulty shown as 1–5 per-instrument "input-level meters." The page must stay a single self-contained `index.html` that opens with no build step or server.

Start by getting oriented and running the build, then ask me for my GitHub username so we can get it live. If anything in the bundle looks broken or unclear, flag it before proceeding.
