# $500 Website Postcard Campaign — Start to Finish

## Overview

A direct mail postcard campaign targeting local businesses without websites. Offer: $500 flat-rate one-page website, live in 7 days, no monthly fees. QR code drives to `richnashawaty.com/simple-website`.

---

## Files

| File | Location | Notes |
|------|----------|-------|
| Lead list | `postcard-leads.csv` | 95 confirmed leads, MA + southern NH |
| Landing page | `richnashawaty.com/simple-website` | QR destination — deployed |
| Demo sites | `middlesex-electric-demo.html`, `stonepath-landscaping-demo.html`, `westside-auto-demo.html` | Live on site as sample screenshots |
| Postcard copy | See below | Version A (personalized) ready |

---

## Step 1 — Scrape More Leads (Optional)

If you want to build the list beyond 95 before mailing, reconnect the Chrome browser and continue scraping Google Maps.

**How to reconnect browser:**
1. Open Brave/Chrome with the Claude extension
2. In Claude chat, ask to connect browser
3. Select "I'm Main" when prompted

**Scraping method:**
- Search: `[category] [town] [state]` on Google Maps
- JavaScript extracts listings and checks for website button
- For no-website hits, pull phone + address from GBP listing
- Add to `postcard-leads.csv`

**Categories that yield best results:** handyman, landscaping, auto repair, painting, fencing, carpet cleaning

**Towns covered so far (MA):** Newton, Lexington, Needham, Billerica, Burlington, Framingham, Chelmsford, Woburn, Lowell, Dracut, Tewksbury, Natick, Marlborough, Andover, North Andover, Methuen, Haverhill, Reading

**Towns covered so far (NH):** Nashua, Manchester, Salem, Derry, Hudson

---

## Step 2 — Clean the Lead List

Open `postcard-leads.csv` in Google Sheets or Excel.

1. **Filter `Has Full Address = No`** — look up missing addresses via:
   - MA businesses: [corp.sec.state.ma.us](https://corp.sec.state.ma.us) — search by business name
   - NH businesses: [sos.nh.gov](https://sos.nh.gov) — search business name
2. **Remove duplicates** — same business appearing under multiple towns
3. **Verify still no website** — spot check 10-15 listings before mailing; some may have built one since scraping

---

## Step 3 — Generate QR Code

1. Go to [qr-code-generator.com](https://qr-code-generator.com) (free)
2. URL: `https://richnashawaty.com/simple-website`
3. Download as **PNG, minimum 500x500px**
4. Save as `qr-code-simple-website.png`

---

## Step 4 — Design the Postcard

**Use Click2Mail's built-in Mailing Online Pro editor** (not Canva) — it handles mail merge natively.

**Size:** 4.25 x 6 inches (standard postcard rate)

### Front Copy

```
[BUSINESS NAME MAIL MERGE FIELD]
is on Google.

But you have no website.
That's costing you customers every day.

───────────────────────────────
A professional website for $500.
Live in 7 days. No monthly fees.
───────────────────────────────

[QR CODE IMAGE]
Scan to see examples →
richnashawaty.com/simple-website
```

**Design notes:**
- Business name in large bold type at top — this is the hook
- Dark background with accent color (match your site's navy/yellow or charcoal/red demo palette)
- QR code bottom right, large enough to scan
- Keep it sparse — trades business owners glance, not read

### Back Copy

```
What you get:

✓ One-page site built for your business
✓ Mobile-friendly, fast, and secure (HTTPS)
✓ Click-to-call button + contact form
✓ Your services, area, and reviews
✓ Live in 7 days — you own it outright
✓ No monthly fees. Ever.

Additional pages available at $150 each.
Hosting ~$100/year paid direct — no markup.

─────────────────────────────────────────

Rich Nashawaty
contact@richnashawaty.com
richnashawaty.com

[ADDRESS BLOCK — auto-filled by Click2Mail]
```

---

## Step 5 — Set Up Click2Mail

1. Go to [click2mail.com](https://click2mail.com) — create a free account
2. Click **"Send a Postcard"**
3. Choose **4.25 x 6 Postcard** format
4. Select **"Mailing Online Pro"** editor (supports mail merge)

### Upload Your Mailing List First
1. Go to **Mailing Lists → Upload List**
2. Upload `postcard-leads.csv`
3. Map columns:
   - `Business Name` → Name / Company
   - `Address` → Street Address
   - `Town` → City
   - `State` → State
   - Leave ZIP blank if not in CSV (Click2Mail will flag missing ones)

### Design in Their Editor
1. Create a two-page document (front + back)
2. Build front layout with text boxes and image box for QR code
3. Where you want the business name: click **Insert → Merge Field → Business Name**
4. This inserts a `{{Business_Name}}` token — prints the actual name for each card
5. Upload your QR code PNG into the image box
6. Back page: add your copy text + leave address area for auto-fill

### Preview
- Click **Preview** — cycles through real records from your CSV
- Verify business name is pulling correctly
- Verify address block is formatted properly

---

## Step 6 — Proof and Order

1. **Proof carefully** — check 5-10 different records in preview
2. Select **Next Day** production if you want fast turnaround
3. Select **First Class** postage for best deliverability
4. **Pay** — estimated ~$0.64/card × 95 cards = ~$61 total

Click2Mail prints and mails by next business day.

---

## Step 7 — Track Responses

Use the outreach tracker widget (built in Claude chat) or a simple Google Sheet:

| Column | What to track |
|--------|--------------|
| Business Name | From lead list |
| Mailed Date | When cards went out |
| Response | Call / QR scan / email |
| Status | Queue / Mailed / Responded / Sold / No response |
| Notes | Owner name, what they said |

**Follow-up call script (10 days after mailing):**

> "Hi, this is Rich Nashawaty — I sent you a postcard recently about building a website for [Business Name]. I noticed you're showing up on Google but don't have a site, and I wanted to see if that's something you've been thinking about. I build one-page sites for local businesses for $500 flat, live in 7 days. Do you have 5 minutes?"

---

## Step 8 — Deliver the Website

Once a client says yes:

1. **Collect:** business name, phone, services list, service area, any photos, Google Business Profile URL (for reviews)
2. **Build:** use the demo sites as templates — swap name, colors, services, photos
3. **Preview:** send them a link to review before going live
4. **Launch:** help them set up Hostinger hosting (~$100/year) and point their domain
5. **Upsell conversation:** "Now that you have a site, local SEO is the next step. Here's what that looks like..."

---

## Pricing Reference

| Item | Cost |
|------|------|
| Click2Mail (95 cards, postage included) | ~$61 |
| QR code generator | Free |
| Postcard design (Click2Mail editor) | Free |
| **Total campaign cost** | **~$61** |
| **Revenue from one client** | **$500** |
| **ROI on first client** | **720%** |

---

## Notes

- **PostcardMania minimum is 1,000** — not cost-effective for targeted lists under 200
- **Vistaprint alternative** — print-only, you stamp and mail manually. ~$35 print + ~$50 postage = $85 for 95 cards
- **Version A postcard** (personalized with business name) will outperform generic copy — the hook is seeing their own business name on the card
- **Best response categories based on scraping:** handyman and auto repair had highest no-website rate; landscapers second
- **NH leads** — postage and delivery same as MA via USPS First Class
