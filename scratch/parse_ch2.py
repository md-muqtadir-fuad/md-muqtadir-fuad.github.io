import fitz
import re

doc = fitz.open(r'C:\Users\DELL\Downloads\pd_report.pdf')

questions = []

for pno in range(26, 43):
    page = doc[pno]
    txt = page.get_text()
    lines = [l.strip() for l in txt.split('\n') if l.strip()]
    
    # 1. Find question prompt
    q_prompt = None
    for l in lines:
        if re.match(r'^\d+\.\s+', l):
            q_prompt = l
            break
            
    # 2. Find options
    options = []
    for l in lines:
        if l.startswith('o ') or l == 'o':
            options.append(l)
            
    # 3. Find Table caption
    tab_cap = None
    for l in lines:
        if l.startswith('Table 2.'):
            tab_cap = l
            break
            
    # 4. Find Figure caption
    fig_cap = None
    for l in lines:
        if l.startswith('Figure 2.'):
            fig_cap = l
            break
            
    # 5. Get Table Data from find_tables()
    tabs = page.find_tables().tables
    tab_data = []
    if tabs:
        raw_tab = tabs[0].extract()
        # Clean rows: ignore row if it looks like the chart text
        for r in raw_tab:
            row_clean = [c.strip() if c else "" for c in r]
            # filter out None or empty or chart text row
            if any(row_clean) and not any('Daily Weekly' in c or 'Time consuming\nIneffective' in c for c in row_clean):
                # keep only valid table columns
                row_filtered = [c for c in row_clean if c is not None]
                tab_data.append(row_filtered)
                
    questions.append({
        'page': pno + 1,
        'prompt': q_prompt,
        'options': options,
        'tab_cap': tab_cap,
        'tab_data': tab_data,
        'fig_cap': fig_cap
    })

print(f"Parsed {len(questions)} survey questions.")
for q in questions[:3]:
    print(f"P{q['page']}: {q['prompt']} | Options: {len(q['options'])} | Tab rows: {len(q['tab_data'])} | Fig: {q['fig_cap']}")
