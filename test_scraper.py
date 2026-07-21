import urllib.request
import re

try:
    req = urllib.request.Request('https://baloto.com/resultados', headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Find all divs with class containing 'ball'
    matches = re.finditer(r'<div[^>]*class="[^"]*ball[^"]*"[^>]*>.*?</div>', html, re.IGNORECASE | re.DOTALL)
    for i, m in enumerate(list(matches)[:15]):
        print(f"Match {i}: {m.group(0)}")
except Exception as e:
    print(f"Error: {e}")
