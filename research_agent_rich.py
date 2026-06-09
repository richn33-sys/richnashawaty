#!/usr/bin/env python3
"""
Content Research Agent — richnashawaty.com
Runs weekly via launchd — emails a structured research brief every Monday at 8am.

Run manually to test:
    python3 research_agent_rich.py

See SKILL.md for full setup instructions.
"""

import sys
import smtplib
import os
from pathlib import Path
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import anthropic

sys.path.insert(0, str(Path(__file__).parent))
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

# ─────────────────────────────────────────────
# CONFIGURATION — update as site grows
# ─────────────────────────────────────────────

SITE_NAME = "richnashawaty.com"
SITE_DESCRIPTION = "an SEO consulting and AI automation site for small businesses in Boston and Greater New England, run by Rich Nashawaty — 20 years experience, former Director of SEO at Ziff Davis, Monster, Kayak, and Care.com"
SITE_NICHE = "SEO consulting, local SEO Boston, AI consulting small business, marketing automation, technical SEO, web design Boston"

# Blog posts already published — agent won't re-suggest these
CURRENT_GUIDES = [
    # Blog posts (15 live)
    "What Does an SEO Consultant Actually Do?",
    "How Much Does an SEO Consultant Cost in Boston?",
    "Why Isn't My Boston Business Ranking on Google?",
    "What Is GEO (Generative Engine Optimization)? A Plain-English Guide for Boston Business Owners",
    "How Much Does AI Automation Cost for Small Business?",
    "Questions to Ask Before Hiring an SEO Consultant in Boston",
    "Boston Neighborhood SEO: How to Rank in Back Bay, Seaport & Beyond",
    "How to Get Cited in AI Overviews: A Boston Business Owner's Guide",
    "Best AI Tools for Small Business Marketing in 2026",
    "How Much Does Local SEO Cost in Boston?",
    "SEO vs. DIY: When to Hire an SEO Consultant vs. Do It Yourself",
    "How to Measure SEO ROI for Your Small Business (2026 Guide)",
    "Technical SEO Audit Checklist for Small Businesses (2026)",
    "SEO vs. GEO vs. AEO: What Boston Business Owners Actually Need to Know",
    "Do You Need a Fractional AI Officer? A Guide for Small Businesses (2026)",
    # Service pages
    "Local SEO Audit ($497) — service page",
    "SEO & Web — service page",
    "AI Consulting — service page",
    "Custom Tools — service page",
    "GEO / AI Search Visibility — service page",
    "Fractional AI Consulting — service page",
    "Cambridge MA SEO — landing page",
    "Route 128 Corridor SEO — landing page",
    "Remote SEO Consultant — landing page",
    "$500 Website Offer — landing page",
    # Free tools
    "AI Automation ROI Calculator — free tool",
    "SEO Audit Checklist — free lead magnet",
]

# Tools and resources already live
CURRENT_TOOLS = [
    "SEO competitor research CLI tool (seo_research.py)",
]

# Boston-area SEO competitors to monitor weekly
COMPETITORS = [
    "natefishmandigital.com",
    "bostonseoconsultants.com",
    "richsanger.com",
    "jhseoagency.com",
    "brickmarketing.com",
    "coalitiontechnologies.com",
]

# Communities where the target audience hangs out
COMMUNITIES = [
    "r/SEO",
    "r/smallbusiness",
    "r/marketing",
    "r/bigseo",
    "r/Entrepreneur",
    "r/bostonsocialclub",
]

# Email branding
BRAND_COLOR = "#c8f060"
BRAND_NAME = "Rich Nashawaty"

# ─────────────────────────────────────────────
# EMAIL CREDENTIALS — set in .env file
# ─────────────────────────────────────────────

GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
ALERT_EMAIL = os.getenv("ALERT_EMAIL")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# ─────────────────────────────────────────────
# CORE LOGIC — no need to edit below this line
# ─────────────────────────────────────────────

def send_email(subject, html_body):
    """Send HTML email via Gmail SMTP."""
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = GMAIL_USER
    msg["To"] = ALERT_EMAIL
    msg.attach(MIMEText(html_body, "html"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.sendmail(GMAIL_USER, ALERT_EMAIL, msg.as_string())


def run_research():
    """Run the research agent and send the weekly brief."""
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    today = datetime.now().strftime("%B %d, %Y")
    current_guides_list = ", ".join(CURRENT_GUIDES)
    current_tools_list = ", ".join(CURRENT_TOOLS)
    competitor_list = ", ".join(COMPETITORS)
    community_list = ", ".join(COMMUNITIES)

    prompt = f"""You are a content research agent for {SITE_NAME} — {SITE_DESCRIPTION}.
Today is {today}.

Already published blog posts: {current_guides_list}
Already live tools and resources: {current_tools_list}

Using web search, research the following and produce a structured weekly brief:

1. NEW BLOG POST IDEAS WORTH WRITING
   - Search for trending questions small business owners and entrepreneurs in Boston and Greater New England are asking right now about: {SITE_NICHE}
   - Identify 3-5 blog topics NOT already covered in the published posts above
   - For each: proposed title, target keyword, why it's timely or valuable, estimated search demand, priority (HIGH/MEDIUM/LOW)
   - Flag anything with urgent news-driven timing (Google algorithm updates, AI news, local Boston business news)
   - Prioritize bottom-funnel topics where someone is close to hiring an SEO consultant or AI consultant

2. NEW SERVICE OR CONTENT OPPORTUNITIES
   - Search for service gaps or content formats that Boston-area SEO and AI consultants are not covering well
   - Identify 2-3 ideas for new service pages, landing pages, case study formats, or lead magnets
   - For each: idea, target keyword, estimated demand, why it differentiates from competitors

3. TRENDING TOPICS & KEYWORDS
   - Search for trending SEO, AI, and small business marketing topics this week
   - Identify 3-5 high-opportunity content angles with strong search intent
   - Flag anything that needs to be published THIS WEEK before the moment passes
   - Pay special attention to: Google algorithm updates, AI tool announcements, local Boston business news

4. COMPETITOR ACTIVITY
   - Search for recent content published by: {competitor_list}
   - Note topics or angles they are covering that {SITE_NAME} is not
   - Flag any content gaps worth closing quickly
   - Note if any competitor is ranking well for a keyword that Rich could realistically target

5. COMMUNITY SENTIMENT
   - Search {community_list} for hot discussions this week about SEO, AI consulting, small business marketing
   - Surface recurring questions or pain points that a blog post could solve
   - Note any questions about hiring SEO consultants, AI automation costs, or local Boston business marketing

Format your response as clean HTML for an email brief. Use clear section headers, bullet points, and priority labels (HIGH/MEDIUM/LOW).
Be specific and actionable.

Be concise — use bullet points only, no paragraphs. Max 2 sentences per item.

Focus on evergreen content only — topics relevant 12 months from now. Skip news-driven or time-sensitive items.

Limit output to exactly 3 sections:
1. BLOG POST IDEAS — 3 ideas maximum
2. SERVICE/CONTENT OPPORTUNITIES — 2 ideas maximum
3. COMPETITOR ACTIVITY — 3 items maximum

Always finish each item completely. If approaching the limit, stop after the current item — never cut off mid-sentence. — every item should tell Rich exactly what to write next, with the target keyword, why it matters, and enough context to act on it immediately.
Write in a direct, professional tone — no fluff.
"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1500,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        messages=[{"role": "user", "content": prompt}]
    )

    brief_html = ""
    for block in message.content:
        if hasattr(block, "text"):
            brief_html += block.text

    email_html = f"""
    <html>
    <body style="font-family: 'Arial', sans-serif; max-width: 700px; margin: 0 auto; padding: 20px; background: #f4f1ea;">
      <div style="background: #181816; padding: 24px 28px; border-radius: 10px; margin-bottom: 24px; border-left: 4px solid {BRAND_COLOR};">
        <h1 style="color: {BRAND_COLOR}; font-family: monospace; margin: 0 0 4px; font-size: 18px;">{BRAND_NAME}<span style="color:{BRAND_COLOR}">.</span></h1>
        <p style="color: #7a7672; font-family: monospace; font-size: 12px; margin: 0;">Weekly Research Brief — {today}</p>
      </div>
      <div style="background: white; padding: 28px; border-radius: 10px; border: 1px solid #e2e0d8;">
        {brief_html}
      </div>
      <hr style="border-color: #e2e0d8; margin: 24px 0 12px;">
      <p style="color: #b8b4ac; font-size: 11px; font-family: monospace;">Generated by Content Research Agent · richnashawaty.com</p>
    </body>
    </html>
    """

    send_email(f"📊 richnashawaty.com Weekly Research Brief — {today}", email_html)
    print(f"✓ Research brief sent successfully — {today}")


if __name__ == "__main__":
    try:
        run_research()
    except Exception as e:
        print(f"Error: {e}")
        try:
            send_email(
                f"⚠️ richnashawaty.com Research Agent Error",
                f"<p>Research agent failed on {datetime.now().strftime('%B %d, %Y')} with error:</p><pre>{str(e)}</pre>"
            )
        except Exception as email_err:
            print(f"Also failed to send error email: {email_err}")
