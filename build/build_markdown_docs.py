#!/usr/bin/env python3
"""Generate content/01-weekly-rhythm-schedule.md from data/rollout_schedule.csv.

The schedule CSV is the calendar: one row per Sunday, each marked meeting/off in
the Status column. Week numbers are computed here (meetings counted in order), so
turning a date on/off never requires renumbering anything by hand.
"""
import csv, os
_R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(_R, "data"); CONTENT = os.path.join(_R, "content")

def read(p):
    with open(p) as f:
        return list(csv.reader(f))

# ---------- 01 Weekly Rhythm & Schedule ----------
sched = read(os.path.join(DATA, "rollout_schedule.csv"))
header, rows = sched[0], sched[1:]
idx = {c: i for i, c in enumerate(header)}

intro = """# Weekly Rhythm & Rollout Schedule

**Launch:** Sun Sep 6, 2026 · **Meeting night:** Sunday evenings, ~60 min · **Terms:** Fall (Sep 6–Dec 13) + Winter (Jan 10–Feb 28)

## The weekly rhythm
Every meeting runs the same three sections, in order — ground, sharpen, play:

1. **Discipleship (~15 min)** — a short, discussion-driven Bible study (NIV).
2. **Musicianship (~20 min)** — the craft around the notes: gear, in-ears, click, charts, the band, the set.
3. **Playing together (~25 min)** — learn and work a song as a band (songs chosen to fit whoever is in the room).

*Timing flexes:* for a 90-min meeting expand to ~25/30/35; for 2 hours, spend the extra time on hands-on gear and a longer band run-through.

## Milestones
- **Week 14 (Dec 13)** — Fall Showcase (invite parents/church).
- **Week 22 (Feb 28)** — a full, connected set; plan the spring term.

## The map
The grid below is the Bible-study and musicianship arc, week by week. Off weeks (holidays/breaks) are marked. Songs are chosen each week to fit who's in attendance, so they aren't programmed here.

"""

def md_table(header, rows):
    out = ["| " + " | ".join(header) + " |",
           "| " + " | ".join("---" for _ in header) + " |"]
    for r in rows:
        out.append("| " + " | ".join(c if c else "" for c in r) + " |")
    return "\n".join(out)

disp_header = ["Week", "Date", "Discipleship (~15 min)", "Passage (NIV)", "Musicianship (~20 min)"]
disp_rows = []
wk = 0
for r in rows:
    is_meeting = r[idx["Status"]].strip().lower() == "meeting"
    if is_meeting:
        wk += 1
        disp_rows.append([str(wk), r[idx["Date"]], r[idx["Discipleship (~15 min)"]],
                          r[idx["Passage (NIV)"]], r[idx["Musicianship (~20 min)"]]])
    else:
        label = r[idx["Note"]] or "Break"
        disp_rows.append(["—", r[idx["Date"]], f"— {label} —", "", "— no meeting —"])

with open(os.path.join(CONTENT, "01-weekly-rhythm-schedule.md"), "w") as f:
    f.write(intro)
    f.write(md_table(disp_header, disp_rows))
    f.write("\n")

print("Wrote 01-weekly-rhythm-schedule.md")
