import re

def fix_download():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    new_download_js = """    function downloadPrediction() {
      const btn = document.getElementById('download-btn');
      const restartBtn = document.querySelector('#phase-result .btn-restart');
      btn.style.display = 'none';
      restartBtn.style.display = 'none';
      
      // Disable animations to prevent html2canvas from failing to render moving elements
      const noAnimStyle = document.createElement('style');
      noAnimStyle.innerHTML = `* { animation: none !important; transition: none !important; }`;
      document.head.appendChild(noAnimStyle);
      
      // Small delay to ensure browser applies the no-animation style before capture
      setTimeout(() => {
          html2canvas(document.getElementById('phase-result'), {
              backgroundColor: '#0a0a0a',
              scale: 2,
              useCORS: true,
              logging: false,
              allowTaint: true
          }).then(canvas => {
              const link = document.createElement('a');
              link.download = 'tarot_baloto_prediccion.jpg';
              link.href = canvas.toDataURL('image/jpeg', 0.9);
              link.click();
              
              btn.style.display = 'inline-block';
              restartBtn.style.display = 'inline-block';
              document.head.removeChild(noAnimStyle);
          }).catch(err => {
              console.error("Error capturing image:", err);
              btn.style.display = 'inline-block';
              restartBtn.style.display = 'inline-block';
              document.head.removeChild(noAnimStyle);
          });
      }, 100);
    }
"""
    
    # We replace from "function downloadPrediction() {" down to the closing brace before </script>
    pattern = re.compile(r'([ \t]*function downloadPrediction\(\) \{.*?\n[ \t]*\})(?=\s*</script>)', re.DOTALL)
    if pattern.search(content):
        content = pattern.sub(new_download_js, content)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Download function fixed.")
    else:
        print("Could not match the downloadPrediction block.")

if __name__ == '__main__':
    fix_download()
