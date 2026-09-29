import json

try:
    with open("baloto_history.json", "r", encoding="utf-8") as f:
        history = json.load(f)
except Exception:
    history = []

latest_baloto = {
    "type": "Baloto",
    "date": "2026-09-14",
    "main_balls": [3, 5, 10, 20, 31],
    "super_ball": 8,
    "jackpot_won": False
}

latest_revancha = {
    "type": "Revancha",
    "date": "2026-09-14",
    "main_balls": [4, 12, 15, 17, 29],
    "super_ball": 16,
    "jackpot_won": False
}

history.append(latest_baloto)
history.append(latest_revancha)

with open("baloto_history.json", "w", encoding="utf-8") as f:
    json.dump(history, f, indent=4)
print("Added Sep 14 results.")
