# -*- coding: utf-8 -*-
import re
import html

def clean_txt(s):
    if s is None:
        return ""
    s = str(s)
    if not s:
        return ""
    s = s.replace('\ufb01', 'fi').replace('\ufb02', 'fl').replace('\ufb03', 'ffi').replace('\ufb04', 'ffl')
    s = s.replace('\u2018', "'").replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"')
    return ' '.join(s.split())

def render_ch6_material_table(tab_data):
    """Table 6.1: Qualitative Analysis of Material Selection for Different Sections"""
    h = []
    h.append('<div class="overflow-x-auto relative max-w-full my-8 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white min-w-[760px]">')
    h.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left w-36">Section</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left w-32">Sub-section</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left w-36">Parts</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left w-40 bg-gray-200/60">Material Selection</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left">Other Material Options</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left w-52">Reasons Behind Selection</th>')
    h.append('    </tr></thead>')
    h.append('    <tbody>')

    sections = [
        ("Brush Cleaning Part", [
            ("Base", "Base", "Nylon", "Polycarbonate, ABS", "Impact resistance, lightweight"),
            ("Brush", "Nylon Brush Fiber", "Nylon 6", "Polypropylene, Polyester (PET)", "Durability, flexibility, water resistance"),
            ("Motor", "DC Motor", "Gear Motor", "Brushed DC Motor", "High torque, speed regulation"),
            ("Mechanism", "Worm Gear", "Mild Steel", "High-Speed Steel, Alloy Steel", "Cost-effective, durability"),
        ]),
        ("Shiner Part", [
            ("Shiner Mechanism", "Vibrating Plate", "Stainless Steel", "Mild Steel, Aluminum Alloy", "Easy to clean, high durability"),
            ("Shiner Mechanism", "Mold Sponge", "Polyurethane Foam", "Rubber, Felt", "Good cushioning, lightweight"),
            ("Shiner Mechanism", "Dispenser", "Mild Steel", "Cast Iron, Mild", "Lightweight, chemical resistance"),
        ]),
        ("Shoe Sole Cleaning Part", [
            ("Roller Mechanism", "Roller Brush", "Nylon Bristle", "Polypropylene, PVC", "Abrasion resistance, flexibility"),
            ("Base", "Base", "Stainless Steel", "High-Density Polyethylene", "Durability, strength"),
        ])
    ]

    for sec_name, rows in sections:
        for r_idx, (sub_sec, parts, mat, others, reasons) in enumerate(rows):
            h.append('      <tr class="border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
            if r_idx == 0:
                h.append(f'        <td rowspan="{len(rows)}" class="border border-black p-2.5 font-bold text-gray-900 bg-gray-50/80 align-top">{sec_name}</td>')
            h.append(f'        <td class="border border-black p-2 font-medium text-gray-800">{sub_sec}</td>')
            h.append(f'        <td class="border border-black p-2 font-semibold text-black">{parts}</td>')
            h.append(f'        <td class="border border-black p-2 font-bold text-black bg-yellow-50/50">{mat}</td>')
            h.append(f'        <td class="border border-black p-2 text-gray-600">{others}</td>')
            h.append(f'        <td class="border border-black p-2 text-gray-700 italic">{reasons}</td>')
            h.append('      </tr>')

    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_ch6_manufacturing_table():
    """Table 6.2: Qualitative Analysis of Manufacturing Process Selection (Merged across Pages 98 & 99)"""
    h = []
    h.append('<div class="overflow-x-auto relative max-w-full my-8 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white min-w-[850px]">')
    h.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left w-36">Section</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left w-32">Sub-section</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left w-32">Parts</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left">Possible Manufacturing Process</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-center w-28">Make / Outsource</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left w-36 bg-gray-200/60">Process Selection</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left w-52">Reasons Behind Selection</th>')
    h.append('    </tr></thead>')
    h.append('    <tbody>')

    sections = [
        ("Brush Cleaning Part", [
            ("Base", "Base", "Injection Molding, Casting", "Make", "Injection Molding", "Uniformity, cost-effective for complex shapes"),
            ("Brush", "Nylon Brush Fiber", "Extrusion, Injection Molding", "Outsource", "Extrusion", "Better control over fiber thickness"),
            ("Motor", "DC Motor", "Assembly", "Outsource", "Assembly", "More convenient to buy pre-assembled"),
            ("Mechanism", "Spur Gear", "Gear Cutting, Hobbing", "Make", "Gear Cutting", "Achieves high dimensional accuracy"),
        ]),
        ("Shiner Part", [
            ("Shiner Mechanism", "Mold Sponge", "Die Cutting", "Make", "Die Cutting", "Cost-effective for soft materials"),
            ("Motor", "Motor", "Assembly", "Outsource", "Assembly", "More convenient to buy pre-assembled"),
        ]),
        ("Shoe Sole Cleaning Part", [
            ("Roller Mechanism", "Roller Brush", "Extrusion, Milling", "Outsource", "Extrusion", "Cost-effective for brush production"),
            ("Base", "Base", "Bending, Welding", "Make", "Bending", "Durability, easy to form"),
        ])
    ]

    for sec_name, rows in sections:
        for r_idx, (sub_sec, parts, poss_proc, mo, sel_proc, reasons) in enumerate(rows):
            mo_badge = '<span class="px-2 py-0.5 bg-black text-white text-[10px] uppercase font-mono font-bold">Make</span>' if mo == "Make" else '<span class="px-2 py-0.5 bg-gray-200 text-gray-800 text-[10px] uppercase font-mono font-bold">Outsource</span>'
            h.append('      <tr class="border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
            if r_idx == 0:
                h.append(f'        <td rowspan="{len(rows)}" class="border border-black p-2.5 font-bold text-gray-900 bg-gray-50/80 align-top">{sec_name}</td>')
            h.append(f'        <td class="border border-black p-2 font-medium text-gray-800">{sub_sec}</td>')
            h.append(f'        <td class="border border-black p-2 font-semibold text-black">{parts}</td>')
            h.append(f'        <td class="border border-black p-2 text-gray-700">{poss_proc}</td>')
            h.append(f'        <td class="border border-black p-2 text-center">{mo_badge}</td>')
            h.append(f'        <td class="border border-black p-2 font-bold text-black bg-yellow-50/50">{sel_proc}</td>')
            h.append(f'        <td class="border border-black p-2 text-gray-700 italic">{reasons}</td>')
            h.append('      </tr>')

    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_ch6_joining_table():
    """Table 6.3: Qualitative Analysis of Parts Joining Method Selection (Merged across Pages 99 & 100)"""
    h = []
    h.append('<div class="overflow-x-auto relative max-w-full my-8 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white min-w-[760px]">')
    h.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left w-48">Parts</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-center w-28">Type of Joint</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left">Joining Method Options</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left w-44 bg-gray-200/60">Joint Selected</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left w-64">Reasons Behind Selection</th>')
    h.append('    </tr></thead>')
    h.append('    <tbody>')

    joints = [
        ("Base and Casing", "Permanent", "Brazing, Soldering, Explosion Welding, Friction Stir Welding", "Brazing", "Cheap, highly available"),
        ("Base and Bearing", "Permanent", "Shrink Fitting, Press Fitting, Adhesive Bonding, Welding", "Arc Welding", "Cost-effective, no requirement of high precision"),
        ("Motor and Shaft", "Temporary", "Threaded Connection, Welding, Tapered Connection with Locking Nut", "Threaded Connection", "Flexibility, easily removable"),
        ("Bearing and Shaft", "Temporary", "Shrink Fitting, Press Fitting, Adhesive Bonding, Set Screw, Locking Collars", "Press Fitting", "Ease of maintenance, good for high-speed applications"),
        ("Shaft and Gear", "Permanent", "Welding, Brazing, Adhesive Bonding, Tapered Shaft and Gear", "Brazing", "Cheap, highly available"),
        ("Shaft and Wheel", "Permanent", "Bolted Joint, Adhesive Bonding, Keyed Joint, Welding", "Brazing", "Cost-effective, simple to execute"),
        ("Wheel and Crank Shaft", "Temporary", "Bolted Flange Connection, Spline Connection, Welding", "Bolted Flange Connection", "High strength, ease of disassembly")
    ]

    for parts, j_type, opts, sel_j, reasons in joints:
        badge = '<span class="px-2 py-0.5 bg-black text-white text-[10px] uppercase font-mono font-bold">Permanent</span>' if j_type == "Permanent" else '<span class="px-2 py-0.5 bg-gray-200 text-gray-800 text-[10px] uppercase font-mono font-bold">Temporary</span>'
        h.append('      <tr class="border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
        h.append(f'        <td class="border border-black p-2.5 font-bold text-gray-900">{parts}</td>')
        h.append(f'        <td class="border border-black p-2 text-center">{badge}</td>')
        h.append(f'        <td class="border border-black p-2 text-gray-700">{opts}</td>')
        h.append(f'        <td class="border border-black p-2 font-bold text-black bg-yellow-50/50">{sel_j}</td>')
        h.append(f'        <td class="border border-black p-2 text-gray-700 italic">{reasons}</td>')
        h.append('      </tr>')

    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_digital_logic_table(tab_data, caption=""):
    """
    Renders a Digital Logic Table with a clean 2-tier header:
    - Row 1: Selection Criteria (rowspan=2), Number of positive decisions (colspan=M), Positive Decisions (rowspan=2), Relative Emphasis (rowspan=2)
    - Row 2: Column numbers 1..M
    - Data rows: 1/0 decision matrix with sticky criteria column
    - Footer row: Total positive decisions
    """
    if not tab_data or len(tab_data) < 3:
        return ""

    r0 = tab_data[0]
    r1 = tab_data[1]
    data_rows = tab_data[2:]

    # Identify decision columns from row 1
    dec_cols = []
    for c_idx in range(1, len(r1)):
        val = clean_txt(r1[c_idx]).replace('\n', '').replace(' ', '')
        if re.match(r'^\d+$', val):
            dec_cols.append((c_idx, val))

    num_dec = len(dec_cols)
    if num_dec == 0:
        return None

    # Title / caption match
    header_title_cell = clean_txt(r0[1]) if len(r0) > 1 and r0[1] else ""
    m_n = re.search(r'N\s*=\s*n\s*\(\s*n\s*-\s*1\s*\)\s*/\s*2\s*=\s*(\d+)\s*\(\s*(\d+)\s*-\s*1\s*\)\s*/\s*2\s*=\s*(\d+)', header_title_cell)
    n_formula = rf"Number of Positive Decisions, $N = \frac{{n(n-1)}}{{2}} = {num_dec}$"
    if m_n:
        n_formula = rf"Number of Positive Decisions, $N = \frac{{n(n-1)}}{{2}} = \frac{{{m_n.group(1)}({m_n.group(1)}-1)}}{{2}} = {m_n.group(3)}$"

    # Criteria column width & table min-width
    min_w = "min-w-[1500px]" if num_dec > 20 else ("min-w-[900px]" if num_dec > 10 else "min-w-[760px]")

    h = []
    h.append('<div class="overflow-x-auto relative max-w-full my-8 border border-black shadow-xs bg-white rounded-xs">')
    h.append(f'  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white {min_w}">')
    
    # 2-tier Header
    h.append('    <thead>')
    h.append('      <tr class="bg-gray-100 text-black border-b border-black">')
    h.append('        <th rowspan="2" class="border border-black p-2.5 font-bold uppercase text-left w-52 sticky left-0 bg-gray-100 z-10 shadow-xs">Selection Criteria</th>')
    h.append(f'        <th colspan="{num_dec}" class="border border-black p-2 font-bold uppercase text-center bg-gray-200/80">{n_formula}</th>')
    h.append('        <th rowspan="2" class="border border-black p-2 font-bold uppercase text-center w-24 align-middle">Positive Decisions</th>')
    h.append(r'        <th rowspan="2" class="border border-black p-2 font-bold uppercase text-center w-28 align-middle">Relative Emphasis ($\alpha$)</th>')
    h.append('      </tr>')
    
    # Second header row: column numbers
    h.append('      <tr class="bg-gray-50 text-black border-b border-black">')
    for _, col_num in dec_cols:
        pad = "p-0.5 text-[9px]" if num_dec > 20 else "p-1 text-[10px]"
        h.append(f'        <th class="border border-black {pad} text-center font-bold text-gray-700 bg-gray-100/70">{col_num}</th>')
    h.append('      </tr>')
    h.append('    </thead>')

    # Body
    h.append('    <tbody>')
    for r_idx, row in enumerate(data_rows):
        crit_name = clean_txt(row[0])
        
        # If crit_name is empty on first row, check if row 0 had extra text after Selection Criteria
        if not crit_name and r_idx == 0:
            hdr_c0 = clean_txt(r0[0])
            crit_cand = re.sub(r'^(Selection\s+Criteria|Criteria)\s*', '', hdr_c0, flags=re.I).strip()
            if crit_cand:
                crit_name = crit_cand

        if not crit_name:
            continue
            
        is_total_row = 'total' in crit_name.lower()
        if is_total_row:
            pos_dec_val = clean_txt(row[-2]) if len(row) >= 2 and clean_txt(row[-2]) else str(num_dec)
            coeff_val = clean_txt(row[-1]) if len(row) >= 1 and clean_txt(row[-1]) else "1.000"
            h.append('      <tr class="bg-gray-100 font-bold border-t-2 border-black">')
            h.append(f'        <td colspan="{num_dec + 1}" class="border border-black p-2 text-right uppercase tracking-wider text-black sticky left-0 bg-gray-100 z-10">Total Positive Decisions</td>')
            h.append(f'        <td class="border border-black p-2 text-center text-black font-bold">{pos_dec_val}</td>')
            h.append(f'        <td class="border border-black p-2 text-center text-black font-bold">{coeff_val}</td>')
            h.append('      </tr>')
        else:
            bg_cls = 'bg-gray-50/70' if r_idx % 2 == 1 else 'bg-white'
            pos_dec_val = clean_txt(row[-2]) if len(row) >= 2 else ""
            coeff_val = clean_txt(row[-1]) if len(row) >= 1 else ""
            
            # Fallback if pos_dec_val or coeff_val is empty (like Page 120 Ease of Assembly)
            if not pos_dec_val:
                calc_pos = sum(1 for c_idx, _ in dec_cols if clean_txt(row[c_idx]) == '1')
                pos_dec_val = str(calc_pos)
            if not coeff_val:
                calc_pos = int(pos_dec_val) if pos_dec_val.isdigit() else sum(1 for c_idx, _ in dec_cols if clean_txt(row[c_idx]) == '1')
                coeff_val = f"{calc_pos / num_dec:.3f}".rstrip('0').rstrip('.')
            
            h.append(f'      <tr class="{bg_cls} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
            h.append(f'        <td class="border border-black p-2 font-bold text-gray-900 sticky left-0 {bg_cls} z-10 shadow-2xs">{crit_name}</td>')
            for c_idx, _ in dec_cols:
                cell_v = clean_txt(row[c_idx]) if c_idx < len(row) else ""
                val_badge = ""
                if cell_v == '1':
                    val_badge = '<span class="font-bold text-black">1</span>'
                elif cell_v == '0':
                    val_badge = '<span class="text-gray-400">0</span>'
                else:
                    val_badge = '<span class="text-gray-200">&minus;</span>'
                pad = "p-0.5 text-[10px]" if num_dec > 20 else "p-1 text-[11px]"
                h.append(f'        <td class="border border-black {pad} text-center font-mono">{val_badge}</td>')
            h.append(f'        <td class="border border-black p-2 text-center font-bold text-black bg-gray-50/50">{pos_dec_val}</td>')
            h.append(f'        <td class="border border-black p-2 text-right font-medium text-gray-800 pr-3">{coeff_val}</td>')
            h.append('      </tr>')

    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_performance_index_table(tab_data, caption=""):
    """
    Renders a Performance Index Table with clean 2-tier header:
    - Row 1: Selection Criteria (rowspan=2), Weighting Factor (α) (rowspan=2), Candidate 1 (colspan=2), Candidate 2 (colspan=2)...
    - Row 2: Scaled Property (β), Weighted Score (αβ) under each candidate
    - Data rows
    - Footer row: Material Performance Index (γ)
    """
    if not tab_data or len(tab_data) < 3:
        return ""

    r0 = tab_data[0]
    r1 = tab_data[1]
    data_rows = tab_data[2:]

    # Detect candidate materials from row 0
    candidates = []
    for c_idx in range(2, len(r0), 2):
        name = clean_txt(r0[c_idx])
        if name:
            candidates.append((c_idx, name))

    if not candidates:
        return None

    h = []
    h.append('<div class="overflow-x-auto relative max-w-full my-8 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white min-w-[750px]">')
    
    # 2-tier Header
    h.append('    <thead>')
    h.append('      <tr class="bg-gray-100 text-black border-b border-black">')
    h.append('        <th rowspan="2" class="border border-black p-2.5 font-bold uppercase text-left w-48 align-middle">Selection Criteria</th>')
    h.append(r'        <th rowspan="2" class="border border-black p-2 font-bold uppercase text-center w-24 align-middle">Weighting Factor ($\alpha$)</th>')
    for _, c_name in candidates:
        h.append(f'        <th colspan="2" class="border border-black p-2 font-bold uppercase text-center bg-gray-200/80">{c_name}</th>')
    h.append('      </tr>')

    # Second row
    h.append('      <tr class="bg-gray-50 text-black border-b border-black">')
    for _ in candidates:
        h.append(r'        <th class="border border-black p-1.5 text-right font-semibold text-[11px] text-gray-700">Scaled ($\beta$)</th>')
        h.append(r'        <th class="border border-black p-1.5 text-right font-bold text-[11px] text-black bg-gray-100/70">Score ($\alpha\beta$)</th>')
    h.append('      </tr>')
    h.append('    </thead>')

    # Body
    h.append('    <tbody>')
    for r_idx, row in enumerate(data_rows):
        crit_name = clean_txt(row[0])
        if not crit_name:
            continue

        is_summary_row = any(w in crit_name.lower() for w in ['performance index', 'material performance', 'index, γ', 'γ'])
        if is_summary_row:
            h.append('      <tr class="bg-gray-100 font-bold border-t-2 border-black">')
            h.append(r'        <td colspan="2" class="border border-black p-2.5 text-right uppercase tracking-wider text-black">Performance Index ($\gamma = \sum \alpha\beta$)</td>')
            for c_idx, _ in candidates:
                score_val = clean_txt(row[c_idx + 1]) if c_idx + 1 < len(row) and clean_txt(row[c_idx + 1]) else clean_txt(row[c_idx])
                h.append(f'        <td colspan="2" class="border border-black p-2.5 text-center text-sm font-bold bg-yellow-100/80 text-black">{score_val}</td>')
            h.append('      </tr>')
        else:
            bg_cls = 'bg-gray-50/70' if r_idx % 2 == 1 else 'bg-white'
            alpha_val = clean_txt(row[1]) if len(row) > 1 else ""
            h.append(f'      <tr class="{bg_cls} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
            h.append(f'        <td class="border border-black p-2 font-bold text-gray-900">{crit_name}</td>')
            h.append(f'        <td class="border border-black p-2 text-center font-medium text-gray-800 bg-gray-50/40">{alpha_val}</td>')
            for c_idx, _ in candidates:
                beta_val = clean_txt(row[c_idx]) if c_idx < len(row) else ""
                alphabeta_val = clean_txt(row[c_idx + 1]) if c_idx + 1 < len(row) else ""
                h.append(f'        <td class="border border-black p-2 text-right text-gray-700">{beta_val}</td>')
                h.append(f'        <td class="border border-black p-2 text-right font-semibold text-black bg-gray-50/30">{alphabeta_val}</td>')
            h.append('      </tr>')

    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_standard_property_table(tab_data, caption=""):
    """Renders a standard material or process property comparison table with clean headers."""
    if not tab_data:
        return ""

    h = []
    h.append('<div class="overflow-x-auto relative max-w-full my-6 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white">')
    
    header = tab_data[0]
    h.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
    for c_idx, col in enumerate(header):
        align = "text-left" if c_idx == 0 else "text-center"
        h.append(f'      <th class="border border-black p-2.5 font-bold uppercase {align}">{clean_txt(col)}</th>')
    h.append('    </tr></thead>')

    h.append('    <tbody>')
    for r_idx, row in enumerate(tab_data[1:]):
        bg_cls = 'bg-gray-50/70' if r_idx % 2 == 1 else 'bg-white'
        h.append(f'      <tr class="{bg_cls} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
        for c_idx, cell in enumerate(row):
            align = "text-left font-semibold text-gray-900" if c_idx == 0 else "text-center text-gray-800"
            h.append(f'        <td class="border border-black p-2 {align}">{clean_txt(cell)}</td>')
        h.append('      </tr>')
    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    return '\n'.join(h)

def get_ch6_7_table_html(pdf_page, t_idx, tab_data, doc_ref):
    """
    Intelligently handles all tables across Chapter 6 (Pages 96-100) and Chapter 7 (Pages 101-125):
    - Table 6.1 on Page 97
    - Table 6.2 on Page 98 (merged with Page 99 Table 1)
    - Skip Page 99 Table 1
    - Table 6.3 on Page 99 (merged with Page 100 Table 1)
    - Skip Page 100 Table 1
    - Table 7.2 on Page 103 (merged with Page 104 Table 1)
    - Skip Page 104 Table 1
    - Table 7.12 on Page 110 (merged with Page 111 Table 1)
    - Skip Page 111 Table 1
    - Digital Logic Tables (two-tier headers with KaTeX math)
    - Performance Index Tables (two-tier headers with candidate colspans and KaTeX math)
    - Standard property comparison tables
    """
    # 1. Chapter 6 Merged Tables
    if pdf_page == 97 and t_idx == 0:
        return render_ch6_material_table(tab_data)

    if pdf_page == 98 and t_idx == 0:
        return render_ch6_manufacturing_table()

    if pdf_page == 99 and t_idx == 0:
        # This is the orphan top half of Table 6.2 -> SKIP (already rendered on Page 98)
        return ""

    if pdf_page == 99 and t_idx == 1:
        # Table 6.3 merged with Page 100 Table 1
        return render_ch6_joining_table()

    if pdf_page == 100 and t_idx == 0:
        # This is the orphan bottom half of Table 6.3 -> SKIP (already rendered on Page 99)
        return ""

    # 2. Chapter 7 Merged Tables
    if pdf_page == 103 and t_idx == 1:
        # Table 7.2: Merge Page 103 Table 2 with Page 104 Table 1
        p104_tabs = doc_ref[103].find_tables().tables
        p104_data = p104_tabs[0].extract() if p104_tabs else []
        merged_7_2 = tab_data + p104_data
        return render_standard_property_table(merged_7_2)

    if pdf_page == 104 and t_idx == 0:
        # This is the bottom half of Table 7.2 -> SKIP (already rendered on Page 103)
        return ""

    if pdf_page == 110 and t_idx == 2:
        # Table 7.12: Merge Page 110 Table 3 with Page 111 Table 1
        p111_tabs = doc_ref[110].find_tables().tables
        p111_data = p111_tabs[0].extract() if p111_tabs else []
        merged_7_12 = [tab_data[0], tab_data[1]] + tab_data[2:] + p111_data
        return render_performance_index_table(merged_7_12)

    if pdf_page == 111 and t_idx == 0:
        # This is the bottom half of Table 7.12 -> SKIP (already rendered on Page 110)
        return ""

    # 3. Dynamic Identification for all other tables in Chapter 6 & 7
    if not tab_data or len(tab_data) < 2:
        return ""

    r0 = tab_data[0]
    r1 = tab_data[1] if len(tab_data) > 1 else []

    is_dl = any('positive decision' in str(c).lower() for c in r0)
    is_pi = any('scaled' in str(c).lower() or 'weighted' in str(c).lower() for c in r0 + r1)

    if is_dl:
        res = render_digital_logic_table(tab_data)
        if res:
            return res

    if is_pi:
        res = render_performance_index_table(tab_data)
        if res:
            return res

    return render_standard_property_table(tab_data)
