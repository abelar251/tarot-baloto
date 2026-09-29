import urllib.request
from bs4 import BeautifulSoup
import re

try:
    req = urllib.request.Request('https://baloto.com/resultados', headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    # Try to find dates in text
    texts = soup.stripped_strings
    for t in texts:
        if re.search(r'\d{1,2}\s+de\s+[a-zA-Z]+\s+de\s+\d{4}', t, re.IGNORECASE) or 'sorteo' in t.lower() or 'fecha' in t.lower():
            print(t)
            
except Exception as e:
    print(f"Error: {e}")
