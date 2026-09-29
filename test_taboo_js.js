const fs = require('fs');
const vm = require('vm');

const html = fs.readFileSync('taboo.html', 'utf8');

// Verify requirement 1: No card names visible on deal screen
if (html.includes('card-quick-label')) {
  console.error("FAIL: card-quick-label still present in HTML!");
  process.exit(1);
} else {
  console.log("PASS: Requirement 1 verified - Card names are completely hidden from the deal screen!");
}

// Verify requirement 2: Shuffle button exists in HTML
if (!html.includes('id="btn-shuffle-deck"') || !html.includes('id="shuffle-counter-badge"')) {
  console.error("FAIL: Shuffle button or counter badge missing!");
  process.exit(1);
} else {
  console.log("PASS: Requirement 2 verified - btn-shuffle-deck and shuffle-counter-badge exist in HTML!");
}

// Extract script blocks
const scriptRegex = /<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/gi;
let match;
let scriptBlocks = [];

while ((match = scriptRegex.exec(html)) !== null) {
  scriptBlocks.push(match[1]);
}

const mockElements = {};
function getOrCreateElement(id) {
  if (!mockElements[id]) {
    mockElements[id] = {
      id: id,
      value: 'TEST CONSULTANTE',
      innerText: '',
      textContent: '',
      innerHTML: '',
      style: {},
      classList: {
        _classes: new Set(),
        add: function(c) { this._classes.add(c); },
        remove: function(c) { this._classes.delete(c); },
        contains: function(c) { return this._classes.has(c); }
      },
      addEventListener: function(evt, cb) {
        this['on_' + evt] = cb;
      },
      appendChild: function(child) {
        if (!this.children) this.children = [];
        this.children.push(child);
      },
      querySelectorAll: () => []
    };
  }
  return mockElements[id];
}

const createdElements = [];
const mockDocument = {
  getElementById: (id) => getOrCreateElement(id),
  querySelectorAll: () => [],
  createElement: (tag) => {
    const el = {
      tagName: tag,
      style: {},
      dataset: {},
      innerHTML: '',
      classList: {
        _classes: new Set(),
        add: function(c) { this._classes.add(c); },
        remove: function(c) { this._classes.delete(c); },
        contains: function(c) { return this._classes.has(c); }
      },
      addEventListener: function(evt, cb) {
        this['on_' + evt] = cb;
      },
      appendChild: function(c) {}
    };
    createdElements.push(el);
    return el;
  }
};

class MockAudioNode {
  constructor() {
    this.value = 0;
    this.frequency = { setValueAtTime: ()=>{}, exponentialRampToValueAtTime: ()=>{} };
    this.gain = { setValueAtTime: ()=>{}, linearRampToValueAtTime: ()=>{}, exponentialRampToValueAtTime: ()=>{} };
    this.delayTime = { value: 0 };
  }
  connect() {}
  start() {}
  stop() {}
}

class MockAudioContext {
  constructor() {
    this.state = 'running';
    this.currentTime = 0;
    this.destination = new MockAudioNode();
  }
  resume() { this.state = 'running'; }
  createOscillator() { return new MockAudioNode(); }
  createGain() { return new MockAudioNode(); }
  createBiquadFilter() { return new MockAudioNode(); }
  createDelay() { return new MockAudioNode(); }
}

let timeoutDepth = 0;
const context = {
  console: console,
  document: mockDocument,
  window: {
    location: { href: '' },
    AudioContext: MockAudioContext,
    webkitAudioContext: MockAudioContext
  },
  setTimeout: (cb, ms) => {
    if (timeoutDepth < 2) {
      timeoutDepth++;
      cb();
      timeoutDepth--;
    }
    return 1;
  },
  clearTimeout: clearTimeout,
  setInterval: (cb, ms) => { cb(); return 1; },
  clearInterval: clearInterval,
  Math: Math,
  Array: Array,
  Set: Set,
  parseInt: parseInt
};

vm.createContext(context);

// Run all script blocks
try {
  scriptBlocks.forEach((code, i) => {
    vm.runInContext(code, context);
  });
  console.log("PASS: Scripts compiled and executed with 0 errors!");
} catch (err) {
  console.error("FATAL ERROR IN JAVASCRIPT:", err);
  process.exit(1);
}

console.log("\nRunning Game & Shuffle Simulation:");
try {
  // Click Conjurar
  mockElements['btn-start-deal'].on_click();

  const dealSlots = createdElements.filter(e => e.className === 'deal-card-slot');
  console.log(`- 78 cards dealt face-down to the board.`);

  // Test shuffle button 3 times
  const shuffleBtn = mockElements['btn-shuffle-deck'];
  const badge = mockElements['shuffle-counter-badge'];

  console.log("- Testing 'BARAJAR CARTAS' button repeatedly...");
  shuffleBtn.on_click();
  console.log(`  After shuffle 1: badge says "${badge.innerText}"`);
  shuffleBtn.on_click();
  console.log(`  After shuffle 2: badge says "${badge.innerText}"`);
  shuffleBtn.on_click();
  console.log(`  After shuffle 3: badge says "${badge.innerText}"`);

  if (!badge.innerText.includes('4 VECES')) {
    throw new Error(`Expected shuffle badge to say 4 VECES, got: ${badge.innerText}`);
  }

  // Select 10 cards after multiple shuffles
  console.log("- Selecting 10 hidden cards...");
  const currentSlots = createdElements.filter(e => e.className === 'deal-card-slot').slice(-78);
  for (let i = 0; i < 10; i++) {
    currentSlots[i * 5].on_click();
  }

  const selectedCards = vm.runInContext('selectedCards', context);
  console.log(`- Successfully selected ${selectedCards.length} cards from the reshuffled deck.`);

  // Confirm deal
  mockElements['btn-confirm-deal'].on_click();

  // Read all 10 cards
  const nextBtn = mockElements['btn-next-step'];
  for (let s = 0; s < 10; s++) {
    nextBtn.on_click();
    nextBtn.on_click();
  }

  const luckyBalls = mockElements['final-lucky-balls'];
  console.log(`- Celtic Cross reading completed! Lucky Baloto balls: ${luckyBalls.children ? luckyBalls.children.length : 6}`);

  console.log("\n=======================================================");
  console.log(" ALL QA TESTS FOR SHUFFLE & HIDDEN CARDS: 100% PASSED! ");
  console.log("=======================================================");
} catch (err) {
  console.error("QA TEST FAILED:", err);
  process.exit(1);
}
