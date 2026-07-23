---
name: session-end
description: Use when the user runs /session-end to close out a Worship Music School working session — records decisions in SESSIONS.md, rebuilds the public site and deliverables if source content changed, and lands everything on main via branch + PR + merge.
---

# Session End

Closes out a working session on this repo: apply any decisions made in conversation to the source files, rebuild what's generated, log the session, and ship it to `main`. See `CLAUDE.md` at repo root for the source-of-truth rule and build commands.

## Steps

1. **Check for anything to do.** `git status`. If the tree is clean and nothing decision-worthy came up this session, tell the user there's nothing to log and stop — don't create empty commits or PRs.

2. **Apply decisions to source, not just notes.** Scan the session for anything decided (name, dates, budget, room, format, song picks, copy edits, etc.) that isn't yet reflected in the repo. Edit the real source: `content/00,02,03,05,06,07-*.md` prose, `content/site-copy.md` (landing-page copy), and `data/*.csv` tables. Never hand-edit `content/01-*.md`, `content/04-*.md`, `docs/index.html`, or `deliverables/*` — those are generated.

3. **Rebuild whatever source touched.**
   ```bash
   python3 build/build_markdown_docs.py   # if data/*.csv changed (rollout schedule or song library)
   python3 build/build_site.py            # always, if anything in content/ or data/ changed — regenerates docs/index.html
   ```
   Also regenerate `deliverables/` if the change is something a parent or leader would print/share (schedule, song library, the full plan doc):
   ```bash
   python3 build/build_xlsx.py
   node build/build_plan_docx.js          # needs `npm i docx` once per machine
   ```

4. **Log the session.** Append a dated entry to `SESSIONS.md` at repo root (create it from the template below if it doesn't exist yet). Write it from what actually happened, not a diff dump — capture the decision and the *why* when there was one, and anything still open. Keep it to a handful of bullets.

5. **Branch, commit, PR, merge.** Even solo, land changes through a PR — it's the reviewable record, and it's what was asked for:
   ```bash
   git checkout -b session-$(date +%Y-%m-%d)      # append -2, -3... if one already exists today
   git add -A
   git commit -m "<what changed and why, not a file list>"
   git push -u origin HEAD
   gh pr create --fill
   gh pr merge --merge --delete-branch
   git checkout main && git pull
   ```

6. **Confirm.** Tell the user what shipped and that the live page is updated: https://evanlemmons.github.io/worship-music-school/ (Pages redeploys within ~1-2 min of landing on `main`).

## SESSIONS.md entry template

```markdown
## YYYY-MM-DD
**Decided:** short bullets — what was decided and why, if non-obvious.
**Changed:** what shipped to the site/repo as a result.
**Open:** anything still unresolved to pick up next time.
```

## Common mistakes

- Editing `data/rollout_schedule.csv` but only running `build_site.py` — also run `build_markdown_docs.py` first, or `content/01-weekly-rhythm-schedule.md` goes stale relative to the CSV.
- Pushing straight to `main` instead of branch + PR + merge.
- Logging file diffs instead of decisions — `git log` already has the diff; `SESSIONS.md` should answer "what did we decide and why" for a future session (or Evan) skimming it later.
- Forgetting `deliverables/` when a change is schedule- or song-library-facing — those are the printable versions leaders actually hand out.
