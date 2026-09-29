import json
import re
from datetime import datetime

MESES = {
    'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
    'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
}

def parse_date(date_str):
    match = re.search(r'(\d{1,2})\s+de\s+([a-zA-Z]+)\s+de\s+(\d{4})', date_str, re.IGNORECASE)
    if match:
        d = int(match.group(1))
        m = MESES.get(match.group(2).lower(), 1)
        y = int(match.group(3))
        return datetime(y, m, d)
    return datetime.min

with open('baloto_history.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

unique_data = {}
for d in data:
    k = f"{d.get('date')} - {d.get('type')}"
    # Keep the latest entry (so if we just appended new draws they overwrite)
    unique_data[k] = d

data = list(unique_data.values())

data.sort(key=lambda x: (parse_date(x.get('date', '')), 0 if x.get('type') == 'Baloto' else 1))

with open('baloto_history.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("Fixed sort.")
