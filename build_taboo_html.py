import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace <title>
html = re.sub(r'<title>.*?</title>', '<title>TABOO: El Sexto Sentido</title>', html)

# Add Press Start font to head
html = html.replace('</head>', '<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">\n</head>')

body_start = html.find('<body>') + len('<body>')
script_start = html.rfind('<script>')

ui_html = """
<style>
    /* Taboo overrides */
    body {
        background-color: #000 !important;
        background-image: none !important;
        color: #33ff33 !important;
        font-family: 'Press Start 2P', monospace !important;
    }
    h1.taboo-title {
        color: #ff3366;
        text-shadow: 2px 2px #000, 0 0 10px #ff3366;
        text-align: center;
        font-size: 2rem;
        margin-top: 40px;
        margin-bottom: 40px;
        font-family: 'Press Start 2P', monospace;
    }
    .nes-container {
        border: 4px solid #33ff33;
        padding: 20px;
        background: rgba(0, 20, 0, 0.8);
        width: 90%;
        max-width: 800px;
        margin: 0 auto;
        box-sizing: border-box;
    }
    input.taboo-input, button.taboo-btn {
        font-family: 'Press Start 2P', monospace;
        background: #000;
        color: #33ff33;
        border: 2px solid #33ff33;
        padding: 10px;
        margin: 10px 0;
        width: 100%;
        box-sizing: border-box;
    }
    button.taboo-btn {
        cursor: pointer;
        background: #33ff33;
        color: #000;
        transition: all 0.2s;
    }
    button.taboo-btn:hover {
        background: #ff3366;
        border-color: #ff3366;
        color: #fff;
    }
    .hidden { display: none !important; }
    
    #cards-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        justify-content: center;
        margin-top: 20px;
    }
    .grid-card-wrapper {
        transform: scale(0.6);
        margin: -30px -20px;
        cursor: pointer;
        transition: transform 0.2s, filter 0.2s;
    }
    .grid-card-wrapper:hover {
        transform: scale(0.65) translateY(-10px);
        filter: drop-shadow(0 0 10px #ff3366);
    }
    .grid-card-wrapper.selected {
        opacity: 0.3;
        pointer-events: none;
    }

    #celtic-cross {
        position: relative;
        width: 100%;
        max-width: 800px;
        height: 700px;
        margin: 0 auto;
    }
    
    .cross-pos {
        position: absolute;
        transform: scale(0.6);
        transition: all 0.5s;
        cursor: pointer;
    }
    .cross-pos.active-glow {
        filter: drop-shadow(0 0 20px #33ff33);
        z-index: 100;
    }
    
    #pos-1 { left: 200px; top: 250px; z-index: 10; }
    #pos-2 { left: 200px; top: 250px; transform: scale(0.6) rotate(90deg); z-index: 11; }
    #pos-3 { left: 200px; top: 450px; }
    #pos-4 { left: 20px; top: 250px; }
    #pos-5 { left: 200px; top: 50px; }
    #pos-6 { left: 380px; top: 250px; }
    
    #pos-7 { left: 580px; top: 450px; }
    #pos-8 { left: 580px; top: 320px; }
    #pos-9 { left: 580px; top: 190px; }
    #pos-10 { left: 580px; top: 60px; }

    #dialog-box {
        border: 4px solid #fff;
        background: #000;
        color: #fff;
        padding: 20px;
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        max-width: 800px;
        font-size: 0.8rem;
        line-height: 1.5;
        z-index: 1000;
        font-family: 'Press Start 2P', monospace;
    }
    
    .typewriter-text {
        min-height: 80px;
    }
</style>

    <h1 class="taboo-title">TABOO</h1>

    <div id="screen-intro" class="nes-container">
        <p>BIENVENIDO A TABOO: EL SEXTO SENTIDO.</p>
        <p>INGRESA TUS DATOS PARA ABRIR EL PORTAL.</p>
        <br>
        <label>NOMBRE:</label>
        <input type="text" id="user-name" class="taboo-input" placeholder="TU NOMBRE">
        <label>FECHA DE NACIMIENTO:</label>
        <input type="date" id="user-dob" class="taboo-input">
        <br><br>
        <button id="btn-start" class="taboo-btn">CONJURAR</button>
    </div>

    <div id="screen-deal" class="hidden">
        <div class="nes-container" style="text-align:center;">
            <p>EL MAZO HA SIDO BARAJADO.</p>
            <p id="selection-status">SELECCIONA 10 CARTAS (0/10)</p>
        </div>
        <div id="cards-grid"></div>
    </div>

    <div id="screen-cross" class="hidden" style="width:100%;">
        <div id="celtic-cross"></div>
    </div>
    
    <div id="dialog-box" class="hidden">
        <div class="typewriter-text" id="dialog-text"></div>
        <button id="btn-next-read" class="taboo-btn hidden" style="margin-top:10px;">CONTINUAR</button>
    </div>
"""

taboo_js = """
// Taboo Logic overrides
window.onload = function() {
    const ls = document.getElementById('loading-screen');
    if (ls) ls.style.display = 'none';
};

const POSITIONS = [
    { id: 1, name: "EL PRESENTE" },
    { id: 2, name: "EL DESAFÍO" },
    { id: 3, name: "LA BASE" },
    { id: 4, name: "EL PASADO" },
    { id: 5, name: "LA CORONA" },
    { id: 6, name: "EL FUTURO CERCANO" },
    { id: 7, name: "TÚ" },
    { id: 8, name: "EL ENTORNO" },
    { id: 9, name: "ESPERANZAS Y TEMORES" },
    { id: 10, name: "EL RESULTADO FINAL" }
];

function generateTarotHTML(c, isFaceUp) {
    if (!isFaceUp) {
        return `<div class="marseille-card"><div class="back-cover" style="width:100%; height:100%; background: repeating-linear-gradient(45deg, #0f0c29, #0f0c29 10px, #302b63 10px, #302b63 20px);"></div></div>`;
    }
    const revMark = c.rev ? '<span style="color:#ff4d4d;font-size:0.8em"> (Inv)</span>' : '';
    const revStyle = c.rev ? 'transform: rotate(180deg); transform-origin: center center;' : '';
    return `
        <div class="marseille-card" style="${revStyle} margin:0 auto; display: flex;">
            <div class="marseille-num">${c.numeral || ''}</div>
            <div class="marseille-art">${c.art}</div>
            <div class="marseille-name">${c.marseilleName || c.name}</div>
        </div>
        <div class="mini-name" style="color:#fff; text-align:center; font-family:'Cinzel',serif; margin-top:10px; font-size:16px;">${c.name}${revMark}</div>
    `;
}

let selectedTabooCards = [];
let currentReadIndex = 0;
let tabooUserName = "";

document.getElementById('btn-start').addEventListener('click', () => {
    tabooUserName = document.getElementById('user-name').value.trim().toUpperCase() || "VIAJERO";
    document.getElementById('screen-intro').classList.add('hidden');
    initDealScreen();
});

function initDealScreen() {
    document.getElementById('screen-deal').classList.remove('hidden');
    const grid = document.getElementById('cards-grid');
    
    let deck = [...MAJOR];
    deck.sort(() => Math.random() - 0.5);
    
    deck.forEach(c => {
        const wrapper = document.createElement('div');
        wrapper.className = 'grid-card-wrapper';
        wrapper.innerHTML = generateTarotHTML(c, false);
        
        wrapper.addEventListener('click', () => {
            if(selectedTabooCards.length < 10) {
                wrapper.classList.add('selected');
                const isRev = Math.random() > 0.5;
                c.rev = isRev;
                selectedTabooCards.push(c);
                document.getElementById('selection-status').innerText = `SELECCIONA 10 CARTAS (${selectedTabooCards.length}/10)`;
                
                if(selectedTabooCards.length === 10) {
                    setTimeout(initCrossScreen, 1000);
                }
            }
        });
        grid.appendChild(wrapper);
    });
}

function initCrossScreen() {
    document.getElementById('screen-deal').classList.add('hidden');
    document.getElementById('screen-cross').classList.remove('hidden');
    const cross = document.getElementById('celtic-cross');
    
    selectedTabooCards.forEach((c, i) => {
        const wrapper = document.createElement('div');
        wrapper.className = 'cross-pos';
        wrapper.id = 'pos-' + (i+1);
        wrapper.innerHTML = generateTarotHTML(c, false);
        cross.appendChild(wrapper);
    });
    
    startReading();
}

function startReading() {
    document.getElementById('dialog-box').classList.remove('hidden');
    readNextCard();
}

let typeWriterInterval = null;

function typeWriter(text, elementId, callback) {
    const el = document.getElementById(elementId);
    el.innerHTML = '';
    let i = 0;
    if(typeWriterInterval) clearInterval(typeWriterInterval);
    
    typeWriterInterval = setInterval(() => {
        el.innerHTML += text.charAt(i);
        i++;
        if(i >= text.length) {
            clearInterval(typeWriterInterval);
            if(callback) callback();
        }
    }, 30);
}

function readNextCard() {
    if(currentReadIndex >= 10) {
        typeWriter(`LA LECTURA HA CONCLUIDO, ${tabooUserName}... EL DESTINO ESTÁ EN TUS MANOS.`, 'dialog-text', () => {
            const btn = document.getElementById('btn-next-read');
            btn.innerText = "VOLVER AL INICIO";
            btn.classList.remove('hidden');
            btn.onclick = () => window.location.href = '/';
        });
        return;
    }
    
    const pos = currentReadIndex + 1;
    const c = selectedTabooCards[currentReadIndex];
    const posInfo = POSITIONS[currentReadIndex];
    
    document.querySelectorAll('.cross-pos').forEach(el => el.classList.remove('active-glow'));
    const cardEl = document.getElementById('pos-' + pos);
    cardEl.classList.add('active-glow');
    
    cardEl.innerHTML = generateTarotHTML(c, true);
    
    const dict = c.rev ? majorMeaningsRev : majorMeanings;
    const info = dict[c.id];
    const cardName = c.name + (c.rev ? " (INVERTIDA)" : "");
    
    const text = `POSICIÓN ${pos}: ${posInfo.name}\\n\\nCARTA: ${cardName}\\n\\n${info.significado}\\n\\nCONSEJO: ${info.consejo}`;
    const htmlText = text.replace(/\\n/g, '<br>');
    
    document.getElementById('btn-next-read').classList.add('hidden');
    
    typeWriter(htmlText, 'dialog-text', () => {
        document.getElementById('btn-next-read').classList.remove('hidden');
    });
    
    currentReadIndex++;
}

document.getElementById('btn-next-read').addEventListener('click', readNextCard);
"""

final_html = html[:body_start] + ui_html + html[script_start:]
final_html = final_html.replace('</script>', taboo_js + '\n</script>')

with open('taboo.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("taboo.html rebuilt cleanly.")
