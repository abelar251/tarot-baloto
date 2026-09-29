import urllib.request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import re
import json
import concurrent.futures
import time

MAX_WORKERS = 10
START_ID = 2709
MIN_ID = START_ID - 500

def fetch_draw(draw_id, draw_type):
    url = f"https://baloto.com/resultados-{draw_type.lower()}/{draw_id}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        date_str = "Fecha Desconocida"
        for t in soup.stripped_strings:
            match = re.search(r'\d{1,2}\s+de\s+[a-zA-Z]+\s+de\s+\d{4}', t, re.IGNORECASE)
            if match:
                date_str = match.group(0)
                break
                
        ball_divs = soup.find_all('div', class_=lambda c: c and 'ball' in c.lower())
        numbers = []
        for d in ball_divs:
            text = d.get_text(strip=True)
            if re.match(r'^\d{1,2}$', text):
                numbers.append(int(text))
                
        # First 6 numbers usually are the draw (5 main, 1 super)
        if len(numbers) >= 6:
            main_balls = numbers[:5]
            super_ball = numbers[5]
            
            # Simple check for jackpot text
            jackpot_won = False
            if 'gran ganador' in html.lower() or 'cayó' in html.lower():
                jackpot_won = True
                
            return {
                "id": draw_id,
                "type": "Baloto" if draw_type.lower() == 'baloto' else "Revancha",
                "date": date_str,
                "main_balls": main_balls,
                "super_ball": super_ball,
                "jackpot_won": jackpot_won
            }
    except HTTPError as e:
        if e.code != 404:
            print(f"HTTPError {e.code} for ID {draw_id}")
    except Exception as e:
        pass
    
    return None

def scrape_all():
    results = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {}
        for draw_id in range(START_ID, MIN_ID - 1, -1):
            futures[executor.submit(fetch_draw, draw_id, "baloto")] = draw_id
            futures[executor.submit(fetch_draw, draw_id, "revancha")] = draw_id
            
        done_count = 0
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            done_count += 1
            if res:
                results.append(res)
            
            if done_count % 100 == 0:
                print(f"Procesados {done_count} peticiones. Encontrados {len(results)} resultados.")

    # Sort by ID descending (newest first), then by type (Baloto first)
    results.sort(key=lambda x: (-x['id'], 0 if x['type'] == 'Baloto' else 1))
    
    # Remove 'id' before saving to match existing format
    final_results = []
    for r in results:
        del r['id']
        final_results.append(r)
        
    with open("baloto_history.json", "w", encoding="utf-8") as f:
        json.dump(final_results, f, indent=4)
        
    print(f"Scraping completado. Total de registros guardados: {len(final_results)}")

if __name__ == "__main__":
    start = time.time()
    scrape_all()
    print(f"Tiempo total: {time.time() - start:.2f} segundos")
