// 78 Cards + Meanings extracted from index.html
const MAJOR = [
      { id: 0, name: 'Le Mat (El Loco)', marseilleName: 'Le Mat', numeral: '', art: '🤡', arcana: 'Mayor', v: 0 },
      { id: 1, name: 'Le Bateleur (El Mago)', marseilleName: 'Le Bateleur', numeral: 'I', art: '🎩', arcana: 'Mayor', v: 1 },
      { id: 2, name: 'La Papesse (La Papisa)', marseilleName: 'La Papesse', numeral: 'II', art: '📖', arcana: 'Mayor', v: 2 },
      { id: 3, name: "L'Impératrice (La Emperatriz)", marseilleName: "L'Impératrice", numeral: 'III', art: '👑', arcana: 'Mayor', v: 3 },
      { id: 4, name: "L'Empereur (El Emperador)", marseilleName: "L'Empereur", numeral: 'IIII', art: '⚔️', arcana: 'Mayor', v: 4 },
      { id: 5, name: 'Le Pape (El Papa)', marseilleName: 'Le Pape', numeral: 'V', art: '✝️', arcana: 'Mayor', v: 5 },
      { id: 6, name: "L'Amoureux (Los Enamorados)", marseilleName: "L'Amoureux", numeral: 'VI', art: '💑', arcana: 'Mayor', v: 6 },
      { id: 7, name: 'Le Chariot (El Carro)', marseilleName: 'Le Chariot', numeral: 'VII', art: '🏆', arcana: 'Mayor', v: 7 },
      { id: 8, name: 'La Justice (La Justicia)', marseilleName: 'La Justice', numeral: 'VIII', art: '⚖️', arcana: 'Mayor', v: 8 },
      { id: 9, name: "L'Hermite (El Ermitaño)", marseilleName: "L'Hermite", numeral: 'VIIII', art: '🕯️', arcana: 'Mayor', v: 9 },
      { id: 10, name: 'La Roue de Fortune (La Rueda)', marseilleName: 'La Roue', numeral: 'X', art: '☸️', arcana: 'Mayor', v: 10 },
      { id: 11, name: 'La Force (La Fuerza)', marseilleName: 'La Force', numeral: 'XI', art: '🦁', arcana: 'Mayor', v: 11 },
      { id: 12, name: 'Le Pendu (El Colgado)', marseilleName: 'Le Pendu', numeral: 'XII', art: '🔄', arcana: 'Mayor', v: 12 },
      { id: 13, name: '(La Muerte)', marseilleName: '', numeral: 'XIII', art: '💀', arcana: 'Mayor', v: 13 },
      { id: 14, name: 'Tempérance (La Templanza)', marseilleName: 'Tempérance', numeral: 'XIIII', art: '🏺', arcana: 'Mayor', v: 14 },
      { id: 15, name: 'Le Diable (El Diablo)', marseilleName: 'Le Diable', numeral: 'XV', art: '😈', arcana: 'Mayor', v: 15 },
      { id: 16, name: 'La Maison Dieu (La Torre)', marseilleName: 'La Maison Dieu', numeral: 'XVI', art: '🗼', arcana: 'Mayor', v: 16 },
      { id: 17, name: "L'Étoile (La Estrella)", marseilleName: "L'Étoile", numeral: 'XVII', art: '⭐', arcana: 'Mayor', v: 17 },
      { id: 18, name: 'La Lune (La Luna)', marseilleName: 'La Lune', numeral: 'XVIII', art: '🌙', arcana: 'Mayor', v: 18 },
      { id: 19, name: 'Le Soleil (El Sol)', marseilleName: 'Le Soleil', numeral: 'XIX', art: '☀️', arcana: 'Mayor', v: 19 },
      { id: 20, name: 'Le Jugement (El Juicio)', marseilleName: 'Le Jugement', numeral: 'XX', art: '📯', arcana: 'Mayor', v: 20 },
      { id: 21, name: 'Le Monde (El Mundo)', marseilleName: 'Le Monde', numeral: 'XXI', art: '🌍', arcana: 'Mayor', v: 21 },
    ];

    // Palos del Arcana Menor y sus multiplicadores místicos
    const SUITS = [
      { name: 'Bastos', sym: '🪄', short: 'B', mult: 2, pip: ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Sota', 'Caballo', 'Reina', 'Rey'] },
      { name: 'Copas', sym: '🏆', short: 'C', mult: 3, pip: ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Sota', 'Caballo', 'Reina', 'Rey'] },
      { name: 'Espadas', sym: '⚔️', short: 'E', mult: 4, pip: ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Sota', 'Caballo', 'Reina', 'Rey'] },
      { name: 'Oros', sym: '🪙', short: 'O', mult: 5, pip: ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Sota', 'Caballo', 'Reina', 'Rey'] },
    ];

        const romanMap = { 1: 'I', 2: 'II', 3: 'III', 4: 'IIII', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'VIIII', 10: 'X' };
    const nameMap = { 'Bastos': 'Bâtons', 'Copas': 'Coupes', 'Espadas': 'Épées', 'Oros': 'Deniers' };
    
    const MINOR = [];
    SUITS.forEach(suit => {
      suit.pip.forEach((pip, i) => {
        const numVal = i + 1; // 1..14
        let numeral = '';
        if (numVal <= 10) numeral = romanMap[numVal];
        
        let courtName = pip;
        if (numVal === 11) courtName = 'Valet';
        if (numVal === 12) courtName = 'Chevalier';
        if (numVal === 13) courtName = 'Reyne';
        if (numVal === 14) courtName = 'Roy';
        
        const isCourt = numVal > 10;
        
        MINOR.push({
          id: 22 + MINOR.length,
          name: `${pip} de ${suit.name}`,
          marseilleName: (isCourt ? `${courtName} de ${nameMap[suit.name]}` : `${pip} de ${nameMap[suit.name]}`),
          numeral: numeral,
          art: suit.sym,
          arcana: `Menor · ${suit.name}`,
          suit: suit,
          pipVal: numVal,
          v: (numVal * suit.mult) % 47 // base value (not final number)
        });
      });
    });

    const FULL_DECK = [...MAJOR, ...MINOR]; // 78 cards

    /* ========================================================
       MÍSTICAS NUEVAS FUNCIONES
       ======================================================== */
    function getMoonPhase() {
      const date = new Date();
      // Un cálculo aproximado de la fase lunar
      const lp = 2551443; 
      const now = date.getTime() / 1000;
      const newMoon = 947182440;
      const phase = ((now - newMoon) % lp) / lp;
      const phases = [
        {name: 'Luna Nueva', icon: '🌑', msg: 'La Luna Nueva marca nuevos inicios. Planta la semilla de tu suerte.'},
        {name: 'Luna Creciente', icon: '🌒', msg: 'La Luna Creciente multiplica tus intenciones.'},
        {name: 'Cuarto Creciente', icon: '🌓', msg: 'El Cuarto Creciente demanda acción. Confía en tu instinto.'},
        {name: 'Luna Gibosa Creciente', icon: '🌔', msg: 'La energía aumenta. Mantén la concentración en tu meta.'},
        {name: 'Luna Llena', icon: '🌕', msg: 'La Luna Llena ilumina tu fortuna. Es tiempo de cosecha y culminación.'},
        {name: 'Luna Gibosa Menguante', icon: '🌖', msg: 'Libera las dudas. Deja ir lo que no te sirve.'},
        {name: 'Cuarto Menguante', icon: '🌗', msg: 'Cierra ciclos. La reflexión profunda afina tu oráculo.'},
        {name: 'Luna Menguante', icon: '🌘', msg: 'Descanso energético. El silencio interior revela los números.'}
      ];
      const phaseIndex = Math.floor(phase * 8 + 0.5) % 8;
      const p = phases[phaseIndex];
      const el = document.getElementById('moon-phase');
      if (el) {
        el.innerHTML = `${p.icon} <strong>${p.name}</strong> — <em>${p.msg}</em>`;
      }
    }
    
    window.addEventListener('load', getMoonPhase);

    function getZodiacSign(dateStr) {
        if (!dateStr) return null;
        const parts = dateStr.split('-');
        if (parts.length !== 3) return null;
        const month = parseInt(parts[1], 10);
        const day = parseInt(parts[2], 10);
        
        if ((month == 1 && day <= 19) || (month == 12 && day >= 22)) return {name: "Capricornio", symbol: "♑", element: "Tierra", mult: 4};
        if ((month == 1 && day >= 20) || (month == 2 && day <= 18)) return {name: "Acuario", symbol: "♒", element: "Aire", mult: 3};
        if ((month == 2 && day >= 19) || (month == 3 && day <= 20)) return {name: "Piscis", symbol: "♓", element: "Agua", mult: 2};
        if ((month == 3 && day >= 21) || (month == 4 && day <= 19)) return {name: "Aries", symbol: "♈", element: "Fuego", mult: 1};
        if ((month == 4 && day >= 20) || (month == 5 && day <= 20)) return {name: "Tauro", symbol: "♉", element: "Tierra", mult: 4};
        if ((month == 5 && day >= 21) || (month == 6 && day <= 20)) return {name: "Géminis", symbol: "♊", element: "Aire", mult: 3};
        if ((month == 6 && day >= 21) || (month == 7 && day <= 22)) return {name: "Cáncer", symbol: "♋", element: "Agua", mult: 2};
        if ((month == 7 && day >= 23) || (month == 8 && day <= 22)) return {name: "Leo", symbol: "♌", element: "Fuego", mult: 1};
        if ((month == 8 && day >= 23) || (month == 9 && day <= 22)) return {name: "Virgo", symbol: "♍", element: "Tierra", mult: 4};
        if ((month == 9 && day >= 23) || (month == 10 && day <= 22)) return {name: "Libra", symbol: "♎", element: "Aire", mult: 3};
        if ((month == 10 && day >= 23) || (month == 11 && day <= 21)) return {name: "Escorpio", symbol: "♏", element: "Agua", mult: 2};
        if ((month == 11 && day >= 22) || (month == 12 && day <= 21)) return {name: "Sagitario", symbol: "♐", element: "Fuego", mult: 1};
        return null;
    }

    function getKuaNumber(year, gender) {
       let sum = 0;
       const yearStr = String(year);
       const lastTwo = yearStr.substring(yearStr.length - 2);
       for (let char of lastTwo) sum += parseInt(char, 10);
       while (sum > 9) {
           let temp = 0;
           for (let char of String(sum)) temp += parseInt(char, 10);
           sum = temp;
       }
       let kua = 0;
       if (gender === 'male') {
           kua = (year < 2000) ? (10 - sum) : (9 - sum);
           if (kua === 5) kua = 2;
       } else {
           kua = (year < 2000) ? (5 + sum) : (6 + sum);
           while (kua > 9) {
               let temp = 0;
               for (let char of String(kua)) temp += parseInt(char, 10);
               kua = temp;
           }
           if (kua === 5) kua = 8;
       }
       if (kua <= 0) kua = 9; 
       return kua;
    }

    function getFlyingStar() {
        const d = new Date();
        let sum = d.getDate() + (d.getMonth() + 1) + d.getFullYear();
        while (sum > 9) {
           let temp = 0;
           for (let char of String(sum)) temp += parseInt(char, 10);
           sum = temp;
        }
        return sum;
    }

    function updateLifePathInfo() {
      const bdate = document.getElementById('birthdate').value;
      const gender = document.getElementById('gender').value;
      const infoEl = document.getElementById('life-path-info');
      if (!bdate) {
        infoEl.style.display = 'none';
        return;
      }
      const cv = calcularCaminoVida(bdate);
      const zodiac = getZodiacSign(bdate);
      const year = parseInt(bdate.split('-')[0], 10);
      const kua = getKuaNumber(year, gender);
      const fStar = getFlyingStar();
      
      if (cv && zodiac && kua) {
        let meaning = '';
        if (cv===1) meaning="El Pionero: Liderazgo e independencia.";
        else if(cv===2) meaning="El Pacificador: Cooperación y armonía.";
        else if(cv===3) meaning="El Comunicador: Creatividad y expresión.";
        else if(cv===4) meaning="El Constructor: Orden y estabilidad.";
        else if(cv===5) meaning="El Aventurero: Libertad y cambio.";
        else if(cv===6) meaning="El Sanador: Responsabilidad y amor.";
        else if(cv===7) meaning="El Buscador: Sabiduría y análisis.";
        else if(cv===8) meaning="El Ejecutivo: Poder material y karma.";
        else if(cv===9) meaning="El Humanitario: Compasión y finales.";
        else if(cv===11) meaning="El Mensajero (Maestro): Intuición suprema.";
        else if(cv===22) meaning="El Arquitecto (Maestro): Grandes obras.";
        else if(cv===33) meaning="El Maestro de Maestros: Amor universal.";
        
        infoEl.innerHTML = `
          <div style="display:flex; align-items:center; justify-content:center; gap: 15px; margin-top: 15px;">
            <div style="width: 70px; height: 70px; border-radius: 50%; background-image: url('zodiac_bg.png'); background-size: cover; background-position: center; border: 2px solid var(--gold); display:flex; align-items:center; justify-content:center; box-shadow: 0 0 15px var(--gold-dark);">
               <span style="font-size: 2.5rem; color: var(--gold-light); text-shadow: 0 0 5px #000;">${zodiac.symbol}</span>
            </div>
            <div style="text-align: left; font-size: 0.85rem;">
               <div style="color: var(--gold); font-size: 1rem; font-family: 'Cinzel', serif;">Signo: ${zodiac.name} (${zodiac.element})</div>
               <div>Tu Camino de Vida es <strong>${cv}</strong>. Tu Número Feng Shui Kua es <strong>${kua}</strong>.</div>
               <div style="color: #b3e5fc;">${meaning}</div>
            </div>
          </div>
        `;
        infoEl.style.display = 'block';
      } else {
        infoEl.style.display = 'none';
      }
    }

    function startRitual() {
      if (selectedCards.length < MAX_PICK) return;
      document.getElementById('ritual-screen').classList.add('active');
      setTimeout(() => {
        document.getElementById('ritual-text').textContent = "Visualiza la fortuna...";
      }, 2000);
      setTimeout(() => {
        document.getElementById('ritual-screen').classList.remove('active');
        revealOracle();
      }, 4000);
    }


    /* ========================================================
       SHUFFLE ALGORITHMS
       ======================================================== */
    function shuffleRiffle(arr) {
      // Multiple riffle passes
      for (let pass = 0; pass < 7; pass++) {
        const half = Math.floor(arr.length / 2);
        const a = arr.slice(0, half);
        const b = arr.slice(half);
        const result = [];
        while (a.length || b.length) {
          if (a.length && (!b.length || Math.random() < .5)) result.push(a.shift());
          else result.push(b.shift());
        }
        arr = result;
      }
      return arr;
    }

    function shuffleOverhand(arr) {
      for (let pass = 0; pass < 12; pass++) {
        let tmp = [], i = 0;
        while (i < arr.length) {
          const chunk = 1 + Math.floor(Math.random() * 8);
          tmp = [...arr.slice(i, i + chunk), ...tmp];
          i += chunk;
        }
        arr = tmp;
      }
      return arr;
    }

    function shuffleCut(arr) {
      // Triple cut + multiple inversions
      for (let pass = 0; pass < 5; pass++) {
        const c1 = 10 + Math.floor(Math.random() * 25);
        const c2 = c1 + 10 + Math.floor(Math.random() * 25);
        const p1 = arr.slice(0, c1);
        const p2 = arr.slice(c1, c2);
        const p3 = arr.slice(c2);
        arr = [...p3, ...p1, ...p2];
        if (Math.random() > 0.5) arr = [...arr.slice(0, 20).reverse(), ...arr.slice(20)];
      }
      return arr;
    }

    /* ========================================================
       STATE
       ======================================================== */
    let deck = [...FULL_DECK];
    let selectedCards = []; // max 6
    const MAX_PICK = 6;
    let shuffleCount = 0;
    let shuffleLog = []; // track sequence of methods used
    let isShuffling = false;

    /* ========================================================
       PHASE 1 → SHUFFLE (cumulative, repeatable)
       ======================================================== */
    function startShuffle(method) {
      if (isShuffling) return; // ignore clicks during animation
      isShuffling = true;

      // Disable buttons during animation
      document.querySelectorAll('.btn-shuffle').forEach(b => b.disabled = true);
      const animDiv = document.getElementById('shuffle-anim');
      const textEl = document.getElementById('shuffle-text');
      animDiv.style.display = 'block';

      const messages = {
        riffle: ['El Tahúr Viajero corta el mazo...', 'Entrelazando los destinos...', 'El caos ordena lo que le corresponde...'],
        overhand: ['El Ermitaño Ancestral mezcla con calma...', 'Las cartas fluyen entre sus manos...', 'El tiempo detiene su marcha...'],
        cut: ['El Mago del Vacío corta el mazo en tres...', 'Inversión de los planos astrales...', 'El portal del destino se abre...'],
      };
      const methodNames = { riffle: 'Riffle', overhand: 'Overhand', cut: 'Corte del Destino' };
      const msgs = messages[method];
      let mi = 0;
      textEl.textContent = msgs[0];
      const interval = setInterval(() => { mi = (mi + 1) % msgs.length; textEl.textContent = msgs[mi]; }, 700);

      setTimeout(() => {
        clearInterval(interval);

        // Apply shuffle ON TOP of current deck state
        if (method === 'riffle') deck = shuffleRiffle(deck);
        if (method === 'overhand') deck = shuffleOverhand(deck);
        if (method === 'cut') deck = shuffleCut(deck);

        // Invertir cartas aleatoriamente al barajar
        deck = deck.map(card => Math.random() < 0.3 ? { ...card, reversed: !card.reversed } : card);

        shuffleCount++;
        shuffleLog.push(methodNames[method]);

        animDiv.style.display = 'none';
        isShuffling = false;
        document.querySelectorAll('.btn-shuffle').forEach(b => b.disabled = false);

        // Update counter label
        const counter = document.getElementById('shuffle-counter');
        const logStr = shuffleLog.slice(-5).join(' → ') + (shuffleLog.length > 5 ? ' (...)' : '');
        counter.innerHTML = `Barajadas: <strong>${shuffleCount}</strong> vez${shuffleCount !== 1 ? 'es' : ''} &nbsp;·&nbsp; ${logStr}`;

        // Show play button on first shuffle
        const playBtn = document.getElementById('btn-play-now');
        playBtn.disabled = false;
        playBtn.style.opacity = '1';
        playBtn.style.pointerEvents = 'auto';
        playBtn.style.cursor = 'pointer';
        playBtn.onmouseover = () => { playBtn.style.boxShadow = 'var(--shadow-glow)'; playBtn.style.borderColor = 'var(--gold)'; playBtn.style.transform = 'translateY(-2px)'; };
        playBtn.onmouseout = () => { playBtn.style.boxShadow = 'none'; playBtn.style.borderColor = 'var(--gold-dark)'; playBtn.style.transform = 'translateY(0)'; };
      }, 2200);
    }

    function playNow() {
      document.getElementById('phase-shuffle').classList.add('hidden');
      showSelectionPhase();
    }

    function quickBet() {
      // 1. Ocultar fase 1
      document.getElementById('phase-shuffle').classList.add('hidden');
      
      // 2. Barajar automáticamente (3 veces mezclando los destinos)
      deck = shuffleRiffle(deck);
      deck = shuffleOverhand(deck);
      deck = shuffleCut(deck);
      // Invertir cartas aleatoriamente
      deck = deck.map(card => Math.random() < 0.3 ? { ...card, reversed: !card.reversed } : card);
      
      // 3. Preparar fase 2 y seleccionar 6 cartas al azar
      showSelectionPhase();
      
      let availableIndices = Array.from({length: deck.length}, (_, i) => i);
      for(let i=0; i<6; i++) {
        let randPos = Math.floor(Math.random() * availableIndices.length);
        let pickedIdx = availableIndices.splice(randPos, 1)[0];
        
        let el = document.querySelector(`.fan-card[data-idx="${pickedIdx}"]`);
        if (el) toggleCard(el, pickedIdx);
      }
      
      // 4. Iniciar el ritual automáticamente
      startRitual();
    }

    /* ========================================================
       PHASE 2 → SELECTION
       ======================================================== */
    function showSelectionPhase() {
      selectedCards = [];
      document.getElementById('phase-select').classList.remove('hidden');
      buildFan();
      buildSelectedRow();
      updateRevealBtn();
    }

    function buildFan() {
      const container = document.getElementById('fan-container');
      container.innerHTML = '';

      const totalCards = deck.length;
      const maxAngle = 65; // from -65 to +65 = 130 degrees span

      deck.forEach((card, i) => {
        const angle = -maxAngle + ( (maxAngle * 2) / (totalCards - 1) ) * i;

        const el = document.createElement('div');
        el.className = 'fan-card';
        el.dataset.idx = i;
        el.style.setProperty('--rot', `${angle}deg`);
        el.style.zIndex = i;

        el.innerHTML = `
          <div class="card-back"><span class="symbol">✦</span></div>
          <div class="card-front">
            <div class="marseille-card">
              <div class="marseille-num">${card.numeral || ''}</div>
              <div class="marseille-art">${card.art}</div>
              <div class="marseille-name">${card.marseilleName || card.name}</div>
            </div>
          </div>`;

        el.addEventListener('click', () => toggleCard(el, i));
        container.appendChild(el);
      });
    }

    function toggleCard(el, idx) {
      const card = deck[idx];
      const alreadySelected = selectedCards.findIndex(c => c.deckIdx === idx);
      
      if (alreadySelected >= 0) {
        return; // Deselection is now handled in the bottom row
      } else {
        if (selectedCards.length >= MAX_PICK) return; // no more
        selectedCards.push({ ...card, deckIdx: idx, orderPicked: selectedCards.length });
        el.classList.add('picked-out');
      }
      updateRevealBtn();
      buildSelectedRow(true);
    }

    function deselectCard(deckIdx) {
      const alreadySelected = selectedCards.findIndex(c => c.deckIdx === deckIdx);
      if (alreadySelected >= 0) {
        selectedCards.splice(alreadySelected, 1);
        const fanEl = document.querySelector(`.fan-card[data-idx="${deckIdx}"]`);
        if (fanEl) fanEl.classList.remove('picked-out');
        buildSelectedRow(false);
        updateRevealBtn();
      }
    }

    function buildSelectedRow(isNewPick = false) {
      const row = document.getElementById('selected-row');
      row.innerHTML = '';
      for (let i = 0; i < MAX_PICK; i++) {
        const slot = document.createElement('div');
        slot.className = 'sel-card-slot';
        if (selectedCards[i]) {
          const c = selectedCards[i];
          const label = i < 5 ? `Baloto #${i + 1}` : '🔴 S.Balota';
          const revMark = c.reversed ? '<span style="color:#ff4d4d;font-size:0.8em"> (Inv)</span>' : '';
          const revStyle = c.reversed ? 'transform: scale(0.7) rotate(180deg); transform-origin: center center;' : 'transform: scale(0.7); transform-origin: center center;';
          slot.classList.add('filled');
          if (isNewPick && i === selectedCards.length - 1) {
            slot.classList.add('pop-in');
          }
          slot.innerHTML = `
        <div style="cursor: pointer; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: center;" onclick="deselectCard(${c.deckIdx})">
          <div class="marseille-card" style="${revStyle} margin:0 auto; display: flex;">
            <div class="marseille-num">${c.numeral || ''}</div>
            <div class="marseille-art">${c.art}</div>
            <div class="marseille-name">${c.marseilleName || c.name}</div>
          </div>
          <div class="mini-name">${c.name}${revMark}</div>
          <div class="mini-pos">${label}</div>
        </div>`;
        } else {
          const label = i < 5 ? `#${i + 1}` : '🔴';
          slot.textContent = label;
        }
        row.appendChild(slot);
      }
      document.getElementById('picked-count').textContent = `${selectedCards.length} / ${MAX_PICK} seleccionadas`;
    }

    function updateRevealBtn() {
      const btn = document.getElementById('reveal-btn');
      btn.disabled = selectedCards.length < MAX_PICK;
    }

    /* ========================================================
       FORMULA MÍSTICA DEL VIAJERO DEL TIEMPO (Hermes-1746)
       
       Inspirada en el método numerológico del libro ficticio
       "Arcana Mathematica" atribuido al Conde Saint-Germain.
    
       Cada carta tiene un valor arcano V.
       La semilla_alma = suma de todos los V de las 6 cartas.
       
       Baloto_i = ((V_i × 7 + i × 13 + semilla) mod 46) + 1
       Super = ((V_5 × 3 + semilla × 5) mod 16) + 1
       
       Los números no se repiten: si hay colisión se aplica
       +1 iterativo (método de San Germain: "el destino siempre
       encuentra su camino").
       ======================================================== */
    function calcularCaminoVida(dateStr) {
      if (!dateStr) return null;
      let digits = dateStr.replace(/\D/g, '');
      if (!digits) return null;
      let sum = 0;
      for (let char of digits) sum += parseInt(char, 10);
      while (sum > 9 && sum !== 11 && sum !== 22 && sum !== 33) {
        let temp = 0;
        for (let char of String(sum)) temp += parseInt(char, 10);
        sum = temp;
      }
      return sum;
    }

    function calculateDailyNumerology() {
      const d = new Date();
      const dateStr = `${d.getDate()}${d.getMonth()+1}${d.getFullYear()}`;
      let sum = 0;
      for (let char of dateStr) sum += parseInt(char, 10);
      while (sum > 9) {
        let temp = 0;
        for (let char of String(sum)) temp += parseInt(char, 10);
        sum = temp;
      }
      return sum;
    }

    function getMirrorNumber(num, max) {
      const str = String(num);
      if (str.length === 2 && str[0] !== str[1]) {
        const mirror = parseInt(str[1] + str[0], 10);
        if (mirror > 0 && mirror <= max) return mirror;
      }
      return num;
    }

    function computeNumbers(cards, caminoVida, zodiac, kua, fStar) {
      // cards[0..4] = baloto, cards[5] = super balota
      let soul = cards.reduce((acc, c) => acc + c.v, 0); // semilla_alma original
      if (caminoVida) soul += (caminoVida * 9);
      if (zodiac) soul += (zodiac.mult * 3);
      if (kua) soul += (kua * 8); // Multiplicador de riqueza Feng Shui
      if (fStar) soul += (fStar * 9); // Estrella de la fortuna futura

      const obtained = [];
      const results = [];

      for (let i = 0; i < 5; i++) {
        const c = cards[i];
        let base = ((c.v * 7 + i * 13 + soul) % 43) + 1;
        let originalBase = base;
        
        let mirrorMsg = "";
        if (c.reversed) {
          const mirror = getMirrorNumber(base, 43);
          if (mirror !== base) {
             base = mirror;
             mirrorMsg = ` → Inv: Espejo ${mirror}`;
          }
        }

        // Ensure no repeat and range 1-43
        let attempt = base;
        let itr = 0;
        while (obtained.includes(attempt)) {
          attempt = (attempt % 43) + 1;
          itr++;
          if (itr > 50) { attempt = Math.floor(Math.random() * 43) + 1; break; }
        }
        obtained.push(attempt);
        results.push({
          num: attempt,
          card: c,
          formula: `((${c.v}×7 + ${i}×13 + ${soul}) mod 43)+1 = ${originalBase}${mirrorMsg}${attempt !== base ? ` → Colisión: ${attempt}` : ''}`
        });
      }

      // Super Balota
      const cs = cards[5];
      const dailyNum = calculateDailyNumerology();
      let superBase = ((cs.v * 3 + soul * 5 + dailyNum * 7) % 16) + 1;
      let originalSuper = superBase;
      let superMirrorMsg = "";
      
      if (cs.reversed) {
         const mirror = getMirrorNumber(superBase, 16);
         if (mirror !== superBase) {
             superBase = mirror;
             superMirrorMsg = ` → Inv: Espejo ${mirror}`;
         }
      }
      
      results.push({
        num: superBase,
        card: cs,
        formula: `((${cs.v}×3 + ${soul}×5 + día:${dailyNum}×7) mod 16)+1 = ${originalSuper}${superMirrorMsg}`,
        isSuper: true
      });

      return results;
    }

    /* ========================================================
       PHASE 3 → ORACLE RESULT
       ======================================================== */
    const ORACLE_PHRASES = [
      'Las estrellas han contemplado tu elección. El tejido del destino se revela...',
      'El velo entre mundos se rasga. Las cartas hablan con la voz del cosmos...',
      'El Conde de Saint-Germain susurra los números desde el éter del tiempo...',
      'Tres velas iluminan el altar del oráculo. Lo que fue escrito, se cumple...',
      'El espejo del Tarot no miente. Recibe los números que el universo te destina...',
    ];

    async function revealOracle() {
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
      const birthdateInput = document.getElementById('birthdate').value;
      const genderInput = document.getElementById('gender') ? document.getElementById('gender').value : 'male';
      const caminoVida = calcularCaminoVida(birthdateInput);
      const zodiac = getZodiacSign(birthdateInput);
      
      let kua = null;
      let fStar = null;
      if (birthdateInput) {
          const year = parseInt(birthdateInput.split('-')[0], 10);
          kua = getKuaNumber(year, genderInput);
          fStar = getFlyingStar();
      }
      
      const results = computeNumbers(selectedCards, caminoVida, zodiac, kua, fStar);
      
      const cvText = document.getElementById('formula-cv-text');
      if (caminoVida && zodiac && kua) {
        cvText.innerHTML = `<em>¡Astrología, Numerología y Feng Shui Aplicados!</em> Tu Camino de Vida es <strong>${caminoVida}</strong>, tu energía es <strong>${zodiac.name}</strong> y tu Número Kua es <strong>${kua}</strong> (Estrella Voladora ${fStar}). Estas fuerzas se han fundido en la semilla base.`;
        cvText.style.color = '#90ee90';
      } else {
        cvText.innerHTML = `Se ha utilizado el algoritmo original puro (sin fecha de nacimiento).`;
        cvText.style.color = 'var(--silver-dark)';
      }

      // Numbers display

      const numDisp = document.getElementById('numbers-display');
      numDisp.innerHTML = '';
      
      const today = new Date();
      let d = new Date(today);
      while (d.getDay() !== 1 && d.getDay() !== 3 && d.getDay() !== 6) {
          d.setDate(d.getDate() + 1);
      }
      const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
      const nextDate = d.toLocaleDateString('es-CO', options);
      
      const dateHeader = document.createElement('h3');
      dateHeader.style.color = '#e5c07b';
      dateHeader.style.textAlign = 'center';
      dateHeader.style.fontFamily = "'Cinzel Decorative', cursive";
      dateHeader.style.fontSize = "1.5rem";
      dateHeader.style.marginBottom = "20px";
      dateHeader.innerHTML = `✦ SORTEO VÁLIDO PARA: ${nextDate.toUpperCase()} ✦`;
      numDisp.appendChild(dateHeader);

      
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
      
      // --- Sincronicidades ---
      let history = JSON.parse(localStorage.getItem('tarotBalotoHistory') || '[]');
      let historyFreq = {};
      history.forEach(h => {
          if (h.nums) h.nums.forEach(n => historyFreq[n] = (historyFreq[n] || 0) + 1);
      });
      // Guardar lectura actual
      history.push({ date: new Date().toISOString(), nums: results.map(r => r.num) });
      if (history.length > 20) history.shift();
      localStorage.setItem('tarotBalotoHistory', JSON.stringify(history));

      results.forEach((r) => {
        const isSync = (historyFreq[r.num] >= 1);
        
        let isRecent = false;
        if(scraperSuccess) {
            if(r.isSuper) {
                isRecent = (r.num === principalSuper || r.num === revanchaSuper);
            } else {
                isRecent = principalNumbers.includes(r.num) || revanchaNumbers.includes(r.num);
            }
        }
        
        let syncClass = '';
        let syncTag = '';
        
        if (isRecent) {
            syncClass = ' recent-glow';
            syncTag = `<div class="sync-tag" style="background:#ff3366; color:white; text-shadow:none;">¡Salió Reciente!</div>`;
        } else if (isSync) {
            syncClass = ' synchronicity-glow';
            syncTag = `<div class="sync-tag">Sincronicidad</div>`;
        }
        
        const ball = document.createElement('div');
        ball.className = 'number-ball' + (r.isSuper ? ' super-ball' : '') + syncClass;
        if (isRecent) {
             ball.style.boxShadow = "0 0 20px #ff3366, inset 0 0 10px #ff3366";
             ball.style.borderColor = "#ff3366";
        }
        ball.innerHTML = `${syncTag}${r.num}<span class="ball-label">${r.isSuper ? 'Super' : 'Baloto'}</span>`;
        ballsContainer.appendChild(ball);
      });
      numDisp.appendChild(ballsContainer);

      // Card reading details
      const reading = document.getElementById('card-reading');
      reading.innerHTML = '';
      
      const tarotMeanings = [
        { title: "Carta 1: El Pasado", desc: "Muestra las experiencias, bloqueos o aprendizajes que te trajeron a tu situación actual." },
        { title: "Carta 2: El Presente", desc: "Representa tu energía, el momento exacto en el que te encuentras y el enfoque principal de tu consulta." },
        { title: "Carta 3: El Futuro Cercano", desc: "Indica la dirección natural hacia la que se dirigen las cosas si todo sigue su curso actual." },
        { title: "Carta 4: Las Influencias Ocultas", desc: "Revela lo que sucede fuera de tu vista o las emociones subconscientes que te afectan." },
        { title: "Carta 5: El Entorno", desc: "Muestra cómo las personas, situaciones o tu ambiente externo están impactando tu vida." },
        { title: "Carta 6: El Resultado / Consejo", desc: "Ofrece la resolución final de la situación o la acción más sabia que debes tomar para tu mayor beneficio." }
      ];

      const majorMeanings = {
        0: {
          significado: "El Loco representa los nuevos comienzos, la aventura y la fe ciega. Te invita a dar un salto a lo desconocido con optimismo.",
          palabrasClave: "Espontaneidad, Inocencia, Viajes, Potencial, Caos fértil",
          consejo: "Atrévete a experimentar sin planificar todo. El universo sostiene a quienes confían.",
          advertencia: "Cuidado con la imprudencia pura y los riesgos innecesarios sin red de seguridad."
        },
        1: {
          significado: "El Mago simboliza la manifestación, la destreza y el poder personal. Tienes a tu disposición todas las herramientas para hacer realidad tus metas.",
          palabrasClave: "Acción, Concentración, Habilidad, Voluntad, Ingenio",
          consejo: "Reclama tu poder y actúa con conciencia. Transforma las ideas en realidad enfocando tu energía.",
          advertencia: "Evita la manipulación o el uso egoísta de tus capacidades. No dejes tus talentos sin usar."
        },
        2: {
          significado: "La Papisa encarna la intuición, el misterio y la sabiduría interior. Hay conocimientos ocultos que están a punto de revelarse.",
          palabrasClave: "Intuición, Secretos, Sabiduría interior, Misticismo",
          consejo: "Escucha tu voz interna y confía en tus instintos. Es un momento para observar en lugar de actuar precipitadamente.",
          advertencia: "La desconexión emocional o el aislamiento extremo pueden bloquear tu verdadero entendimiento."
        },
        3: {
          significado: "La Emperatriz representa la abundancia, la fertilidad y la expresión creativa. Simboliza un periodo de prosperidad y crecimiento desbordante.",
          palabrasClave: "Creatividad, Fertilidad, Belleza, Abundancia, Naturaleza",
          consejo: "Nutre tus proyectos y relaciones. Disfruta de los placeres sensoriales y deja que tu lado creativo florezca.",
          advertencia: "Cuidado con el apego sofocante, la sobreprotección o el abandono de tu propio cuidado personal."
        },
        4: {
          significado: "El Emperador es el arquetipo de la estructura, la estabilidad y la autoridad. Habla de liderazgo y construcción sobre bases sólidas.",
          palabrasClave: "Estructura, Reglas, Disciplina, Liderazgo, Lógica",
          consejo: "Establece orden y toma el control de tu vida. La disciplina y la organización serán tus mejores aliados ahora.",
          advertencia: "Evita la tiranía, la rigidez mental extrema y el deseo desmedido de controlar a los demás."
        },
        5: {
          significado: "El Papa habla de tradición, creencias compartidas y enseñanza espiritual. Es la conexión entre lo terrenal y lo divino.",
          palabrasClave: "Tradición, Mentoría, Creencias, Valores compartidos",
          consejo: "Busca conocimiento en mentores o sistemas de valores establecidos. Aprende de la experiencia de otros.",
          advertencia: "Cuestiona el dogmatismo ciego o el seguir reglas anticuadas que ya no resuenan con tu verdad."
        },
        6: {
          significado: "Los Enamorados significan amor, armonía y elecciones trascendentales. Representa la alineación de tus valores personales.",
          palabrasClave: "Amor, Decisiones, Armonía, Unión, Valores",
          consejo: "Toma decisiones basadas en tu verdad interior y en el amor puro. Busca el equilibrio en tus relaciones.",
          advertencia: "La indecisión paralizante o elegir caminos fáciles pero deshonestos traerá desarmonía."
        },
        7: {
          significado: "El Carro simboliza la victoria, el control y la superación de obstáculos. El triunfo llega a través de tu esfuerzo dirigido.",
          palabrasClave: "Victoria, Determinación, Avance, Fuerza de voluntad",
          consejo: "Mantén la confianza para dirigir fuerzas opuestas hacia una sola dirección. Sigue adelante sin dudar.",
          advertencia: "No pases por encima de los demás para lograr tus metas. Controla tu agresividad."
        },
        8: {
          significado: "La Justicia encarna la equidad, la verdad y la ley kármica. Toda acción tiene una reacción; cosechas lo que siembras.",
          palabrasClave: "Equidad, Verdad, Karma, Responsabilidad, Equilibrio",
          consejo: "Actúa con integridad absoluta y busca el equilibrio en todas las áreas. Asume la responsabilidad de tus actos.",
          advertencia: "El autoengaño y la negación de la verdad atraerán consecuencias negativas severas."
        },
        9: {
          significado: "El Ermitaño es el buscador de la verdad. Representa la introspección, la soledad voluntaria y la guía interior.",
          palabrasClave: "Introspección, Soledad sabia, Búsqueda, Reflexión",
          consejo: "Haz una pausa para encontrar respuestas dentro de ti. Desconéctate del ruido exterior para escuchar tu alma.",
          advertencia: "El aislamiento prolongado puede convertirse en paranoia o miedo a conectar con los demás."
        },
        10: {
          significado: "La Rueda de la Fortuna indica ciclos, destino y puntos de inflexión. Habla de suerte inesperada y la intervención del karma.",
          palabrasClave: "Ciclos, Destino, Cambio inevitable, Suerte, Evolución",
          consejo: "Fluye con los cambios inevitables. Recuerda que lo que hoy está abajo, mañana estará arriba.",
          advertencia: "Aferrarse al pasado o resistirse al flujo natural de la vida solo traerá sufrimiento innecesario."
        },
        11: {
          significado: "La Fuerza no es violencia, sino el coraje, la persuasión y el dominio interior frente a instintos bajos.",
          palabrasClave: "Coraje, Resiliencia, Compasión, Paciencia, Dominio",
          consejo: "Enfrenta tus miedos y pasiones con compasión y resiliencia. Eres más fuerte de lo que crees.",
          advertencia: "No dejes que tus instintos primitivos, la ira o la inseguridad tomen el control de tus decisiones."
        },
        12: {
          significado: "El Colgado representa una pausa necesaria, la rendición y el sacrificio para obtener iluminación y otra perspectiva.",
          palabrasClave: "Pausa, Nuevas perspectivas, Rendición, Sacrificio",
          consejo: "Suspende tus acciones por ahora. Dejar ir la necesidad de control te traerá la respuesta que buscas.",
          advertencia: "Cuidado con el martirio inútil o estancarte en una posición de víctima sin propósito."
        },
        13: {
          significado: "La Muerte simboliza los finales inevitables, la transformación profunda y el cierre de un ciclo para un nuevo inicio.",
          palabrasClave: "Transformación, Finales, Renacimiento, Transición",
          consejo: "No temas al cambio. Cierra ese capítulo de forma definitiva para que lo nuevo pueda entrar a tu vida.",
          advertencia: "Aferrarse desesperadamente a lo que ya está muerto solo pudre el presente e impide tu evolución."
        },
        14: {
          significado: "La Templanza es el arte del equilibrio, la moderación y la sanación al mezclar elementos opuestos.",
          palabrasClave: "Equilibrio, Moderación, Sanación, Alquimia, Fluidez",
          consejo: "Busca el punto medio. Ten paciencia y mezcla los contrastes de tu vida para encontrar armonía.",
          advertencia: "Los extremos y los excesos te desestabilizarán. No te precipites en buscar resultados inmediatos."
        },
        15: {
          significado: "El Diablo refleja nuestras sombras, apegos materiales, tentaciones y adicciones que nos quitan la libertad.",
          palabrasClave: "Apegos, Sombra, Materialismo, Tentación, Ataduras",
          consejo: "Reconoce tus miedos ocultos y ataduras. La libertad empieza al iluminar tu propia oscuridad.",
          advertencia: "Estás atrapado en un ciclo tóxico o adicción. Es urgente cortar los lazos que te destruyen."
        },
        16: {
          significado: "La Torre marca un cambio repentino, una revelación disruptiva y el derrumbe de estructuras inestables.",
          palabrasClave: "Caos purificador, Revelación, Cambio drástico, Crisis",
          consejo: "Deja que caigan las ilusiones y cimientos falsos. De estas ruinas construirás una verdad más sólida.",
          advertencia: "Luchar contra esta caída solo hará que el impacto sea más doloroso. Acepta el desastre necesario."
        },
        17: {
          significado: "La Estrella trae esperanza, inspiración, sanación y renovación espiritual después de un periodo turbulento.",
          palabrasClave: "Esperanza, Renovación, Serenidad, Inspiración divina",
          consejo: "Confía plenamente, estás en el camino correcto y bendecido. Mantén la fe y sigue tu estrella guía.",
          advertencia: "Cuidado con perder la fe y caer en el cinismo o la desesperanza cuando la luz ya está brillando."
        },
        18: {
          significado: "La Luna representa la intuición profunda pero también la ilusión, los miedos irracionales y la confusión.",
          palabrasClave: "Ilusión, Miedos, Subconsciente, Intuición, Misterio",
          consejo: "Navega a través de tus miedos y confía en tu instinto. No todo es lo que parece en la superficie.",
          advertencia: "El autoengaño, la ansiedad proyectada y las paranoias te están nublando el juicio. Busca claridad."
        },
        19: {
          significado: "El Sol es la carta de la positividad radiante, el éxito, la vitalidad y la alegría absoluta.",
          palabrasClave: "Alegría, Éxito, Vitalidad, Claridad, Optimismo",
          consejo: "Disfruta de la calidez, confía en tu luz interior y celebra tus logros. Todo se está iluminando.",
          advertencia: "No dejes que tu ego se infle excesivamente ni te ciegues por un optimismo ingenuo."
        },
        20: {
          significado: "El Juicio es un despertar, una absolución y un llamado interior a renacer a un nivel de conciencia superior.",
          palabrasClave: "Renacimiento, Llamado, Absolución, Evaluación",
          consejo: "Evalúa tu vida con honestidad, perdona tu pasado y responde al llamado para evolucionar.",
          advertencia: "Ignorar este llamado o juzgarte a ti mismo con extrema dureza te dejará atascado en el pasado."
        },
        21: {
          significado: "El Mundo significa la completitud, la integración y la realización final de un largo viaje.",
          palabrasClave: "Plenitud, Realización, Integración, Éxito final",
          consejo: "Celebra la culminación de tu esfuerzo. Estás entero y listo para iniciar un ciclo aún mayor.",
          advertencia: "El estancamiento por falta de cierre o el temor a terminar una etapa te impiden alcanzar la plenitud."
        }
      };
      
      const majorMeaningsRev = {
        0: {
          significado: "El Loco invertido indica actos temerarios, caos sin propósito o parálisis por miedo a lo desconocido.",
          palabrasClave: "Imprudencia, Temeridad, Irresponsabilidad, Miedo",
          consejo: "Mira antes de saltar. Evalúa los riesgos reales antes de tomar decisiones impulsivas y destructivas.",
          advertencia: "La negligencia y la falta de consideración por las consecuencias traerán problemas serios."
        },
        1: {
          significado: "El Mago invertido señala manipulación, ilusiones engañosas, potencial desperdiciado o falta de enfoque claro.",
          palabrasClave: "Manipulación, Engaño, Talento oculto, Dispersión",
          consejo: "Enfócate en intenciones honestas. Deja de desperdiciar tu energía en trucos y asume tu poder real.",
          advertencia: "Estás siendo engañado o te estás engañando a ti mismo utilizando tus talentos de forma destructiva."
        },
        2: {
          significado: "La Papisa invertida revela desconexión de la intuición, secretos oscuros o miedo a escuchar la voz interior.",
          palabrasClave: "Desconexión, Secretos negativos, Intuición bloqueada",
          consejo: "Reconecta contigo mismo en silencio. No ignores las señales sutiles que tu cuerpo y mente te dan.",
          advertencia: "La represión de la verdad o chismes malintencionados saldrán a la luz causando daño."
        },
        3: {
          significado: "La Emperatriz invertida muestra bloqueos creativos, asfixia emocional o descuido de las necesidades propias.",
          palabrasClave: "Bloqueo, Dependencia, Vacío, Asfixia",
          consejo: "Vuelve a conectar con la naturaleza y nutre tu propia alma antes de intentar cuidar a otros.",
          advertencia: "El exceso de control maternal o la negligencia hacia ti mismo agotarán tu fuerza vital."
        },
        4: {
          significado: "El Emperador invertido es el exceso de rigidez, el abuso de autoridad o, por el contrario, un caos inmaduro.",
          palabrasClave: "Tiranía, Caos, Rigidez, Inmadurez, Control excesivo",
          consejo: "Cede un poco de control y sé más flexible. Aprende a liderar inspirando en lugar de imponiendo.",
          advertencia: "El despotismo y la tiranía alejarán a las personas que necesitas para mantener tu reino en pie."
        },
        5: {
          significado: "El Papa invertido sugiere dogmatismo, rebeldía ciega o seguir a gurús y estructuras que carecen de verdad.",
          palabrasClave: "Dogma, Falso profeta, Rebeldía, Conformismo",
          consejo: "Rompe con las tradiciones que ya no te sirven. Crea tu propia brújula moral e intelectual.",
          advertencia: "Cuidado con los malos consejos, instituciones corruptas o el conformismo ciego que anula tu espíritu."
        },
        6: {
          significado: "Los Enamorados invertidos reflejan desarmonía, elecciones equivocadas o relaciones basadas en valores incompatibles.",
          palabrasClave: "Desequilibrio, Mala elección, Conflicto, Desconexión",
          consejo: "Reevalúa si tus elecciones actuales están realmente alineadas con tus principios más profundos.",
          advertencia: "Las decisiones basadas en gratificación instantánea o presiones externas fracturarán tu paz."
        },
        7: {
          significado: "El Carro invertido indica pérdida de dirección, agresividad sin control o barreras que parecen insuperables.",
          palabrasClave: "Falta de control, Dispersión, Bloqueos, Agresividad",
          consejo: "Detente un momento para recalibrar tus objetivos antes de estrellarte. Recupera la compostura.",
          advertencia: "Forzar las cosas usando agresividad desmedida te llevará a perder absolutamente todo."
        },
        8: {
          significado: "La Justicia invertida es el karma negativo no resuelto, la injusticia, parcialidad o huir de la responsabilidad.",
          palabrasClave: "Injusticia, Deshonestidad, Karma pendiente, Parcialidad",
          consejo: "Acepta tus errores y asume las consecuencias. Solo la verdad te permitirá volver al equilibrio.",
          advertencia: "El universo siempre equilibra la balanza; escapar de tus responsabilidades ahora empeorará tu deuda."
        },
        9: {
          significado: "El Ermitaño invertido señala soledad patológica, aislamiento tóxico o negarse a madurar y reflexionar.",
          palabrasClave: "Aislamiento, Paranoia, Rechazo de ayuda, Terquedad",
          consejo: "Es hora de salir de la cueva. Integra el aprendizaje en el mundo real y reconecta con otros.",
          advertencia: "El miedo al exterior y el orgullo ciego te están convirtiendo en un recluso sin sabiduría."
        },
        10: {
          significado: "La Rueda invertida muestra resistencia extrema al cambio, mala suerte temporal y ciclos destructivos que se repiten.",
          palabrasClave: "Estancamiento, Mala suerte, Resistencia, Repetición",
          consejo: "Deja de resistirte al giro inminente. Aprende la lección para poder romper el ciclo repetitivo.",
          advertencia: "Creerte víctima perpetua del destino te mantendrá atrapado indefinidamente en la misma miseria."
        },
        11: {
          significado: "La Fuerza invertida es dudar de uno mismo, debilidad interior o dejar que la ira cruda domine tus acciones.",
          palabrasClave: "Inseguridad, Impulsividad animal, Debilidad, Duda",
          consejo: "Vuelve a confiar en tu resiliencia silenciosa. Controla tus emociones antes de que te controlen a ti.",
          advertencia: "Actuar desde el ego frágil o la agresión pura es una muestra de debilidad, no de verdadero poder."
        },
        12: {
          significado: "El Colgado invertido advierte sobre sacrificios inútiles, estancamiento improductivo o terquedad egoísta.",
          palabrasClave: "Martirio, Estancamiento, Terquedad, Frustración",
          consejo: "Deja de hacer esfuerzos inútiles por algo que no cambia. Toma acción o asume una nueva estrategia.",
          advertencia: "Hacerte la víctima para manipular a otros o para no actuar solo prolongará tu agonía y la de los demás."
        },
        13: {
          significado: "La Muerte invertida es la negación profunda, la resistencia al final y el mantenimiento doloroso del status quo.",
          palabrasClave: "Estancamiento, Resistencia, Agonía, Miedo al cambio",
          consejo: "Suelta de una vez lo que ya no tiene vida. Permitir la limpieza es la única cura real para tu dolor.",
          advertencia: "Aferrarse desesperadamente a cosas obsoletas es emocionalmente cancerígeno y frena tu futuro."
        },
        14: {
          significado: "La Templanza invertida revela desequilibrio caótico, impaciencia y choques constantes de fuerzas opuestas.",
          palabrasClave: "Desequilibrio, Excesos, Impaciencia, Conflicto",
          consejo: "Baja la intensidad. Aléjate de los extremos y busca urgentemente un respiro para reequilibrarte.",
          advertencia: "Actuar de manera compulsiva, excesiva o extremista en este momento romperá estructuras importantes."
        },
        15: {
          significado: "El Diablo invertido es la posibilidad de liberarse de ataduras oscuras, superar adicciones o revelar secretos tóxicos.",
          palabrasClave: "Liberación, Superación, Desapego, Revelación",
          consejo: "Aprovecha la claridad. Rompe las cadenas ahora que finalmente ves cómo te limitaban.",
          advertencia: "Estar a punto de liberarte puede desencadenar miedos profundos; no regreses a tu zona de confort tóxica."
        },
        16: {
          significado: "La Torre invertida implica aferrarse a ruinas dolorosas, evitar el desastre a toda costa o una advertencia inminente.",
          palabrasClave: "Ruinas prolongadas, Negación de crisis, Miedo al dolor",
          consejo: "El cambio doloroso es inevitable; construir parches sobre terreno inestable solo pospone lo inevitable.",
          advertencia: "Resistir la caída de la torre hará que sufras el estrés del derrumbe por mucho más tiempo del necesario."
        },
        17: {
          significado: "La Estrella invertida señala desesperanza aplastante, desconexión del propósito espiritual y falta de fe.",
          palabrasClave: "Desánimo, Falta de fe, Desconexión, Cinismo",
          consejo: "Encuentra pequeñas fuentes de luz a tu alrededor. El universo no te ha abandonado, tú cerraste los ojos.",
          advertencia: "Permitir que el cinismo tome el control apagará toda posibilidad de inspiración y recuperación mágica."
        },
        18: {
          significado: "La Luna invertida indica que la confusión empieza a disiparse y emergen verdades ocultas, o un engaño profundo se revela.",
          palabrasClave: "Claridad, Secretos revelados, Superación de miedos",
          consejo: "Enfrenta valientemente la verdad cruda que ahora ves. Usa tu intuición para caminar hacia la luz.",
          advertencia: "Las mentiras y las ilusiones ya no te protegerán. Preparate para lidiar con el impacto de la realidad cruda."
        },
        19: {
          significado: "El Sol invertido es una vitalidad menguante, alegría aplazada temporalmente, ego herido o falta de entusiasmo verdadero.",
          palabrasClave: "Tristeza temporal, Ego excesivo, Falta de brillo",
          consejo: "Conecta con la gratitud por las pequeñas cosas para volver a encender tu fuego interno. Sé humilde.",
          advertencia: "La necesidad constante de atención y la arrogancia quemarán a quienes intentan calentarse en tu fuego."
        },
        20: {
          significado: "El Juicio invertido son dudas existenciales, negarse a evolucionar, juicios severos o quedarse anclado en remordimientos.",
          palabrasClave: "Dudas, Severidad, Estancamiento kármico, Culpa",
          consejo: "Perdónate. Deja de juzgarte tan duramente por el pasado y permítete avanzar hacia tu transformación.",
          advertencia: "Vivir en la culpa constante y el autojuicio severo te negará permanentemente el renacimiento."
        },
        21: {
          significado: "El Mundo invertido es la frustración por no alcanzar la meta, ciclos incompletos y falta de resolución definitiva.",
          palabrasClave: "Estancamiento, Frustración, Ciclos abiertos, Vacío",
          consejo: "Afronta las tareas pendientes. No te distraigas con nuevos proyectos antes de completar el actual.",
          advertencia: "Evitar el final de una etapa te mantendrá flotando en un limbo, sin poder abrazar una verdadera vida."
        }
      };

      const minorMeanings = {
        'Bastos': {
          significado: "El Fuego. Rige la energía, la pasión, la creatividad ardiente y el poder del emprendimiento.",
          palabrasClave: "Acción, Pasión, Impulso, Creatividad, Voluntad",
          consejo: "Toma acción inmediata. Usa tu pasión como motor para superar los obstáculos presentes.",
          advertencia: "La impulsividad desenfrenada o la ambición ciega puede causar incendios incontrolables."
        },
        'Copas': {
          significado: "El Agua. Rige el mundo emocional, las relaciones, el amor incondicional y la intuición curativa.",
          palabrasClave: "Emociones, Amor, Intuición, Sanación, Relaciones",
          consejo: "Abre tu corazón a la empatía y cuida tus vínculos emocionales. La sanación llega conectando profundamente.",
          advertencia: "Evita ahogarte en el drama emocional o perderte en idealizaciones románticas irreales."
        },
        'Espadas': {
          significado: "El Aire. Rige el intelecto superior, la lógica cortante, los pensamientos y la comunicación decisiva.",
          palabrasClave: "Verdad, Intelecto, Conflicto mental, Lógica, Claridad",
          consejo: "Usa tu lógica para cortar la confusión y enfrentar la realidad. Sé honesto aunque duela.",
          advertencia: "Cuidado con la crueldad, las palabras dañinas, y la parálisis por el análisis o exceso mental."
        },
        'Oros': {
          significado: "La Tierra. Rige el mundo material, las finanzas, el trabajo diligente y la construcción de tu legado físico.",
          palabrasClave: "Prosperidad, Estabilidad, Finanzas, Esfuerzo material",
          consejo: "Sé pragmático y diligente. Construye el futuro ladrillo a ladrillo con paciencia terrenal.",
          advertencia: "El materialismo extremo, la avaricia o el descuido espiritual socavarán tus verdaderos cimientos."
        }
      };

      const minorMeaningsRev = {
        'Bastos': {
          significado: "El Fuego invertido señala agotamiento total, dirección dispersa, rabia o proyectos que mueren antes de nacer.",
          palabrasClave: "Agotamiento, Rabia, Impulsividad destructiva",
          consejo: "Descansa y recanaliza tu chispa creativa antes de forzar acciones que nacerán muertas.",
          advertencia: "El enojo incontrolable y la impaciencia quemarán los puentes que has construido."
        },
        'Copas': {
          significado: "El Agua invertida revela inestabilidad extrema, bloqueos afectivos, apegos tóxicos o desconexión emocional.",
          palabrasClave: "Bloqueo emocional, Dependencia tóxica, Represión",
          consejo: "Prioriza tu salud mental y sana tus traumas ocultos antes de buscar validación en terceros.",
          advertencia: "El chantaje emocional y manipular los sentimientos de los demás se devolverán en tu contra."
        },
        'Espadas': {
          significado: "El Aire invertido indica caos mental severo, manipulación psicológica, paranoia o ansiedad paralizante.",
          palabrasClave: "Caos mental, Ansiedad, Manipulación, Confusión",
          consejo: "Detén la rumiación de pensamientos oscuros. Necesitas calma urgente para restablecer tu centro lógico.",
          advertencia: "Usar mentiras afiladas o enredarte en intrigas mentales terminará cortándote a ti mismo."
        },
        'Oros': {
          significado: "La Tierra invertida muestra problemas financieros, miopía espiritual, avaricia, o inestabilidad del hogar.",
          palabrasClave: "Estancamiento, Pobreza, Avaricia, Descuido material",
          consejo: "Revisa meticulosamente tus bases materiales y no tomes riesgos financieros innecesarios.",
          advertencia: "Priorizar únicamente las posesiones por encima de las personas convertirá tu imperio en polvo."
        }
      };
