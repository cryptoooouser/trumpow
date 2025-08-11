# Build a clean single-page website for $TRUPOW (Trump + Powell meme coin)
# The user requested a site with ONLY the contract address (no socials).
# We'll bundle index.html, styles.css, script.js, and include the generated logo if available.

import os, shutil, zipfile, textwrap

site_dir = "/mnt/data/trupow_site"
os.makedirs(site_dir, exist_ok=True)

# Try to use the generated TRUPOW logo; if not found, make a placeholder.
src_logo = "/mnt/data/A_political_caricature-style_digital_illustration_.png"
logo_path = os.path.join(site_dir, "trupow-logo.png")
try:
    if os.path.exists(src_logo):
        shutil.copy(src_logo, logo_path)
    else:
        from PIL import Image, ImageDraw, ImageFont
        img = Image.new("RGBA", (768,768), (255, 226, 173, 255))
        d = ImageDraw.Draw(img)
        d.rectangle((60,60,708,708), outline=(20,20,20,255), width=8)
        d.text((140,360), "$TRUPOW", fill=(20,20,20,255))
        img.save(logo_path)
except Exception:
    from PIL import Image, ImageDraw
    img = Image.new("RGBA", (512,512), (240, 200, 120, 255))
    d = ImageDraw.Draw(img)
    d.text((140,230), "$TRUPOW", fill=(10,10,10,255))
    img.save(logo_path)

# Placeholder contract (user will paste real one)
contract_placeholder = "PASTE_YOUR_TRUPOW_CONTRACT_ADDRESS_HERE"
pump_link_placeholder = "#"   # user can replace with their Pump.fun link later
chart_link_placeholder = "#"  # user can replace with Dexscreener later

index_html = textwrap.dedent(f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>$TRUPOW — Trump × Powell Meme Coin</title>
  <meta name="description" content="$TRUPOW — When the MAGA pump meets the Fed’s money printer. Meme coin on Solana.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <header class="site-header">
    <div class="container nav">
      <div class="brand">
        <img src="trupow-logo.png" class="logo" alt="$TRUPOW logo">
        <span class="wordmark">$TRUPOW</span>
      </div>
      <nav class="actions">
        <a class="btn outline" href="{pump_link_placeholder}" target="_blank" rel="noopener">Buy on Pump.fun</a>
        <a class="btn solid" href="#how-to-buy">How to Buy</a>
      </nav>
    </div>
  </header>

  <section class="hero">
    <div class="container hero-inner">
      <div class="hero-left">
        <h1><span class="accent">$TRUPOW</span> — Trump × Powell</h1>
        <p class="sub">When the MAGA pump meets the Fed’s money printer. No promises. No roadmap. Just vibes.</p>

        <div class="contract">
          <label>Contract Address</label>
          <div class="contract-row">
            <input id="contractInput" value="{contract_placeholder}" readonly>
            <button id="copyBtn" class="btn copy">Copy</button>
          </div>
          <small class="muted">Always verify this address from official posts.</small>
        </div>

        <div class="cta">
          <a class="btn solid" href="{pump_link_placeholder}" target="_blank" rel="noopener">Buy on Pump.fun</a>
          <a class="btn outline" href="{chart_link_placeholder}" target="_blank" rel="noopener">View Chart</a>
        </div>
      </div>
      <div class="hero-right">
        <img src="trupow-logo.png" class="hero-logo" alt="$TRUPOW logo large">
      </div>
    </div>
    <div class="bg-glow"></div>
  </section>

  <section class="about">
    <div class="container">
      <h2>About $TRUPOW</h2>
      <p><strong>When the MAGA pump meets the Fed’s money printer.</strong> $TRUPOW is the ultimate mashup of political chaos and monetary madness — fusing the hype of Donald J. Trump with the market-moving power of Jerome “Rate Hike” Powell. It’s a community-driven meme coin on Solana made for headlines, chart breaks, and maximum entertainment.</p>
      <ul class="pill-points">
        <li>Meme coin. No promises.</li>
        <li>Launched via Pump.fun; liquidity handled on eligibility.</li>
        <li>High risk — verify the contract before trading.</li>
      </ul>
    </div>
  </section>

  <section id="how-to-buy" class="how">
    <div class="container">
      <h2>How to Buy</h2>
      <ol class="steps">
        <li><strong>Install Phantom</strong> (or Solflare) and create a wallet.</li>
        <li><strong>Fund with SOL</strong> from an exchange (Coinbase, Binance, etc.).</li>
        <li><strong>Open Pump.fun</strong> and use the button above or search for $TRUPOW.</li>
        <li><strong>Verify the Contract</strong> address matches the one shown here.</li>
        <li><strong>Swap SOL → $TRUPOW</strong> and you’re in.</li>
      </ol>
      <div class="safety"><strong>Safety:</strong> This is a meme coin. No financial advice. Beware of DM scams and fake links.</div>
    </div>
  </section>

  <footer class="site-footer">
    <div class="container">
      <p id="footerLine">© The $TRUPOW community. Meme coin — for entertainment only.</p>
    </div>
  </footer>

  <script src="script.js"></script>
</body>
</html>
""")

styles_css = """
:root{
  --bg:#0b0b0b;
  --panel:#121212;
  --muted:#9aa0a6;
  --text:#e9eef5;
  --accent:#f59e0b; /* gold */
  --accent-2:#e11d48; /* red */
  --ring:rgba(241,196,15,0.35);
}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:var(--bg);color:var(--text);font-family:'Inter',system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif}
img{max-width:100%;display:block}
a{color:inherit;text-decoration:none}

.container{max-width:1120px;margin:0 auto;padding:0 20px}

.site-header{position:sticky;top:0;background:rgba(11,11,11,0.7);backdrop-filter:blur(8px);border-bottom:1px solid #1e1e1e;z-index:20}
.nav{display:flex;align-items:center;justify-content:space-between;height:64px}
.brand{display:flex;align-items:center;gap:12px}
.logo{width:40px;height:40px;border-radius:10px;box-shadow:0 0 0 3px var(--ring)}
.wordmark{font-weight:800;letter-spacing:0.4px}

.actions{display:flex;gap:10px}
.btn{border:1px solid #2a2a2a;padding:10px 14px;border-radius:10px;font-weight:700;transition:0.2s ease;display:inline-flex;align-items:center;gap:8px}
.btn:hover{transform:translateY(-1px)}
.btn.solid{background:var(--accent);border-color:var(--accent);color:#111}
.btn.outline{background:transparent;color:var(--text)}
.btn.copy{background:#1e1e1e;border-color:#2c2c2c;color:#e9eef5}

.hero{position:relative;border-bottom:1px solid #1e1e1e;overflow:hidden}
.hero-inner{display:grid;grid-template-columns:1.1fr 0.9fr;gap:32px;align-items:center;min-height:72vh;padding:36px 0}
.hero-left h1{font-size:42px;line-height:1.1;margin:0 0 12px}
.accent{color:var(--accent)}
.sub{color:#e6e6e6;opacity:0.95}

.contract{margin:22px 0 10px}
.contract label{display:block;font-size:13px;color:var(--muted);margin-bottom:8px}
.contract-row{display:flex;gap:10px}
.contract-row input{flex:1;background:#0f0f0f;border:1px solid #242424;color:var(--text);padding:12px;border-radius:10px;font-family:inherit}
.contract-row .btn{padding:12px 14px}

.hero-right{display:flex;justify-content:center}
.hero-logo{width:360px;max-width:90%;border-radius:18px;box-shadow:0 24px 80px rgba(241,196,15,0.25)}

.bg-glow{position:absolute;inset:auto -20% -40% -20%;height:50%;background:radial-gradient(60% 120% at 50% 0%, rgba(241,196,15,0.25), transparent 60%)}

.about,.how{padding:56px 0;border-bottom:1px solid #1e1e1e}
h2{font-size:28px;margin:0 0 14px}
.pill-points{display:flex;flex-wrap:wrap;gap:10px;padding:0;margin:14px 0 0;list-style:none}
.pill-points li{border:1px solid #2a2a2a;padding:10px 12px;border-radius:999px;background:#101010}

.steps{margin:0;padding-left:20px}
.steps li{margin-top:10px}
.safety{margin-top:14px;color:var(--muted);font-size:14px}

.site-footer{padding:26px 0;color:var(--muted);font-size:14px}

@media (max-width:900px){
  .hero-inner{grid-template-columns:1fr;gap:20px}
  .hero-left h1{font-size:34px}
  .hero-logo{width:280px}
}
"""

script_js = """
// Footer
const footer = document.getElementById('footerLine');
if (footer) footer.textContent = `© ${new Date().getFullYear()} The $TRUPOW community. Meme coin — for entertainment only.`;

// Copy contract
const copyBtn = document.getElementById('copyBtn');
const contractInput = document.getElementById('contractInput');
if (copyBtn && contractInput){
  copyBtn.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(contractInput.value.trim());
      copyBtn.textContent = 'Copied!';
      setTimeout(()=> copyBtn.textContent = 'Copy', 1400);
    } catch(e){
      alert('Copy failed. Select and copy manually.');
    }
  });
}
"""

# Write files
with open(os.path.join(site_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)
with open(os.path.join(site_dir, "styles.css"), "w", encoding="utf-8") as f:
    f.write(styles_css)
with open(os.path.join(site_dir, "script.js"), "w", encoding="utf-8") as f:
    f.write(script_js)

# Zip bundle
zip_path = "/mnt/data/trupow-site.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for fname in ["index.html","styles.css","script.js","trupow-logo.png"]:
        z.write(os.path.join(site_dir, fname), arcname=fname)

zip_path
