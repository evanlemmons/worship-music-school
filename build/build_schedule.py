#!/usr/bin/env python3
"""Build the week-by-week rollout schedule CSV mapping all three tracks."""
import csv, os
DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
os.makedirs(DATA, exist_ok=True)

# (Week, Date, Term, Discipleship, Passage, Musicianship, Song Focus, Milestone/Notes)
rows = [
 ("1","Sun Sep 6","Fall","Kickoff: What is worship, really?","Romans 12:1–2","What a band actually is — roles & how a Sunday comes together","10,000 Reasons — introduce & jam","LAUNCH NIGHT. Names, instruments, expectations, fun."),
 ("2","Sun Sep 13","Fall","Worship in spirit and truth","John 4:1–26","How sound gets to the room (signal flow)","10,000 Reasons — learn & play",""),
 ("3","Sun Sep 20","Fall","Made to worship","Genesis 1:26–31; Psalm 8","Cables, connections & clean power","What A Beautiful Name — begin",""),
 ("4","Sun Sep 27","Fall","The heart behind the song","1 Samuel 16:1–13; Amos 5:21–24","In-ear monitors & stage sound","What A Beautiful Name — finish","MILESTONE: first song, start to finish."),
 ("5","Sun Oct 4","Fall","Why God is worth it (worth-ship)","Revelation 4–5","Tuning, tone & gain staging","This Is Amazing Grace — begin",""),
 ("6","Sun Oct 11","Fall","David: the wholehearted worshiper","2 Samuel 6:12–23","The click & the loop","This Is Amazing Grace — finish (to a click)",""),
 ("7","Sun Oct 18","Fall","Worship when you don't feel it","Psalm 42–43","Rehearsing at home","Build My Life — begin",""),
 ("8","Sun Oct 25","Fall","The Bible's own songbook","Psalm 100 (Psalms overview)","Charts & the Nashville number system","Build My Life — finish (from a chart)",""),
 ("9","Sun Nov 1","Fall","Worship costs something","2 Samuel 24:18–25; Mark 12:41–44","Rehearsing as a band","Stand By Me — secular change-up","Feel & pocket; the famous bass line."),
 ("10","Sun Nov 8","Fall","Servant, not star","Philippians 2:1–11; Colossians 3:23","The music director — cues & communication","Goodness of God — begin (6/8 feel)",""),
 ("11","Sun Nov 15","Fall","Gratitude","Psalm 103; 1 Thessalonians 5:16–18","Dynamics & arrangement","Goodness of God — finish",""),
 ("—","Sun Nov 22","Fall","— Thanksgiving break —","","— no meeting —","","Break — no meeting."),
 ("12","Sun Nov 29","Fall","The first Christmas songs","Luke 1:46–55 (Magnificat)","Planning a set & picking songs","Christmas set: Joy to the World + Silent Night — begin","Start Showcase prep."),
 ("13","Sun Dec 6","Fall","Point away from yourself","Colossians 1:15–20; John 3:30","The production world — sound, lights, lyrics, stage plot","Christmas set: add O Come All Ye Faithful; polish",""),
 ("14","Sun Dec 13","Fall","Showcase & testimony","Psalm 96:1–3","Soundcheck & line check","SHOWCASE — perform the Christmas set","MILESTONE: Fall Showcase. Invite parents/church."),
 ("—","Sun Dec 20","—","— Christmas break —","","— no meeting —","","Break — no meeting."),
 ("—","Sun Dec 27","—","— Christmas break —","","— no meeting —","","Break — no meeting."),
 ("15","Sun Jan 3","Winter","Reset: the worshiping life","Colossians 3:1–17","Gear deep-dive I — strings & keys, pedals","Living Hope — begin","New term. Set individual goals."),
 ("16","Sun Jan 10","Winter","The full range of worship","Psalm 13; Psalm 150","Gear deep-dive II — drums & vocals","Living Hope — finish",""),
 ("17","Sun Jan 17","Winter","Young and setting the example","1 Timothy 4:12","Communication & tools (Planning Center)","Graves Into Gardens — begin",""),
 ("18","Sun Jan 24","Winter","One body, many parts","1 Corinthians 12:12–27","Being a bandmate — rhythm-section lock","Isn't She Lovely — secular groove","Rhythm section feature."),
 ("19","Sun Jan 31","Winter","Chasing God's presence","Exodus 33:12–23; Psalm 84","Leading vs. playing","King of Kings — begin (a student leads)",""),
 ("20","Sun Feb 7","Winter","Use what you've been given","Matthew 25:14–30; 1 Peter 4:10–11","Building & running a full set","Assemble a full Winter set (3–4 songs)",""),
 ("21","Sun Feb 14","Winter","Worship as witness","Psalm 40:1–3; Matthew 5:14–16","Record it & review it","Run & record the full set; polish",""),
 ("22","Sun Feb 21","Winter","The one thing","Psalm 27:4","Put it together & what's next","Full-set 'final' + next-step conversations","MILESTONE: full connected set. Plan spring term."),
]

cols = ["Week","Date","Term","Discipleship (~15 min)","Passage (NIV)","Musicianship (~20 min)","Playing Together (~25 min)","Milestones / Notes"]
with open(os.path.join(DATA, "rollout_schedule.csv"),"w",newline="") as f:
    w = csv.writer(f)
    w.writerow(cols)
    w.writerows(rows)
meetings = sum(1 for r in rows if r[0] != "—")
print(f"Wrote {len(rows)} rows ({meetings} meetings, {len(rows)-meetings} break weeks) to rollout_schedule.csv")
