#!/usr/bin/env python3
import csv, os
_R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(_R, "data"); CONTENT = os.path.join(_R, "content")

def read(p):
    with open(p) as f:
        return list(csv.reader(f))

# ---------- 01 Weekly Rhythm & Schedule ----------
sched = read(os.path.join(DATA, "rollout_schedule.csv"))
header, rows = sched[0], sched[1:]
intro = """# Weekly Rhythm & Rollout Schedule

**Launch:** Sun Sep 6, 2026 · **Meeting night:** Sunday evenings, ~60 min · **Terms:** Fall (Sep 6–Dec 13) + Winter (Jan 3–Feb 21)

## The weekly rhythm
Every meeting runs the same three sections, in order — ground, sharpen, play:

1. **Discipleship (~15 min)** — a short, discussion-driven Bible study (NIV).
2. **Musicianship (~20 min)** — the craft around the notes: gear, in-ears, click, charts, the band, the set.
3. **Playing together (~25 min)** — learn and work that week's song as a band.

*Timing flexes:* for a 90-min meeting expand to ~25/30/35; for 2 hours, spend the extra time on hands-on gear and a longer band run-through. Newer musicians take two weeks per song ("begin" then "finish"); advanced players push ahead.

## Milestones
- **Week 4** — first song, start to finish.
- **Week 14 (Dec 13)** — Fall Showcase (invite parents/church).
- **Week 22 (Feb 21)** — a full, connected set; plan the spring term.

## The map
The grid below cross-references all three tracks each week. Full study notes are in the Discipleship doc; full topic detail in the Musicianship doc; song details and difficulty in the Song Library.

"""
def md_table(header, rows):
    out = ["| " + " | ".join(header) + " |",
           "| " + " | ".join("---" for _ in header) + " |"]
    for r in rows:
        out.append("| " + " | ".join(c if c else "" for c in r) + " |")
    return "\n".join(out)

display_cols = [c for c in header if c != "Song Title"]
di_idx = [header.index(c) for c in display_cols]
display_rows = [[r[i] for i in di_idx] for r in rows]

with open(os.path.join(CONTENT, "01-weekly-rhythm-schedule.md"),"w") as f:
    f.write(intro)
    f.write(md_table(display_cols, display_rows))
    f.write("\n")

# ---------- 04 Song Library ----------
lib = read(os.path.join(DATA, "song_library.csv"))
lh, lrows = lib[0], lib[1:]
# columns index
idx = {c:i for i,c in enumerate(lh)}
intro2 = """# Song Library & Difficulty Guide

A working backlog of songs to draw from — mostly worship, a Christmas set for the Showcase, and secular change-ups for range and fun. It's built to grow: add rows as you find songs that work.

## How to read the difficulty ratings
Each song is rated **1–5 per instrument** (Drums, Bass, Guitar, Keys, Vocals), plus an **Overall**:

- **1** = very easy — a true beginner can play it this week.
- **2** = easy — a few weeks of experience.
- **3** = intermediate — comfortable player; some real parts.
- **4** = advanced — confident player; arrangement/feel demands.
- **5** = hard — a feature part; for your strongest player.

The point of per-instrument ratings is **mixed-level bands**: a song can be a 2 on bass and a 4 on vocals, so you can hand a beginner bassist and an advanced vocalist the *same song* and both are challenged appropriately. Match each seat to the player.

## How to use it
- **Pick by the weakest-needed seat.** For a newer band, choose songs where the parts you need are low numbers; simplify the rest.
- **"Begin/finish" pacing.** Newer musicians get two weeks per song; strong players learn it in one and help teach.
- **Keys shown are band-friendly starting keys** — transpose to fit your vocalist (that's the Week 8 number-system lesson in action).
- **Lean worship, season with variety.** Roughly one secular change-up every several weeks keeps it fresh without losing the mission.
- **This is the "download" list.** `Chart URL`, `Chord Chart URL`, and `Reference Track URL` are columns in `data/song_library.csv` — fill them in and rebuild, and they show up as links on the public site's Song Library and week-by-week Schedule (also worth mirroring into the Groups Resources tab).

"""
show_cols = ["Title","Artist","Key","BPM","Feel","Drums","Bass","Guitar","Keys","Vocals","Overall","Best For","Teaching Focus"]
sc_idx = [idx[c] for c in show_cols]
def section(title, type_name):
    sub = [r for r in lrows if r[idx["Type"]]==type_name]
    hdr = show_cols
    rows2 = [[r[i] for i in sc_idx] for r in sub]
    return f"## {title} ({len(sub)})\n\n" + md_table(hdr, rows2) + "\n\n"

with open(os.path.join(CONTENT, "04-song-library.md"),"w") as f:
    f.write(intro2)
    f.write(section("Worship songs","Worship"))
    f.write(section("Christmas set (for the Showcase)","Christmas"))
    f.write(section("Secular change-ups","Secular"))
    f.write("*Full column set (including Notes) is in the Song Library spreadsheet, which you can sort and filter.*\n")

print("Wrote 01-weekly-rhythm-schedule.md and 04-song-library.md")
