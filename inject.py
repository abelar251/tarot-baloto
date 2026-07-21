import re

def inject_code():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. CSS
    css_to_insert = """
    /* ==============================
       TEMPORAL SCANNER & SCRAPER
    ============================== */
    #temporal-scanner {
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      background: rgba(0, 0, 0, 0.95);
      z-index: 10000;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: #0f0;
      font-family: 'Courier New', Courier, monospace;
      text-shadow: 0 0 10px #0f0;
      transition: opacity 0.5s;
    }
    #temporal-scanner.hidden {
      display: none;
      opacity: 0;
    }
    .glitch-text {
      font-size: 2rem;
      margin-bottom: 20px;
      animation: glitch 1s linear infinite;
      text-align: center;
    }
    .scan-log {
      width: 90%;
      max-width: 600px;
      height: 250px;
      border: 1px solid #0f0;
      padding: 15px;
      overflow-y: hidden;
      font-size: 1.1rem;
      text-align: left;
      background: rgba(0,25,0,0.5);
    }
    .log-line {
      margin: 8px 0;
      opacity: 0;
      animation: fadeIn 0.1s forwards;
    }
    .log-line.warn { color: #ff0; text-shadow: 0 0 10px #ff0; }
    .log-line.err { color: #f00; text-shadow: 0 0 10px #f00; }
    .log-line.success { color: #0ff; text-shadow: 0 0 10px #0ff; }
    @keyframes glitch {
      2%, 64% { transform: translate(2px,0) skew(0deg); }
      4%, 60% { transform: translate(-2px,0) skew(0deg); }
      62% { transform: translate(0,0) skew(5deg); }
    }
    @keyframes fadeIn {
      to { opacity: 1; }
    }
    .probability-badge {
      background: linear-gradient(45deg, #ffd700, #daa520);
      color: #000;
      padding: 8px 20px;
      border-radius: 20px;
      font-family: 'Cinzel', serif;
      font-weight: bold;
      font-size: 1.2rem;
      margin-top: 25px;
      margin-bottom: 10px;
      box-shadow: 0 0 15px #ffd700;
      animation: pulse 2s infinite;
      text-align: center;
    }
"""
    if "TEMPORAL SCANNER & SCRAPER" not in content:
        content = re.sub(r'([ \t]*}\s*)(/\* ==============================\s*LAYOUT\s*============================== \*/)', r'\1' + css_to_insert + r'\n    \2', content)

    # 2. HTML
    html_to_insert = """
    <!-- === TEMPORAL SCANNER MODAL === -->
    <div id="temporal-scanner" class="hidden">
      <div class="glitch-text">INICIANDO ESCÁNER TEMPORAL...</div>
      <div class="scan-log" id="scan-log"></div>
    </div>
"""
    if "TEMPORAL SCANNER MODAL" not in content:
        content = re.sub(r'([ \t]*<!-- === PHASE 3: RESULTADO === -->)', html_to_insert + r'\n\1', content)

    # 3. JS
    new_js = """    async function revealOracle() {
      document.getElementById('phase-select').classList.add('hidden');
      
      const scanner = document.getElementById('temporal-scanner');
      const scanLog = document.getElementById('scan-log');
      scanner.classList.remove('hidden');
      scanLog.innerHTML = '';
      
      const lines = [
        "Estableciendo conexión con la Deep Web...",
        "Hackeando el portal temporal de Baloto...",
        "Extrayendo últimos resultados oficiales en vivo..."
      ];
      
      // Mostrar primeras lineas del log
      for (let text of lines) {
        const div = document.createElement('div');
        div.className = 'log-line';
        div.innerHTML = "> " + text;
        scanLog.appendChild(div);
        scanLog.scrollTop = scanLog.scrollHeight;
        await new Promise(r => setTimeout(r, 800));
      }

      // === INICIO DEL SCRAPER INTEGRADO ===
      let latestNumbers = [];
      let latestSuper = null;
      let scraperSuccess = false;

      try {
        const response = await fetch('https://api.allorigins.win/get?url=' + encodeURIComponent('https://baloto.com/resultados'));
        if (response.ok) {
          const data = await response.json();
          const parser = new DOMParser();
          const doc = parser.parseFromString(data.contents, 'text/html');
          
          doc.querySelectorAll('.yellow-ball-results, .yellow-ball, .red-ball, .pink-ball-results, .red-ball-big').forEach(el => {
              const numText = el.textContent.trim();
              const num = parseInt(numText, 10);
              if (!isNaN(num)) {
                  if (el.classList.contains('red-ball') || el.classList.contains('pink-ball-results') || el.classList.contains('red-ball-big')) {
                      if (latestSuper === null) latestSuper = num;
                  } else {
                      if (latestNumbers.length < 5) latestNumbers.push(num);
                  }
              }
          });
          
          if(latestNumbers.length === 5) {
            scraperSuccess = true;
          }
        }
      } catch (e) {
        console.error("Scraper Temporal Falló:", e);
      }
      // === FIN DEL SCRAPER ===

      if(scraperSuccess) {
         const div = document.createElement('div');
         div.className = 'log-line success';
         div.innerHTML = "> [ÉXITO] Resultados reales extraídos: " + latestNumbers.join('-') + " Super: " + latestSuper;
         scanLog.appendChild(div);
      } else {
         const div = document.createElement('div');
         div.className = 'log-line warn';
         div.innerHTML = "> [ADVERTENCIA] Defensas cuánticas bloquearon el Scraper. Usando memoria Akáshica...";
         scanLog.appendChild(div);
      }
      scanLog.scrollTop = scanLog.scrollHeight;
      await new Promise(r => setTimeout(r, 1500));

      const lateLines = [
        "<span class='warn'>[ALERTA] Buscando ecos temporales y paradojas de viajeros del tiempo...</span>",
        "Analizando patrones cuánticos de tus cartas elegidas...",
        "<span class='err'>Ninguna anomalía temporal detectada. El tejido del tiempo está intacto.</span>",
        "Calculando algoritmo de probabilidad de números fríos/calientes...",
        "Generando Alineación Mística..."
      ];

      for (let text of lateLines) {
        const div = document.createElement('div');
        div.className = 'log-line';
        div.innerHTML = "> " + text;
        scanLog.appendChild(div);
        scanLog.scrollTop = scanLog.scrollHeight;
        await new Promise(r => setTimeout(r, 600 + Math.random() * 400));
      }

      setTimeout(() => {
        scanner.classList.add('hidden');
        showOracleResults(scraperSuccess, latestNumbers, latestSuper);
      }, 1500);
    }

    function showOracleResults(scraperSuccess, latestNumbers, latestSuper) {
      document.getElementById('phase-result').classList.remove('hidden');

      const phrase = ORACLE_PHRASES[Math.floor(Math.random() * ORACLE_PHRASES.length)];
      document.getElementById('oracle-text').textContent = phrase;

      // Compute standard formula from cards
      const results = computeNumbers(selectedCards);

      // Numbers display
      const numDisp = document.getElementById('numbers-display');
      numDisp.innerHTML = '';
      
      // Calculate a fun probability based on card values and scraper success
      let baseProb = 85 + (results[5].num / 16) * 10 + (Math.random() * 4.9);
      if(scraperSuccess) baseProb = Math.min(99.99, baseProb + 1.5); // Bono probabilístico si scraper funcionó
      
      const probBadge = document.createElement('div');
      probBadge.className = 'probability-badge';
      probBadge.innerHTML = `🌟 Alineación de Probabilidad: ${baseProb.toFixed(2)}% 🌟`;
      numDisp.appendChild(probBadge);
      
      const ballsContainer = document.createElement('div');
      ballsContainer.style.display = 'flex';
      ballsContainer.style.justifyContent = 'center';
      ballsContainer.style.flexWrap = 'wrap';
      ballsContainer.style.gap = '15px';
      
      results.forEach((r) => {
        const ball = document.createElement('div');
        ball.className = 'number-ball' + (r.isSuper ? ' super-ball' : '');
        ball.innerHTML = `${r.num}<span class="ball-label">${r.isSuper ? 'Super' : 'Baloto'}</span>`;
        ballsContainer.appendChild(ball);
      });
      numDisp.appendChild(ballsContainer);

      // Card reading details
      const reading = document.getElementById('card-reading');
      reading.innerHTML = '';
      results.forEach((r) => {
        const div = document.createElement('div');
        div.className = 'reading-card' + (r.isSuper ? ' is-super' : '');
        div.innerHTML = `
      <div class="art">${r.card.art}</div>
      <div class="rname">${r.card.name}</div>
      <div class="arcana-tag">${r.card.arcana}</div>
      <div class="rnum">${r.isSuper ? '🔴 ' : ''} ${r.num}</div>
      <div class="formula-line">${r.formula}</div>
    `;
        reading.appendChild(div);
      });
    }"""
    
    if "async function revealOracle()" not in content:
        # Match from "function revealOracle() {" to just before "/* ===" or "function restart()"
        pattern = re.compile(r'([ \t]*function revealOracle\(\) \{.*?\n[ \t]*\})(?=\s*/\* ========================================================\s*RESTART)', re.DOTALL)
        content = pattern.sub(new_js, content)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    inject_code()
    print("Injection complete.")
