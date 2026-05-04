# CLAUDE.md — richnashawaty.com
> Read this file before every task.

## Project Location
`~/Desktop/ClaudeWork/Rich/`

## Hosting & Deploy
- **Domain:** richnashawaty.com (registered on Namecheap)
- **Host:** Hostinger
- **Nameservers:** Hostinger nameservers (set in Namecheap)
- **GitHub repo:** github.com/richn33-sys/richnashawaty
- **Deploy command (run on server after push):**
  ```bash
  cd ~/domains/richnashawaty.com/public_html && git fetch origin && git reset --hard origin/main
  ```
- **Full deploy workflow:**
  1. Make changes locally in `~/Desktop/ClaudeWork/Rich/`
  2. Run: `python3 ~/Desktop/ClaudeWork/Rich/deploy.py "describe what changed"`
  3. SSH in and run deploy command above
- **Note:** Use SSH force pull — same as AIToolGrade and MyDCACalc

## What This Project Is
Personal consulting website for Rich Nashawaty. Four-page site covering three service lanes — SEO & Web Design, AI Consulting, and Custom Tools & Builds. Built in pure HTML/CSS, no framework, no CMS.

## File Structure
```
~/Desktop/ClaudeWork/Rich/
├── index.html          ← Homepage (hero, proof of work, 3 lanes, about, CTA)
├── seo-web.html        ← SEO & Web Design service page
├── ai-consulting.html  ← AI Consulting service page
├── custom-tools.html   ← Custom Tools & Builds service page
├── deploy.py           ← Deploy script (local only, not pushed)
├── CLAUDE.md           ← This file (not pushed)
└── .gitignore          ← Ignores CLAUDE.md, deploy.py, .DS_Store
```

## Design System (CSS Variables)
All pages share these variables — never hardcode colors:
```css
--bg: #181816        /* page background */
--bg2: #201f1c       /* section/card background */
--bg3: #272521       /* deeper background */
--text: #f4f1ea      /* primary text */
--text2: #b8b4ac     /* secondary text */
--text3: #7a7672     /* muted/meta text */
--accent: #c8f060    /* brand yellow-green — CTAs, highlights */
--accent2: #a8d040   /* accent hover state */
--adim: rgba(200,240,96,0.08)
--adim2: rgba(200,240,96,0.14)
--border: rgba(255,255,255,0.10)
--border-h: rgba(255,255,255,0.18)
```

## Typography
```css
--serif: 'Instrument Serif', serif    /* headings, logo, quotes */
--sans: 'DM Sans', sans-serif         /* body text, nav */
--mono: 'DM Mono', monospace          /* labels, badges, tags, meta */
```
Google Fonts link (include in every page head):
```html
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
```

## Contact & Branding
- **Email:** contact@richnashawaty.com
- **Name on site:** Rich Nashawaty
- **Tagline:** I build systems that grow your business and run without you.
- **SEO experience:** 20 years — freelance (White Mountain Process 2006–2010), agency (Catalyst, 451 Marketing, Charles River Interactive 2010–2016), enterprise in-house (Kayak, Monster, Ziff Davis, Care.com 2016–present)
- **Key credentials:** 19 languages / 11 global domains at Monster, Director of SEO at Ziff Davis, $750k revenue built from zero

## Nav Structure (all pages must stay in sync)
```
Rich Nashawaty.    SEO & Web    AI Consulting    Custom Tools    [Let's Talk CTA]
```
### href patterns by file location (all files are at root level)
- All internal links use flat paths: `href="index.html"`, `href="seo-web.html"`, etc.

## Page Summary
| File | Purpose | Key Sections |
|------|---------|--------------|
| `index.html` | Homepage | Hero, stats bar, positioning statement, proof of work (6 cards), 3 service lanes, about, CTA |
| `seo-web.html` | SEO & Web | Hero, cred strip, career arc (3 stages), services (4), tools list, website types, process, CTA |
| `ai-consulting.html` | AI Consulting | Hero, honest note, problem/solution, 3 offerings, audience, process, CTA |
| `custom-tools.html` | Custom Tools | Hero, 4 live builds (with LIVE badges), 6 build categories, philosophy, process, CTA |

## Proof of Work (for copy reference)
1. **Stock Trading Bot** — Python, Yahoo Finance, RSI/MACD/Bollinger, DIP+MOMENTUM strategies, Flask dashboard, macOS daemon
2. **Crypto Trading Bot** — Python, CoinGecko API, news sentiment, launchd, Gmail alerts, BTC/ETH/SOL/AVAX
3. **YouTube Video Pipeline** — n8n + Claude API + ElevenLabs, MWF schedule, auto-upload
4. **AIToolGrade.com** — 16 reviews, 6 categories, blog, Google indexed
5. **MyDCACalc.com** — 3 calculators, 4 guides, automated content pipeline
6. **Shopify Store** — hands-off e-commerce, automation-first

## SEO Tools (for copy reference)
Botify, Screaming Frog, SEMrush, Ahrefs, Sitebulb, Lumar (Deepcrawl), Google Search Console, GA4, Jira, Asana

## Coding Conventions
- **No JavaScript frameworks** — vanilla HTML/CSS only
- **No external CSS files** — all styles are inline `<style>` blocks per page
- **No separate JS files** — any JS is inline `<script>` at bottom of body
- **Self-contained pages** — each page has its full nav, styles, and footer
- Mobile breakpoint at `900px` (grid collapses) and `640px` (nav collapses)
- Nav is sticky with `backdrop-filter: blur(18px)`

## Do NOT Touch Without Asking
- CSS variable names — changing them breaks all pages
- Nav structure — always update ALL pages when changing nav
- Email address — currently `contact@richnashawaty.com` across all pages
- Color palette — defined above, do not hardcode

## Updating All Pages (Python pattern for nav/footer changes)
```python
import os

files = ['index.html', 'seo-web.html', 'ai-consulting.html', 'custom-tools.html']
base = os.path.expanduser('~/Desktop/Rich')

for fname in files:
    path = os.path.join(base, fname)
    content = open(path).read()
    content = content.replace('OLD_STRING', 'NEW_STRING')
    open(path, 'w').write(content)
    print(f"Updated {fname}")
```

## Deploy Workflow
```bash
# From ~/Desktop/ClaudeWork/Rich/
python3 deploy.py "your commit message here"
# Then SSH into Hostinger and run the force pull
```

## What to Build Next
- [ ] Set up contact@richnashawaty.com mailbox in Hostinger
- [ ] Connect Calendly to "Book a Free Strategy Call" buttons
- [ ] Add Google Search Console verification once live
- [ ] Submit sitemap.xml (create once live)
- [ ] LinkedIn profile update linking to site
