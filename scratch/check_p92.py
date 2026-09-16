with open('blog-semi-automated-shoe-cleaning-machine.html', 'r', encoding='utf-8') as f:
    html = f.read()

p92 = html.find('id="page-92"')
p93 = html.find('id="page-93"')
print(html[p92:p93])
