# Update index.html Taboo link
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Replace button for taboo with robust <a> link
pattern = r'<button[^>]*onclick="[^"]*\/taboo[^"]*"[^>]*>[\s\S]*?<\/button>'
replacement = """<a href="/taboo" style="position: fixed; bottom: 20px; left: 20px; z-index: 9999; background: radial-gradient(circle at center, #ff8c00, #8b0000); color: white; font-size: 1rem; font-weight: bold; border: 2px solid #ffcc00; padding: 10px; border-radius: 50%; width: 90px; height: 90px; cursor: pointer; box-shadow: 0 0 20px #ff4500; font-family: 'Cinzel', serif; display: flex; flex-direction: column; align-items: center; justify-content: center; text-decoration: none; transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
    <span style="font-size: 28px; line-height: 1;">☀️</span>
    <span style="font-size: 0.8rem; letter-spacing: 1px; margin-top: 5px; text-shadow: 0 0 5px #000; color: #fff;">TABOO</span>
</a>"""

new_text, count = re.subn(pattern, replacement, text)
if count > 0:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print(f"Successfully updated {count} button(s) in index.html to <a> link.")
else:
    print("Pattern did not match. Let's inspect.")
