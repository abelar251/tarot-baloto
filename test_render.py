test_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
body { background: #000; color: #fff; font-family: 'Press Start 2P', monospace, sans-serif; }
.card {
  width: 80px; height: 130px; background-color: #f4e8c1;
  border: 2px solid #1a1a1a; display: flex; flex-direction: column; align-items: center; justify-content: space-around;
  margin: 10px; float: left;
}
.art-old {
  font-size: 2.1rem;
  filter: sepia(0.6) hue-rotate(-10deg) saturate(1.2) contrast(1.2);
  line-height: 1;
}
.art-new {
  font-family: 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji', sans-serif;
  color: #1a1a1a;
  font-size: 2.2rem;
  line-height: 1;
}
.label { font-size: 10px; color: #1a1a1a; }
</style>
</head>
<body>
  <div class="card">
    <div class="label">Old ⚔️</div>
    <div class="art-old">⚔️</div>
  </div>
  <div class="card">
    <div class="label">New ⚔️</div>
    <div class="art-new">⚔️</div>
  </div>
  <div class="card">
    <div class="label">Old 🪄</div>
    <div class="art-old">🪄</div>
  </div>
  <div class="card">
    <div class="label">New 🪄</div>
    <div class="art-new">🪄</div>
  </div>
  <div class="card">
    <div class="label">Old 🪙</div>
    <div class="art-old">🪙</div>
  </div>
  <div class="card">
    <div class="label">New 🪙</div>
    <div class="art-new">🪙</div>
  </div>
</body>
</html>
"""

with open('test_render.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

print("test_render.html created.")
