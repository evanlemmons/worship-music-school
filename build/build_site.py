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

# ---------- copy deck (all editable landing-page text lives in content/site-copy.md) ----------
def load_copy():
    text = open(os.path.join(CONTENT, "site-copy.md"), encoding="utf-8").read()
    out = {}
    for chunk in text.split("\n## ")[1:]:
        nl = chunk.index("\n")
        out[chunk[:nl].strip()] = chunk[nl + 1:].strip()
    return out
COPY = load_copy()

def _inline(md_text):
    """Render a short copy string, stripping the single wrapping <p> markdown adds."""
    h = md2html(md_text.strip())
    if h.startswith("<p>") and h.endswith("</p>") and "<p>" not in h[3:]:
        h = h[3:-4]
    return h
def ci(key):                       # inline copy slot (heading, eyebrow, sentence)
    return _inline(COPY[key])
def cattr(key):                    # copy destined for an HTML attribute
    return html.escape(COPY[key].strip(), quote=True)
def crows(key):                    # bulleted slot -> list of ' | '-split field lists
    rows = []
    for line in COPY[key].splitlines():
        line = line.strip()
        if line.startswith("- "):
            rows.append([f.strip() for f in line[2:].split(" | ")])
    return rows

# ---------- term-split collapsibles ----------
def term_details(path):
    text = open(os.path.join(CONTENT, path)).read()
    parts = text.split("\n## ")
    intro = strip_h1(parts[0]).strip()
    out = [f'<div class="prose lead">{md2html(intro)}</div>']
    for p in parts[1:]:
        nl = p.index("\n"); title = p[:nl].strip(); body = p[nl+1:]
        out.append(f'<details class="wk"><summary>{html.escape(title)}</summary>'
                   f'<div class="prose">{md2html(body)}</div></details>')
    return "\n".join(out)

def full_details(path, summary, teaser):
    text = strip_h1(open(os.path.join(CONTENT, path)).read()).strip()
    return (f'<p class="teaser">{teaser}</p>'
            f'<details class="deep"><summary>{html.escape(summary)}</summary>'
            f'<div class="prose">{md2html(text)}</div></details>')

# ---------- schedule ----------
def schedule_html():
    """Bible-study + musicianship arc. Week numbers are computed (meetings counted
    in order), so toggling a date's Status between meeting/off needs no renumbering."""
    rows = read_csv(os.path.join(DATA, "rollout_schedule.csv"))
    head = rows[0]; idx = {c: i for i, c in enumerate(head)}
    trs = []
    wk = 0
    for r in rows[1:]:
        date = r[idx["Date"]]; term = r[idx["Term"]]
        is_meeting = r[idx["Status"]].strip().lower() == "meeting"
        if is_meeting:
            wk += 1
            cls = term.lower()
            trs.append(
                f'<tr class="{cls}">'
                f'<td class="col-week mono">{wk}</td>'
                f'<td class="col-date">{html.escape(date)}</td>'
                f'<td class="col-disc">{html.escape(r[idx["Discipleship (~15 min)"]])}</td>'
                f'<td class="col-pass mono2">{html.escape(r[idx["Passage (NIV)"]])}</td>'
                f'<td class="col-mus">{html.escape(r[idx["Musicianship (~20 min)"]])}</td></tr>')
        else:
            label = html.escape(r[idx["Note"]] or "Break")
            trs.append(
                f'<tr class="brk">'
                f'<td class="col-week mono">—</td>'
                f'<td class="col-date">{html.escape(date)}</td>'
                f'<td class="col-disc" colspan="3">— {label} · no meeting —</td></tr>')
    return "\n".join(trs)

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
nav a.lnk.active{background:var(--pine-800);color:#fff}
.tbd{display:flex;gap:16px;align-items:flex-start;background:var(--card);border:1px solid var(--line);
  border-radius:14px;padding:22px 24px;margin-top:18px;max-width:70ch}
.tbd-tag{font-family:"IBM Plex Mono",monospace;font-size:.72rem;font-weight:600;letter-spacing:.1em;
  background:var(--amber-soft);color:#8a5a12;padding:4px 10px;border-radius:20px;white-space:nowrap;margin-top:3px}
.tbd p{margin:0;color:var(--ink-soft)}
.leader-hero{background:var(--pine-800);color:#eaf3f0;padding:60px 0 48px}
.leader-hero .eyebrow{color:var(--amber)}
.leader-hero h1{font-family:"Fraunces",serif;font-size:clamp(2rem,5vw,3rem);margin:.2rem 0 .6rem;color:#fff;line-height:1.05}
.leader-hero p{max-width:64ch;color:#cfe0dc;margin:0}
nav a.lnk.ext{color:var(--amber-2);font-weight:600}
nav a.lnk.ext:hover{background:var(--amber-soft);color:var(--amber-2)}

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
.col-res{white-space:nowrap}
.reslink{display:inline-block;font-family:"IBM Plex Mono",monospace;font-size:.68rem;text-transform:uppercase;
  letter-spacing:.05em;padding:3px 8px;border-radius:20px;margin:0 4px 4px 0;text-decoration:none;
  background:var(--amber-soft);color:#8a5a12;border:1px solid transparent;transition:.15s}
.reslink:hover{background:var(--amber);color:#fff}
.res-empty{font-size:.78rem;color:#9a9a90;font-style:italic}

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

def nav_html(links, extra=""):
    """links: list of (href, label). extra: trailing raw HTML (e.g. an external link)."""
    items = "".join(f'<a class="lnk" href="{h}">{_inline(l)}</a>' for h, l in links)
    return f"""
<nav><div class="wrap">
<span class="brand">{ci("nav_brand")} <span class="dot">●</span></span>
{items}{extra}
</div></nav>
"""

# The leader page is intentionally NOT linked from the landing nav (kept low-profile
# for sign-up visitors); leaders reach it by URL. Add a (…, 'leader.html') ext link here
# if you'd rather make it discoverable.
landing_nav = nav_html([(f'#{a}', l) for a, l in crows("nav_links")])
leader_nav = nav_html([('#behind', 'Setup'), ('#discuss', 'Open questions')],
                      extra='<a class="lnk ext" href="index.html">← Main page</a>')

hero_facts_html = "".join(
    f'<span><span class="k">{_inline(lab)}</span> &nbsp;<b>{_inline(val)}</b></span>'
    for lab, val in crows("hero_facts"))
rhythm_cards_html = "".join(
    f'<div class="part p{i}"><div class="bar"></div><div class="num">{_inline(num)}</div>'
    f'<h3>{_inline(t)}</h3><div class="time">{_inline(tm)}</div><p>{_inline(d)}</p></div>'
    for i, (num, t, tm, d) in enumerate(crows("rhythm_cards"), 1))

_terms = crows("terms_list")
_miles = [m[0] for m in crows("terms_milestones")]
terms_rail_html = ""
for _i, (_nm, _dates, _wks, _title, _desc) in enumerate(_terms):
    terms_rail_html += (
        f'<div class="trm"><div class="when"><span class="big">{_inline(_nm)}</span>'
        f'{_inline(_dates)}<br>{_inline(_wks)}</div>'
        f'<div><h3>{_inline(_title)}</h3><p>{_inline(_desc)}</p></div></div>')
    if _i < len(_miles):
        terms_rail_html += f'<div class="milestone"><span class="star">★</span> {_inline(_miles[_i])}</div>'
team_html = "".join(
    f'<div class="mem"><div class="role">{_inline(role)}</div><h4>{_inline(nm)}</h4><p>{_inline(bio)}</p></div>'
    for role, nm, bio in crows("team_members"))

behind_html = "".join(
    full_details(fname, summary, _inline(teaser)) for fname, summary, teaser in crows("behind_cards"))

confirmed_html = "".join(
    f'<li>{_inline(lab)} <span class="as">{_inline(ann)}</span></li>' for lab, ann in crows("discuss_confirmed"))
assumptions_html = "".join(
    f'<li>{_inline(lab)} <span class="as">{_inline(ann)}</span></li>' for lab, ann in crows("discuss_assumptions"))
open_html = "".join(f'<li>{_inline(x[0])}</li>' for x in crows("discuss_open"))

HERO = f"""
<header class="hero">
  <div class="eq">{eq_bars}</div>
  <div class="glow"></div>
  <div class="wrap">
    <p class="eyebrow">{ci("hero_eyebrow")}</p>
    <h1>{ci("hero_title")}<span class="sub">{ci("hero_subtitle")}</span></h1>
    <p class="vision">{ci("hero_vision")}</p>
    <div class="facts">
      {hero_facts_html}
    </div>
  </div>
</header>
"""

OVERVIEW = f"""
<section id="overview"><div class="wrap reveal">
  <p class="eyebrow">{ci("overview_eyebrow")}</p>
  <h2>{ci("overview_heading")}</h2>
  <p class="lede">{ci("overview_lede")}</p>
  <p style="max-width:64ch;color:var(--ink-soft);margin-top:1rem">{ci("overview_body")}</p>
</div></section>
"""

RHYTHM = f"""
<section id="rhythm"><div class="wrap reveal">
  <p class="eyebrow">{ci("rhythm_eyebrow")}</p>
  <h2>{ci("rhythm_heading")}</h2>
  <p class="lede">{ci("rhythm_lede")}</p>
  <div class="grid3">
    {rhythm_cards_html}
  </div>
  <p class="note">{ci("rhythm_note")}</p>
</div></section>
"""

TERMS = f"""
<section id="terms"><div class="wrap reveal">
  <p class="eyebrow">{ci("terms_eyebrow")}</p>
  <h2>{ci("terms_heading")}</h2>
  <div class="time-rail">
    {terms_rail_html}
  </div>
  <div style="margin-top:34px">
    <p class="eyebrow">{ci("team_eyebrow")}</p>
    <div class="team">
      {team_html}
    </div>
  </div>
</div></section>
"""

SCHEDULE = f"""
<section id="schedule"><div class="wrap reveal">
  <p class="eyebrow">{ci("schedule_eyebrow")}</p>
  <h2>{ci("schedule_heading")}</h2>
  <p class="lede">{ci("schedule_lede")}</p>
  <div class="tablewrap"><table>
    <thead><tr>
      <th class="col-week">Wk</th><th class="col-date">Date</th>
      <th class="col-disc">Discipleship</th><th class="col-pass">Passage (NIV)</th>
      <th class="col-mus">Musicianship</th>
    </tr></thead>
    <tbody>{schedule_html()}</tbody>
  </table></div>
</div></section>
"""

STUDIES = f"""
<section id="studies"><div class="wrap reveal">
  <p class="eyebrow">{ci("studies_eyebrow")}</p>
  <h2>{ci("studies_heading")}</h2>
  {term_details("02-discipleship-track.md")}
</div></section>
"""

MUSIC = f"""
<section id="musicianship"><div class="wrap reveal">
  <p class="eyebrow">{ci("music_eyebrow")}</p>
  <h2>{ci("music_heading")}</h2>
  {term_details("03-musicianship-track.md")}
</div></section>
"""

SONGS = f"""
<section id="songs"><div class="wrap reveal">
  <p class="eyebrow">{ci("songs_eyebrow")}</p>
  <h2>{ci("songs_heading")}</h2>
  <div class="tbd">
    <span class="tbd-tag">TBD</span>
    <p>{ci("songs_lede")}</p>
  </div>
</div></section>
"""

BEHIND = f"""
<section id="behind"><div class="wrap reveal">
  <p class="eyebrow">{ci("behind_eyebrow")}</p>
  <h2>{ci("behind_heading")}</h2>
  <p class="lede">{ci("behind_lede")}</p>
  {behind_html}
</div></section>
"""

DISCUSS = f"""
<section id="discuss" class="discuss"><div class="wrap reveal">
  <p class="eyebrow">{ci("discuss_eyebrow")}</p>
  <h2>{ci("discuss_heading")}</h2>
  <p class="lede">{ci("discuss_lede")}</p>
  <div class="qcols">
    <div class="qbox"><h3>{ci("discuss_col_confirmed")}</h3><ul>{confirmed_html}</ul></div>
    <div class="qbox"><h3>{ci("discuss_col_assumptions")}</h3><ul>{assumptions_html}</ul></div>
    <div class="qbox"><h3>{ci("discuss_col_open")}</h3><ol>{open_html}</ol></div>
  </div>
  <p style="margin-top:24px;color:#cfe0dc">{ci("discuss_closing")}</p>
</div></section>
"""

FOOTER = f"""
<footer><div class="wrap">
  <span>{ci("footer_left")}</span>
  <span class="mono" style="font-size:.78rem">{ci("footer_right")}</span>
</div></footer>
"""

LEADER_HERO = f"""
<header class="leader-hero"><div class="wrap">
  <p class="eyebrow">{ci("leader_eyebrow")}</p>
  <h1>{ci("leader_title")}</h1>
  <p>{ci("leader_intro")}</p>
</div></header>
"""

SCRIPT = """
<script>
// reveal on scroll
if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches){
  const io=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12});
  document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
}else{document.querySelectorAll('.reveal').forEach(el=>el.classList.add('in'));}
// scrollspy: highlight the nav link for the section crossing the viewport middle
const spy=[...document.querySelectorAll('nav a.lnk')].filter(a=>(a.getAttribute('href')||'').startsWith('#'));
const byId=new Map(spy.map(a=>[a.getAttribute('href').slice(1),a]));
const secs=spy.map(a=>document.getElementById(a.getAttribute('href').slice(1))).filter(Boolean);
if(secs.length){
  const spyIO=new IntersectionObserver((es)=>{
    es.forEach(e=>{if(e.isIntersecting){spy.forEach(a=>a.classList.remove('active'));const a=byId.get(e.target.id);if(a)a.classList.add('active');}});
  },{rootMargin:'-50% 0px -50% 0px',threshold:0});
  secs.forEach(s=>spyIO.observe(s));
}
</script>
"""

FAVICON = ("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'>"
           "<rect width='32' height='32' rx='7' fill='%23123a40'/>"
           "<path d='M20 7l-9 2v11.5a3.2 3.2 0 1 0 2 3V13l7-1.6v6.1a3.2 3.2 0 1 0 2 3V7z' fill='%23dc9a34'/></svg>")

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400&family=Figtree:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">'

def page(title, description, nav, body):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:type" content="website">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{FONTS}
<style>{CSS}</style>
</head>
<body>
{nav}
{body}
{FOOTER}
{SCRIPT}
</body>
</html>"""

# ---- Landing page: for anyone interested / involved ----
index_body = HERO + OVERVIEW + RHYTHM + TERMS + SCHEDULE + STUDIES + MUSIC + SONGS
index_html = page(cattr("meta_title"), cattr("meta_description"), landing_nav, index_body)
with open(os.path.join(SITE, "index.html"), "w") as f:
    f.write(index_html)

# ---- Leader page: setup + open questions, separate from the landing page ----
leader_body = LEADER_HERO + BEHIND + DISCUSS
leader_html = page(cattr("leader_meta_title"), cattr("leader_meta_description"), leader_nav, leader_body)
with open(os.path.join(SITE, "leader.html"), "w") as f:
    f.write(leader_html)

print(f"Wrote index.html ({len(index_html):,} bytes) and leader.html ({len(leader_html):,} bytes)")
