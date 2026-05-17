#!/usr/bin/env python3
"""
Injects FAQ sections + FAQPage schema into all three service pages.
Run: python3 ~/Desktop/ClaudeWork/Rich/add_faqs.py
"""

import os

BASE = os.path.expanduser("~/Desktop/ClaudeWork/Rich")

# ── FAQPage schema blocks ──────────────────────────────────────────────────────

SEO_SCHEMA = """
  <!-- FAQPage Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "How long does SEO take to show results?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Most businesses see meaningful ranking movement within 3 to 6 months. Competitive markets like Boston can take longer. SEO is a compounding channel — results build over time and don't disappear when you stop paying for ads."
        }
      },
      {
        "@type": "Question",
        "name": "What is included in an SEO audit?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A technical SEO audit covers site architecture, crawlability, page speed, mobile usability, duplicate content, broken links, and indexation issues. It also includes keyword gap analysis, competitor benchmarking, and a prioritized action plan."
        }
      },
      {
        "@type": "Question",
        "name": "Do I need ongoing SEO or is a one-time audit enough?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "It depends on your goals and market. A one-time audit identifies what needs fixing — but SEO is ongoing because search engines update constantly, competitors evolve, and your site changes. Most businesses benefit from ongoing support after an initial audit."
        }
      },
      {
        "@type": "Question",
        "name": "What makes a good SEO consultant in Boston?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Look for someone with verifiable experience across technical SEO, content strategy, and local search — not just one area. They should understand your specific market, be transparent about timelines, and be able to show real outcomes from past work, not just rankings."
        }
      }
    ]
  }
  </script>"""

AI_SCHEMA = """
  <!-- FAQPage Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What does an AI consultant actually do for a small business?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "An AI consultant identifies the repetitive, manual tasks in your business that can be automated — then builds the systems to replace them. This could mean automating customer follow-up, building reporting pipelines, creating content workflows, or connecting tools that don't talk to each other."
        }
      },
      {
        "@type": "Question",
        "name": "Do I need technical knowledge to work with an AI consultant?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. A good AI consultant translates your business problems into technical solutions and handles the build. You describe what's taking too much time or costing too much money — they figure out what to build and how."
        }
      },
      {
        "@type": "Question",
        "name": "How much does AI consulting cost for a small business?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "It varies by scope. Simple automations can be built in a few hours. Complex multi-system workflows take longer. Most small business AI consulting engagements are project-based with a defined deliverable — you know the cost before work begins."
        }
      },
      {
        "@type": "Question",
        "name": "What AI tools do you use for small business automation?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The right tools depend on the problem. Common options include n8n for workflow automation, Claude API for AI-powered tasks, Python for custom scripts, and integrations with tools you already use like Google Workspace, Shopify, or your CRM."
        }
      }
    ]
  }
  </script>"""

TOOLS_SCHEMA = """
  <!-- FAQPage Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What kind of custom tools can you build for my business?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Common builds include trading bots, automated reporting dashboards, content pipelines, lead generation tools, data scrapers, email automation systems, and custom calculators or web apps. If your business has a repetitive process, it can probably be automated."
        }
      },
      {
        "@type": "Question",
        "name": "How long does it take to build a custom tool?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Simple tools — scripts, automations, dashboards — can be built in days. More complex systems with multiple integrations take 2 to 4 weeks. Every project starts with a clear scope and timeline so you know what to expect before work begins."
        }
      },
      {
        "@type": "Question",
        "name": "Will I be able to maintain the tool after it's built?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. Everything is built to run with minimal maintenance and handed off with documentation. The goal is a system that works for you without requiring ongoing technical support — though that's available if you need it."
        }
      },
      {
        "@type": "Question",
        "name": "Do you build tools using AI?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "When it makes sense, yes. AI is useful for specific tasks — content generation, data analysis, pattern recognition — but not every problem needs it. The right tool for the job is whatever actually solves the problem reliably and efficiently."
        }
      }
    ]
  }
  </script>"""

# ── FAQ HTML sections ──────────────────────────────────────────────────────────

SEO_FAQ_HTML = """
  <!-- FAQ Section -->
  <section style="padding:5rem 0;background:var(--bg);">
    <div class="container">
      <span class="label">FAQ</span>
      <h2>Common questions about SEO consulting</h2>
      <p class="sub" style="max-width:520px;margin-top:0.75rem;">Straight answers to the questions most Boston businesses ask before starting an SEO engagement.</p>
      <div style="margin-top:2.5rem;display:flex;flex-direction:column;gap:1rem;">

        <details style="background:var(--bg2);border:1px solid var(--border);border-radius:10px;padding:1.25rem 1.5rem;">
          <summary style="font-weight:600;color:var(--text);cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;font-size:1rem;">
            How long does SEO take to show results?
            <span style="color:var(--accent);font-size:1.2rem;flex-shrink:0;margin-left:1rem;">+</span>
          </summary>
          <p style="color:var(--text2);margin-top:1rem;line-height:1.75;font-size:0.95rem;">Most businesses see meaningful ranking movement within 3 to 6 months. Competitive markets like Boston can take longer. SEO is a compounding channel — results build over time and don't disappear when you stop paying for ads.</p>
        </details>

        <details style="background:var(--bg2);border:1px solid var(--border);border-radius:10px;padding:1.25rem 1.5rem;">
          <summary style="font-weight:600;color:var(--text);cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;font-size:1rem;">
            What is included in an SEO audit?
            <span style="color:var(--accent);font-size:1.2rem;flex-shrink:0;margin-left:1rem;">+</span>
          </summary>
          <p style="color:var(--text2);margin-top:1rem;line-height:1.75;font-size:0.95rem;">A technical SEO audit covers site architecture, crawlability, page speed, mobile usability, duplicate content, broken links, and indexation issues. It also includes keyword gap analysis, competitor benchmarking, and a prioritized action plan.</p>
        </details>

        <details style="background:var(--bg2);border:1px solid var(--border);border-radius:10px;padding:1.25rem 1.5rem;">
          <summary style="font-weight:600;color:var(--text);cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;font-size:1rem;">
            Do I need ongoing SEO or is a one-time audit enough?
            <span style="color:var(--accent);font-size:1.2rem;flex-shrink:0;margin-left:1rem;">+</span>
          </summary>
          <p style="color:var(--text2);margin-top:1rem;line-height:1.75;font-size:0.95rem;">It depends on your goals and market. A one-time audit identifies what needs fixing — but SEO is ongoing because search engines update constantly, competitors evolve, and your site changes. Most businesses benefit from ongoing support after an initial audit.</p>
        </details>

        <details style="background:var(--bg2);border:1px solid var(--border);border-radius:10px;padding:1.25rem 1.5rem;">
          <summary style="font-weight:600;color:var(--text);cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;font-size:1rem;">
            What makes a good SEO consultant in Boston?
            <span style="color:var(--accent);font-size:1.2rem;flex-shrink:0;margin-left:1rem;">+</span>
          </summary>
          <p style="color:var(--text2);margin-top:1rem;line-height:1.75;font-size:0.95rem;">Look for someone with verifiable experience across technical SEO, content strategy, and local search — not just one area. They should understand your specific market, be transparent about timelines, and be able to show real outcomes from past work, not just rankings.</p>
        </details>

      </div>
    </div>
  </section>"""

AI_FAQ_HTML = """
  <!-- FAQ Section -->
  <section style="padding:5rem 0;background:var(--bg);">
    <div class="container">
      <span class="label">FAQ</span>
      <h2>Common questions about AI consulting</h2>
      <p class="sub" style="max-width:520px;margin-top:0.75rem;">What small business owners typically ask before starting an AI automation engagement.</p>
      <div style="margin-top:2.5rem;display:flex;flex-direction:column;gap:1rem;">

        <details style="background:var(--bg2);border:1px solid var(--border);border-radius:10px;padding:1.25rem 1.5rem;">
          <summary style="font-weight:600;color:var(--text);cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;font-size:1rem;">
            What does an AI consultant actually do for a small business?
            <span style="color:var(--accent);font-size:1.2rem;flex-shrink:0;margin-left:1rem;">+</span>
          </summary>
          <p style="color:var(--text2);margin-top:1rem;line-height:1.75;font-size:0.95rem;">An AI consultant identifies the repetitive, manual tasks in your business that can be automated — then builds the systems to replace them. This could mean automating customer follow-up, building reporting pipelines, creating content workflows, or connecting tools that don't talk to each other.</p>
        </details>

        <details style="background:var(--bg2);border:1px solid var(--border);border-radius:10px;padding:1.25rem 1.5rem;">
          <summary style="font-weight:600;color:var(--text);cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;font-size:1rem;">
            Do I need technical knowledge to work with an AI consultant?
            <span style="color:var(--accent);font-size:1.2rem;flex-shrink:0;margin-left:1rem;">+</span>
          </summary>
          <p style="color:var(--text2);margin-top:1rem;line-height:1.75;font-size:0.95rem;">No. A good AI consultant translates your business problems into technical solutions and handles the build. You describe what's taking too much time or costing too much money — they figure out what to build and how.</p>
        </details>

        <details style="background:var(--bg2);border:1px solid var(--border);border-radius:10px;padding:1.25rem 1.5rem;">
          <summary style="font-weight:600;color:var(--text);cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;font-size:1rem;">
            How much does AI consulting cost for a small business?
            <span style="color:var(--accent);font-size:1.2rem;flex-shrink:0;margin-left:1rem;">+</span>
          </summary>
          <p style="color:var(--text2);margin-top:1rem;line-height:1.75;font-size:0.95rem;">It varies by scope. Simple automations can be built in a few hours. Complex multi-system workflows take longer. Most small business AI consulting engagements are project-based with a defined deliverable — you know the cost before work begins.</p>
        </details>

        <details style="background:var(--bg2);border:1px solid var(--border);border-radius:10px;padding:1.25rem 1.5rem;">
          <summary style="font-weight:600;color:var(--text);cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;font-size:1rem;">
            What AI tools do you use for small business automation?
            <span style="color:var(--accent);font-size:1.2rem;flex-shrink:0;margin-left:1rem;">+</span>
          </summary>
          <p style="color:var(--text2);margin-top:1rem;line-height:1.75;font-size:0.95rem;">The right tools depend on the problem. Common options include n8n for workflow automation, Claude API for AI-powered tasks, Python for custom scripts, and integrations with tools you already use like Google Workspace, Shopify, or your CRM.</p>
        </details>

      </div>
    </div>
  </section>"""

TOOLS_FAQ_HTML = """
  <!-- FAQ Section -->
  <section style="padding:5rem 0;background:var(--bg);">
    <div class="container">
      <span class="label">FAQ</span>
      <h2>Common questions about custom tools</h2>
      <p class="sub" style="max-width:520px;margin-top:0.75rem;">What to expect when you commission a custom-built tool or automation system.</p>
      <div style="margin-top:2.5rem;display:flex;flex-direction:column;gap:1rem;">

        <details style="background:var(--bg2);border:1px solid var(--border);border-radius:10px;padding:1.25rem 1.5rem;">
          <summary style="font-weight:600;color:var(--text);cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;font-size:1rem;">
            What kind of custom tools can you build for my business?
            <span style="color:var(--accent);font-size:1.2rem;flex-shrink:0;margin-left:1rem;">+</span>
          </summary>
          <p style="color:var(--text2);margin-top:1rem;line-height:1.75;font-size:0.95rem;">Common builds include trading bots, automated reporting dashboards, content pipelines, lead generation tools, data scrapers, email automation systems, and custom calculators or web apps. If your business has a repetitive process, it can probably be automated.</p>
        </details>

        <details style="background:var(--bg2);border:1px solid var(--border);border-radius:10px;padding:1.25rem 1.5rem;">
          <summary style="font-weight:600;color:var(--text);cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;font-size:1rem;">
            How long does it take to build a custom tool?
            <span style="color:var(--accent);font-size:1.2rem;flex-shrink:0;margin-left:1rem;">+</span>
          </summary>
          <p style="color:var(--text2);margin-top:1rem;line-height:1.75;font-size:0.95rem;">Simple tools — scripts, automations, dashboards — can be built in days. More complex systems with multiple integrations take 2 to 4 weeks. Every project starts with a clear scope and timeline so you know what to expect before work begins.</p>
        </details>

        <details style="background:var(--bg2);border:1px solid var(--border);border-radius:10px;padding:1.25rem 1.5rem;">
          <summary style="font-weight:600;color:var(--text);cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;font-size:1rem;">
            Will I be able to maintain the tool after it's built?
            <span style="color:var(--accent);font-size:1.2rem;flex-shrink:0;margin-left:1rem;">+</span>
          </summary>
          <p style="color:var(--text2);margin-top:1rem;line-height:1.75;font-size:0.95rem;">Yes. Everything is built to run with minimal maintenance and handed off with documentation. The goal is a system that works for you without requiring ongoing technical support — though that's available if you need it.</p>
        </details>

        <details style="background:var(--bg2);border:1px solid var(--border);border-radius:10px;padding:1.25rem 1.5rem;">
          <summary style="font-weight:600;color:var(--text);cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;font-size:1rem;">
            Do you build tools using AI?
            <span style="color:var(--accent);font-size:1.2rem;flex-shrink:0;margin-left:1rem;">+</span>
          </summary>
          <p style="color:var(--text2);margin-top:1rem;line-height:1.75;font-size:0.95rem;">When it makes sense, yes. AI is useful for specific tasks — content generation, data analysis, pattern recognition — but not every problem needs it. The right tool for the job is whatever actually solves the problem reliably and efficiently.</p>
        </details>

      </div>
    </div>
  </section>"""

# ── Inject into files ──────────────────────────────────────────────────────────

PAGES = [
    {
        "file": "seo-web.html",
        "schema": SEO_SCHEMA,
        "faq_html": SEO_FAQ_HTML,
    },
    {
        "file": "ai-consulting.html",
        "schema": AI_SCHEMA,
        "faq_html": AI_FAQ_HTML,
    },
    {
        "file": "custom-tools.html",
        "schema": TOOLS_SCHEMA,
        "faq_html": TOOLS_FAQ_HTML,
    },
]

updated = 0
skipped = 0

for page in PAGES:
    path = os.path.join(BASE, page["file"])

    if not os.path.exists(path):
        print(f"  SKIP  {page['file']} — file not found")
        skipped += 1
        continue

    content = open(path, encoding="utf-8").read()

    if "FAQPage" in content:
        print(f"  SKIP  {page['file']} — FAQ already present")
        skipped += 1
        continue

    # Inject schema before </head>
    content = content.replace("</head>", page["schema"] + "\n</head>")

    # Inject FAQ HTML before </main> or before the contact section
    if '<section id="contact"' in content:
        content = content.replace('<section id="contact"', page["faq_html"] + '\n\n  <section id="contact"')
    elif "</main>" in content:
        content = content.replace("</main>", page["faq_html"] + "\n</main>")
    else:
        # fallback: before closing footer
        content = content.replace("<footer", page["faq_html"] + "\n\n<footer")

    open(path, "w", encoding="utf-8").write(content)
    print(f"  OK    {page['file']}")
    updated += 1

print(f"\n  {updated} pages updated, {skipped} skipped")
print("\nDone. Deploy next:")
print('  python3 ~/Desktop/ClaudeWork/Rich/deploy.py "add FAQ sections to service pages"')
