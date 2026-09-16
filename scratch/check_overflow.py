from bs4 import BeautifulSoup
import re

with open('blog-semi-automated-shoe-cleaning-machine.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check for elements that might cause horizontal scroll
# 1. Look for fixed widths
fixed_widths = re.findall(r'class="[^"]*(?:w-\[\d+px\]|min-w-\[\d+px\])[^"]*"', html)
print(f"Total fixed width elements found: {len(fixed_widths)}")
from collections import Counter
print("Top fixed width classes:", Counter(fixed_widths).most_common(10))

# 2. Look for tables outside overflow-x-auto
soup = BeautifulSoup(html, 'html.parser')
tables = soup.find_all('table')
print(f"\nTotal tables: {len(tables)}")
tables_without_overflow = []
for idx, tab in enumerate(tables):
    parent = tab.parent
    parent_classes = parent.get('class', [])
    if 'overflow-x-auto' not in parent_classes and 'overflow-x-scroll' not in parent_classes:
        tables_without_overflow.append((idx, parent.name, parent_classes))

print(f"Tables WITHOUT overflow-x-auto on parent: {len(tables_without_overflow)}")
for t in tables_without_overflow[:10]:
    print("  Table without overflow:", t)
