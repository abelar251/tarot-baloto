html_button = """
<button onclick="window.open('/predict', '_blank')" style="position: fixed; bottom: 20px; right: 20px; z-index: 9999; background: linear-gradient(135deg, #bc13fe, #d85cff); color: white; font-size: 1.2rem; font-weight: bold; border: none; padding: 15px 30px; border-radius: 50px; cursor: pointer; box-shadow: 0 4px 15px rgba(188, 19, 254, 0.4); font-family: sans-serif;">🔮 Pronóstico Matemático</button>
"""
with open('index.html', 'a', encoding='utf-8') as f:
    f.write(html_button)
print("Button appended!")
