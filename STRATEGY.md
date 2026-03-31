# Age Expectations — Monetization & Growth Strategy

_Owner: Jarvis | Started: 2026-03-31_
_Goal: Generate revenue from ageexpectations.com_

## Current State (Mar 31, 2026)
- **91 pages** across 16 age brackets (0-18 years)
- **AEO-optimized** — answer-first format, JSON-LD schema, FAQ sections
- **Instagram** — @ageexpectations, 66 queued posts, 13 confirmed posted
- **Pinterest** — Pins generated but NOT auto-posted
- **Revenue: $0** — No monetization in place
- **Analytics: None** — No traffic data whatsoever

## Phase 1: Foundation (Week 1-2) — CURRENT
_Get data, get traffic flowing, set up basic monetization_

### 1.1 Analytics (BLOCKER: needs Erik)
- [ ] **Erik task:** Add Google Analytics 4 (GA4) to the site
  - Create GA4 property for ageexpectations.com
  - Give Jarvis the Measurement ID (G-XXXXXXX)
  - OR: Enable Cloudflare Web Analytics if on CF Pages
- [ ] Add GA4 snippet to Astro layout once we have the ID

### 1.2 Content Growth (Jarvis can do autonomously)
- [ ] Continue nightly content generation (target: 120 pages by end of April)
- [ ] Priority gaps: 5-6 years (sleep, behavior, milestones), teen mental health, learning disabilities
- [ ] Each new article = 1 Instagram post + 1 Pinterest pin

### 1.3 SEO & Traffic
- [ ] Submit sitemap to Google Search Console
  - **Erik task:** Verify ageexpectations.com in Google Search Console, share access
- [ ] Create /sitemap.xml if not already present
- [ ] Verify all pages have proper meta descriptions, canonical URLs

### 1.4 Pinterest Automation
- [ ] Build Pinterest API posting script (or use RSS-to-Pinterest via Tailwind/Buffer)
  - **Erik task:** Set up Pinterest Business account if not done, get API credentials
- [ ] Auto-post pins for all new and existing articles

### 1.5 Basic Monetization — Google AdSense
- [ ] **Erik task:** Apply for Google AdSense (needs manual account creation + site review)
- [ ] Once approved: Add ad units to article pages (sidebar + in-content)
- [ ] Expected: $2-10/day initially with modest traffic, grows with content

## Phase 2: Growth (Week 3-6)
_Scale traffic, add affiliate revenue_

### 2.1 Affiliate Links
- [ ] Amazon Associates — link to recommended parenting books, baby products, developmental toys per age
- [ ] **Erik task:** Sign up for Amazon Associates (needs manual application)
- [ ] Add "Recommended Resources" sections to existing articles
- [ ] Target: $50-200/month from affiliate links once traffic is 5k+/month

### 2.2 Content Depth
- [ ] Add printable milestone checklists per age (PDF downloads)
- [ ] Add "compare ages" feature (what's normal at 3 vs 4)
- [ ] Target 150+ pages by end of Phase 2

### 2.3 Email List
- [ ] Add email signup (free age-specific milestone guide as lead magnet)
- [ ] **Erik task:** Set up Mailchimp/ConvertKit free account
- [ ] Weekly parenting tips email (automated from new content)

### 2.4 Social Growth
- [ ] Instagram: increase to 2-3 posts/day, add Reels
- [ ] Pinterest: 5-10 pins/day (repins + new content)
- [ ] Consider TikTok clips from article summaries

## Phase 3: Scale (Month 2-3)
_Premium features, higher RPM ads_

### 3.1 Premium Ad Networks
- [ ] Once at 10k sessions/month: Apply to Mediavine or Raptive (much higher RPM than AdSense)
- [ ] Target: $15-50 RPM vs AdSense $2-5 RPM

### 3.2 Digital Products
- [ ] Downloadable age-specific development guides (PDF, $4.99)
- [ ] "What to Expect" style comprehensive guides per year
- [ ] Gumroad or Lemon Squeezy for payments (no Erik infrastructure needed)

### 3.3 Sponsored Content
- [ ] Once traffic is 10k+/month, reach out to parenting brands
- [ ] Baby product reviews, pediatrician-recommended tools
- [ ] Target: $200-500 per sponsored post

## Revenue Projections (Conservative)
| Timeframe | Traffic | Revenue Source | Est. Monthly |
|-----------|---------|---------------|-------------|
| Month 1 | 500-2k | AdSense | $5-30 |
| Month 2 | 2k-5k | AdSense + Affiliates | $30-150 |
| Month 3 | 5k-15k | Better ads + Affiliates + Digital | $150-500 |
| Month 6 | 15k-50k | Mediavine + Affiliates + Products | $500-2000 |

## Daily Routine (Jarvis)
1. **Content:** Generate 1-2 new articles targeting high-value gaps
2. **Social:** Post to Instagram, queue Pinterest pins
3. **SEO:** Monitor Search Console (once set up), optimize underperforming pages
4. **Monetization:** Implement next monetization item on the list
5. **Report:** Track progress in daily log below

---

## Daily Log

### 2026-03-31
- Created strategy document
- Set up daily review cron
- **Erik tasks identified (see Phase 1.1, 1.3, 1.5)**

---

## Erik's Task Queue
_Things only Erik can do (needs human accounts/approvals):_

1. **GA4 Setup** — Create property, share Measurement ID
2. **Google Search Console** — Verify site, share access
3. **Google AdSense** — Apply for account (biggest revenue unlocker)
4. **Amazon Associates** — Sign up for affiliate program
5. **Pinterest Business** — Set up account + API credentials (if not done)
6. **Email Service** — Create free Mailchimp/ConvertKit account
