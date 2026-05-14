#!/usr/bin/env python3
"""
SEO Competitor Research Tool
Usage: python3 seo_research.py "your keyword here"
Analyzes competitor title tags and generates blog topic ideas.
"""

import sys
import json
import os
import anthropic
from datetime import datetime

def run_research(keyword: str):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set.")
        print("Run: export ANTHROPIC_API_KEY=your_key_here")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    print(f"\n{'='*60}")
    print(f"  SEO COMPETITOR RESEARCH")
    print(f"  Keyword: {keyword}")
    print(f"  {datetime.now().strftime('%B %d, %Y %I:%M %p')}")
    print(f"{'='*60}\n")
    print("Searching the web and analyzing competitors...\n")

    prompt = f"""You are an SEO research analyst. Use web search to find and analyze the top 8-10 pages currently ranking for the keyword: "{keyword}"

For each ranking page:
1. Find the actual title tag
2. Note the domain
3. Count the characters
4. Identify keywords and modifiers used

Then provide a complete analysis. Respond ONLY with a valid JSON object — no markdown, no backticks, no extra text before or after. Use this exact structure:

{{
  "keyword": "{keyword}",
  "titles": [
    {{
      "rank": 1,
      "domain": "example.com",
      "title": "Full Title Tag Here",
      "char_count": 58,
      "keywords": ["keyword1", "keyword2"],
      "modifiers": ["modifier1", "modifier2"],
      "rating": "strong"
    }}
  ],
  "avg_char_count": 55,
  "common_keywords": ["kw1", "kw2", "kw3", "kw4", "kw5", "kw6", "kw7"],
  "missing_opportunities": ["gap1", "gap2", "gap3", "gap4"],
  "insights": [
    "Specific insight about title tag patterns",
    "Specific insight about keyword usage and placement",
    "Specific insight about length and structure",
    "Specific opportunity you could exploit"
  ],
  "recommended_title_formulas": [
    "Formula 1: [Primary KW] + [Modifier] + [Location] — [Benefit]",
    "Formula 2: [Action] + [Primary KW] + [Location] + [Credibility hook]",
    "Formula 3: [Number] + [KW] + [Promise]"
  ],
  "blog_topics": [
    {{ "title": "Blog Post Title", "type": "how-to", "target_kw": "target keyword", "rationale": "Why this would rank and convert" }},
    {{ "title": "Blog Post Title", "type": "listicle", "target_kw": "target keyword", "rationale": "Why this would rank and convert" }},
    {{ "title": "Blog Post Title", "type": "comparison", "target_kw": "target keyword", "rationale": "Why this would rank and convert" }},
    {{ "title": "Blog Post Title", "type": "guide", "target_kw": "target keyword", "rationale": "Why this would rank and convert" }},
    {{ "title": "Blog Post Title", "type": "question", "target_kw": "target keyword", "rationale": "Why this would rank and convert" }},
    {{ "title": "Blog Post Title", "type": "how-to", "target_kw": "target keyword", "rationale": "Why this would rank and convert" }},
    {{ "title": "Blog Post Title", "type": "listicle", "target_kw": "target keyword", "rationale": "Why this would rank and convert" }},
    {{ "title": "Blog Post Title", "type": "guide", "target_kw": "target keyword", "rationale": "Why this would rank and convert" }},
    {{ "title": "Blog Post Title", "type": "question", "target_kw": "target keyword", "rationale": "Why this would rank and convert" }},
    {{ "title": "Blog Post Title", "type": "comparison", "target_kw": "target keyword", "rationale": "Why this would rank and convert" }}
  ]
}}

Rating scale: "strong" = well optimized, "average" = decent, "weak" = poor.
Make all blog topics highly specific and useful for a consulting/service business targeting "{keyword}".
"""

    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=4000,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        messages=[{"role": "user", "content": prompt}]
    )

    # Extract the text block from the response
    text_block = None
    for block in response.content:
        if block.type == "text":
            text_block = block.text
            break

    if not text_block:
        print("ERROR: No text response received from API.")
        sys.exit(1)

    # Parse JSON
    raw = text_block.strip()
    # Strip any accidental markdown fences
    if "```" in raw:
        raw = raw.replace("```json", "").replace("```", "").strip()
    start = raw.find("{")
    end = raw.rfind("}") + 1
    if start == -1:
        print("ERROR: Could not parse JSON response.")
        print("Raw response:", raw[:500])
        sys.exit(1)
    raw = raw[start:end]

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"ERROR: JSON parse failed — {e}")
        print("Raw response:", raw[:500])
        sys.exit(1)

    print_report(data)
    save_report(data, keyword)


def print_report(d):
    titles = d.get("titles", [])
    strong = sum(1 for t in titles if t.get("rating") == "strong")
    weak = sum(1 for t in titles if t.get("rating") == "weak")
    avg = round(d.get("avg_char_count", 0))

    # Stats summary
    print(f"SUMMARY")
    print(f"  Competitors analyzed : {len(titles)}")
    print(f"  Avg title length     : {avg} chars")
    print(f"  Strong titles        : {strong}")
    print(f"  Weak titles          : {weak}")
    print()

    # Common keywords
    common = d.get("common_keywords", [])
    if common:
        print("COMMON KEYWORDS IN COMPETITOR TITLES")
        print("  " + " | ".join(common))
        print()

    # Gaps
    gaps = d.get("missing_opportunities", [])
    if gaps:
        print("KEYWORD GAPS — YOUR OPPORTUNITIES")
        for g in gaps:
            print(f"  → {g}")
        print()

    # Title tags
    print("COMPETITOR TITLE TAGS")
    print("-" * 60)
    for t in titles:
        rank = t.get("rank", "?")
        domain = t.get("domain", "")
        title = t.get("title", "")
        chars = t.get("char_count", 0)
        rating = t.get("rating", "").upper()
        char_flag = "⚠ TOO LONG" if chars > 60 else ("⚠ SHORT" if chars < 40 else "✓")

        print(f"  #{rank} {domain}")
        print(f"     \"{title}\"")
        print(f"     {chars} chars {char_flag}  |  {rating}")

        mods = t.get("modifiers", [])
        if mods:
            print(f"     Modifiers: {', '.join(mods)}")
        print()

    # Insights
    insights = d.get("insights", [])
    if insights:
        print("ANALYSIS & INSIGHTS")
        print("-" * 60)
        for i, insight in enumerate(insights, 1):
            print(f"  {i}. {insight}")
        print()

    # Title formulas
    formulas = d.get("recommended_title_formulas", [])
    if formulas:
        print("RECOMMENDED TITLE FORMULAS")
        print("-" * 60)
        for f in formulas:
            print(f"  • {f}")
        print()

    # Blog topics
    topics = d.get("blog_topics", [])
    if topics:
        print("BLOG TOPIC IDEAS")
        print("-" * 60)
        for i, t in enumerate(topics, 1):
            print(f"  {i:02d}. [{t.get('type','').upper()}] {t.get('title','')}")
            print(f"       KW: {t.get('target_kw','')}")
            print(f"       → {t.get('rationale','')}")
            print()


def save_report(data, keyword):
    safe_kw = keyword.lower().replace(" ", "_").replace("/", "_")[:40]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"seo_report_{safe_kw}_{timestamp}.json"
    filepath = os.path.join(os.path.expanduser("~/Desktop/ClaudeWork/Rich"), filename)

    # Also save a plain text version
    txt_filename = f"seo_report_{safe_kw}_{timestamp}.txt"

    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        print(f"{'='*60}")
        print(f"  JSON report saved: ~/Desktop/ClaudeWork/Rich/{filename}")
        print(f"{'='*60}\n")
    except Exception as e:
        print(f"(Could not save report: {e})")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 seo_research.py \"your keyword here\"")
        print("Example: python3 seo_research.py \"SEO consultant Boston\"")
        sys.exit(1)

    keyword = " ".join(sys.argv[1:])
    run_research(keyword)
