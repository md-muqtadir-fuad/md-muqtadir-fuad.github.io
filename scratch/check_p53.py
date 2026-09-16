with open('blog-semi-automated-shoe-cleaning-machine.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="page-53"')
next_idx = html.find('id="page-54"')
print(html[idx:next_idx])
