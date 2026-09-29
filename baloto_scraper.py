import requests
from bs4 import BeautifulSoup
import json
import os
import re

class BalotoScraper:
    def __init__(self, output_file="baloto_history.json"):
        self.url = "https://baloto.com/resultados"
        self.output_file = output_file
        
    def scrape_current_results(self):
        """Scrapes the visible results from the baloto website."""
        print(f"Buscando resultados en {self.url}...")
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Buscamos divs que en su clase tengan la palabra 'ball'
            ball_divs = soup.find_all('div', class_=lambda c: c and 'ball' in c.lower())
            
            # Buscamos la fecha del sorteo
            date_str = None
            texts = soup.stripped_strings
            for t in texts:
                match = re.search(r'\d{1,2}\s+de\s+[a-zA-Z]+\s+de\s+\d{4}', t, re.IGNORECASE)
                if match:
                    date_str = match.group(0)
                    break
            
            if not date_str:
                date_str = "Fecha Desconocida"

            # Limpiamos el texto para obtener solo números
            numbers = []
            for d in ball_divs:
                text = d.get_text(strip=True)
                # Ensure it's a number and only 1 or 2 digits
                if re.match(r'^\d{1,2}$', text):
                    numbers.append(int(text))
            
            results = []
            
            # El portal usualmente muestra Baloto primero, luego Revancha (grupos de 6)
            # Cada grupo tiene 5 balotas y 1 super balota
            for i in range(0, len(numbers), 6):
                if i + 5 < len(numbers):
                    draw_type = "Baloto" if i == 0 else "Revancha" if i == 6 else f"Sorteo_{i//6}"
                    main_balls = numbers[i:i+5]
                    super_ball = numbers[i+5]
                    # Simple check for jackpot text on the live page
                    jackpot_won = False
                    if 'gran ganador' in response.text.lower() or 'cayó baloto' in response.text.lower():
                        jackpot_won = True
                        
                    results.append({
                        "type": draw_type,
                        "date": date_str,
                        "main_balls": main_balls,
                        "super_ball": super_ball,
                        "jackpot_won": jackpot_won
                    })
            
            return results
        except Exception as e:
            print(f"Error al hacer scraping de Baloto: {e}")
            return []

    def load_history(self):
        """Load existing history if any."""
        if os.path.exists(self.output_file):
            with open(self.output_file, 'r', encoding='utf-8') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def save_history(self, new_results):
        """Save results to JSON history file."""
        history = self.load_history()
        
        # En una app real cruzaríamos por fecha/número de sorteo para no duplicar,
        # pero aquí simplemente guardaremos si son diferentes al último.
        
        added = 0
        for nr in new_results:
            # Check if this exact draw is already the last one in history
            if history:
                last_of_type = [h for h in history if h.get('type') == nr['type']]
                if last_of_type:
                    last = last_of_type[-1]
                    if last['main_balls'] == nr['main_balls'] and last['super_ball'] == nr['super_ball']:
                        continue # Already saved
            
            history.append(nr)
            added += 1
            
        with open(self.output_file, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=4)
            
        return added

if __name__ == "__main__":
    scraper = BalotoScraper()
    results = scraper.scrape_current_results()
    if results:
        print(f"Se encontraron {len(results)} sorteos en la página.")
        for r in results:
            print(f"{r['type']}: {r['main_balls']} - Super Balota: {r['super_ball']}")
        added = scraper.save_history(results)
        print(f"Se añadieron {added} nuevos registros al historial.")
    else:
        print("No se encontraron resultados.")
