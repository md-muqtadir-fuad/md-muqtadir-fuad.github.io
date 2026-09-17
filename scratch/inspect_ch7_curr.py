with open('blog-semi-automated-shoe-cleaning-machine.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
pos7 = content.find('id="ch-07"')
if pos7 == -1:
    pos7 = content.find('id="ch-7"')
if pos7 == -1:
    pos7 = content.find('Chapter 07')
print('Chapter 7 start pos:', pos7)

pos8 = content.find('id="ch-08"')
if pos8 == -1:
    pos8 = content.find('id="ch-8"')
if pos8 == -1:
    pos8 = content.find('Chapter 08')
print('Chapter 8 start pos:', pos8)

ch7_html = content[pos7:pos8]
print('Length of Chapter 7 HTML:', len(ch7_html))
print('Tables in Chapter 7 HTML:', len(re.findall(r'<table', ch7_html)))
print('Page markers in Chapter 7 HTML:', re.findall(r'id="page-\d+"', ch7_html))
print('Headings in Chapter 7 HTML:', re.findall(r'<h[1-6][^>]*>.*?</h[1-6]>', ch7_html))
