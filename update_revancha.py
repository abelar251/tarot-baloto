import re

def update_code():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add revancha badge css
    css_to_add = """
    .probability-badge.revancha {
      background: linear-gradient(45deg, #ff4500, #ff8c00);
      box-shadow: 0 0 15px #ff4500;
      color: #fff;
    }"""
    if ".probability-badge.revancha" not in content:
        content = content.replace('.probability-badge {', css_to_add + '\n    .probability-badge {')

    # 2. Rewrite revealOracle and showOracleResults
    new_js = """    async function revealOracle() {
      document.getElementById('phase-select').classList.add('hidden');
      
      const scanner = document.getElementById('temporal-scanner');
      const scanLog = document.getElementById('scan-log');
      scanner.classList.remove('hidden');
      scanLog.innerHTML = '';
      
      const lines = [
        "Alineando los astros en la bóveda celeste...",
        "Consultando los registros etéreos del destino...",
        "Invocando la esencia de los números sagrados..."
      ];
      
      // Mostrar primeras lineas del log
      for (let text of lines) {
        const div = document.createElement('div');
        div.className = 'log-line';
        div.innerHTML = "✧ " + text;
        scanLog.appendChild(div);
        scanLog.scrollTop = scanLog.scrollHeight;
        await new Promise(r => setTimeout(r, 800));
      }

      // === INICIO DEL SCRAPER INTEGRADO ===
      let principalNumbers = [];
      let principalSuper = null;
      let revanchaNumbers = [];
      let revanchaSuper = null;
      let scraperSuccess = false;

      try {
        const response = await fetch('https://api.allorigins.win/get?url=' + encodeURIComponent('https://baloto.com/resultados'));
        if (response.ok) {
          const data = await response.json();
          const parser = new DOMParser();
          const doc = parser.parseFromString(data.contents, 'text/html');
          
          let allNumbers = [];
          let allSupers = [];
          
          doc.querySelectorAll('.yellow-ball-results, .yellow-ball, .red-ball, .pink-ball-results, .red-ball-big').forEach(el => {
              const numText = el.textContent.trim();
              const num = parseInt(numText, 10);
              if (!isNaN(num)) {
                  if (el.classList.contains('red-ball') || el.classList.contains('pink-ball-results') || el.classList.contains('red-ball-big')) {
                      allSupers.push(num);
                  } else {
                      allNumbers.push(num);
                  }
              }
          });
          
          if(allNumbers.length >= 10 && allSupers.length >= 2) {
            principalNumbers = allNumbers.slice(0, 5);
            principalSuper = allSupers[0];
            revanchaNumbers = allNumbers.slice(5, 10);
            revanchaSuper = allSupers[1];
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
         div.innerHTML = "✧ [REVELACIÓN] Principal: " + principalNumbers.join('-') + " S:" + principalSuper + " | Revancha: " + revanchaNumbers.join('-') + " S:" + revanchaSuper;
         scanLog.appendChild(div);
      } else {
         const div = document.createElement('div');
         div.className = 'log-line warn';
         div.innerHTML = "✧ [MISTERIO] La niebla oculta el plano terrenal. Accediendo a los Registros Akáshicos...";
         scanLog.appendChild(div);
      }
      scanLog.scrollTop = scanLog.scrollHeight;
      await new Promise(r => setTimeout(r, 1500));

      const lateLines = [
        "<span class='warn'>[VISIÓN] Escuchando los susurros de los viajeros del tiempo...</span>",
        "Trazando el hilo dorado de tus arcanos elegidos...",
        "<span class='err'>El tejido del destino se encuentra inmaculado. La profecía es clara.</span>",
        "Sopesando el equilibrio entre el Sol y la Luna...",
        "Manifestando tu fortuna celestial..."
      ];

      for (let text of lateLines) {
        const div = document.createElement('div');
        div.className = 'log-line';
        div.innerHTML = "✧ " + text;
        scanLog.appendChild(div);
        scanLog.scrollTop = scanLog.scrollHeight;
        await new Promise(r => setTimeout(r, 600 + Math.random() * 400));
      }

      setTimeout(() => {
        scanner.classList.add('hidden');
        showOracleResults(scraperSuccess);
      }, 1500);
    }

    function showOracleResults(scraperSuccess) {
      document.getElementById('phase-result').classList.remove('hidden');

      const phrase = ORACLE_PHRASES[Math.floor(Math.random() * ORACLE_PHRASES.length)];
      document.getElementById('oracle-text').textContent = phrase;

      // Compute standard formula from cards
      const results = computeNumbers(selectedCards);

      // Numbers display
      const numDisp = document.getElementById('numbers-display');
      numDisp.innerHTML = '';
      
      // Calculate a fun probability based on card values and scraper success
      let baseProb = 80 + (results[5].num / 16) * 10 + (Math.random() * 4.9);
      let probPrin = baseProb;
      let probRev = baseProb + (Math.random() * 6 - 3); // Slightly different probability for Revancha
      
      if(scraperSuccess) {
         probPrin = Math.min(99.99, probPrin + 1.5);
         probRev = Math.min(99.99, probRev + 2.1);
      }
      
      const probsContainer = document.createElement('div');
      probsContainer.style.display = 'flex';
      probsContainer.style.justifyContent = 'center';
      probsContainer.style.gap = '20px';
      probsContainer.style.flexWrap = 'wrap';
      
      const probBadgePrin = document.createElement('div');
      probBadgePrin.className = 'probability-badge';
      probBadgePrin.innerHTML = `🌟 Baloto Principal: ${probPrin.toFixed(2)}% 🌟`;
      probsContainer.appendChild(probBadgePrin);
      
      const probBadgeRev = document.createElement('div');
      probBadgeRev.className = 'probability-badge revancha';
      probBadgeRev.innerHTML = `🔥 Baloto Revancha: ${probRev.toFixed(2)}% 🔥`;
      probsContainer.appendChild(probBadgeRev);
      
      numDisp.appendChild(probsContainer);
      
      const ballsContainer = document.createElement('div');
      ballsContainer.style.display = 'flex';
      ballsContainer.style.justifyContent = 'center';
      ballsContainer.style.flexWrap = 'wrap';
      ballsContainer.style.gap = '15px';
      ballsContainer.style.marginTop = '20px';
      
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
    
    # We replace from "async function revealOracle() {" down to the end of showOracleResults
    pattern = re.compile(r'([ \t]*async function revealOracle\(\) \{.*?\n[ \t]*\})(?=\s*/\* ========================================================\s*RESTART)', re.DOTALL)
    if pattern.search(content):
        content = pattern.sub(new_js, content)
    else:
        print("Could not match the JS block. Make sure regex is correct.")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_code()
