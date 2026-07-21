import re

def update_code():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add html2canvas to head
    if "html2canvas.min.js" not in content:
        content = content.replace("</head>", '    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>\n</head>')

    # 2. Add download button in HTML
    btn_html = """      <div style="text-align: center; margin-top: 30px;">
        <button id="download-btn" style="background: linear-gradient(45deg, #d4af37, #b8860b); color: #000; font-family: 'Cinzel', serif; font-weight: bold; border: none; padding: 10px 20px; font-size: 1.2rem; cursor: pointer; border-radius: 5px; box-shadow: 0 0 10px #d4af37; margin-bottom: 20px; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'" onclick="downloadPrediction()">📥 Descargar Predicción (JPEG)</button>
      </div>
"""
    if "Descargar Predicción" not in content:
        content = content.replace('<button class="btn-shuffle" onclick="restart()">Comenzar Nueva Lectura</button>', btn_html + '      <button class="btn-shuffle" onclick="restart()">Comenzar Nueva Lectura</button>')

    # 3. Inject getNextBalotoDate() inside showOracleResults
    date_js = """
      const numDisp = document.getElementById('numbers-display');
      numDisp.innerHTML = '';
      
      const today = new Date();
      let d = new Date(today);
      while (d.getDay() !== 3 && d.getDay() !== 6) {
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
"""
    # Replace the existing numDisp logic
    content = content.replace("      const numDisp = document.getElementById('numbers-display');\n      numDisp.innerHTML = '';", date_js)

    # 4. Add downloadPrediction function at the end of script
    download_js = """
    function downloadPrediction() {
      const btn = document.getElementById('download-btn');
      const restartBtn = document.querySelector('#phase-result .btn-shuffle');
      btn.style.display = 'none';
      restartBtn.style.display = 'none';
      
      html2canvas(document.getElementById('phase-result'), {
          backgroundColor: '#0a0a0a',
          scale: 2
      }).then(canvas => {
          const link = document.createElement('a');
          link.download = 'tarot_baloto_prediccion.jpg';
          link.href = canvas.toDataURL('image/jpeg', 0.9);
          link.click();
          
          btn.style.display = 'inline-block';
          restartBtn.style.display = 'inline-block';
      });
    }
"""
    if "function downloadPrediction()" not in content:
        content = content.replace('</script>', download_js + '</script>')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_code()
