# How to publish this page (GitHub Pages)

Two ways. The first needs no terminal.

## Option A — GitHub website only (~2 minutes, easiest)

1. Go to <https://github.com/new> and create a repository. Name it something like `worship-music-school`. Set it to **Public**. Don't add a README (this folder already has one). Click **Create repository**.
2. On the new repo page, click **uploading an existing file** (or **Add file → Upload files**).
3. Drag in the contents of this folder: `index.html`, `README.md`, and `.nojekyll`.
   - If `.nojekyll` is hard to select (hidden dot-file), you can skip it — it's optional for this page.
4. Click **Commit changes**.
5. Go to **Settings → Pages** (left sidebar).
6. Under **Build and deployment → Source**, choose **Deploy from a branch**. Set **Branch** to `main` and folder to `/ (root)`. Click **Save**.
7. Wait ~1 minute, then refresh. GitHub shows your live URL at the top of the Pages screen:
   `https://<your-username>.github.io/worship-music-school/`

That URL is fully public — anyone can open it, no login. Share it freely.

## Option B — Terminal with git

From inside this folder:

```bash
git init
git add .
git commit -m "Worship Music School — plan page v1"
git branch -M main
# create the repo on github.com first (Public), then:
git remote add origin https://github.com/<your-username>/worship-music-school.git
git push -u origin main
```

Then enable Pages: **Settings → Pages → Deploy from a branch → main → /(root) → Save**.

## Updating the page later
Replace `index.html` (upload a new version in the web UI, or `git commit` + `git push`). GitHub Pages redeploys automatically within a minute or two.

## Tip: a cleaner URL
If you name the repository exactly `<your-username>.github.io`, the site publishes at `https://<your-username>.github.io/` (no repo name in the path). Great if this becomes the group's main site later.
