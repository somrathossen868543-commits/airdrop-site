# 🚀 Complete Setup Guide — CryptoDrops.io Clone

## আপনি যা পাচ্ছেন:
- ✅ airdrops.io-র হুবহু clone (সব feature সহ)
- ✅ Gemini AI প্রতি ৬ ঘণ্টায় auto-update করবে
- ✅ Adsterra ads support
- ✅ Custom domain support  
- ✅ Google Search-এ আসবে (SEO ready)
- ✅ Cost: $0

---

## STEP 1 — GitHub Account তৈরি করুন

1. https://github.com এ যান
2. Sign Up করুন (free)
3. Email verify করুন

---

## STEP 2 — New Repository তৈরি করুন

1. GitHub-এ login করুন
2. উপরে ডানে "+" বাটন → "New repository"
3. Repository name দিন: `airdrop-site` (বা যেকোনো নাম)
4. **Public** রাখুন (এটা important!)
5. "Create repository" চাপুন

---

## STEP 3 — ফাইলগুলো Upload করুন

### Option A: Web দিয়ে (সহজ)
1. Repository পেজে "uploading an existing file" click করুন
2. এই guide-এর সাথে দেওয়া সব ফাইল drag করে drop করুন
3. "Commit changes" চাপুন

### Option B: GitHub Desktop দিয়ে (recommended)
1. https://desktop.github.com থেকে GitHub Desktop download করুন
2. Repository clone করুন
3. ফাইলগুলো সেই folder-এ রাখুন
4. Commit করে Push করুন

**ফাইল structure এরকম হবে:**
```
airdrop-site/
├── index.html
├── robots.txt
├── sitemap.xml
├── _config.yml
├── data/
│   └── airdrops.json
├── scripts/
│   └── update_airdrops.py
└── .github/
    └── workflows/
        └── update-airdrops.yml
```

---

## STEP 4 — GitHub Pages চালু করুন

1. Repository → Settings (উপরে)
2. বাম দিকে "Pages" click করুন
3. Source: "Deploy from a branch"
4. Branch: "main" → "/ (root)" → Save

5-10 মিনিট পরে আপনার সাইট live হবে:
`https://YOURUSERNAME.github.io/airdrop-site/`

---

## STEP 5 — Gemini API Key নিন (FREE)

1. https://aistudio.google.com যান
2. Google account দিয়ে login করুন
3. "Get API Key" → "Create API Key"
4. Key copy করুন (এরকম দেখাবে: `AIzaSy...`)

**Free tier:** প্রতিদিন 1,500 requests — আপনার জন্য বেশি যথেষ্ট!

---

## STEP 6 — API Key GitHub-এ add করুন (Secret)

1. Repository → Settings → Secrets and variables → Actions
2. "New repository secret" চাপুন
3. Name: `GEMINI_API_KEY`
4. Secret: আপনার API key paste করুন
5. "Add secret" চাপুন

---

## STEP 7 — প্রথমবার AI Run করুন

1. Repository → Actions tab
2. "Auto Update Airdrops" workflow click করুন
3. "Run workflow" → "Run workflow" (green button)
4. ৩-৫ মিনিট অপেক্ষা করুন
5. আপনার সাইট নতুন AI-generated airdrops দিয়ে update হবে!

এখন থেকে প্রতি ৬ ঘণ্টায় automatic হবে।

---

## STEP 8 — Adsterra Ads Setup

1. https://adsterra.com যান → Sign Up (Publisher হিসেবে)
2. "Add Site" → আপনার GitHub Pages URL দিন
3. Approve হওয়ার পরে Ad Code নিন
4. `index.html` খুলুন
5. এই comment গুলোর জায়গায় আপনার ad code paste করুন:
   - `<!-- Adsterra Head Ad Code — paste here -->` 
   - `<div id="adsterra-banner-top"></div>`
   - `<div id="adsterra-mid"></div>`
   - `<div id="adsterra-sidebar"></div>`

**Tips:** Adsterra-তে "Direct Link" ads সবচেয়ে বেশি revenue দেয় crypto sites-এ।

---

## STEP 9 — Custom Domain (.com) লাগানো

### Domain কেনা:
- https://namecheap.com (সবচেয়ে সস্তা, ~$8-10/year for .com)
- https://porkbun.com (আরও সস্তা)

### GitHub Pages-এ connect করা:
1. Repository → Settings → Pages
2. "Custom domain" এ আপনার domain টাইপ করুন (যেমন: `cryptodrops.io`)
3. Save করুন
4. Namecheap-এ গিয়ে DNS settings:
   - Type: `A` → Value: `185.199.108.153`
   - Type: `A` → Value: `185.199.109.153`
   - Type: `A` → Value: `185.199.110.153`
   - Type: `A` → Value: `185.199.111.153`
   - Type: `CNAME` → Name: `www` → Value: `YOURUSERNAME.github.io`
5. ২৪-৪৮ ঘণ্টার মধ্যে domain কাজ করবে

### HTTPS চালু করুন:
- Settings → Pages → "Enforce HTTPS" checkbox tick করুন

---

## STEP 10 — Google Search-এ আনুন

### Google Search Console:
1. https://search.google.com/search-console যান
2. "Add property" → আপনার URL দিন
3. Verify করুন (HTML file বা DNS method)
4. Sitemap submit করুন: `https://yoursite.com/sitemap.xml`

### SEO Tips:
- প্রতিটা airdrop-এর জন্য আলাদা page বানান (আরও traffic)
- Title: "Free [ProjectName] Airdrop 2026 — How to Claim"
- Update frequency বেশি হলে Google বেশি crawl করে

---

## Site Update করতে যা যা করতে হবে আপনার:

```
কিছুই না! AI সব করবে 🤖

প্রতি ৬ ঘণ্টায়:
→ Gemini AI নতুন airdrops generate করে
→ airdrops.json update হয়
→ সাইট automatically নতুন data দেখায়
```

---

## Revenue Potential (USA/UK traffic):

| Traffic | Monthly Revenue (Adsterra) |
|---------|---------------------------|
| 1,000 visitors/day | $30-80 |
| 5,000 visitors/day | $150-400 |
| 20,000 visitors/day | $600-1,500 |

Crypto niche-এ CPM সবচেয়ে বেশি ($5-20 per 1000 views)।

---

## Problems হলে:

- GitHub Actions fail করলে → Actions tab-এ error দেখুন
- Site load না হলে → Settings → Pages check করুন
- AI কাজ না করলে → Secrets-এ API key ঠিক আছে কিনা দেখুন

**সাহায্য লাগলে screenshot নিয়ে আসুন!**
