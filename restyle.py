import re

def restyle_code():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update CSS
    old_css = """    /* ==============================
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
    }"""
    
    new_css = """    /* ==============================
       MYSTIC ORACLE SCANNER
    ============================== */
    #temporal-scanner {
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      background: radial-gradient(circle at center, rgba(30,10,40,0.95), rgba(0,0,0,0.98));
      z-index: 10000;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: #e5c07b;
      font-family: 'IM Fell English SC', serif;
      transition: opacity 0.8s;
    }
    #temporal-scanner.hidden {
      display: none;
      opacity: 0;
    }
    .glitch-text {
      font-size: 2.2rem;
      margin-bottom: 25px;
      animation: breathe 3s ease-in-out infinite;
      text-align: center;
      font-family: 'Cinzel Decorative', cursive;
      text-shadow: 0 0 15px rgba(229,192,123,0.6);
    }
    .scan-log {
      width: 90%;
      max-width: 600px;
      height: 280px;
      border: 1px solid rgba(229,192,123,0.4);
      border-radius: 10px;
      padding: 20px;
      overflow-y: hidden;
      font-size: 1.2rem;
      text-align: center;
      background: rgba(20,10,30,0.7);
      box-shadow: inset 0 0 30px rgba(0,0,0,0.8);
      position: relative;
    }
    .scan-log::before {
      content: '✧';
      position: absolute;
      top: 5px; left: 50%;
      transform: translateX(-50%);
      color: #e5c07b;
      opacity: 0.5;
    }
    .log-line {
      margin: 12px 0;
      opacity: 0;
      animation: mysticFadeIn 1.5s forwards;
      letter-spacing: 1px;
    }
    .log-line.warn { color: #d4af37; text-shadow: 0 0 8px #d4af37; }
    .log-line.err { color: #cd5c5c; text-shadow: 0 0 8px #cd5c5c; }
    .log-line.success { color: #f8e297; text-shadow: 0 0 10px #f8e297; }
    @keyframes breathe {
      0%, 100% { transform: scale(1); opacity: 0.8; }
      50% { transform: scale(1.02); opacity: 1; text-shadow: 0 0 25px rgba(229,192,123,0.9); }
    }
    @keyframes mysticFadeIn {
      0% { opacity: 0; transform: translateY(10px); filter: blur(4px); }
      100% { opacity: 1; transform: translateY(0); filter: blur(0); }
    }"""
    
    content = content.replace(old_css, new_css)

    # 2. Update HTML
    old_html = """    <!-- === TEMPORAL SCANNER MODAL === -->
    <div id="temporal-scanner" class="hidden">
      <div class="glitch-text">INICIANDO ESCÁNER TEMPORAL...</div>
      <div class="scan-log" id="scan-log"></div>
    </div>"""
    
    new_html = """    <!-- === MYSTIC ORACLE SCANNER MODAL === -->
    <div id="temporal-scanner" class="hidden">
      <div class="glitch-text">✦ INVOCANDO EL ORÁCULO DE MARSELLA ✦</div>
      <div class="scan-log" id="scan-log"></div>
    </div>"""
    
    content = content.replace(old_html, new_html)

    # 3. Update JS Text arrays
    # lines
    content = content.replace(
        '"Estableciendo conexión con la Deep Web...",',
        '"Alineando los astros en la bóveda celeste...",'
    )
    content = content.replace(
        '"Hackeando el portal temporal de Baloto...",',
        '"Consultando los registros etéreos del destino...",'
    )
    content = content.replace(
        '"Extrayendo últimos resultados oficiales en vivo..."',
        '"Invocando la esencia de los números sagrados..."'
    )
    content = content.replace(
        'div.innerHTML = "> " + text;',
        'div.innerHTML = "✧ " + text;'
    )

    # scraper success log
    content = content.replace(
        '> [ÉXITO] Resultados reales extraídos:',
        '✧ [REVELACIÓN] Los números han descendido del plano terrenal:'
    )
    content = content.replace(
        '> [ADVERTENCIA] Defensas cuánticas bloquearon el Scraper. Usando memoria Akáshica...',
        '✧ [MISTERIO] La niebla oculta el plano terrenal. Accediendo a los Registros Akáshicos...'
    )

    # lateLines
    content = content.replace(
        "<span class='warn'>[ALERTA] Buscando ecos temporales y paradojas de viajeros del tiempo...</span>",
        "<span class='warn'>[VISIÓN] Escuchando los susurros de los viajeros del tiempo...</span>"
    )
    content = content.replace(
        "Analizando patrones cuánticos de tus cartas elegidas...",
        "Trazando el hilo dorado de tus arcanos elegidos..."
    )
    content = content.replace(
        "<span class='err'>Ninguna anomalía temporal detectada. El tejido del tiempo está intacto.</span>",
        "<span class='err'>El tejido del destino se encuentra inmaculado. La profecía es clara.</span>"
    )
    content = content.replace(
        "Calculando algoritmo de probabilidad de números fríos/calientes...",
        "Sopesando el equilibrio entre el Sol y la Luna..."
    )
    content = content.replace(
        "Generando Alineación Mística...",
        "Manifestando tu fortuna celestial..."
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    restyle_code()
