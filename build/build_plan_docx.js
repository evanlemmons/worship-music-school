const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType, PageBreak
} = require('docx');
const fs = require('fs');
const path = require('path');
const DELIV = path.join(__dirname, '..', 'deliverables');
fs.mkdirSync(DELIV, { recursive: true });

const TEAL = "1F4E5F";
const GRAY = "666666";
const LIGHT = "F2F7F4";
const CW = 9360; // content width for US Letter, 1" margins

const H1 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 260, after: 120 },
  children: [new TextRun({ text, bold: true, color: TEAL, font: "Calibri", size: 30 })],
});
const P = (runs, opts={}) => new Paragraph({
  spacing: { after: 140, line: 276 }, ...opts,
  children: Array.isArray(runs) ? runs : [new TextRun({ text: runs, font: "Calibri", size: 22 })],
});
const R = (text, o={}) => new TextRun({ text, font: "Calibri", size: 22, ...o });
const bullet = (text) => new Paragraph({
  bullet: { level: 0 }, spacing: { after: 80, line: 276 },
  children: [new TextRun({ text, font: "Calibri", size: 22 })],
});

function cell(text, { w, header=false, bold=false, fill } = {}) {
  return new TableCell({
    width: { size: w, type: WidthType.DXA },
    shading: fill ? { type: ShadingType.CLEAR, color: "auto", fill } : undefined,
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    children: [new Paragraph({
      children: [new TextRun({
        text, font: "Calibri", size: header ? 20 : 20,
        bold: header || bold, color: header ? "FFFFFF" : "000000",
      })],
    })],
  });
}
function table(colWidths, rows) {
  const borders = {
    top: { style: BorderStyle.SINGLE, size: 4, color: "D0D0D0" },
    bottom: { style: BorderStyle.SINGLE, size: 4, color: "D0D0D0" },
    left: { style: BorderStyle.SINGLE, size: 4, color: "D0D0D0" },
    right: { style: BorderStyle.SINGLE, size: 4, color: "D0D0D0" },
    insideHorizontal: { style: BorderStyle.SINGLE, size: 4, color: "D0D0D0" },
    insideVertical: { style: BorderStyle.SINGLE, size: 4, color: "D0D0D0" },
  };
  return new Table({
    columnWidths: colWidths,
    width: { size: CW, type: WidthType.DXA },
    borders,
    rows: rows.map((r, i) => new TableRow({
      tableHeader: i === 0,
      children: r.map((c, j) => cell(c, {
        w: colWidths[j], header: i === 0,
        fill: i === 0 ? TEAL : (i % 2 === 0 ? LIGHT : undefined),
      })),
    })),
  });
}

const children = [];

// Title block
children.push(new Paragraph({
  spacing: { after: 40 },
  children: [new TextRun({ text: "Worship Music School", bold: true, color: TEAL, font: "Calibri", size: 52 })],
}));
children.push(new Paragraph({
  spacing: { after: 20 },
  children: [new TextRun({ text: "Program Plan for a Young Musicians' Discipleship & Development Group", font: "Calibri", size: 24, color: GRAY })],
}));
children.push(new Paragraph({
  spacing: { after: 240 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: TEAL, space: 6 } },
  children: [new TextRun({ text: "North Metro Church · Kennesaw, GA   |   Launching Sunday, September 6, 2026   |   Prepared July 2026", font: "Calibri", size: 20, color: GRAY })],
}));

// Vision callout
children.push(new Paragraph({
  spacing: { after: 200, before: 60 },
  shading: { type: ShadingType.CLEAR, color: "auto", fill: LIGHT },
  border: {
    top:{style:BorderStyle.SINGLE,size:2,color:"D9E6DF"}, bottom:{style:BorderStyle.SINGLE,size:2,color:"D9E6DF"},
    left:{style:BorderStyle.SINGLE,size:18,color:TEAL}, right:{style:BorderStyle.SINGLE,size:2,color:"D9E6DF"},
  },
  children: [new TextRun({ text: "Our aim: to form young musicians into worshipers first and skilled, stage-ready band members second — growing them in Christ, in craft, and in the real-world skills of playing music together.", italics: true, font: "Calibri", size: 24, color: "244A3B" })],
}));

// Why
children.push(H1("Why this exists"));
children.push(P("Most churches can teach a teenager to play an instrument, and many can run a Bible study. Very few do both in the same room, on purpose, led by people who have actually done it professionally. This group closes that gap. We want students to leave able to explain what worship really is and live like it, to understand the whole ecosystem of being a working musician — not just the notes, but the gear, the team, and the preparation — and to sit in with a band and confidently hold their part on a real stage."));
children.push(P('The name "Worship Music School" is a working title; the heart of it is discipleship through music.'));

// Weekly meeting
children.push(H1("The three-part weekly meeting"));
children.push(P("Every meeting is built on the same three sections, in this order. The order matters: we ground ourselves before we sharpen skills, and we sharpen skills before we play — so that playing together is the celebration the rest of the night points toward."));
children.push(table([2100, 1300, 5960], [
  ["Section", "Time", "What happens"],
  ["1 · Discipleship", "~15 min", "A short, discussion-driven Bible study (NIV). The first term deliberately explores worship as a whole life, not just singing — and we spend real time getting to know each other."],
  ["2 · Musicianship", "~20 min", "The craft nobody teaches you: signal flow and gear, in-ear monitors, playing to a click, charts, rehearsing at home vs. as a band, the music director's role, planning a set, and production (sound, lights, lyrics, stage plots)."],
  ["3 · Playing together", "~25 min", "We learn and work a song as a band and actually play it. Repertoire leans worship, with the occasional secular song for range and fun; each song reinforces that week's lesson where possible."],
]));
children.push(P([R("Timing note: ", {italics:true, bold:true, color:GRAY}), R("the split assumes a ~60-minute meeting. If we stretch to 90 minutes, expand to roughly 25 / 30 / 35; for a full two hours, the extra time is best spent on hands-on gear and a longer band run-through.", {italics:true, color:GRAY, size:20})]));

// Who / leaders
children.push(H1("Who it's for, and who leads"));
children.push(P("The group is designed for young musicians, roughly middle-through-high-school age, across a range of experience — from students still learning their instrument to those ready for real repertoire. The curriculum uses tiered, per-instrument parts so a beginner and an experienced player can be in the same band and both have something meaningful to play."));
children.push(P([
  R("The strength of the group is that its leaders have lived this. ", {}),
  R("Evan Lemmons", {bold:true}), R(" is a former professional touring and session musician — bass professionally, drums at an intermediate level, with functional piano and guitar — and currently plays and leads at North Metro. A ", {}),
  R("full-time music teacher", {bold:true}), R(" co-leads, anchoring instrument instruction and theory on piano and guitar. A ", {}),
  R("professional vocalist", {bold:true}), R(" anchors vocal coaching, harmony, and leading a congregation. All three currently serve on North Metro's team. Between them the group covers the full band — bass, drums, keys, guitar, and voice — plus real stage and professional experience.", {}),
]));

// Terms
children.push(H1("The first two terms"));
children.push(P("We treat September through February as two connected terms with a natural break at Christmas. A detailed, week-by-week schedule and a full song library are provided as companion spreadsheets."));
children.push(table([1150, 1500, 4310, 2400], [
  ["Term", "Dates", "What we cover", "Milestone"],
  ["Fall — “What Is Worship?”", "Sep 6 – Dec 13 (14 wks)", "Foundations. A biblical theology of worship-as-life; the ecosystem of playing (gear, signal flow, in-ears, click, charts, rehearsing); accessible worship songs that grow in difficulty.", "Fall Showcase (Dec 13) — the term's repertoire performed for families / a service."],
  ["Winter — “The Worshiping Life”", "Jan 3 – Feb 21 (8 wks)", "Deepening. The Psalms and the character of a worship leader; gear deep-dives, set planning, leading vs. playing, and self-review; the band works toward a full, connected set.", "A full connected set (Feb 21) — planned, flowing, with transitions; plan spring."],
]));

// Milestones + measures
children.push(H1("What students build toward"));
children.push(P("The program is organized around visible milestones so students, parents, and leaders can all see progress: the whole band playing their first song start to finish by about week four; the Fall Showcase before Christmas; a full, connected set by the end of February; and — for those who are ready — an on-ramp to shadowing and serving on a real North Metro team."));
children.push(P([R("How we'll know it's working: ", {bold:true}), R("students can explain what worship is in their own words; they show up prepared, with parts practiced at home; the band can hold a song together with a click and real dynamics; and — the quiet one that matters most — they want to be there, and they're inviting friends.", {})]));

// Rollout
children.push(H1("Getting there: rollout timeline"));
children.push(table([2600, 1900, 4860], [
  ["Phase", "When", "Key actions"],
  ["Setup", "Now → late Aug", "Confirm leaders, room, night, and tech; set up Planning Center (Registrations, People, Groups, Services); build promotion; open signups."],
  ["Promotion push", "Late Aug → Sep 6", "On-stage announcements, parent emails, socials; registrations close and roster is set; leaders pre-learn the first songs; gather loaner gear."],
  ["Fall term", "Sep 6 – Dec 13", "Weekly meetings; first-song milestone (~wk 4); Thanksgiving-week break (Nov 22); Fall Showcase (Dec 13)."],
  ["Christmas break", "Dec 23 & 30", "No meetings."],
  ["Winter term", "Jan 3 – Feb 21", "Weekly meetings; full-set milestone; plan spring term and any team placements."],
]));

// Ask of church
children.push(H1("What we'd ask of the church"));
children.push(P("The program can start lean and grow. Specifically, it needs:"));
children.push(bullet("A consistent room with adequate power and space for a small band setup and a discussion circle, plus a screen for lyrics/charts."));
children.push(bullet("Access to (or storage for) basic backline — drums, keys, a couple of amps or DIs, a small PA or monitor solution, and a few mics — much of which may already exist midweek."));
children.push(bullet("A modest recurring budget for consumables (cables, sticks, strings, batteries, in-ear tips) and any curriculum materials; a specific figure will follow a gear inventory."));
children.push(bullet("Confirmation that all leaders and helpers are background-checked and cleared per the church's child-safety policy, and a clear staff point of contact."));

// Assumptions
children.push(H1("A few things confirmed, a few still assumed"));
children.push(P("This plan was drafted from the initial brief; the meeting night/time is now locked, and a few other parameters remain assumed and easy to adjust — none of them change the structure, only the specifics:"));
children.push(bullet("Meeting night/time: confirmed — Sunday evenings, ~60 minutes, starting Sept 6."));
children.push(bullet("Ages: middle + high school (~12–18)."));
children.push(bullet("Experience: a wide mix, which is why parts are tiered per instrument."));
children.push(bullet("Group size: designed for a single band of roughly 5–12, splitting cleanly into two bands if larger."));

// Repository appendix
children.push(H1("The full plan is already built out"));
children.push(P("Behind this summary sits a complete, organized repository the leaders can run the program from and grow over time: the program overview; a week-by-week rollout schedule (also a spreadsheet); the discipleship / Bible-study arc; the musicianship topic arc; a song library of ~45 songs rated by difficulty per instrument (also a spreadsheet); a Planning Center setup guide; a promotion and communication kit with ready-to-send templates; and a logistics, safety, and open-questions file. Everything is drafted and ready to refine together."));

const doc = new Document({
  creator: "Worship Music School",
  title: "Worship Music School — Program Plan",
  sections: [{
    properties: { page: {
      size: { width: 12240, height: 15840 },
      margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 },
    } },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(path.join(DELIV, "Worship Music School - Program Plan.docx"), buf);
  console.log("Saved Program Plan docx");
});
