# Enhanced Builder for taboo.html with 100% Guaranteed Visual Card Art

with open('taboo_78_data.js', 'r', encoding='utf-8') as f:
    tarot_data_js = f.read()

template = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TABOO: El Sexto Sentido | Tarot Baloto (Edición 78 Cartas)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=IM+Fell+English+SC&family=Press+Start+2P&display=swap" rel="stylesheet">
  <style>
    :root {
      --nes-bg: #07050d;
      --nes-purple: #1f1135;
      --nes-green: #39ff14;
      --nes-yellow: #f8e71c;
      --nes-red: #ff3366;
      --nes-cyan: #00ffff;
      --nes-gold: #c8a951;
      --card-bg: #f4e8c1;
      --card-back-w: 62px;
      --card-back-h: 98px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--nes-bg);
      color: #fff;
      font-family: 'Press Start 2P', monospace, sans-serif;
      min-height: 100vh;
      overflow-x: hidden;
      position: relative;
      user-select: none;
    }

    /* CRT scanline effect */
    body::before {
      content: " ";
      display: block;
      position: fixed;
      top: 0; left: 0; bottom: 0; right: 0;
      background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.22) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.02), rgba(0, 255, 0, 0.01), rgba(0, 255, 0, 0.02));
      z-index: 999;
      background-size: 100% 3px, 6px 100%;
      pointer-events: none;
      opacity: 0.65;
    }

    /* Background stars */
    .starfield {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 0;
    }
    .star {
      position: absolute;
      background-color: #ffffff;
      border-radius: 50%;
      opacity: 0.6;
      animation: twinkle 3s infinite ease-in-out;
    }
    @keyframes twinkle {
      0%, 100% { opacity: 0.2; transform: scale(0.8); }
      50% { opacity: 1; transform: scale(1.2); }
    }

    /* Main Container */
    .game-container {
      position: relative;
      z-index: 10;
      max-width: 1200px;
      margin: 0 auto;
      padding: 15px 15px 120px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    /* Top Sound & Return Bar */
    .top-bar {
      width: 100%;
      max-width: 1100px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 15px;
      flex-wrap: wrap;
      gap: 10px;
    }
    .bar-btn {
      font-family: 'Press Start 2P', monospace;
      font-size: 0.6rem;
      background: rgba(12, 8, 24, 0.85);
      color: var(--nes-gold);
      border: 2px solid var(--nes-gold);
      padding: 7px 12px;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }
    .bar-btn:hover {
      background: var(--nes-gold);
      color: #000;
      box-shadow: 0 0 10px rgba(200, 169, 81, 0.6);
    }
    .bar-btn.active-glow {
      border-color: var(--nes-green);
      color: var(--nes-green);
      animation: pulseGlow 1.5s infinite alternate;
    }
    @keyframes pulseGlow {
      from { box-shadow: 0 0 5px var(--nes-green); }
      to { box-shadow: 0 0 15px var(--nes-green); }
    }

    /* Header */
    .taboo-header {
      text-align: center;
      margin-bottom: 20px;
    }
    .taboo-logo {
      display: inline-flex;
      align-items: center;
      gap: 15px;
      margin-bottom: 8px;
    }
    .taboo-sun {
      font-size: 2.2rem;
      filter: drop-shadow(0 0 10px #ffcc00);
      animation: pulseSun 2s infinite alternate ease-in-out;
    }
    @keyframes pulseSun {
      from { transform: scale(1) rotate(0deg); }
      to { transform: scale(1.15) rotate(15deg); }
    }
    h1.taboo-title {
      font-size: 2.2rem;
      letter-spacing: 4px;
      color: var(--nes-yellow);
      text-shadow: 4px 4px #8b0000, 0 0 20px rgba(255, 51, 102, 0.8);
      display: inline-block;
    }
    .taboo-subtitle {
      font-size: 0.62rem;
      color: var(--nes-cyan);
      letter-spacing: 2px;
      margin-top: 6px;
      text-shadow: 2px 2px #000;
    }

    /* NES Frame Box */
    .nes-box {
      background: rgba(10, 8, 20, 0.95);
      border: 4px solid #fff;
      box-shadow: 0 0 0 4px #000, 0 0 25px rgba(200, 169, 81, 0.3);
      border-radius: 4px;
      padding: 25px;
      width: 100%;
      max-width: 680px;
      margin: 15px auto;
    }
    .nes-box.wide {
      max-width: 1150px;
      padding: 20px;
    }

    /* Form Fields */
    .field-group {
      margin-bottom: 20px;
      text-align: left;
    }
    .field-label {
      display: block;
      font-size: 0.75rem;
      color: var(--nes-green);
      margin-bottom: 8px;
      letter-spacing: 1px;
    }
    .nes-input, .nes-select {
      width: 100%;
      background: #000;
      border: 3px solid var(--nes-gold);
      color: #fff;
      padding: 12px;
      font-family: 'Press Start 2P', monospace;
      font-size: 0.8rem;
      outline: none;
      transition: border-color 0.2s;
    }
    .nes-input:focus, .nes-select:focus {
      border-color: var(--nes-cyan);
      box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
    }

    /* Buttons */
    .btn-nes {
      font-family: 'Press Start 2P', monospace;
      font-size: 0.8rem;
      background: linear-gradient(180deg, #ff3366 0%, #aa0033 100%);
      color: #fff;
      border: 3px solid #fff;
      box-shadow: 0 4px 0 #4a0011;
      padding: 12px 20px;
      cursor: pointer;
      display: inline-block;
      text-align: center;
      text-decoration: none;
      transition: all 0.1s;
      letter-spacing: 1px;
    }
    .btn-nes:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 0 #4a0011, 0 0 15px rgba(255, 51, 102, 0.8);
      background: linear-gradient(180deg, #ff5588 0%, #cc0044 100%);
    }
    .btn-nes:active {
      transform: translateY(2px);
      box-shadow: 0 2px 0 #4a0011;
    }
    .btn-nes.gold {
      background: linear-gradient(180deg, #f8e71c 0%, #c89c0a 100%);
      color: #000;
      box-shadow: 0 4px 0 #684f00;
    }
    .btn-nes.gold:hover {
      background: linear-gradient(180deg, #fff04d 0%, #e0b010 100%);
      box-shadow: 0 6px 0 #684f00, 0 0 15px rgba(248, 231, 28, 0.8);
    }
    .btn-nes.cyan {
      background: linear-gradient(180deg, #00f0ff 0%, #0088aa 100%);
      color: #000;
      box-shadow: 0 4px 0 #004455;
    }
    .btn-nes.cyan:hover {
      background: linear-gradient(180deg, #33f6ff 0%, #00aacc 100%);
      box-shadow: 0 6px 0 #004455, 0 0 15px rgba(0, 240, 255, 0.8);
    }

    /* Status Bar */
    .status-badge {
      display: inline-block;
      padding: 8px 16px;
      background: #110826;
      border: 2px dashed var(--nes-green);
      color: var(--nes-green);
      font-size: 0.72rem;
      margin-bottom: 12px;
      letter-spacing: 1px;
    }

    /* 78-CARD GRID DISPLAY - MYSTERIOUS & HIDDEN */
    #cards-deal-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      justify-content: center;
      max-width: 1100px;
      margin: 10px auto;
      max-height: 520px;
      overflow-y: auto;
      padding: 14px 6px;
      border: 2px solid #221535;
      background: rgba(5, 3, 10, 0.85);
      border-radius: 4px;
    }
    #cards-deal-grid::-webkit-scrollbar {
      width: 8px;
    }
    #cards-deal-grid::-webkit-scrollbar-track {
      background: #000;
    }
    #cards-deal-grid::-webkit-scrollbar-thumb {
      background: var(--nes-gold);
    }

    .deal-card-slot {
      cursor: pointer;
      position: relative;
      width: var(--card-back-w);
      height: var(--card-back-h);
      transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275), filter 0.2s;
      flex-shrink: 0;
    }
    .deal-card-slot:hover {
      transform: translateY(-8px) scale(1.12);
      filter: drop-shadow(0 0 10px var(--nes-yellow));
      z-index: 50;
    }
    .deal-card-slot.selected {
      filter: drop-shadow(0 0 14px var(--nes-green));
      transform: scale(1.05);
    }
    .deal-card-slot.selected .card-back-face {
      border-color: var(--nes-green);
      background: linear-gradient(135deg, #0d381e 0%, #061f10 50%, #0d381e 100%);
    }
    .deal-card-slot .card-order-tag {
      position: absolute;
      top: -6px;
      right: -6px;
      background: var(--nes-green);
      color: #000;
      font-size: 0.6rem;
      font-weight: bold;
      padding: 3px 6px;
      border-radius: 3px;
      border: 1px solid #fff;
      z-index: 20;
      box-shadow: 0 0 8px var(--nes-green);
    }

    /* Shuffle Animation */
    @keyframes shuffleCardAnim {
      0% { transform: scale(1) translateY(0); }
      25% { transform: scale(0.9) translateY(-14px) rotate(5deg); }
      50% { transform: scale(1.08) translateY(8px) rotate(-5deg); }
      75% { transform: scale(0.95) translateY(-4px); }
      100% { transform: scale(1) translateY(0); }
    }
    .card-shuffling {
      animation: shuffleCardAnim 0.38s ease-in-out;
    }

    /* Card Back Design */
    .card-back-face {
      width: 100%;
      height: 100%;
      background: linear-gradient(135deg, #6b1a1a 0%, #3a0a0a 50%, #6b1a1a 100%);
      border: 2px solid var(--nes-gold);
      border-radius: 4px;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
      box-sizing: border-box;
    }
    .card-back-face::before {
      content: '';
      position: absolute;
      inset: 3px;
      border: 1px solid rgba(200, 169, 81, 0.5);
      border-radius: 2px;
      background: repeating-linear-gradient(45deg,
        transparent, transparent 3px,
        rgba(200, 169, 81, 0.12) 3px, rgba(200, 169, 81, 0.12) 5px);
    }
    .card-back-face .symbol {
      font-size: 1.5rem;
      color: rgba(200, 169, 81, 0.7);
      z-index: 1;
    }

    /* MARSEILLE FULL CARD (IN CELTIC CROSS) */
    .marseille-card {
      width: 80px;
      height: 130px;
      background-color: var(--card-bg);
      border: 2px solid #1a1a1a;
      border-radius: 4px;
      padding: 4px;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.8);
      position: relative;
    }
    .marseille-card::before {
      content: '';
      position: absolute;
      top: 2px; left: 2px; right: 2px; bottom: 2px;
      border: 1px solid #1a1a1a;
      pointer-events: none;
    }
    .marseille-num {
      font-family: 'Cinzel', serif;
      font-weight: bold;
      font-size: 0.82rem;
      color: #1a1a1a;
      border-bottom: 1px solid #1a1a1a;
      width: 100%;
      text-align: center;
      padding-bottom: 1px;
    }
    .marseille-art {
      font-family: 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji', sans-serif;
      color: #1a1a1a !important;
      font-size: 2.2rem;
      line-height: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      height: 56px;
      text-align: center;
      user-select: none;
    }
    .marseille-art svg {
      filter: drop-shadow(1px 1px 2px rgba(0, 0, 0, 0.3));
    }
    .marseille-name {
      font-family: 'IM Fell English SC', serif;
      font-size: 0.48rem;
      color: #1a1a1a;
      border-top: 1px solid #1a1a1a;
      width: 100%;
      text-align: center;
      padding-top: 2px;
      text-transform: uppercase;
      line-height: 1;
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
    }

    /* Screen 3: Celtic Cross Layout */
    .cross-stage {
      position: relative;
      width: 100%;
      max-width: 950px;
      height: 720px;
      margin: 10px auto 30px;
      background: radial-gradient(circle at center, rgba(35, 15, 60, 0.5) 0%, rgba(5, 3, 10, 0.95) 75%);
      border: 3px solid #332255;
      border-radius: 8px;
    }

    .cross-slot {
      position: absolute;
      width: 80px;
      height: 130px;
      transform-origin: center center;
      transition: transform 0.4s ease, filter 0.3s;
    }
    .cross-slot.active-card {
      filter: drop-shadow(0 0 25px var(--nes-green)) drop-shadow(0 0 8px #fff);
      z-index: 200 !important;
      transform: scale(1.15) !important;
    }
    .cross-slot.crossed {
      transform: rotate(90deg);
      z-index: 25;
    }
    .cross-slot.active-card.crossed {
      transform: rotate(90deg) scale(1.15) !important;
    }

    .pos-label {
      position: absolute;
      bottom: -22px;
      left: 50%;
      transform: translateX(-50%);
      font-size: 0.5rem;
      white-space: nowrap;
      color: var(--nes-yellow);
      background: #000;
      padding: 2px 4px;
      border: 1px solid #555;
      letter-spacing: 0.5px;
    }

    /* Celtic Cross Coordinates */
    #cross-pos-1 { left: 300px; top: 270px; z-index: 10; }
    #cross-pos-2 { left: 300px; top: 270px; }
    #cross-pos-3 { left: 300px; top: 480px; z-index: 10; }
    #cross-pos-4 { left: 120px; top: 270px; z-index: 10; }
    #cross-pos-5 { left: 300px; top: 60px;  z-index: 10; }
    #cross-pos-6 { left: 480px; top: 270px; z-index: 10; }

    #cross-pos-7  { left: 740px; top: 510px; z-index: 10; }
    #cross-pos-8  { left: 740px; top: 360px; z-index: 10; }
    #cross-pos-9  { left: 740px; top: 210px; z-index: 10; }
    #cross-pos-10 { left: 740px; top: 60px;  z-index: 10; }

    /* Card Reversed style */
    .is-reversed .marseille-card {
      transform: rotate(180deg);
    }
    .reversed-badge {
      position: absolute;
      top: -8px;
      left: 50%;
      transform: translateX(-50%);
      background: #cc0000;
      color: #fff;
      font-size: 0.45rem;
      padding: 2px 4px;
      border: 1px solid #fff;
      z-index: 15;
    }

    /* NES Dialogue Box */
    .dialogue-panel {
      position: fixed;
      bottom: 12px;
      left: 50%;
      transform: translateX(-50%);
      width: 94%;
      max-width: 980px;
      background: #000;
      border: 4px solid #fff;
      box-shadow: 0 0 0 4px #000, 0 0 30px rgba(0, 0, 0, 0.95);
      padding: 16px 20px;
      z-index: 500;
      min-height: 140px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .dialogue-header {
      font-size: 0.72rem;
      color: var(--nes-yellow);
      margin-bottom: 8px;
      border-bottom: 2px dashed #444;
      padding-bottom: 6px;
      display: flex;
      justify-content: space-between;
    }
    .dialogue-body {
      font-size: 0.72rem;
      line-height: 1.6;
      color: #fff;
      min-height: 60px;
      letter-spacing: 0.5px;
      white-space: pre-wrap;
      word-break: break-word;
    }
    .dialogue-footer {
      display: flex;
      justify-content: flex-end;
      align-items: center;
      margin-top: 10px;
      gap: 12px;
    }
    .blink-arrow {
      font-size: 0.9rem;
      color: var(--nes-green);
      animation: blink 0.8s infinite;
    }
    @keyframes blink {
      0%, 100% { opacity: 1; }
      50% { opacity: 0; }
    }

    /* Final Result Modal */
    .result-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.88);
      z-index: 600;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px;
    }
    .baloto-balls-row {
      display: flex;
      justify-content: center;
      gap: 12px;
      margin: 25px 0;
      flex-wrap: wrap;
    }
    .b-ball {
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background: radial-gradient(circle at 35% 35%, #fff 0%, #e6b800 45%, #8a6700 100%);
      color: #000;
      font-size: 1.1rem;
      font-weight: bold;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.8), inset 0 2px 4px rgba(255, 255, 255, 0.8);
      border: 2px solid #fff;
    }
    .b-ball.superbalota {
      background: radial-gradient(circle at 35% 35%, #ff9999 0%, #ff0033 45%, #880011 100%);
      color: #fff;
      border: 2px solid #ffcccc;
    }

    .hidden {
      display: none !important;
    }

    /* Responsive adjustments */
    @media (max-width: 820px) {
      h1.taboo-title { font-size: 1.4rem; }
      .cross-stage {
        height: 600px;
        transform: scale(0.75);
        transform-origin: top center;
        margin-bottom: -120px;
      }
      .dialogue-panel {
        padding: 12px;
        min-height: 120px;
      }
      .dialogue-body {
        font-size: 0.65rem;
      }
    }
  </style>
</head>
<body>

  <!-- Starfield background -->
  <div class="starfield" id="stars-container"></div>

  <div class="game-container">
    
    <!-- Top Navigation & 32-Bit Sound Control Bar -->
    <div class="top-bar">
      <a href="/" class="bar-btn">◀ VOLVER A BALOTO</a>
      <div style="display: flex; gap: 8px; flex-wrap: wrap;">
        <button id="btn-music-toggle" class="bar-btn active-glow">🎵 BGM 32-BIT: ON</button>
        <button id="btn-sound-toggle" class="bar-btn">🔊 SFX: ON</button>
      </div>
    </div>

    <!-- Header -->
    <header class="taboo-header">
      <div class="taboo-logo">
        <span class="taboo-sun">☀️</span>
        <h1 class="taboo-title">TABOO</h1>
        <span class="taboo-sun">☀️</span>
      </div>
      <div class="taboo-subtitle">THE SIXTH SENSE • EL SEXTO SENTIDO (78 CARTAS)</div>
    </header>

    <!-- SCREEN 1: CONSULTATION INPUT -->
    <div id="screen-intro" class="nes-box">
      <div style="text-align: center; margin-bottom: 20px;">
        <p style="color: var(--nes-yellow); font-size: 0.8rem; line-height: 1.8;">
          BIENVENIDO AL ORÁCULO DE TABOO.<br>
          LOS 78 ARCANOS DEL UNIVERSO TE ESPERAN.
        </p>
      </div>

      <div class="field-group">
        <label class="field-label" for="user-name">NOMBRE DEL CONSULTANTE:</label>
        <input type="text" id="user-name" class="nes-input" placeholder="INGRESA TU NOMBRE" maxlength="20" autocomplete="off">
      </div>

      <div class="field-group">
        <label class="field-label" for="user-dob">FECHA DE NACIMIENTO:</label>
        <input type="date" id="user-dob" class="nes-input" value="1995-07-15">
      </div>

      <div class="field-group">
        <label class="field-label" for="user-focus">INTENCIÓN O ASUNTO DE LA CONSULTA:</label>
        <select id="user-focus" class="nes-select">
          <option value="GENERAL">DESTINO GENERAL Y FORTUNA</option>
          <option value="BALOTO">NÚMEROS SAGRADOS DEL BALOTO</option>
          <option value="DINERO">PROSPERIDAD Y RIQUEZA</option>
          <option value="AMOR">VÍNCULOS Y RELACIONES</option>
          <option value="DECISION">BIFURCACIÓN Y CONSEJO</option>
        </select>
      </div>

      <div style="text-align: center; margin-top: 30px;">
        <button id="btn-start-deal" class="btn-nes gold">⚡ CONJURAR EL DESTINO ⚡</button>
      </div>
    </div>

    <!-- SCREEN 2: DEALING & CARD SELECTION (78 OCULTAS + BARAJAR) -->
    <div id="screen-deal" class="nes-box wide hidden">
      <div style="text-align: center;">
        <div id="selection-counter" class="status-badge">
          SELECCIONA 10 CARTAS DEL MAZO OCULTO (0 / 10)
        </div>
        <p style="font-size: 0.62rem; color: #bbb; margin-bottom: 12px;">
          Las 78 cartas yacen boca abajo ante ti. Confía en tu intuición y sexto sentido.
        </p>

        <!-- Shuffle Deck Action & Counter -->
        <div style="margin: 10px 0 16px; display: flex; justify-content: center; align-items: center; gap: 15px; flex-wrap: wrap;">
          <button id="btn-shuffle-deck" class="btn-nes cyan">🔀 BARAJAR CARTAS</button>
          <span id="shuffle-counter-badge" class="bar-btn" style="cursor: default; pointer-events: none; border-color: var(--nes-cyan); color: var(--nes-cyan);">
            BARAJADO: 1 VEZ
          </span>
        </div>
      </div>

      <!-- The 78-Card Deck Grid (Pure Mystery - No Names Visible) -->
      <div id="cards-deal-grid"></div>

      <!-- Action Confirmation Button once 10 cards selected -->
      <div style="text-align: center; margin-top: 15px;">
        <button id="btn-confirm-deal" class="btn-nes gold hidden">✨ DISPONER LA CRUZ CELTA (10/10) ✨</button>
      </div>
    </div>

    <!-- SCREEN 3: CELTIC CROSS DISPLAY -->
    <div id="screen-cross" class="hidden" style="width: 100%;">
      <div style="text-align: center; margin-bottom: 10px;">
        <div class="status-badge" style="border-color: var(--nes-yellow); color: var(--nes-yellow);">
          DISPOSICIÓN: LA CRUZ CELTA DE TABOO
        </div>
      </div>

      <!-- The Cross Board -->
      <div class="cross-stage" id="cross-board">
        <!-- 10 position slots created dynamically -->
      </div>
    </div>

  </div>

  <!-- FIXED NES DIALOGUE BOX (ACTIVE DURING CROSS READING) -->
  <div id="dialogue-box" class="dialogue-panel hidden">
    <div class="dialogue-header">
      <span id="diag-pos-title">POSICIÓN I: EL PRESENTE</span>
      <span id="diag-step-counter">1 / 10</span>
    </div>
    <div class="dialogue-body" id="diag-text-content"></div>
    <div class="dialogue-footer">
      <span class="blink-arrow">▶</span>
      <button id="btn-next-step" class="btn-nes" style="padding: 8px 16px; font-size: 0.7rem;">SIGUIENTE CARTA</button>
    </div>
  </div>

  <!-- FINAL SUMMARY MODAL -->
  <div id="modal-final-summary" class="result-overlay hidden">
    <div class="nes-box" style="max-width: 650px; text-align: center; border-color: var(--nes-yellow);">
      <h2 style="color: var(--nes-yellow); font-size: 1.15rem; margin-bottom: 15px; text-shadow: 2px 2px #ff0055;">
        ★ DESTINO CONSUMADO ★
      </h2>
      <p id="summary-user-text" style="font-size: 0.72rem; color: var(--nes-cyan); line-height: 1.8; margin-bottom: 20px;">
        El Sexto Sentido ha hablado para ti.
      </p>

      <div style="background: rgba(0,0,0,0.7); padding: 15px; border: 2px dashed var(--nes-green); margin-bottom: 20px;">
        <div style="font-size: 0.7rem; color: var(--nes-green); margin-bottom: 10px;">
          🔮 TUS 5 NÚMEROS DE LA SUERTE Y SUPERBALOTA:
        </div>
        <div class="baloto-balls-row" id="final-lucky-balls">
          <!-- Lucky balls dynamically placed -->
        </div>
        <div style="font-size: 0.6rem; color: #bbb; line-height: 1.6;" id="final-advice-text">
          Que la fortuna del cosmos guíe tus jugadas en el Baloto.
        </div>
      </div>

      <div style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
        <button id="btn-restart-game" class="btn-nes">NUEVA CONSULTA</button>
        <a href="/" class="btn-nes gold">IR AL DASHBOARD</a>
      </div>
    </div>
  </div>

  <!-- EMBEDDED COMPLETE 78 TAROT CARDS DATA -->
  <script>
__TAROT_DATA__
  </script>

  <!-- 32-BIT SOUND ENGINE & TABOO GAME LOGIC -->
  <script>
    /* ========================================================
       32-BIT CONSOLE AUDIO ENGINE (WEB AUDIO API)
       FM Synthesis + Ambient Polyphony + Stereo Spatial Delay
       ======================================================== */
    class Console32BitAudio {
      constructor() {
        this.ctx = null;
        this.musicEnabled = true;
        this.sfxEnabled = true;
        this.bgmPlaying = false;
        this.currentStep = 0;
        this.timer = null;

        this.progression = [
          {
            bass: 73.42, // D2
            pad: [146.83, 220.00, 261.63, 329.63], // D3, A3, C4, E4
            arp: [587.33, 659.25, 698.46, 880.00, 1046.50, 880.00, 698.46, 659.25]
          },
          {
            bass: 58.27, // Bb1
            pad: [116.54, 174.61, 233.08, 293.66], // Bb2, F3, Bb3, D4
            arp: [466.16, 587.33, 698.46, 739.99, 932.33, 739.99, 698.46, 587.33]
          },
          {
            bass: 49.00, // G1
            pad: [98.00, 146.83, 196.00, 293.66], // G2, D3, G3, D4
            arp: [392.00, 466.16, 587.33, 698.46, 880.00, 698.46, 587.33, 466.16]
          },
          {
            bass: 55.00, // A1
            pad: [110.00, 164.81, 220.00, 277.18], // A2, E3, A3, C#4
            arp: [440.00, 554.37, 659.25, 739.99, 880.00, 739.99, 659.25, 554.37]
          }
        ];
      }

      init() {
        if (!this.ctx) {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          if (AudioContext) {
            this.ctx = new AudioContext();

            this.delayNode = this.ctx.createDelay();
            this.delayNode.delayTime.value = 0.32;

            this.delayFeedback = this.ctx.createGain();
            this.delayFeedback.gain.value = 0.38;

            this.delayFilter = this.ctx.createBiquadFilter();
            this.delayFilter.type = 'lowpass';
            this.delayFilter.frequency.value = 1600;

            this.delayNode.connect(this.delayFilter);
            this.delayFilter.connect(this.delayFeedback);
            this.delayFeedback.connect(this.delayNode);

            this.wetGain = this.ctx.createGain();
            this.wetGain.gain.value = 0.28;
            this.delayFilter.connect(this.wetGain);
            this.wetGain.connect(this.ctx.destination);
          }
        }
        if (this.ctx && this.ctx.state === 'suspended') {
          this.ctx.resume();
        }
      }

      startBGM() {
        this.init();
        if (this.bgmPlaying || !this.musicEnabled) return;
        this.bgmPlaying = true;
        this.currentStep = 0;
        this.scheduleNextBar();
      }

      stopBGM() {
        this.bgmPlaying = false;
        if (this.timer) {
          clearTimeout(this.timer);
          this.timer = null;
        }
      }

      scheduleNextBar() {
        if (!this.bgmPlaying || !this.musicEnabled) return;
        const chord = this.progression[this.currentStep % this.progression.length];
        const barDuration = 3.6;

        this.playBass(chord.bass, barDuration);

        chord.pad.forEach((freq, idx) => {
          this.playPadVoice(freq, barDuration, 0.035 - idx * 0.005);
        });

        const arpNotes = chord.arp;
        const stepTime = barDuration / arpNotes.length;
        arpNotes.forEach((f, i) => {
          setTimeout(() => {
            if (this.bgmPlaying && this.musicEnabled) {
              this.playFmBell(f, 0.45, 0.04);
            }
          }, i * stepTime * 1000);
        });

        this.currentStep++;
        this.timer = setTimeout(() => {
          this.scheduleNextBar();
        }, barDuration * 1000);
      }

      playFmBell(freq, duration = 0.5, vol = 0.05) {
        if (!this.ctx || this.ctx.state !== 'running') return;
        try {
          const now = this.ctx.currentTime;
          const carrier = this.ctx.createOscillator();
          const modulator = this.ctx.createOscillator();
          const modGain = this.ctx.createGain();
          const outGain = this.ctx.createGain();

          carrier.type = 'sine';
          carrier.frequency.setValueAtTime(freq, now);

          modulator.type = 'sine';
          modulator.frequency.setValueAtTime(freq * 2.01, now);
          modGain.gain.setValueAtTime(freq * 1.5, now);
          modGain.gain.exponentialRampToValueAtTime(0.01, now + duration);

          modulator.connect(modGain);
          modGain.connect(carrier.frequency);

          outGain.gain.setValueAtTime(vol, now);
          outGain.gain.exponentialRampToValueAtTime(0.0001, now + duration);

          carrier.connect(outGain);
          outGain.connect(this.ctx.destination);
          if (this.delayNode) outGain.connect(this.delayNode);

          carrier.start(now);
          modulator.start(now);
          carrier.stop(now + duration);
          modulator.stop(now + duration);
        } catch(e) {}
      }

      playPadVoice(freq, duration = 3.6, vol = 0.03) {
        if (!this.ctx || this.ctx.state !== 'running') return;
        try {
          const now = this.ctx.currentTime;
          const osc1 = this.ctx.createOscillator();
          const osc2 = this.ctx.createOscillator();
          const filter = this.ctx.createBiquadFilter();
          const gain = this.ctx.createGain();

          osc1.type = 'triangle';
          osc2.type = 'sawtooth';

          osc1.frequency.setValueAtTime(freq, now);
          osc2.frequency.setValueAtTime(freq * 1.003, now);

          filter.type = 'lowpass';
          filter.frequency.setValueAtTime(450, now);
          filter.frequency.exponentialRampToValueAtTime(950, now + duration * 0.5);
          filter.frequency.exponentialRampToValueAtTime(350, now + duration);

          gain.gain.setValueAtTime(0.0001, now);
          gain.gain.linearRampToValueAtTime(vol, now + 0.8);
          gain.gain.linearRampToValueAtTime(vol * 0.7, now + duration * 0.7);
          gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);

          osc1.connect(filter);
          osc2.connect(filter);
          filter.connect(gain);
          gain.connect(this.ctx.destination);
          if (this.delayNode) gain.connect(this.delayNode);

          osc1.start(now);
          osc2.start(now);
          osc1.stop(now + duration);
          osc2.stop(now + duration);
        } catch(e) {}
      }

      playBass(freq, duration = 3.6) {
        if (!this.ctx || this.ctx.state !== 'running') return;
        try {
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const filter = this.ctx.createBiquadFilter();
          const gain = this.ctx.createGain();

          osc.type = 'triangle';
          osc.frequency.setValueAtTime(freq, now);

          filter.type = 'lowpass';
          filter.frequency.setValueAtTime(220, now);

          gain.gain.setValueAtTime(0.001, now);
          gain.gain.linearRampToValueAtTime(0.08, now + 0.2);
          gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);

          osc.connect(filter);
          filter.connect(gain);
          gain.connect(this.ctx.destination);

          osc.start(now);
          osc.stop(now + duration);
        } catch(e) {}
      }

      shuffleSound() {
        if (!this.sfxEnabled) return;
        this.init();
        const notes = [329.63, 440.00, 587.33, 659.25, 880.00, 1174.66, 880.00, 659.25];
        notes.forEach((f, idx) => {
          setTimeout(() => {
            this.playFmBell(f, 0.14, 0.05);
            this.typeTick();
          }, idx * 40);
        });
      }

      cardSelectSound() {
        if (!this.sfxEnabled) return;
        this.init();
        this.playFmBell(880, 0.4, 0.08);
        setTimeout(() => this.playFmBell(1318.51, 0.5, 0.07), 70);
      }

      cardDeselectSound() {
        if (!this.sfxEnabled) return;
        this.init();
        this.playFmBell(440, 0.2, 0.06);
      }

      cardHoverSound() {
        if (!this.sfxEnabled) return;
        this.init();
        this.playFmBell(1760, 0.08, 0.015);
      }

      revealSound() {
        if (!this.sfxEnabled) return;
        this.init();
        const notes = [587.33, 739.99, 880.00, 1174.66];
        notes.forEach((f, idx) => {
          setTimeout(() => this.playFmBell(f, 0.6, 0.07), idx * 80);
        });
      }

      typeTick() {
        if (!this.sfxEnabled) return;
        this.init();
        if (!this.ctx) return;
        try {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'square';
          osc.frequency.setValueAtTime(320 + Math.random() * 60, this.ctx.currentTime);
          gain.gain.setValueAtTime(0.02, this.ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + 0.025);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start();
          osc.stop(this.ctx.currentTime + 0.025);
        } catch(e) {}
      }

      clickSound() {
        if (!this.sfxEnabled) return;
        this.init();
        this.playFmBell(659.25, 0.1, 0.05);
      }

      victoryFanfare() {
        if (!this.sfxEnabled) return;
        this.init();
        const chords = [
          [587.33, 739.99, 880.00],
          [659.25, 830.61, 987.77],
          [880.00, 1108.73, 1318.51],
          [1174.66, 1479.98, 1760.00]
        ];
        chords.forEach((chord, i) => {
          setTimeout(() => {
            chord.forEach(f => this.playFmBell(f, 1.2, 0.07));
          }, i * 220);
        });
      }
    }

    const audio = new Console32BitAudio();

    const musicBtn = document.getElementById('btn-music-toggle');
    const soundBtn = document.getElementById('btn-sound-toggle');

    musicBtn.addEventListener('click', () => {
      audio.init();
      audio.musicEnabled = !audio.musicEnabled;
      if (audio.musicEnabled) {
        musicBtn.innerText = '🎵 BGM 32-BIT: ON';
        musicBtn.classList.add('active-glow');
        audio.startBGM();
      } else {
        musicBtn.innerText = '🔇 BGM 32-BIT: OFF';
        musicBtn.classList.remove('active-glow');
        audio.stopBGM();
      }
    });

    soundBtn.addEventListener('click', () => {
      audio.init();
      audio.sfxEnabled = !audio.sfxEnabled;
      soundBtn.innerText = audio.sfxEnabled ? '🔊 SFX: ON' : '🔇 SFX: OFF';
    });

    /* ========================================================
       STARFIELD INITIALIZER
       ======================================================== */
    (function createStars() {
      const cont = document.getElementById('stars-container');
      if (!cont) return;
      for (let i = 0; i < 90; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        const size = Math.random() < 0.2 ? 3 : Math.random() < 0.6 ? 2 : 1;
        star.style.width = size + 'px';
        star.style.height = size + 'px';
        star.style.left = Math.random() * 100 + '%';
        star.style.top = Math.random() * 100 + '%';
        star.style.animationDelay = (Math.random() * 4) + 's';
        cont.appendChild(star);
      }
    })();

    /* ========================================================
       CELTIC CROSS 10 POSITIONS DEFINITION
       ======================================================== */
    const CELTIC_POSITIONS = [
      {
        id: 1,
        title: "EL PRESENTE",
        coords: "cross-pos-1",
        desc: "El núcleo de tu situación actual, tu energía predominante y el punto de partida de la consulta."
      },
      {
        id: 2,
        title: "EL DESAFÍO",
        coords: "cross-pos-2",
        crossed: true,
        desc: "La fuerza que cruza tu camino. El obstáculo inmediato o la lección crucial a conquistar."
      },
      {
        id: 3,
        title: "LA BASE (LO INCONSCIENTE)",
        coords: "cross-pos-3",
        desc: "Los cimientos ocultos, las raíces del pasado y las motivaciones profundas que sostienen el presente."
      },
      {
        id: 4,
        title: "EL PASADO RECIENTE",
        coords: "cross-pos-4",
        desc: "Acontecimientos o energías que acaban de terminar pero cuyo eco aún influye directamente."
      },
      {
        id: 5,
        title: "LA CORONA (LO CONSCIENTE)",
        coords: "cross-pos-5",
        desc: "Tus aspiraciones conscientes, tu meta suprema y lo mejor que puedes esperar alcanzar."
      },
      {
        id: 6,
        title: "EL FUTURO CERCANO",
        coords: "cross-pos-6",
        desc: "La energía inminente. El siguiente giro del destino en los días y semanas por venir."
      },
      {
        id: 7,
        title: "EL CONSULTANTE",
        coords: "cross-pos-7",
        desc: "Tu postura interna, tu estado mental y emocional, y cómo te proyectas ante este trance."
      },
      {
        id: 8,
        title: "EL ENTORNO",
        coords: "cross-pos-8",
        desc: "Las influencias del mundo exterior: la familia, amigos, rivales o el ambiente que te rodea."
      },
      {
        id: 9,
        title: "ESPERANZAS Y TEMORES",
        coords: "cross-pos-9",
        desc: "Las emociones más secretas: aquello que anhelas desesperadamente o el miedo que temes enfrentar."
      },
      {
        id: 10,
        title: "EL RESULTADO FINAL",
        coords: "cross-pos-10",
        desc: "La culminación del camino si las energías actuales siguen su curso. El destino revelado por Taboo."
      }
    ];

    /* ========================================================
       GAME STATE
       ======================================================== */
    let userName = "CONSULTANTE";
    let userDob = "1995-07-15";
    let userFocus = "GENERAL";
    let full78Deck = [];
    let selectedCards = [];
    let currentReadingStep = 0;
    let typeWriterInterval = null;
    let isTyping = false;
    let currentFullText = "";
    let shuffleCount = 1;

    // Helper: generate 100% visible, high-contrast Marseille card art
    function getCardFrontHTML(card) {
      let artHTML = '';
      
      if (card.arcana === 'Mayor') {
        let extraStyle = '';
        if (['✝️'].includes(card.art)) extraStyle = 'color: #8b0000;';
        else if (['⚖️', '💀', '⚔️'].includes(card.art)) extraStyle = 'color: #1a1a1a;';
        else if (['🕯️', '☀️'].includes(card.art)) extraStyle = 'color: #d35400;';
        else if (['☸️'].includes(card.art)) extraStyle = 'color: #1f618d;';
        else if (['⭐'].includes(card.art)) extraStyle = 'color: #f39c12;';
        else extraStyle = 'color: #1a1a1a;';

        artHTML = `<span class="emoji-art" style="${extraStyle}">${card.art}</span>`;
      } else {
        const isCourt = card.pipVal > 10;
        const suitName = card.suit ? card.suit.name : 'Bastos';

        if (isCourt) {
          let figureIcon = '👱‍♂️';
          if (card.pipVal === 12) figureIcon = '🐎';
          if (card.pipVal === 13) figureIcon = '👸';
          if (card.pipVal === 14) figureIcon = '🤴';

          let suitIcon = '🌿';
          if (suitName === 'Copas') suitIcon = '🏆';
          else if (suitName === 'Espadas') suitIcon = '⚔️';
          else if (suitName === 'Oros') suitIcon = '🟡';

          artHTML = `<span class="court-art" style="font-size: 1.5rem; color:#1a1a1a; display:inline-flex; align-items:center;">${figureIcon}<span style="font-size: 0.95rem; margin-left:2px;">${suitIcon}</span></span>`;
        } else {
          // Pip cards (As - 10) with 100% universal crisp Marseille SVGs
          if (suitName === 'Bastos') {
            artHTML = `<svg class="tarot-svg" width="36" height="36" viewBox="0 0 36 36"><line x1="8" y1="28" x2="28" y2="8" stroke="#7a3e14" stroke-width="4.5" stroke-linecap="round"/><path d="M15 17c2-4 6-4 8-2s2 6-2 8" fill="#2ecc71"/><path d="M12 21c-3 1-4 4-2 6s5 2 6-1" fill="#27ae60"/><circle cx="28" cy="8" r="3.5" fill="#e67e22"/></svg>`;
          } else if (suitName === 'Copas') {
            artHTML = `<svg class="tarot-svg" width="36" height="36" viewBox="0 0 36 36"><path d="M11 7h14v10c0 4-3 7-7 7s-7-3-7-7V7z" fill="#f39c12" stroke="#b78c06" stroke-width="1.5"/><path d="M18 24v5M13 29h10" stroke="#b78c06" stroke-width="2.5" stroke-linecap="round"/><ellipse cx="18" cy="7" rx="7" ry="2" fill="#e67e22"/><circle cx="18" cy="14" r="2.5" fill="#c0392b"/></svg>`;
          } else if (suitName === 'Espadas') {
            artHTML = `<svg class="tarot-svg" width="36" height="36" viewBox="0 0 36 36"><line x1="9" y1="27" x2="27" y2="9" stroke="#2c3e50" stroke-width="3" stroke-linecap="round"/><line x1="7" y1="23" x2="13" y2="29" stroke="#7f8c8d" stroke-width="4"/><circle cx="7" cy="29" r="2" fill="#f39c12"/><line x1="9" y1="9" x2="27" y2="27" stroke="#2980b9" stroke-width="3" stroke-linecap="round"/><line x1="13" y1="7" x2="7" y2="13" stroke="#7f8c8d" stroke-width="4"/><circle cx="7" cy="7" r="2" fill="#f39c12"/></svg>`;
          } else if (suitName === 'Oros') {
            artHTML = `<svg class="tarot-svg" width="36" height="36" viewBox="0 0 36 36"><circle cx="18" cy="18" r="15" fill="#f1c40f" stroke="#b78c06" stroke-width="2"/><circle cx="18" cy="18" r="10.5" fill="none" stroke="#b78c06" stroke-width="1.5" stroke-dasharray="3,2"/><text x="18" y="23" font-size="14" text-anchor="middle" fill="#7d5f04" font-weight="bold">✦</text></svg>`;
          }
        }
      }

      const roman = card.numeral ? card.numeral : (card.pipVal ? String(card.pipVal) : '');
      const name = card.marseilleName || card.name;

      return `
        <div class="marseille-card">
          <div class="marseille-num">${roman}</div>
          <div class="marseille-art">${artHTML}</div>
          <div class="marseille-name">${name}</div>
        </div>
      `;
    }

    // Helper: generate card back HTML (Completely hidden & anonymous)
    function getCardBackHTML() {
      return `
        <div class="card-back-face">
          <span class="symbol">✦</span>
        </div>
      `;
    }

    /* ========================================================
       FLOW STEP 1: CONJURATION
       ======================================================== */
    document.getElementById('btn-start-deal').addEventListener('click', () => {
      audio.init();
      audio.clickSound();
      audio.startBGM();

      const nameInput = document.getElementById('user-name').value.trim();
      if (nameInput) userName = nameInput.toUpperCase();
      userDob = document.getElementById('user-dob').value || "1995-07-15";
      userFocus = document.getElementById('user-focus').value;

      document.getElementById('screen-intro').classList.add('hidden');
      initDealScreen();
    });

    /* ========================================================
       FLOW STEP 2: DEAL SCREEN & DISPLAYING 78 HIDDEN CARDS
       ======================================================== */
    function initDealScreen() {
      document.getElementById('screen-deal').classList.remove('hidden');
      selectedCards = [];
      shuffleCount = 1;
      updateShuffleBadge();
      updateSelectionUI();

      full78Deck = [...FULL_DECK];
      full78Deck.sort(() => Math.random() - 0.5);

      render78CardsGrid();
    }

    function render78CardsGrid(triggerAnim = false) {
      const grid = document.getElementById('cards-deal-grid');
      grid.innerHTML = '';

      full78Deck.forEach((card, idx) => {
        const slot = document.createElement('div');
        slot.className = 'deal-card-slot';
        slot.dataset.id = card.id;

        if (triggerAnim) {
          slot.classList.add('card-shuffling');
          slot.style.animationDelay = (Math.random() * 0.2) + 's';
        }

        const selIdx = selectedCards.findIndex(c => c.id === card.id);
        const isSelected = selIdx !== -1;

        slot.innerHTML = `
          ${getCardBackHTML()}
          ${isSelected ? `<div class="card-order-tag">${selIdx + 1}</div>` : ''}
        `;

        if (isSelected) {
          slot.classList.add('selected');
        }

        slot.addEventListener('mouseenter', () => {
          if (!slot.classList.contains('selected')) {
            audio.cardHoverSound();
          }
        });

        slot.addEventListener('click', () => {
          handleCardClick(card, slot);
        });

        grid.appendChild(slot);
      });
    }

    function handleCardClick(card, slot) {
      const selIdx = selectedCards.findIndex(c => c.id === card.id);

      if (selIdx !== -1) {
        selectedCards.splice(selIdx, 1);
        audio.cardDeselectSound();
        render78CardsGrid();
        updateSelectionUI();
        return;
      }

      if (selectedCards.length >= 10) {
        audio.clickSound();
        return;
      }

      const isReversed = Math.random() < 0.35;
      selectedCards.push({
        ...card,
        isReversed: isReversed
      });

      audio.cardSelectSound();
      render78CardsGrid();
      updateSelectionUI();
    }

    function updateSelectionUI() {
      const count = selectedCards.length;
      const counterEl = document.getElementById('selection-counter');
      const confirmBtn = document.getElementById('btn-confirm-deal');

      if (count < 10) {
        counterEl.innerText = `SELECCIONA 10 CARTAS DEL MAZO OCULTO (${count} / 10)`;
        counterEl.style.borderColor = 'var(--nes-green)';
        counterEl.style.color = 'var(--nes-green)';
        confirmBtn.classList.add('hidden');
      } else {
        counterEl.innerText = `¡10 CARTAS CONJURADAS! LISTO PARA EL LANCE`;
        counterEl.style.borderColor = 'var(--nes-yellow)';
        counterEl.style.color = 'var(--nes-yellow)';
        confirmBtn.classList.remove('hidden');
      }
    }

    function updateShuffleBadge() {
      const badge = document.getElementById('shuffle-counter-badge');
      if (badge) {
        badge.innerText = `BARAJADO: ${shuffleCount} ${shuffleCount === 1 ? 'VEZ' : 'VECES'}`;
      }
    }

    document.getElementById('btn-shuffle-deck').addEventListener('click', () => {
      audio.shuffleSound();
      shuffleCount++;
      updateShuffleBadge();

      selectedCards = [];
      updateSelectionUI();

      full78Deck.sort(() => Math.random() - 0.5);
      render78CardsGrid(true);
    });

    document.getElementById('btn-confirm-deal').addEventListener('click', () => {
      audio.clickSound();
      initCelticCrossScreen();
    });

    /* ========================================================
       FLOW STEP 3: CELTIC CROSS DISPOSITION
       ======================================================== */
    function initCelticCrossScreen() {
      document.getElementById('screen-deal').classList.add('hidden');
      document.getElementById('screen-cross').classList.remove('hidden');
      document.getElementById('dialogue-box').classList.remove('hidden');

      const board = document.getElementById('cross-board');
      board.innerHTML = '';

      CELTIC_POSITIONS.forEach((pos, idx) => {
        const cardData = selectedCards[idx];
        const cardSlot = document.createElement('div');
        cardSlot.className = 'cross-slot';
        cardSlot.id = pos.coords;
        if (pos.crossed) cardSlot.classList.add('crossed');

        cardSlot.innerHTML = `
          ${getCardBackHTML()}
          <div class="pos-label">POS ${idx + 1}</div>
        `;

        board.appendChild(cardSlot);
      });

      currentReadingStep = 0;
      setTimeout(revealCurrentStep, 600);
    }

    /* ========================================================
       FLOW STEP 4: SEQUENTIAL READING & TYPEWRITER
       ======================================================== */
    function revealCurrentStep() {
      if (currentReadingStep >= 10) {
        finishReading();
        return;
      }

      const pos = CELTIC_POSITIONS[currentReadingStep];
      const card = selectedCards[currentReadingStep];
      const slotEl = document.getElementById(pos.coords);

      audio.revealSound();

      document.querySelectorAll('.cross-slot').forEach(el => el.classList.remove('active-card'));
      slotEl.classList.add('active-card');

      const revClass = card.isReversed ? 'is-reversed' : '';
      const revBadge = card.isReversed ? '<div class="reversed-badge">INVERTIDA</div>' : '';
      
      slotEl.innerHTML = `
        <div class="${revClass}" style="position:relative;">
          ${revBadge}
          ${getCardFrontHTML(card)}
        </div>
        <div class="pos-label">POS ${pos.id}: ${pos.title.substring(0, 10)}</div>
      `;

      let cardSignificado = "";
      let cardConsejo = "";

      if (card.arcana === 'Mayor') {
        const dict = card.isReversed ? majorMeaningsRev : majorMeanings;
        const info = dict[card.id] || {
          significado: "Las fuerzas arcanas mayores trazan un hito en tu destino.",
          consejo: "Sintoniza tu intuición con este símbolo sagrado."
        };
        cardSignificado = info.significado;
        cardConsejo = info.consejo;
      } else {
        const suitName = card.suit ? card.suit.name : 'Bastos';
        const dict = card.isReversed ? minorMeaningsRev : minorMeanings;
        const info = dict[suitName] || {
          significado: "La energía de este arcano menor rige los aspectos cotidianos y prácticos.",
          consejo: "Aplica la templanza de este elemento en tus acciones diarias."
        };
        cardSignificado = `${card.name} (${card.arcana}): ${info.significado}`;
        cardConsejo = info.consejo;
      }

      const cardStateTitle = card.name + (card.isReversed ? ' [INVERTIDA]' : ' [AL DERECHO]');
      document.getElementById('diag-pos-title').innerText = `POSICIÓN ${pos.id}: ${pos.title}`;
      document.getElementById('diag-step-counter').innerText = `${pos.id} / 10`;

      const fullMessage = "CARTA: " + cardStateTitle.toUpperCase() + "\\n" +
                          "ORÁCULO: " + pos.desc + "\\n\\n" +
                          "REVELACIÓN: " + cardSignificado + "\\n\\n" +
                          "CONSEJO DE TABOO: " + cardConsejo;

      typeWriter(fullMessage, 'diag-text-content');
    }

    function typeWriter(text, elementId) {
      const el = document.getElementById(elementId);
      el.textContent = '';
      if (typeWriterInterval) clearInterval(typeWriterInterval);

      currentFullText = text;
      isTyping = true;
      let i = 0;

      typeWriterInterval = setInterval(() => {
        if (i < text.length) {
          el.textContent += text.charAt(i);
          if (i % 2 === 0 && text.charAt(i) !== ' ' && text.charAt(i) !== '\\n') {
            audio.typeTick();
          }
          i++;
        } else {
          clearInterval(typeWriterInterval);
          isTyping = false;
        }
      }, 16);
    }

    document.getElementById('btn-next-step').addEventListener('click', () => {
      if (isTyping) {
        clearInterval(typeWriterInterval);
        document.getElementById('diag-text-content').textContent = currentFullText;
        isTyping = false;
        audio.clickSound();
      } else {
        audio.clickSound();
        currentReadingStep++;
        revealCurrentStep();
      }
    });

    /* ========================================================
       FLOW STEP 5: FINAL RESOLUTION & BALOTO PREDICTION
       ======================================================== */
    function finishReading() {
      audio.victoryFanfare();
      document.getElementById('dialogue-box').classList.add('hidden');
      
      let seed = 0;
      const dobClean = userDob.replace(/[^0-9]/g, '');
      for (let ch of dobClean) seed += parseInt(ch, 10);
      selectedCards.forEach((c, idx) => {
        seed += (c.id + 1) * (idx + 3);
      });

      const luckyNumbers = new Set();
      let salt = 1;
      while (luckyNumbers.size < 5) {
        const num = ((seed * salt * 7 + salt * 13) % 43) + 1;
        luckyNumbers.add(num);
        salt++;
      }
      const sortedBalls = Array.from(luckyNumbers).sort((a, b) => a - b);
      const superBalota = ((seed * 11) % 16) + 1;

      const ballsCont = document.getElementById('final-lucky-balls');
      ballsCont.innerHTML = '';
      sortedBalls.forEach(n => {
        const b = document.createElement('div');
        b.className = 'b-ball';
        b.innerText = n;
        ballsCont.appendChild(b);
      });

      const sb = document.createElement('div');
      sb.className = 'b-ball superbalota';
      sb.title = 'Superbalota';
      sb.innerText = superBalota;
      ballsCont.appendChild(sb);

      document.getElementById('summary-user-text').textContent = 
        "CONSULTANTE: " + userName + "\\n" +
        "LOS 78 ARCANOS DE TABOO HAN ALINEADO LAS ENERGÍAS OCULTAS DE TU DESTINO.";

      document.getElementById('modal-final-summary').classList.remove('hidden');
    }

    document.getElementById('btn-restart-game').addEventListener('click', () => {
      audio.clickSound();
      document.getElementById('modal-final-summary').classList.add('hidden');
      document.getElementById('screen-cross').classList.add('hidden');
      document.getElementById('screen-deal').classList.add('hidden');
      document.getElementById('screen-intro').classList.remove('hidden');
      document.querySelectorAll('.cross-slot').forEach(el => el.classList.remove('active-card'));
    });
  </script>
</body>
</html>
"""

final_html = template.replace('__TAROT_DATA__', tarot_data_js)

with open('taboo.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Generated taboo.html with 100% visible card arts ({len(final_html)} bytes).")
