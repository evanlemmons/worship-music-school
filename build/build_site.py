#!/usr/bin/env python3
"""Build a single self-contained index.html for public sharing (GitHub Pages ready)."""
import csv, html, markdown

import os
_R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(_R, "content"); DATA = os.path.join(_R, "data"); SITE = os.path.join(_R, "docs")
os.makedirs(SITE, exist_ok=True)
def read_csv(p):
    with open(p) as f: return list(csv.reader(f))
def md2html(text):
    return markdown.markdown(text, extensions=['extra','sane_lists'])
def strip_h1(t):
    return "\n".join(l for l in t.split("\n") if not l.startswith("# "))

# ---------- term-split collapsibles ----------
def term_details(path, open_first=True):
    text = open(os.path.join(CONTENT, path)).read()
    parts = text.split("\n## ")
    intro = strip_h1(parts[0]).strip()
    out = [f'<div class="prose lead">{md2html(intro)}</div>']
    for i, p in enumerate(parts[1:]):
        nl = p.index("\n"); title = p[:nl].strip(); body = p[nl+1:]
        op = " open" if (open_first and i == 0) else ""
        out.append(f'<details class="wk"{op}><summary>{html.escape(title)}</summary>'
                   f'<div class="prose">{md2html(body)}</div></details>')
    return "\n".join(out)

def full_details(path, summary, teaser):
    text = strip_h1(open(os.path.join(CONTENT, path)).read()).strip()
    return (f'<p class="teaser">{teaser}</p>'
            f'<details class="deep"><summary>{html.escape(summary)}</summary>'
            f'<div class="prose">{md2html(text)}</div></details>')

# ---------- schedule ----------
def meter(label, val):
    val = int(val)
    segs = "".join(
        f'<i class="s s{k}{" on" if k <= val else ""}"></i>' for k in range(1, 6))
    return (f'<span class="meter" role="img" aria-label="{label} difficulty {val} of 5" '
            f'title="{label}: {val}/5">{segs}</span>')

def schedule_html():
    rows = read_csv(os.path.join(DATA, "rollout_schedule.csv"))[1:]
    trs = []
    for r in rows:
        wk, date, term, disc, pas, mus, song, notes = r
        is_break = wk == "—"
        cls = "brk" if is_break else term.lower()
        mile = any(k in notes for k in ("MILESTONE", "SHOWCASE", "LAUNCH"))
        notes_html = html.escape(notes)
        if mile:
            notes_html = f'<span class="mile">{notes_html}</span>'
        trs.append(
            f'<tr class="{cls}">'
            f'<td class="col-week mono">{html.escape(wk)}</td>'
            f'<td class="col-date">{html.escape(date)}</td>'
            f'<td class="col-term"><span class="tg tg-{cls}">{html.escape(term)}</span></td>'
            f'<td class="col-disc">{html.escape(disc)}</td>'
            f'<td class="col-pass mono2">{html.escape(pas)}</td>'
            f'<td class="col-mus">{html.escape(mus)}</td>'
            f'<td class="col-song">{html.escape(song)}</td>'
            f'<td class="col-notes">{notes_html}</td></tr>')
    return "\n".join(trs)

# ---------- songs ----------
def songs_html():
    data = read_csv(os.path.join(DATA, "song_library.csv"))
    head = data[0]; idx = {c: i for i, c in enumerate(head)}
    rows = []
    for r in data[1:]:
        t = r[idx["Type"]].lower()
        rows.append(
            f'<tr data-type="{t}">'
            f'<td class="song"><div class="t">{html.escape(r[idx["Title"]])}</div>'
            f'<div class="a">{html.escape(r[idx["Artist"]])}</div>'
            f'<div class="tf">{html.escape(r[idx["Teaching Focus"]])}</div></td>'
            f'<td><span class="chip c-{t}">{html.escape(r[idx["Type"]])}</span>'
            f'<div class="bf">{html.escape(r[idx["Best For"]])}</div></td>'
            f'<td class="mono ctr">{html.escape(r[idx["Key"]])}</td>'
            f'<td class="mono ctr">{html.escape(r[idx["BPM"]])}</td>'
            f'<td class="ctr">{meter("Drums", r[idx["Drums"]])}</td>'
            f'<td class="ctr">{meter("Bass", r[idx["Bass"]])}</td>'
            f'<td class="ctr">{meter("Guitar", r[idx["Guitar"]])}</td>'
            f'<td class="ctr">{meter("Keys", r[idx["Keys"]])}</td>'
            f'<td class="ctr">{meter("Vocals", r[idx["Vocals"]])}</td>'
            f'<td class="ctr">{meter("Overall", r[idx["Overall"]])}</td></tr>')
    return "\n".join(rows)

CSS = r"""
:root{
  --pine-900:#0d262b; --pine-800:#123a40; --pine-700:#1a4b51; --pine-600:#256169;
  --pine-300:#8fb6b4; --paper:#fbf8f2; --paper-2:#f2ede2; --card:#ffffff;
  --ink:#182a2c; --ink-soft:#4d5f60; --line:#e3dccd; --amber:#dc9a34; --amber-2:#c8842a;
  --amber-soft:#f6e6c3; --good:#4fa07c; --mid:#dc9a34; --hot:#cd6446; --faint:#d9dad0;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);
  font-family:"Figtree",system-ui,-apple-system,sans-serif;font-size:17px;line-height:1.65;
  -webkit-font-smoothing:antialiased;overflow-x:hidden}
h1,h2,h3,h4{font-family:"Fraunces",Georgia,serif;font-weight:600;line-height:1.12;
  letter-spacing:-.01em;color:var(--pine-800)}
a{color:var(--pine-700)}
.eyebrow{font-family:"IBM Plex Mono",monospace;font-size:.72rem;letter-spacing:.22em;
  text-transform:uppercase;color:var(--amber-2);font-weight:500;margin:0 0 .6rem}
.mono{font-family:"IBM Plex Mono",monospace}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px}
section{padding:78px 0;border-top:1px solid var(--line)}
section > .wrap > h2{font-size:2.05rem;margin:.1rem 0 1.1rem}
.lede{font-size:1.18rem;color:var(--ink-soft);max-width:60ch}

/* NAV */
nav{position:sticky;top:0;z-index:50;background:rgba(251,248,242,.86);
  backdrop-filter:blur(9px);border-bottom:1px solid var(--line)}
nav .wrap{display:flex;align-items:center;gap:6px;height:60px;overflow-x:auto;scrollbar-width:none}
nav .wrap::-webkit-scrollbar{display:none}
nav .brand{font-family:"Fraunces",serif;font-weight:600;color:var(--pine-800);
  font-size:1.05rem;margin-right:auto;white-space:nowrap;display:flex;align-items:center;gap:.5rem}
nav .brand .dot{color:var(--amber-2)}
nav a.lnk{font-size:.86rem;color:var(--ink-soft);text-decoration:none;padding:.4rem .7rem;
  border-radius:8px;white-space:nowrap;font-weight:500}
nav a.lnk:hover{background:var(--paper-2);color:var(--pine-800)}

/* HERO */
.hero{position:relative;background:radial-gradient(120% 120% at 78% -10%,#1c565c 0%,var(--pine-800) 42%,var(--pine-900) 100%);
  color:#eaf3f0;border-top:none;overflow:hidden;padding:96px 0 84px}
.hero .glow{position:absolute;inset:0;background:radial-gradient(46% 40% at 80% 8%,rgba(220,154,52,.34),transparent 60%);
  pointer-events:none}
.hero .wrap{position:relative;z-index:2}
.hero .eyebrow{color:var(--amber);opacity:.95}
.hero h1{color:#fff;font-size:clamp(2.7rem,7vw,5rem);font-weight:700;margin:.2rem 0 .5rem;letter-spacing:-.02em}
.hero h1 .sub{display:block;font-size:clamp(1.05rem,2.2vw,1.5rem);font-weight:400;font-style:italic;
  color:var(--amber-soft);margin-top:.5rem;letter-spacing:0}
.hero p.vision{font-size:1.24rem;max-width:56ch;color:#d8e7e3;margin:1.1rem 0 1.7rem}
.facts{display:flex;flex-wrap:wrap;gap:14px 30px;font-family:"IBM Plex Mono",monospace;
  font-size:.82rem;letter-spacing:.03em;color:#bcd6d0;border-top:1px solid rgba(255,255,255,.14);padding-top:20px;max-width:760px}
.facts b{color:#fff;font-weight:600}
.facts .k{color:var(--amber)}
/* equalizer signature */
.eq{position:absolute;right:0;bottom:0;left:0;height:120px;display:flex;align-items:flex-end;
  gap:5px;padding:0 6px;opacity:.5;z-index:1;pointer-events:none;mask-image:linear-gradient(90deg,transparent,#000 22%,#000 78%,transparent)}
.eq-bar{flex:1;min-width:3px;background:linear-gradient(180deg,var(--amber),#2a6a70);border-radius:3px 3px 0 0;
  height:16%;animation:eq 1.7s ease-in-out infinite alternate}
@keyframes eq{to{height:92%}}

/* CARDS: three-part night */
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:8px}
.part{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:24px;position:relative;overflow:hidden}
.part .bar{position:absolute;top:0;left:0;right:0;height:5px}
.part.p1 .bar{background:var(--pine-600)} .part.p2 .bar{background:var(--amber)} .part.p3 .bar{background:var(--hot)}
.part .num{font-family:"IBM Plex Mono",monospace;font-size:.78rem;color:var(--ink-soft);letter-spacing:.1em}
.part h3{font-size:1.28rem;margin:.5rem 0 .1rem}
.part .time{font-family:"IBM Plex Mono",monospace;font-size:.82rem;color:var(--amber-2);margin-bottom:.6rem}
.part p{margin:0;color:var(--ink-soft);font-size:.98rem}
.note{margin-top:20px;font-size:.92rem;color:var(--ink-soft);font-style:italic}

/* TERMS timeline */
.time-rail{display:grid;grid-template-columns:1fr;gap:14px;margin-top:10px}
.trm{display:grid;grid-template-columns:150px 1fr;gap:20px;background:var(--card);border:1px solid var(--line);
  border-radius:14px;padding:20px 22px}
.trm .when{font-family:"IBM Plex Mono",monospace;font-size:.82rem;color:var(--pine-700);font-weight:500}
.trm .when .big{display:block;font-family:"Fraunces",serif;font-size:1.35rem;color:var(--pine-800);margin-bottom:.2rem;font-weight:600}
.trm h3{margin:.1rem 0 .3rem;font-size:1.2rem}
.trm p{margin:0;color:var(--ink-soft);font-size:.97rem}
.milestone{display:flex;align-items:center;gap:10px;padding:12px 18px;background:linear-gradient(90deg,var(--amber-soft),transparent);
  border-left:3px solid var(--amber);border-radius:8px;margin:6px 0;font-weight:500;color:var(--pine-800)}
.milestone .star{color:var(--amber-2)}

/* team */
.team{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:8px}
.mem{background:var(--paper-2);border-radius:14px;padding:20px}
.mem h4{margin:0 0 .3rem;font-size:1.08rem}
.mem .role{font-family:"IBM Plex Mono",monospace;font-size:.72rem;text-transform:uppercase;letter-spacing:.12em;color:var(--amber-2)}
.mem p{margin:.4rem 0 0;font-size:.92rem;color:var(--ink-soft)}

/* TABLES */
.tablewrap{overflow-x:auto;border:1px solid var(--line);border-radius:14px;background:var(--card);margin-top:18px}
table{border-collapse:collapse;width:100%;min-width:760px;font-size:.9rem}
thead th{background:var(--pine-800);color:#eaf3f0;font-family:"Figtree",sans-serif;font-weight:600;
  text-align:left;padding:12px 12px;font-size:.8rem;letter-spacing:.02em;position:sticky;top:0}
tbody td{padding:11px 12px;border-top:1px solid var(--line);vertical-align:top}
tbody tr.fall td{background:#fdfaf4} tbody tr.winter td{background:#f4f8fa}
tbody tr.brk td{background:#f0efe9;color:#9a9a90;font-style:italic}
.mono2{font-family:"IBM Plex Mono",monospace;font-size:.8rem;color:var(--ink-soft)}
.tg{font-family:"IBM Plex Mono",monospace;font-size:.66rem;text-transform:uppercase;letter-spacing:.08em;
  padding:2px 8px;border-radius:20px;white-space:nowrap}
.tg-fall{background:var(--amber-soft);color:#8a5a12} .tg-winter{background:#dcebf0;color:#1c5763} .tg-brk{background:#e4e3db;color:#8a8a80}
.mile{background:var(--amber-soft);padding:2px 6px;border-radius:6px;font-weight:600;color:#8a5a12}
.col-week{text-align:center;font-weight:600;color:var(--pine-700)}

/* meters */
.meter{display:inline-flex;gap:2px;align-items:flex-end;height:16px}
.meter .s{width:5px;height:7px;background:var(--faint);border-radius:1px}
.meter .s.s2{height:9px}.meter .s.s3{height:11px}.meter .s.s4{height:13px}.meter .s.s5{height:15px}
.meter .s1.on,.meter .s2.on{background:var(--good)}
.meter .s3.on,.meter .s4.on{background:var(--mid)}
.meter .s5.on{background:var(--hot)}
.legend{display:flex;flex-wrap:wrap;gap:16px;align-items:center;margin:6px 0 2px;font-size:.86rem;color:var(--ink-soft)}
.legend .lg{display:inline-flex;align-items:center;gap:7px}
.song .t{font-weight:600;color:var(--pine-800)} .song .a{font-size:.8rem;color:var(--ink-soft)}
.song .tf{font-size:.76rem;color:#8a7f6a;margin-top:2px;font-style:italic}
.ctr{text-align:center}
.chip{font-family:"IBM Plex Mono",monospace;font-size:.66rem;text-transform:uppercase;letter-spacing:.06em;
  padding:2px 8px;border-radius:20px;white-space:nowrap}
.c-worship{background:#e2efe8;color:#26674c} .c-christmas{background:#f4e6ee;color:#8a3765} .c-secular{background:#e8ecf4;color:#3a4d7a}
.bf{font-size:.72rem;color:var(--ink-soft);margin-top:4px}
.filters{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 2px}
.filters button{font-family:"IBM Plex Mono",monospace;font-size:.76rem;letter-spacing:.04em;border:1px solid var(--line);
  background:var(--card);color:var(--ink-soft);padding:6px 13px;border-radius:20px;cursor:pointer;transition:.15s}
.filters button:hover{border-color:var(--pine-300)}
.filters button.act{background:var(--pine-800);color:#fff;border-color:var(--pine-800)}

/* collapsibles / prose */
details.wk,details.deep{background:var(--card);border:1px solid var(--line);border-radius:12px;margin:12px 0;overflow:hidden}
details.wk summary,details.deep summary{cursor:pointer;padding:16px 20px;font-family:"Fraunces",serif;
  font-weight:600;color:var(--pine-800);font-size:1.1rem;list-style:none;display:flex;align-items:center;gap:10px}
details summary::-webkit-details-marker{display:none}
details summary::before{content:"+";font-family:"IBM Plex Mono",monospace;color:var(--amber-2);font-size:1.2rem;
  width:18px;display:inline-block;transition:.2s}
details[open] summary::before{content:"–"}
details summary:hover{background:var(--paper-2)}
.prose{padding:2px 22px 20px}
.prose.lead{padding:0 2px 6px}
.prose h3{font-size:1.12rem;color:var(--pine-700);margin:1.2rem 0 .3rem}
.prose h2{font-size:1.3rem;margin:1.3rem 0 .4rem}
.prose p{margin:.5rem 0;color:#2c3d3e}
.prose strong{color:var(--pine-800)}
.prose ul{margin:.4rem 0 .8rem;padding-left:1.2rem} .prose li{margin:.25rem 0}
.prose blockquote{margin:.7rem 0;padding:12px 18px;background:var(--paper-2);border-left:3px solid var(--pine-300);
  border-radius:0 8px 8px 0;color:#33474a;font-size:.95rem}
.prose hr{border:none;border-top:1px solid var(--line);margin:1.3rem 0}
.prose code{font-family:"IBM Plex Mono",monospace;font-size:.85em;background:var(--paper-2);padding:1px 5px;border-radius:5px}
.teaser{color:var(--ink-soft);max-width:64ch}

/* discuss */
.discuss{background:linear-gradient(135deg,var(--pine-800),var(--pine-900));color:#eaf3f0}
.discuss h2{color:#fff} .discuss .eyebrow{color:var(--amber)}
.discuss .lede{color:#cfe0dc}
.qcols{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:22px;margin-top:22px}
.qbox{background:rgba(255,255,255,.055);border:1px solid rgba(255,255,255,.13);border-radius:14px;padding:22px}
.qbox h3{color:#fff;font-size:1.12rem;margin:0 0 .7rem}
.qbox ol,.qbox ul{margin:0;padding-left:1.2rem;color:#d3e2de} .qbox li{margin:.4rem 0;font-size:.95rem}
.qbox .as{font-family:"IBM Plex Mono",monospace;font-size:.8rem;color:var(--amber);display:block;margin-top:.1rem}

/* footer */
footer{background:var(--pine-900);color:#a9c4bf;padding:44px 0;border-top:none;font-size:.9rem}
footer .wrap{display:flex;flex-wrap:wrap;gap:14px;justify-content:space-between;align-items:center}
footer b{color:#eaf3f0}

.reveal{opacity:0;transform:translateY(14px);transition:opacity .6s ease,transform .6s ease}
.reveal.in{opacity:1;transform:none}

@media(max-width:820px){
  .grid3,.team{grid-template-columns:1fr} .qcols{grid-template-columns:1fr}
  .trm{grid-template-columns:1fr;gap:8px} section{padding:56px 0}
  .col-term,.col-pass{display:none}
}
@media(prefers-reduced-motion:reduce){
  .eq-bar{animation:none;height:40%} .reveal{transition:none;opacity:1;transform:none} html{scroll-behavior:auto}
}
"""

# ---- equalizer bars ----
import math
eq_bars = ""
for i in range(30):
    dur = 1.1 + (i % 5) * 0.28
    delay = (i * 0.11) % 1.6
    h = 12 + (i * 7) % 40
    eq_bars += f'<span class="eq-bar" style="animation-duration:{dur:.2f}s;animation-delay:{delay:.2f}s;height:{h}%"></span>'

NAV = """
<nav><div class="wrap">
<span class="brand">Worship Music School <span class="dot">●</span></span>
<a class="lnk" href="#overview">Overview</a>
<a class="lnk" href="#rhythm">The Night</a>
<a class="lnk" href="#schedule">Schedule</a>
<a class="lnk" href="#studies">Studies</a>
<a class="lnk" href="#musicianship">Musicianship</a>
<a class="lnk" href="#songs">Songs</a>
<a class="lnk" href="#behind">Setup</a>
<a class="lnk" href="#discuss">Discuss</a>
</div></nav>
"""

HERO = f"""
<header class="hero">
  <div class="eq">{eq_bars}</div>
  <div class="glow"></div>
  <div class="wrap">
    <p class="eyebrow">North Metro Church · Kennesaw, GA</p>
    <h1>Worship Music School<span class="sub">Discipleship &amp; development for young musicians</span></h1>
    <p class="vision">Forming young musicians into worshipers first and skilled, stage-ready band members second — growing them in Christ, in craft, and in the real-world skills of playing music together.</p>
    <div class="facts">
      <span><span class="k">launch</span> &nbsp;<b>Sun · Sep 6, 2026</b></span>
      <span><span class="k">rhythm</span> &nbsp;<b>Weekly · ~60 min</b></span>
      <span><span class="k">a night</span> &nbsp;<b>3 sections</b></span>
      <span><span class="k">first terms</span> &nbsp;<b>22 meetings · Sep–Feb</b></span>
      <span><span class="k">draft v1</span> &nbsp;<b>for discussion</b></span>
    </div>
  </div>
</header>
"""

OVERVIEW = """
<section id="overview"><div class="wrap reveal">
  <p class="eyebrow">The idea</p>
  <h2>Discipleship, taught through music</h2>
  <p class="lede">Most churches can teach a teenager to play an instrument, and many can run a Bible study. Very few do both in the same room, on purpose, led by people who have done it professionally. This group closes that gap.</p>
  <p style="max-width:64ch;color:var(--ink-soft);margin-top:1rem">We want students to leave able to explain what worship really is and live like it, to understand the whole ecosystem of being a working musician — not just the notes, but the gear, the team, and the preparation — and to sit in with a band and confidently hold their part on a real stage. The name is a working title; the heart of it is discipleship through music.</p>
</div></section>
"""

RHYTHM = """
<section id="rhythm"><div class="wrap reveal">
  <p class="eyebrow">Every week, the same shape</p>
  <h2>The three-part night</h2>
  <p class="lede">Ground, sharpen, play — in that order, so that playing together is the celebration the rest of the night points toward.</p>
  <div class="grid3">
    <div class="part p1"><div class="bar"></div><div class="num">01</div><h3>Discipleship</h3><div class="time">~15 minutes</div><p>A short, discussion-driven Bible study (NIV). The first term explores worship as a whole life, not just singing — and we get to know each other.</p></div>
    <div class="part p2"><div class="bar"></div><div class="num">02</div><h3>Musicianship</h3><div class="time">~20 minutes</div><p>The craft nobody teaches you: signal flow and gear, in-ears, playing to a click, charts, rehearsing, the music director, planning a set, and production.</p></div>
    <div class="part p3"><div class="bar"></div><div class="num">03</div><h3>Playing together</h3><div class="time">~25 minutes</div><p>We learn and work a song as a band and actually play it. Repertoire leans worship, with the occasional secular song for range and fun.</p></div>
  </div>
  <p class="note">Timing assumes a ~60-minute meeting. If we stretch to 90 minutes, expand to roughly 25 / 30 / 35; for a full two hours, the extra time goes to hands-on gear and a longer band run-through.</p>
</div></section>
"""

TERMS = """
<section id="terms"><div class="wrap reveal">
  <p class="eyebrow">The arc</p>
  <h2>Two terms, one break at Christmas</h2>
  <div class="time-rail">
    <div class="trm"><div class="when"><span class="big">Fall</span>Sep 6 – Dec 13<br>14 weeks</div>
      <div><h3>&ldquo;What Is Worship?&rdquo;</h3><p>Foundations. A biblical theology of worship-as-life; the ecosystem of playing (gear, signal flow, in-ears, click, charts, rehearsing); accessible worship songs that grow in difficulty.</p></div></div>
    <div class="milestone"><span class="star">★</span> Fall Showcase — Dec 13 · the term&rsquo;s repertoire performed for families / a service</div>
    <div class="trm"><div class="when"><span class="big">Winter</span>Jan 3 – Feb 21<br>8 weeks</div>
      <div><h3>&ldquo;The Worshiping Life&rdquo;</h3><p>Deepening. The Psalms and the character of a worship leader; gear deep-dives, set planning, leading vs. playing, and self-review; the band works toward a full, connected set.</p></div></div>
    <div class="milestone"><span class="star">★</span> A full connected set — Feb 21 · planned, flowing, with transitions; then plan spring</div>
  </div>
  <div style="margin-top:34px">
    <p class="eyebrow">Who leads</p>
    <div class="team">
      <div class="mem"><div class="role">Lead</div><h4>Evan Lemmons</h4><p>Former touring &amp; session musician — bass professionally, drums at an intermediate level, functional piano &amp; guitar. Plays and leads at North Metro. Anchors the rhythm section and the &ldquo;life of a working musician&rdquo; teaching.</p></div>
      <div class="mem"><div class="role">Co-lead</div><h4>Music educator</h4><p>A full-time music teacher, strong on piano and guitar. Anchors instrument instruction and theory fundamentals.</p></div>
      <div class="mem"><div class="role">Vocals</div><h4>Professional vocalist</h4><p>A professional vocalist who leads on the North Metro team. Anchors vocal coaching, harmony, and leading a congregation.</p></div>
    </div>
  </div>
</div></section>
"""

SCHEDULE = f"""
<section id="schedule"><div class="wrap reveal">
  <p class="eyebrow">Week by week</p>
  <h2>The rollout schedule</h2>
  <p class="lede">All 22 meetings, with each week&rsquo;s Bible study, musicianship topic, and song lined up together. Dates run Sunday evenings from Sep 6.</p>
  <div class="tablewrap"><table>
    <thead><tr>
      <th class="col-week">Wk</th><th class="col-date">Date</th><th class="col-term">Term</th>
      <th class="col-disc">Discipleship</th><th class="col-pass">Passage (NIV)</th>
      <th class="col-mus">Musicianship</th><th class="col-song">Playing together</th><th class="col-notes">Milestones</th>
    </tr></thead>
    <tbody>{schedule_html()}</tbody>
  </table></div>
</div></section>
"""

STUDIES = f"""
<section id="studies"><div class="wrap reveal">
  <p class="eyebrow">Section 01 · the full arc</p>
  <h2>Discipleship &amp; Bible studies</h2>
  {term_details("02-discipleship-track.md")}
</div></section>
"""

MUSIC = f"""
<section id="musicianship"><div class="wrap reveal">
  <p class="eyebrow">Section 02 · the full arc</p>
  <h2>Musicianship topics</h2>
  {term_details("03-musicianship-track.md")}
</div></section>
"""

SONGS = f"""
<section id="songs"><div class="wrap reveal">
  <p class="eyebrow">Section 03 · the backlog</p>
  <h2>Song library</h2>
  <p class="lede">45 songs — mostly worship, a Christmas set for the Showcase, and secular change-ups for range. Difficulty is rated 1–5 <em>per instrument</em>, shown as input-level meters, so a beginner and an advanced player can take the same song and both be challenged.</p>
  <div class="legend">
    <span class="lg"><span class="meter"><i class="s s1 on"></i><i class="s s2 on"></i><i class="s s3"></i><i class="s s4"></i><i class="s s5"></i></span> easier</span>
    <span class="lg"><span class="meter"><i class="s s1 on"></i><i class="s s2 on"></i><i class="s s3 on"></i><i class="s s4 on"></i><i class="s s5"></i></span> harder</span>
    <span class="lg"><b>1</b> very easy · <b>3</b> intermediate · <b>5</b> a feature part</span>
  </div>
  <div class="filters">
    <button class="act" data-f="all">All 45</button>
    <button data-f="worship">Worship 29</button>
    <button data-f="christmas">Christmas 6</button>
    <button data-f="secular">Secular 10</button>
  </div>
  <div class="tablewrap"><table id="songtable">
    <thead><tr>
      <th>Song</th><th>Type</th><th class="ctr">Key</th><th class="ctr">BPM</th>
      <th class="ctr" title="Drums">Dr</th><th class="ctr" title="Bass">Ba</th><th class="ctr" title="Guitar">Gt</th>
      <th class="ctr" title="Keys">Ky</th><th class="ctr" title="Vocals">Vo</th><th class="ctr" title="Overall">All</th>
    </tr></thead>
    <tbody>{songs_html()}</tbody>
  </table></div>
</div></section>
"""

BEHIND = f"""
<section id="behind"><div class="wrap reveal">
  <p class="eyebrow">Making it run</p>
  <h2>Setup, promotion &amp; logistics</h2>
  <p class="lede">The operational side — how we sign people up, spread the word, and cover the practical bases. Expand any section for the full detail.</p>
  {full_details("05-planning-center-setup.md","Planning Center setup — the full guide","Registrations is the front door, People is the roster, Groups is the week-to-week home base, and Services is both the teaching tool and the real thing we&rsquo;re preparing them for.")}
  {full_details("06-promotion-communication.md","Promotion &amp; communication kit — emails, scripts, FAQ","Ready-to-adapt templates: a parent email, a student invite, an on-stage announcement, promo slide copy, an FAQ, and the weekly-communication cadence that keeps a group alive.")}
  {full_details("07-logistics-safety.md","Logistics, safety &amp; the didn&rsquo;t-think-of-that list","Room and gear, a starter budget, child-safety essentials, leader roles, contingencies, and a running list of ideas worth deciding on early.")}
</div></section>
"""

DISCUSS = """
<section id="discuss" class="discuss"><div class="wrap reveal">
  <p class="eyebrow">Let&rsquo;s decide together</p>
  <h2>Open questions &amp; next steps</h2>
  <p class="lede">This is a first draft meant to start the conversation. A few things are confirmed, a few are still assumptions, and a few decisions are still genuinely open — that&rsquo;s where your input comes in.</p>
  <div class="qcols">
    <div class="qbox"><h3>Confirmed</h3><ul>
      <li>Meeting night &amp; length <span class="as">Sunday evenings, ~60 min, launching Sep 6, 2026</span></li>
    </ul></div>
    <div class="qbox"><h3>Assumptions to confirm</h3><ul>
      <li>Ages <span class="as">assumed middle + high school (~12–18)</span></li>
      <li>Experience mix <span class="as">assumed a wide range — hence tiered, per-instrument song parts</span></li>
      <li>Group size <span class="as">designed for one band of ~5–12; splits cleanly into two</span></li>
    </ul></div>
    <div class="qbox"><h3>Decisions still open</h3><ol>
      <li>Final name &amp; whether we want a simple logo/brand</li>
      <li>Room on the church calendar for Sunday evenings</li>
      <li>Grade range — all-levels, or set a floor?</li>
      <li>Free vs. a small materials fee, and the gear budget</li>
      <li>Showcase format — standalone, or folded into a service</li>
      <li>Who owns Planning Center admin &amp; parent communication</li>
      <li>What existing gear we can use so we only buy the gaps</li>
    </ol></div>
  </div>
  <p style="margin-top:24px;color:#cfe0dc">Have a reaction, a name idea, or a student in mind? That&rsquo;s exactly what this page is for — bring it to Evan and the team.</p>
</div></section>
"""

FOOTER = """
<footer><div class="wrap">
  <span><b>Worship Music School</b> · North Metro Church, Kennesaw GA</span>
  <span class="mono" style="font-size:.78rem">Draft v1 · July 2026 · for discussion</span>
</div></footer>
"""

SCRIPT = """
<script>
// song filter (in-memory only)
const btns=document.querySelectorAll('.filters button');
const rows=[...document.querySelectorAll('#songtable tbody tr')];
btns.forEach(b=>b.addEventListener('click',()=>{
  btns.forEach(x=>x.classList.remove('act'));b.classList.add('act');
  const f=b.dataset.f;
  rows.forEach(r=>{r.style.display=(f==='all'||r.dataset.type===f)?'':'none';});
}));
// reveal on scroll
if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches){
  const io=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12});
  document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
}else{document.querySelectorAll('.reveal').forEach(el=>el.classList.add('in'));}
</script>
"""

FAVICON = ("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'>"
           "<rect width='32' height='32' rx='7' fill='%23123a40'/>"
           "<path d='M20 7l-9 2v11.5a3.2 3.2 0 1 0 2 3V13l7-1.6v6.1a3.2 3.2 0 1 0 2 3V7z' fill='%23dc9a34'/></svg>")

HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Worship Music School — North Metro Church</title>
<meta name="description" content="A weekly discipleship & development group for young musicians at North Metro Church: Bible study, real musician skills, and playing together as a band. First-terms plan, Sept 2026–Feb 2027.">
<meta property="og:title" content="Worship Music School — North Metro Church">
<meta property="og:description" content="Discipleship, musicianship, and playing together — a weekly group for young musicians. The first-terms plan, open for discussion.">
<meta property="og:type" content="website">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400&family=Figtree:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{NAV}
{HERO}
{OVERVIEW}
{RHYTHM}
{TERMS}
{SCHEDULE}
{STUDIES}
{MUSIC}
{SONGS}
{BEHIND}
{DISCUSS}
{FOOTER}
{SCRIPT}
</body>
</html>"""

with open(os.path.join(SITE, "index.html"), "w") as f:
    f.write(HTML)
print(f"Wrote index.html ({len(HTML):,} bytes)")
