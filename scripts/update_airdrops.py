import os
import json
import requests
import datetime
import google.generativeai as genai

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
DATA_FILE = "data/airdrops.json"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

PROMPT = """
You are an expert crypto airdrop researcher. Your job is to generate a realistic, accurate list of current crypto airdrops for 2026.

Generate a JSON array of 15-20 crypto airdrop objects. Each object must have these exact fields:

{
  "name": "Project Name",
  "emoji": "single relevant emoji",
  "logo": "",
  "section": "latest" OR "hot" OR "potential",
  "heat": integer between 20 and 500 (popularity score),
  "confirmed": true or false,
  "isNew": true or false,
  "claimLive": true or false,
  "sponsored": false,
  "value": "$XXX" or null,
  "action": "Clear description of what user must do to qualify",
  "chains": ["Chain1", "Chain2"],
  "tags": ["ethereum" or "solana" or "layer2" or "hot" or "confirmed"],
  "link": "#",
  "description": "2-3 sentence description for SEO"
}

Rules:
- Mix of real and plausible projects (Ethereum, Solana, L2s, DeFi protocols)
- "hot" section: heat > 300, well-known projects
- "latest" section: newer projects, heat 50-300
- "potential" section: speculative, no confirmed token yet, heat 20-150
- Actions should be specific and realistic (trade, stake, refer, bridge, complete quests)
- Some should have confirmed=true, some claimLive=true
- Include variety: DeFi, NFT, Gaming, Infrastructure projects
- Values only for giveaway-style drops ($50-$1000 range)

IMPORTANT: Return ONLY the JSON array, no markdown, no explanation, no code blocks. Start directly with [ and end with ]
"""

def fetch_airdrops_with_ai():
    print("Calling Gemini API...")
    response = model.generate_content(PROMPT)
    text = response.text.strip()
    
    # Clean up if Gemini wraps in markdown
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    text = text.strip()
    
    airdrops = json.loads(text)
    print(f"Generated {len(airdrops)} airdrops")
    return airdrops

def save_airdrops(airdrops):
    # Add metadata
    airdrops.append({"lastUpdated": datetime.datetime.utcnow().isoformat() + "Z"})
    
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(airdrops, f, indent=2, ensure_ascii=False)
    print(f"Saved to {DATA_FILE}")

def update_sitemap(airdrops):
    today = datetime.date.today().isoformat()
    urls = [
        "/", "/latest.html", "/hot.html", "/potential.html",
        "/claims.html", "/blog.html", "/faq.html", "/contact.html"
    ]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls:
        sitemap += f"  <url><loc>https://YOURSITE.github.io{url}</loc><lastmod>{today}</lastmod></url>\n"
    sitemap += "</urlset>"
    with open("sitemap.xml", "w") as f:
        f.write(sitemap)
    print("Sitemap updated")

if __name__ == "__main__":
    try:
        airdrops = fetch_airdrops_with_ai()
        save_airdrops(airdrops)
        update_sitemap(airdrops)
        print("✅ Airdrops updated successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")
        # Keep existing data if AI fails
        exit(0)
