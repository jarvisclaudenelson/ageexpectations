# AgeExpectations.com

A static parenting reference site covering child development from newborn through 18 years. Optimized for Answer Engine Optimization (AEO) with JSON-LD structured data, semantic HTML, and LLM-citation-friendly content.

## Tech Stack

- **Astro** — static site generator
- **@astrojs/sitemap** — auto-generated sitemap
- Vanilla CSS — no framework, mobile-first
- JSON-LD Article + FAQPage schema on every page

## Development

```bash
npm install
npm run dev       # Start dev server at localhost:4321
npm run build     # Build static output to ./dist
npm run preview   # Preview the built site locally
```

## Deploy to Cloudflare Pages

1. Push this repo to GitHub
2. In Cloudflare Pages dashboard, create a new project linked to the repo
3. Build settings:
   - **Build command:** `npm run build`
   - **Build output directory:** `dist`
   - **Node version:** 18+ (set `NODE_VERSION=18` env var if needed)

## Deploy to GitHub Pages

1. Push to GitHub
2. In repo Settings > Pages, select GitHub Actions as source
3. Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages
on:
  push:
    branches: [main]
jobs:
  build-deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pages: write
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci && npm run build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist
      - uses: actions/deploy-pages@v4
```

## Content Structure

- `/` — Homepage with age range index
- `/ages/{age-slug}/` — Age overview pages
- `/ages/{age-slug}/{topic}/` — Topic-specific articles

### Age Ranges
Newborn, 1-3 Mo, 3-6 Mo, 6-9 Mo, 9-12 Mo, 12-18 Mo, 18-24 Mo, 2-3 Yr, 3-4 Yr, 4-5 Yr, 5-6 Yr, 6-8 Yr, 8-10 Yr, 10-12 Yr, 12-14 Yr, 14-18 Yr

### Topics per Age
Milestones, Sleep, Feeding & Nutrition, Behavior & Emotions, Language & Communication, Play & Learning, Health & Safety, Red Flags

## AEO Features

- JSON-LD `Article` + `FAQPage` schema on every page
- `robots.txt` allows all crawlers
- Auto-generated `sitemap.xml`
- "Is it normal" / "What to expect" / "Signs of" phrasing in H2 headers
- Clean semantic HTML — no JS-heavy rendering
- Direct-answer meta descriptions
