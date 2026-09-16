import re

with open('blog-semi-automated-shoe-cleaning-machine.html', 'r', encoding='utf-8') as f:
    c = f.read()

anchors = [
    'ch-01', 'ch-02', 'ch-03', 'ch-04', 'ch-05', 'ch-06', 'ch-07', 'ch-08', 'ch-9',
    'sec-2-3', 'sec-5-3-1', 'sec-5-3-2', 'sec-5-3-3', 'sec-5-3-4', 'sec-5-3-5',
    'table-of-contents', 'list-of-tables', 'list-of-illustrations',
    'copyright-notice', 'forwarding-letter', 'preface', 'abstract', 'acknowledgement',
    'conclusion', 'appendix', 'page-147', 'reference'
]

print('=== ANCHORS CHECK ===')
missing = [a for a in anchors if f'id="{a}"' not in c and f"id='{a}'" not in c]
print('Missing anchors:', missing if missing else 'None! All 27 present.')

print('=== TABLES CHECK ===')
print('=== CHAPTER IDS IN HTML ===')
print(re.findall(r'id=[\"\']ch-[^\"\']+[\"\']', c))
print('TOC links to ch-:', re.findall(r'href=[\"\']#ch-[^\"\']+[\"\']', c))


# Check specific cells in Table A.1 and A.2
print('G10060 present:', 'G10060' in c)
print('G10950 present:', 'G10950' in c)
print('Beryllium copper present:', 'Beryllium copper' in c)
print('Titanium alloys present:', 'Titanium alloys' in c)
