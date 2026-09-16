import re

def verify():
    with open('blog-semi-automated-shoe-cleaning-machine.html', 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"Total HTML length: {len(content):,} characters")

    # 1. Check Chapter 8 header and section anchors
    sections = [
        'ch-08', 'sec-8-1', 'sec-8-2', 'sec-8-2-1', 'sec-8-2-2', 'sec-8-2-3',
        'sec-8-2-4', 'sec-8-2-5', 'sec-8-3', 'sec-8-3-1', 'sec-8-3-2', 'sec-8-3-3',
        'sec-8-3-4', 'sec-8-3-5', 'sec-8-3-6', 'sec-8-4', 'sec-8-4-1', 'sec-8-4-2',
        'sec-8-4-3', 'sec-8-5', 'sec-8-6', 'sec-8-7', 'sec-8-7-1', 'sec-8-7-2',
        'sec-8-7-3', 'sec-8-7-4', 'sec-8-7-5'
    ]
    missing_sec = [s for s in sections if f'id="{s}"' not in content]
    if missing_sec:
        print(f"FAILED: Missing section IDs: {missing_sec}")
    else:
        print(f"PASSED: All {len(sections)} section anchors present.")

    # 2. Check Tables 8.1 through 8.7
    tables = [
        'Table 8. 1: Purchasing Cost per Unit (External Parts)',
        'Table 8. 2: Manufacturing Overhead Cost',
        'Table 8. 3: Total Manufacturing Cost',
        'Table 8. 4: Administrative Cost of Personnel',
        'Table 8. 5: Total Non-Manufacturing Cost',
        'Table 8. 6: Total Yearly Cost',
        'Table 8. 7: Direct Material Cost'
    ]
    for t in tables:
        if t in content:
            print(f"PASSED: Table title found -> '{t}'")
        else:
            print(f"FAILED: Missing table title -> '{t}'")

    # 3. Check Unified Table 8.1 has all parts
    t8_1_parts = ['Spur Gear', 'Worm Gear', 'AC to DC Converter', 'Nut & Bolt Set', 'Ball Bearing', 'DC Motor (1 HP)', 'Solid Shoe Shiner']
    for p in t8_1_parts:
        if p in content:
            print(f"PASSED: Table 8.1 part found -> '{p}'")
        else:
            print(f"FAILED: Table 8.1 missing part -> '{p}'")

    # 4. Check for dirty vector chart text on Page 134
    dirty_snippets = ['VC TC FC REV', '0 100 200 300 400 500 600', 'BEP Analysis']
    p134_idx = content.find('id="page-134"')
    p135_idx = content.find('id="page-135"')
    p134_chunk = content[p134_idx:p135_idx] if (p134_idx != -1 and p135_idx != -1) else ""
    
    found_dirty = False
    for ds in dirty_snippets:
        if ds in p134_chunk:
            print(f"FAILED: Found dirty vector OCR snippet on Page 134: '{ds}'")
            found_dirty = True
    if not found_dirty:
        print("PASSED: Page 134 is completely clean of vector chart OCR text.")

    # 5. Check Break Even Equilibrium Formula and Payback
    if 'Q_{BEP} = 226' in content and '0.40 \\text{ years}' in content:
        print("PASSED: Break-Even Equilibrium and Payback formulas rendered in KaTeX.")
    else:
        print("FAILED: Break-Even formulas missing or incorrect.")

    # 6. Check Sensitivity Summary Matrix
    if 'Sensitivity Ranking Across All Cost Drivers' in content and '25.22%' in content and '6.64%' in content:
        print("PASSED: Sensitivity Summary Ranking Matrix rendered.")
    else:
        print("FAILED: Sensitivity Summary Ranking Matrix missing.")

    # 7. Check TOC links for Chapter 8
    toc_links = ['#ch-08', '#sec-8-2', '#sec-8-3', '#sec-8-4', '#sec-8-6', '#sec-8-7']
    for tl in toc_links:
        if f'href="{tl}"' in content:
            print(f"PASSED: Sidebar TOC link found -> '{tl}'")
        else:
            print(f"FAILED: Sidebar TOC link missing -> '{tl}'")

if __name__ == '__main__':
    verify()
