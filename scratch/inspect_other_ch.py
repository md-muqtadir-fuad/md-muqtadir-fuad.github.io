with open('blog-semi-automated-shoe-cleaning-machine.html', 'r', encoding='utf-8') as f:
    content = f.read()

for ch_id in ['ch-01', 'ch-02', 'ch-03', 'ch-04', 'ch-08', 'ch-09']:
    p = content.find(f'id="{ch_id}"')
    if p != -1:
        print(f'=== {ch_id} ===')
        print(content[p:p+300])
        print('...\n')
