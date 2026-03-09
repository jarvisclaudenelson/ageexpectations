# AgeExpectations.com Strategy

## Objective
Build a high-density, structured parenting resource optimized for **Answer Engine Optimization (AEO)** and LLM ingestion (Perplexity, SearchGPT, Gemini).

## Core Pillars

### 1. Vertical Depth (Month-by-Month)
- **Granular Windows:** Prioritize month-by-month content for 0–24 months, then 6-month windows until age 5, then yearly.
- **Precision Value:** Target precise queries (e.g., "14-month-old feeding") over general categories ("toddler feeding").

### 2. AEO Architecture
- **Schema.org Dominance:** Every page must include `Article`, `FAQPage`, and `Milestone` schemas.
- **Key Takeaways:** Every article begins with a concise "Bottom Line" block for rapid scraping/snippets.
- **Fact-First Tone:** Zero fluff/intro filler. Start with data and expert-backed advice.

### 3. The Topic Grid (Standardized Linking)
Standard sub-pages for every age:
- **Overview** (The general pulse)
- **Sleep** (Patterns and regressions)
- **Feeding** (Transitions and nutrition)
- **Health** (Safety, vitals, red flags)
- **Language/Social** (Communication)
- **Play** (Age-appropriate activities)

### 4. Interactive Utility
- **Calculators:** Precise age-based prediction tools (e.g., "Next expected regression").
- **Checklists:** Actionable audits (e.g., "9-Month Babyproofing").

### 5. Automated Consistency
- **Daily Build:** Three articles per day via cron `age-expectations-content` (2:30 AM, 10:30 AM, 6:30 PM CT).
- **Bulk Ramps:** Periodic manual bulk runs to fill skeleton categories.
- **Gap Analysis:** Ongoing scans of the `src/pages/ages/` directory to prioritize missing content.

---
*Created: March 9, 2026*
