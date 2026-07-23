#!/usr/bin/env python3
"""Build the Rollout Schedule spreadsheet from data/rollout_schedule.csv."""
import csv, os
_R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(_R, "data"); DELIV = os.path.join(_R, "deliverables")
os.makedirs(DELIV, exist_ok=True)
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def read(p):
    with open(p) as f:
        return list(csv.reader(f))

thin = Side(style="thin", color="D0D0D0")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
HEADER_FILL = PatternFill("solid", fgColor="1F4E5F")
HEADER_FONT = Font(name="Arial", size=11, bold=True, color="FFFFFF")
BASE_FONT = Font(name="Arial", size=10)

def style_header(ws, ncols, row=1):
    for c in range(1, ncols+1):
        cell = ws.cell(row=row, column=c)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        cell.border = border
    ws.row_dimensions[row].height = 30

# ============ Schedule ============
sched = read(os.path.join(DATA, "rollout_schedule.csv"))
sh, srows = sched[0], sched[1:]
idx = {c: i for i, c in enumerate(sh)}

# Build display rows with computed week numbers (meetings counted in order).
disp_header = ["Week", "Date", "Term", "Discipleship (~15 min)", "Passage (NIV)", "Musicianship (~20 min)", "Note"]
disp = []
wk = 0
for r in srows:
    is_meeting = r[idx["Status"]].strip().lower() == "meeting"
    if is_meeting:
        wk += 1
        disp.append([str(wk), r[idx["Date"]], r[idx["Term"]], r[idx["Discipleship (~15 min)"]],
                     r[idx["Passage (NIV)"]], r[idx["Musicianship (~20 min)"]], r[idx["Note"]]])
    else:
        disp.append(["—", r[idx["Date"]], r[idx["Term"]], "— no meeting —", "", "", r[idx["Note"]]])

wb = Workbook()
ws = wb.active
ws.title = "Rollout Schedule"

ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(disp_header))
t = ws.cell(row=1, column=1, value="Worship Music School — Weekly Rollout Schedule (Sept 2026 – Feb 2027)")
t.font = Font(name="Arial", size=14, bold=True, color="1F4E5F")
t.alignment = Alignment(horizontal="left", vertical="center")
ws.row_dimensions[1].height = 26
sub = ws.cell(row=2, column=1, value="Sundays, ~60 min · 3 sections/week: Discipleship (~15) · Musicianship (~20) · Playing Together (~25). Songs are chosen weekly to fit who attends.")
ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=len(disp_header))
sub.font = Font(name="Arial", size=9, italic=True, color="666666")

hdr_row = 3
for j, name in enumerate(disp_header, 1):
    ws.cell(row=hdr_row, column=j, value=name)
style_header(ws, len(disp_header), row=hdr_row)

FALL = PatternFill("solid", fgColor="FBF3E9")
WINTER = PatternFill("solid", fgColor="EAF2F8")
BREAK = PatternFill("solid", fgColor="EDEDED")

for i, r in enumerate(disp):
    xl = hdr_row + 1 + i
    is_break = (r[0] == "—")
    term = r[2]
    for j, val in enumerate(r, 1):
        cell = ws.cell(row=xl, column=j, value=val)
        cell.font = BASE_FONT if not is_break else Font(name="Arial", size=10, italic=True, color="999999")
        cell.border = border
        cell.alignment = Alignment(wrap_text=True, vertical="top",
                                   horizontal="center" if j in (1, 2, 3) else "left")
        if is_break:
            cell.fill = BREAK
        elif term == "Fall":
            cell.fill = FALL
        elif term == "Winter":
            cell.fill = WINTER

widths = [6, 12, 8, 30, 26, 34, 22]
for j, w in enumerate(widths, 1):
    ws.column_dimensions[get_column_letter(j)].width = w
ws.freeze_panes = f"A{hdr_row+1}"
ws.auto_filter.ref = f"A{hdr_row}:{get_column_letter(len(disp_header))}{hdr_row+len(disp)}"
ws.sheet_view.showGridLines = False
wb.save(os.path.join(DELIV, "Worship Music School - Rollout Schedule.xlsx"))
print("Saved schedule xlsx")
