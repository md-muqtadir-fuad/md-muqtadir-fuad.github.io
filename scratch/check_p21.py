with open('blog-semi-automated-shoe-cleaning-machine.html', encoding='utf-8') as f:
    c = f.read()

pos = c.find('id="page-21"')
print("Pos:", pos)
if pos != -1:
    print(c[pos:pos+1500])
