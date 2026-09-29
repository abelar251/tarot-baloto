import json
import random
from datetime import datetime, timedelta

history = []
start_date = datetime.now() - timedelta(days=70) # Roughly 10 weeks, 2 draws per week = 20 draws

for i in range(20):
    # Baloto
    b_balls = sorted(random.sample(range(1, 44), 5))
    b_super = random.randint(1, 16)
    history.append({
        "type": "Baloto",
        "date": start_date.strftime("%Y-%m-%d"),
        "main_balls": b_balls,
        "super_ball": b_super,
        "jackpot_won": random.choice([True, False, False, False, False, False, False, False, False, False]) # 10% chance
    })
    
    # Revancha
    r_balls = sorted(random.sample(range(1, 44), 5))
    r_super = random.randint(1, 16)
    history.append({
        "type": "Revancha",
        "date": start_date.strftime("%Y-%m-%d"),
        "main_balls": r_balls,
        "super_ball": r_super,
        "jackpot_won": random.choice([True, False, False, False, False, False, False, False, False, False]) # 10% chance
    })
    
    start_date += timedelta(days=3 if i % 2 == 0 else 4)

with open("baloto_history.json", "w", encoding="utf-8") as f:
    json.dump(history, f, indent=4)

print("Generated 40 history records.")
