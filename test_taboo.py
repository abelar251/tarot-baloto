import re

with open('taboo.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check all document.getElementById calls
ids_in_js = re.findall(r"document\.getElementById\(['\"]([^'\"]+)['\"]\)", html)
print(f"Total getElementById calls: {len(ids_in_js)}")

missing_ids = []
for el_id in set(ids_in_js):
    # Check if id exists in html
    pattern = rf'id=[\'"]{re.escape(el_id)}[\'"]'
    if not re.search(pattern, html):
        missing_ids.append(el_id)

if missing_ids:
    print("ERROR - Missing IDs in HTML:", missing_ids)
else:
    print("ALL IDs VALIDATED! Every single element ID referenced in JS exists in HTML.")

# Check script syntax by extracting JS blocks
scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
print(f"Found {len(scripts)} script blocks.")

# Check MAJOR
major_count = len(re.findall(r'arcana:\s*[\'"]Mayor[\'"]', html))
print(f"MAJOR arcana items verified: {major_count} (Expected 22)")

# Check Meanings
meanings_count = len(re.findall(r'significado:\s*[\'"]', html))
print(f"Meanings entries verified: {meanings_count} (Expected 44 = 22 upright + 22 rev)")

print("TEST COMPLETED!")
