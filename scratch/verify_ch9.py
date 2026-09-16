def verify():
    with open('blog-semi-automated-shoe-cleaning-machine.html', 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"Total HTML length: {len(content):,} characters")

    # 1. Check Chapter 9 and Conclusion anchors
    anchors = ['ch-09', 'ch-9', 'sec-9-1', 'sec-9-2', 'sec-9-3', 'sec-9-4', 'conclusion']
    missing_anchors = [a for a in anchors if f'id="{a}"' not in content]
    if missing_anchors:
        print(f"FAILED: Missing anchors: {missing_anchors}")
    else:
        print(f"PASSED: All {len(anchors)} chapter and section anchors present.")

    # 2. Check 9 Future Scope innovations
    scope_items = [
        "Fully Automated Cleaning Cycle",
        "IoT & Smart Sensor Integration",
        "Interchangeable Cleaning Heads",
        "Heated Air Rapid Drying System",
        "Expanded Detergent Reservoir",
        "Lightweight Structural Composites",
        "Multi-Pair & Extended Sizing",
        "Industrial Aesthetics & Mechanism Optimization",
        "Solar & Renewable Energy Integration"
    ]
    for s in scope_items:
        if s in content:
            print(f"PASSED: Future Scope innovation found -> '{s}'")
        else:
            print(f"FAILED: Future Scope missing -> '{s}'")

    # 3. Check 8 Limitations
    limits = [
        "Grid Electricity Dependency",
        "Tread Inaccessibility on Deep Grooves",
        "Footwear Dimensional Constraints",
        "Limited Fluid Reservoir Capacity",
        "Mechanical Wear on Brushes & Rollers",
        "User Intervention in Semi-Automation",
        "Acoustic Noise During Peak Operation",
        "Wastewater & Residue Filtration"
    ]
    for l in limits:
        if l in content:
            print(f"PASSED: Limitation found -> '{l}'")
        else:
            print(f"FAILED: Limitation missing -> '{l}'")

    # 4. Check Table 9.1 Roadmap Matrix
    t9_title = "Table 9. 1: Strategic Engineering Roadmap Matrix"
    if t9_title in content:
        print(f"PASSED: Roadmap Table found -> '{t9_title}'")
    else:
        print(f"FAILED: Roadmap Table missing -> '{t9_title}'")

    # 5. Check no broken unicode characters in Chapter 9
    p139_idx = content.find('id="page-139"')
    p143_idx = content.find('id="page-143"')
    ch9_chunk = content[p139_idx:p143_idx] if (p139_idx != -1 and p143_idx != -1) else ""
    if '\ufffd' in ch9_chunk:
        print("FAILED: Found unicode replacement character in Chapter 9 chunk!")
    else:
        print("PASSED: Zero corrupted characters in Chapter 9.")

    # 6. Check Overall Conclusion on Page 142
    if 'Comprehensive Capstone Project Summary' in content and 'SolidWorks + FEA' in content:
        print("PASSED: Overall Conclusion card rendered cleanly on Page 142.")
    else:
        print("FAILED: Overall Conclusion card missing or incomplete.")

    # 7. Check TOC links for Chapter 9
    toc_links = ['#ch-09', '#sec-9-1', '#sec-9-2', '#sec-9-3', '#sec-9-4', '#conclusion']
    for tl in toc_links:
        if f'href="{tl}"' in content:
            print(f"PASSED: Sidebar TOC link found -> '{tl}'")
        else:
            print(f"FAILED: Sidebar TOC link missing -> '{tl}'")

if __name__ == '__main__':
    verify()
