import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ch6_7_catalog.json', 'r', encoding='utf-8') as f:
    cat = json.load(f)
t120 = cat['120']['tables'][1]
for idx, r in enumerate(t120):
    cleaned = [c.replace('\n', ' ') if c else '' for c in r]
    print(f"Row {idx:2d} (len {len(r):2d}): {cleaned}")
