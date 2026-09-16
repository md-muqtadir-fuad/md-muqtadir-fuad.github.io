with open('blog-semi-automated-shoe-cleaning-machine.html', encoding='utf-8') as f:
    c = f.read()

pos = c.find('Figure 2. 3: Cost of single shoe cleaning')
print("Position:", pos)
if pos != -1:
    # Print 2000 chars before
    print("BEFORE FIGURE 2.3:")
    print(c[max(0, pos-2500):pos+400])
