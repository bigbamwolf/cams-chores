# Cams Chores

Phone-first chore app for Cams. Self-contained, installable to her home screen, offline-friendly, no backend.

## What is in this folder
* `index.html` the whole app, inline CSS + JS
* `manifest.webmanifest` PWA install manifest
* `sw.js` service worker (offline cache)
* `icon-192.png`, `icon-512.png`, `icon-512-maskable.png` app icons
* `make_icons.py` re-generates the icons (Pillow)

## Deploy options (free, HTTPS link to send Cams)

Pick one. All three give a public HTTPS URL, which is required for "Add to Home Screen" + PWA install on iOS.

### Option 1, Netlify Drop (fastest, 30 seconds)
1. Open https://app.netlify.com/drop
2. Drag the entire `cams-chores` folder onto the page
3. Copy the URL it gives, send to Cams
4. To rename the subdomain, claim the site, then Site settings, Change site name

### Option 2, Cloudflare Pages (free, custom subdomain)
1. Open https://pages.cloudflare.com, click Create a project, Direct upload
2. Project name, e.g. `cams-chores`
3. Drag the entire folder, click Deploy
4. Live URL is `https://cams-chores.pages.dev`

### Option 3, GitHub Pages
1. `cd /Users/macbookair/Claude/cams-chores`
2. `git init && git add . && git commit -m "Cams Chores"`
3. Create a public repo, e.g. `cams-chores`, push
4. Repo Settings, Pages, Source = main, save
5. Live URL is `https://<user>.github.io/cams-chores/`

### Test on her phone
1. Open the URL on her iPhone Safari (or Android Chrome)
2. iPhone: Share, Add to Home Screen
3. Android: menu, Install app
4. The icon lands on her home screen, opens full screen like a real app

## How it works
* All chore data lives in `localStorage` on her phone, survives close, refresh, offline
* Service worker caches the app so it loads with no signal
* No accounts, no backend, no sync (single device by design)

## Theme switch
Three dots in the top right, peach, sky, lavender. She picks, sticks across reloads.

## If she wants to wipe everything
In the browser, open the URL, then in dev tools console run
```
localStorage.clear(); location.reload();
```
Or just uninstall the home-screen icon and reinstall.
