# Build Tickets — GBP Cluster (P1 #2)
richnashawaty.com · June 28, 2026

> **Reframe (important):** The GBP *pillar post already exists* — Post 23, `blog/google-business-profile-optimization-checklist-boston.html` (June 19). Do **not** build a second one. The cluster's real gaps are a **service page** and a **lead magnet**; Post 23 becomes the hub that funnels into both. Three tickets below + one maintenance fix.

**Audience framing (applies to the WHOLE cluster — added per Rich, June 28):**
Assume the reader does **not** know what a Google Business Profile is. Every GBP page/post opens in plain English: one sentence defining it (*"the free listing that shows up on Google Maps and in the panel beside search results when someone looks up your business"*), note it was formerly called **Google My Business**, and lead with **why it matters** before any tactics. No jargon-first, no acronym-first. ⚠️ Post 23 ("…Optimization Checklist…") currently assumes the reader already knows the term — that awareness gap is what **Ticket 0** below fills.

**Shared build rules (apply to all tickets):**
- Clone an existing similar page; never start from blank. Use the design-system CSS vars (`--bg`, `--accent` #c8f060, etc.) — never hardcode colors.
- Nav: add only `<div id="nav-root"></div>` + the nav.js `<script>`. No hardcoded nav/hamburger CSS or markup (nav.js injects it). Include the toggle JS before `</body>`.
- Fonts: async load pattern (Instrument Serif / DM Sans / DM Mono).
- GA4 tag + canonical + OG tags on every page.
- After build: validate HTML, confirm GA4 tag present, confirm nav.js reference, check internal links resolve.
- Deploy: `deploy-rich "message"`. Add new root pages to `sitemap.xml` manually (only blog posts use `new_post.py`). **Also fix the existing sitemap gap: `how-to-vet-seo-consultant.html` is missing.**
- Skill to run post-build: `geo-audit` skill on the new service page (extractability + citation surface).

---

## TICKET 0 (optional, top-of-funnel) — "What Is a Google Business Profile?" awareness post
**Status:** NEW blog post. The entry spoke for the SMB who doesn't know the term — catches a reader the rest of the cluster skips.
**File:** `blog/what-is-google-business-profile-boston-business.html`
**Primary keyword:** `what is a google business profile` · **Secondary:** `do i need a google business profile`, `google my business vs google business profile`, `google business profile for small business`
**Clone from:** any recent explainer post (e.g. `blog/what-is-geo-generative-engine-optimization-boston.html` — same plain-English "what is X" shape).

**Outline:**
1. Plain-English definition — what a GBP is, in one sentence, no acronyms. Note the GMB→GBP rename so older readers connect the dots.
2. Where it shows up — Maps, the Local Pack, the right-hand panel. Screenshot-style description.
3. Why it matters for a Boston SMB — free, most-viewed asset, drives calls/directions; 80%+ of local searches trigger a map pack.
4. "Do you even have one?" — how to check if a profile exists / is claimed.
5. Soft next step → the optimization checklist (Post 23) for "now that you have one, here's how to win."

**Schema:** `FAQPage`, `BreadcrumbList`.
**Internal links — OUT:** → Post 23 (the checklist, "next step"), → `gbp-checklist.html` (lead magnet), → `../google-business-profile-optimization-boston.html` (service). 
**Internal links — IN:** add a link from Post 3 (`why-isnt-my-boston-business-ranking`) and Post 10 (`how-much-does-local-seo-cost-boston`).
**Funnel role:** awareness post (Ticket 0) → checklist post (Post 23) → service (Ticket 1) / lead magnet (Ticket 2). This is the missing top of the GBP funnel.

**Claude Code kickoff:**
```
Read CLAUDE.md at ~/Desktop/ClaudeWork/Rich/CLAUDE.md first.
TASK: Build awareness-stage blog post blog/what-is-google-business-profile-boston-business.html.
Clone the explainer shape of blog/what-is-geo-generative-engine-optimization-boston.html.
Audience: an SMB owner who does NOT know what a Google Business Profile is — define it plainly, note the Google My Business rename, lead with why it matters before any tactics.
Link out to Post 23 (checklist), gbp-checklist.html, and the GBP service page.
Run new_post.py to add the blog-index card + sitemap entry. Show diff before deploy.
```

---

## TICKET 1 — GBP Audit + Optimization service page  ⭐ build first (the real gap)
**Status:** NEW. No standalone GBP service exists today.
**File:** `google-business-profile-optimization-boston.html` (root level)
**Primary keyword:** `google business profile optimization boston` · **Secondary:** `gbp audit boston`, `google maps optimization boston service`
**Offer:** GBP Audit + Optimization, **$297–$497 one-time** (low-commitment entry point; most consultants bundle GBP into retainers — you don't). Step-up path to the $497 Local SEO Audit.
**Clone from:** `local-seo-audit.html` (closest structure: productized fixed-fee service page).

**Outline:**
1. Hero — "Google Business Profile Optimization for Boston Businesses" + one-time price + primary CTA (mailto contact).
2. The problem — GBP is the most-viewed asset a local business owns; 80%+ of local searches trigger a map pack; top-3 Local Pack captures the majority of clicks. Most owners get primary category wrong.
3. What's included — fixed-fee deliverables: primary/secondary category audit, services & attributes, photo/post cadence setup, review-velocity plan, neighborhood + MBTA proximity signals, AI-readiness for Maps summaries. (Mirror the "price includes" list style from local-seo-audit.html.)
4. Boston-specific angle — neighborhood/T-stop search behavior; tie to the Local Pack review thresholds.
5. Process + turnaround (e.g., 5–7 business days).
6. Who it's for / who it's not.
7. FAQ (FAQPage schema).
8. CTA band → contact + secondary link to $497 Local SEO Audit.

**Schema:** `Service` (with `offers` $297–497), `FAQPage`, `BreadcrumbList`.

**Internal links — OUT (from this page):**
- `local-seo-audit.html` (the $497 step-up)
- `blog/google-business-profile-optimization-checklist-boston.html` (Post 23 — "see the full 26-point checklist")
- `gbp-checklist.html` (Ticket 2 lead magnet — "grab the free checklist")
- `blog/boston-neighborhood-seo-back-bay-seaport.html` (Post 7)

**Internal links — IN (add a link TO this page from):**
- `seo-web.html` (services list, alongside Cambridge/Route 128)
- `local-seo-audit.html`
- `blog/google-business-profile-optimization-checklist-boston.html` (Post 23 — CTA box)
- `blog/why-isnt-my-boston-business-ranking-on-google.html` (Post 3)
- `blog/how-much-does-local-seo-cost-boston.html` (Post 10)
- `seo-cambridge-ma.html` + `seo-route-128-ma.html`

**Nav decision:** keep OUT of nav for now (like Cambridge/Fractional pages) — link from the local-SEO cluster. Promote to nav later if it converts.

**Claude Code kickoff:**
```
Read CLAUDE.md at ~/Desktop/ClaudeWork/Rich/CLAUDE.md first.
TASK: Build new service page google-business-profile-optimization-boston.html (root level).
Clone the structure/style of local-seo-audit.html. Offer: GBP Audit + Optimization, $297–$497 one-time.
Use the outline + internal-link map in this ticket. Add Service + FAQPage + BreadcrumbList schema.
Then add an inbound link to it from seo-web.html, local-seo-audit.html, seo-cambridge-ma.html, and seo-route-128-ma.html.
Add the page to sitemap.xml (and fix the missing how-to-vet-seo-consultant.html entry while there).
Run the geo-audit skill on the finished page. Do NOT deploy yet — show me the diff first.
```

---

## TICKET 2 — GBP checklist lead magnet (email-gated)
**Status:** NEW.
**Files (mirror the existing pattern exactly):** `gbp-checklist.html` (email-gate landing, indexable) + `gbp-checklist-full.html` (the full checklist, **noindex**, post-form destination).
**Clone from:** `seo-audit-checklist.html` + `seo-audit-checklist-full.html` (your existing lead-magnet pattern — Formspree email gate → full page).
**Primary keyword:** `google business profile checklist boston` · **Secondary:** `gbp checklist`, `local seo checklist boston`
**Content source:** lift the 26 items + Boston-specific angles (MBTA T-stop, neighborhood review thresholds, weekly-post cadence) straight from Post 23 — repackaged as a download, not rewritten.

**Outline (landing `gbp-checklist.html`):**
1. Hook — "The Boston GBP Checklist: the 26 things that actually move you into the Local Pack."
2. What they get + why it's Boston-specific (no competitor packages this).
3. Email gate (Formspree) → on submit, redirect to `gbp-checklist-full.html`.
4. Soft CTA to the $297–497 service ("want it done for you?").

**Full page (`gbp-checklist-full.html`, noindex):** the 26-item checklist + a closing CTA to Ticket 1 service and `local-seo-audit.html`.

**Optional upgrade:** also generate a branded **PDF** (`boston-gbp-checklist.pdf`) as a downloadable on the full page — use the `pdf` skill, site tokens (accent #c8f060 on #181816), reuse the RN logo. Nice-to-have; the HTML pattern ships without it.

**Schema:** none needed on the gate beyond standard; full page is noindex.

**Internal links — IN (add CTA boxes pointing to `gbp-checklist.html` from):**
- `blog/google-business-profile-optimization-checklist-boston.html` (Post 23 — primary driver)
- `local-seo-audit.html`, `seo-web.html`, and the Ticket 1 service page

**Internal links — OUT:** full page → Ticket 1 service + `local-seo-audit.html`.

**Claude Code kickoff:**
```
Read CLAUDE.md at ~/Desktop/ClaudeWork/Rich/CLAUDE.md first.
TASK: Build a GBP checklist lead magnet mirroring seo-audit-checklist.html + seo-audit-checklist-full.html.
Create gbp-checklist.html (indexable email-gate landing, Formspree) and gbp-checklist-full.html (noindex destination).
Pull the 26 checklist items + Boston angles from blog/google-business-profile-optimization-checklist-boston.html — repackage, don't rewrite.
Add inbound CTA boxes from Post 23, local-seo-audit.html, and seo-web.html.
Add gbp-checklist.html to sitemap.xml (NOT the -full page — it's noindex). Show me the diff before deploy.
```

---

## TICKET 3 — Wire Post 23 as the cluster hub (edit, not a build)
**Status:** EDIT existing file. Small, do it alongside Tickets 1–2.
**File:** `blog/google-business-profile-optimization-checklist-boston.html`
**Action:** add two outbound links it doesn't have yet:
- → `../google-business-profile-optimization-boston.html` (Ticket 1 service — "want this done for you?")
- → `../gbp-checklist.html` (Ticket 2 — "download the checklist")
It already links to `local-seo-audit.html`, the neighborhood post, and `seo-cambridge-ma.html` — leave those. Goal: Post 23 ranks/earns the organic traffic, then funnels readers to the service + lead magnet.

**Claude Code kickoff:**
```
Read CLAUDE.md at ~/Desktop/ClaudeWork/Rich/CLAUDE.md first.
TASK: Edit blog/google-business-profile-optimization-checklist-boston.html — add two CTA links: one to ../google-business-profile-optimization-boston.html (service) and one to ../gbp-checklist.html (lead magnet). Keep existing links. Show diff.
```

---

## MAINTENANCE FIX (do this so the agent stops re-suggesting existing posts)
Update `CURRENT_GUIDES` in `~/rich-research/research_agent_rich.py` — it's missing recent posts (16–24), which is why Sunday's brief re-pitched the existing GBP post. Add at minimum the GBP checklist (Post 23) and all titles through Post 24.

**Claude Code kickoff:**
```
Read CLAUDE.md at ~/Desktop/ClaudeWork/Rich/CLAUDE.md first.
TASK: Update CURRENT_GUIDES in ~/rich-research/research_agent_rich.py to include all published blog titles through Post 24 (notably the GBP Optimization Checklist and SEO Budget posts). This stops the weekly agent from re-suggesting topics that already exist.
```

---

### Suggested execution order
Ticket 1 (service) → Ticket 2 (lead magnet) → Ticket 3 (5-min hub wiring) → maintenance fix. Then one `deploy-rich "GBP cluster: service page + lead magnet + hub links"`, verify live, and run the geo-audit skill on the service page.

**Next up (say the word):** same ticket treatment for P1 #1 (Consultant vs Agency post — pending your un-defer decision) and P1 #3 (AI Readiness tool + post).
