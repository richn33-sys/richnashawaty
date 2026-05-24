# SEO Service System — Context & Planning

**Source:** Sarvesh Shrivastava "Top 20 Claude Prompts for SEO" (Alventra Marketing). Reviewed, de-hyped, and adapted into a usable system for richnashawaty.com's local SEO offering.

**Purpose of this doc:** working context for the SEO business thread — what the source was, what's worth keeping, how it maps to our funnel, and what to build next.

---

## TL;DR

The source article is engagement-bait wrapping competent, widely-known local SEO. The framing ("the 90% nobody uses," "secrets agencies don't know") is false scarcity and a funnel to the author's agency. **But the underlying tactics are mostly sound** and map cleanly onto what we already do: local SEO + web builds for trades businesses (HVAC, plumbing, landscaping, auto repair) in Middlesex County, MA.

We extracted the substance into a 4-phase audit system and a client-facing audit bundle. See the two companion files:
- `local-seo-audit-checklist.md` — the full internal working system (all 4 phases, 20 tactics)
- `local-seo-audit-one-pager.md` — client-facing sales sheet for the Phase 1 + citations bundle

---

## What's genuinely valuable (keep)

- **GBP competitive teardown** — pull competitor categories, attributes, review velocity, posting cadence, service descriptions into comparison sheets, act on gaps. Core of the offering.
- **Review velocity > raw count** — correct and underused. A listing earning 15/month beats one sitting on 200 old reviews.
- **GSC page-2 keywords (positions 11–20)** — highest-ROI tactic in the whole list. Demand already exists; one optimization push from visibility.
- **NAP / citation consistency** — bread-and-butter, results often within ~30 days.
- **Service + city page architecture** — Google ranks pages not sites; no page for [service]+[city] = no ranking for it.
- **Review-sentiment → copy** — writing client copy in customers' actual language. Real CRO.

## What's oversold (discount)

- **Entity / knowledge-graph optimization (#18)** — pitched as "the moat." For a small HVAC company, Wikipedia eligibility and knowledge panels are mostly unreachable. Only the LocalBusiness JSON-LD schema actually does work. Keep the schema, drop the hype.
- **"See changes in days," "outrank established businesses in 90 days, watched it happen dozens of times"** — unfalsifiable, no data. Never repeat to clients.
- **"Most agencies/SEOs don't know this exists"** (review sentiment, entity) — both are standard. The scarcity claim is the tell.
- **The 42% / 35% photo stat** — old, poorly-sourced Google figure. Do not put in any client-facing material.

---

## The system (4 phases, condensed)

Full detail in `local-seo-audit-checklist.md`. Summary:

1. **Phase 1 — GBP (prompts 1–8):** categories, attributes, review velocity, review responses, posts, services, description, photos. Highest immediate impact.
2. **Phase 2 — Website (9–13):** keyword gap, money-page audit, service+city pages, GSC page-2 sprint, review-sentiment copy.
3. **Phase 3 — Backlinks/authority (14–16):** competitor backlinks, citation/NAP audit, search-intent mapping.
4. **Phase 4 — Content/tracking (17–20):** content gap, entity/schema, posting-pattern analysis, monthly report.

Tools required for parts of Phases 2–4: SEMrush, Ahrefs, GSC, GA4.

---

## How it maps to our funnel

Current funnel: **$400–500 flat website build → SEO retainer upsell.** This system slots in cleanly:

- **Lead magnet / entry product:** "Local SEO Audit" = Phase 1 + citation audit (#15). Fixed price, 5–7 day turnaround, produces tangible comparison spreadsheets. One-pager already drafted.
- **Retainer execution:** Phases 2–3 (page builds, citation fixes, link building, intent mapping) = the monthly work.
- **Retainer reporting:** Phase 4 #20 monthly report = the recurring deliverable that justifies the retainer and keeps reporting on calls, not vanity traffic.
- **Audit credits toward month 1** if they continue → low-friction path from audit to retainer.

---

## Operational notes / cautions

- **Tool access:** use client's own SEMrush/Ahrefs/GSC/GA4 accounts with permission; never share credentials in chat.
- **Scraping at volume:** repeated automated GBP/Maps scraping gets flaky, can hit rate limits and tool ToS. Pull deliberately. (Same lessons as the Chrome MCP work — `get_page_text` on a loaded tab, JS scroll for Maps ~5 results at a time, `web_fetch` markdown + low token limit for contact pages.)
- **No timeline promises** in any client material. Present as high-confidence improvements without committing to dates.
- **Productizing:** the comparison-spreadsheet format is what clients perceive as rigorous — lead with it in every deliverable.

---

## Next actions / open questions

- [ ] Set the audit price in the one-pager (`[$ — set your number]` placeholder).
- [ ] Add contact/booking link to the one-pager.
- [ ] Decide whether to build the audit as a templated process doc (repeatable per client) or keep it manual for the first few.
- [ ] Test the GBP teardown prompts against a real local competitor set to validate output quality before selling.
- [ ] Consider: which trades vertical to target first for the audit offer (HVAC list already compiled; landscapers + auto repair queued).
