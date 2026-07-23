# How this page is published (GitHub Pages)

**Live URL:** https://evanlemmons.github.io/worship-music-school/
**Repo:** https://github.com/evanlemmons/worship-music-school (public)

## Current setup
GitHub Pages is configured to deploy from the `main` branch, `/docs` folder — that's this folder. `docs/index.html` is the published page; `docs/.nojekyll` disables Jekyll processing so the self-contained HTML is served as-is.

`docs/index.html` is **generated** — never hand-edit it. Edit `content/*.md` and `data/*.csv` at the repo root, then rebuild:
```bash
python3 build/build_site.py     # regenerates docs/index.html
git add -A && git commit -m "..." && git push
```
GitHub Pages redeploys automatically within a minute or two of a push to `main`.

## If you ever need to recreate this from scratch
```bash
git init
git add .
git commit -m "Worship Music School — plan page v1"
git branch -M main
gh repo create worship-music-school --public --source=. --remote=origin --push
gh api -X POST repos/<your-username>/worship-music-school/pages \
  -f "source[branch]=main" -f "source[path]=/docs"
```
Without `gh`: create the repo at <https://github.com/new> (Public), push, then **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main` → Folder: `/docs` → Save**.

Note: GitHub Pages branch deploys only support `/ (root)` or `/docs` as the folder — no other subfolder works. That's why the site lives in `docs/` rather than `site/`.

## Tip: a cleaner URL
Naming the repository exactly `<your-username>.github.io` publishes at `https://<your-username>.github.io/` with no repo name in the path. Not used here since `worship-music-school` is a dedicated ministry repo, separate from any personal GitHub Pages site.
