def fix_button():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Insert the button correctly
    btn_html = """
      <div style="text-align: center; margin-top: 30px;">
        <button id="download-btn" style="background: linear-gradient(45deg, #d4af37, #b8860b); color: #000; font-family: 'Cinzel', serif; font-weight: bold; border: none; padding: 10px 20px; font-size: 1.2rem; cursor: pointer; border-radius: 5px; box-shadow: 0 0 10px #d4af37; margin-bottom: 20px; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'" onclick="downloadPrediction()">📥 Descargar Predicción (JPEG)</button>
      </div>
"""
    target = '<button class="btn-restart" onclick="restart()">↺ Nueva Consulta</button>'
    
    if "Descargar Predicción" not in content:
        content = content.replace(target, btn_html + '      <center>' + target + '</center>')
    
    # 2. Fix the JS querySelector
    content = content.replace(".querySelector('#phase-result .btn-shuffle')", ".querySelector('#phase-result .btn-restart')")
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Button fixed successfully.")

if __name__ == '__main__':
    fix_button()
