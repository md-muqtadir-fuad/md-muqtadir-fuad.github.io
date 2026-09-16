# -*- coding: utf-8 -*-
import html

def get_appendix_a_html(pdf_page):
    page_html = []
    
    questions = [
        # Page 143 (Q1-Q4)
        {
            "page": 143,
            "items": [
                {"num": 1, "text": "How often do you clean your shoes?", "opts": ["Daily", "Weekly", "Monthly", "Quarterly"]},
                {"num": 2, "text": "How do you currently clean your shoes?", "opts": ["Hand wash", "Wet wipes", "Professional cleaning"]},
                {"num": 3, "text": "How much do you spend on a single shoe cleaning?", "opts": ["Under 50/=", "50-100 /=", "100-150/=", "150-200/=", "Over 200/="]},
                {"num": 4, "text": "What challenges do you face when cleaning your shoes?", "opts": ["Time consuming", "Ineffective", "Unavailability"]}
            ]
        },
        # Page 144 (Q5-Q9)
        {
            "page": 144,
            "items": [
                {"num": 5, "text": "How satisfied are you with your current shoe cleaning method?", "opts": ["Very satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very dissatisfied"]},
                {"num": 6, "text": "Would you be interested in a machine that cleans your shoes automatically?", "opts": ["Yes", "No", "Maybe"]},
                {"num": 7, "text": "What features would be most important to you in a shoe cleaning machine?", "opts": ["Speed of cleaning", "Effectiveness", "Ease of use", "Eco-friendliness"]},
                {"num": 8, "text": "Would you prefer a machine that is portable or one that stays in one place?", "opts": ["Portable", "Stationary", "No preference"]},
                {"num": 9, "text": "What factors influence your decision to purchase a new cleaning device?", "opts": ["Reviews", "Brand reputation", "Recommendations"]}
            ]
        },
        # Page 145 (Q10-Q15)
        {
            "page": 145,
            "items": [
                {"num": 10, "text": "Have you seen similar products on the market?", "opts": ["Yes", "No"]},
                {"num": 11, "text": "What additional features would make a shoe cleaning machine more appealing to you?", "opts": ["Automation", "Disinfectant", "Shiner", "Easy to operate"]},
                {"num": 12, "text": "In which environment would the shoe cleaning machine be most used in your workplace?", "opts": ["Office lobby", "Staff changing rooms", "Warehouse/Factory", "Hospital entryway"]},
                {"num": 13, "text": "How often would you expect to perform maintenance on such a machine?", "opts": ["Weekly", "Monthly", "Quarterly", "Yearly"]},
                {"num": 14, "text": "How concerned are you about cross-contamination and hygiene in common areas like lobbies or entry points where the shoe cleaning machine might be placed?", "opts": ["Very concerned", "Somewhat concerned", "Not concerned"]},
                {"num": 15, "text": "How important is it for the machine to have environmentally friendly features, such as energy efficiency or low water consumption?", "opts": ["Extremely important", "Important", "Neutral", "Not important"]}
            ]
        },
        # Page 146 (Q16-Q17)
        {
            "page": 146,
            "items": [
                {"num": 16, "text": "Would noise levels be a concern if the machine was placed in an area with frequent foot traffic?", "opts": ["Yes, it should be quiet", "Noise is acceptable if it's efficient", "No preference"]},
                {"num": 17, "text": "How likely are you to recommend such a machine to other organizations if it meets your expectations?", "opts": ["Very likely", "Likely", "Neutral", "Unlikely"]}
            ]
        }
    ]

    for group in questions:
        if group["page"] == pdf_page:
            if pdf_page == 143:
                page_html.append('<h2 class="text-2xl md:text-3xl font-bold font-mono tracking-tight mt-12 mb-6 pb-2 border-b-2 border-black" id="appendix">APPENDIX</h2>')
                page_html.append('<h3 class="text-xl font-bold font-mono tracking-tight mb-3 text-black">Appendix A: Questionnaire for Survey</h3>')
                page_html.append('<p class="text-sm font-serif italic text-gray-600 mb-6">Field survey instrument administered to 34 participants across academic institutions, corporate offices, and commercial establishments in Dhaka.</p>')
                page_html.append('<div class="border border-gray-300 p-5 bg-gray-50/60 mb-6 rounded-xs font-mono text-xs">')
                page_html.append('  <div class="font-bold text-xs uppercase tracking-wider text-black mb-3 flex items-center gap-2"><span class="w-2 h-2 bg-black inline-block"></span>Participant Demographic Information</div>')
                page_html.append('  <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">')
                page_html.append('    <div><span class="text-gray-500 uppercase">Name:</span> <span class="border-b border-gray-400 block pb-1 text-gray-400 mt-1">___________________________</span></div>')
                page_html.append('    <div><span class="text-gray-500 uppercase">Age:</span> <span class="border-b border-gray-400 block pb-1 text-gray-400 mt-1">_______</span></div>')
                page_html.append('    <div><span class="text-gray-500 uppercase">Address / Organization:</span> <span class="border-b border-gray-400 block pb-1 text-gray-400 mt-1">___________________________</span></div>')
                page_html.append('  </div>')
                page_html.append('</div>')

            for q in group["items"]:
                page_html.append('<div class="question-item mb-4 p-4 border border-gray-200 bg-white hover:border-black transition-colors rounded-xs">')
                page_html.append(f'  <div class="font-mono font-bold text-sm text-black mb-3 flex items-start gap-2.5">')
                page_html.append(f'    <span class="px-2 py-0.5 bg-black text-white text-xs shrink-0 font-mono">Q{q["num"]:02d}</span>')
                page_html.append(f'    <span>{html.escape(q["text"])}</span>')
                page_html.append('  </div>')
                page_html.append('  <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-2.5 pl-2 sm:pl-9">')
                for opt in q["opts"]:
                    page_html.append(f'    <div class="flex items-center gap-2 font-mono text-xs text-gray-700 bg-gray-50/70 border border-gray-200 px-2.5 py-1.5 rounded-xs">')
                    page_html.append('      <span class="w-3 h-3 rounded-full border border-gray-400 bg-white inline-block shrink-0"></span>')
                    page_html.append(f'      <span>{html.escape(opt)}</span>')
                    page_html.append('    </div>')
                page_html.append('  </div>')
                page_html.append('</div>')

    return '\n'.join(page_html)

def get_appendix_b_html():
    page_html = []
    page_html.append('<div class="my-8" id="page-147">')
    page_html.append('  <h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mb-2 text-black">Appendix B: Result of Tensile Test and Physical Constants of Some Materials</h3>')
    page_html.append('  <p class="text-sm font-serif italic text-gray-600 mb-8">Empirical material characterization standards, mechanical tensile/yield properties, and physical property tables utilized in structural design, component sizing, and finite element stress verification.</p>')

    # Table A-1 Data
    table_a1_data = [
        ("G10060", "1006", "HR", "300 (43)", "170 (24)", "30", "55", "86"),
        ("G10060", "1006", "CD", "330 (48)", "280 (41)", "20", "45", "95"),
        ("G10100", "1010", "HR", "320 (47)", "180 (26)", "28", "50", "95"),
        ("G10100", "1010", "CD", "370 (53)", "300 (44)", "20", "40", "105"),
        ("G10150", "1015", "HR", "340 (50)", "190 (27.5)", "28", "50", "101"),
        ("G10150", "1015", "CD", "390 (56)", "320 (47)", "18", "40", "111"),
        ("G10180", "1018", "HR", "400 (58)", "220 (32)", "25", "50", "116"),
        ("G10180", "1018", "CD", "440 (64)", "370 (54)", "15", "40", "126"),
        ("G10200", "1020", "HR", "380 (55)", "210 (30)", "25", "50", "111"),
        ("G10200", "1020", "CD", "470 (68)", "390 (57)", "15", "40", "131"),
        ("G10300", "1030", "HR", "470 (68)", "260 (37.5)", "20", "42", "137"),
        ("G10300", "1030", "CD", "520 (76)", "440 (64)", "12", "35", "149"),
        ("G10350", "1035", "HR", "500 (72)", "270 (39.5)", "18", "40", "143"),
        ("G10350", "1035", "CD", "550 (80)", "460 (67)", "12", "35", "163"),
        ("G10400", "1040", "HR", "520 (76)", "290 (42)", "18", "40", "149"),
        ("G10400", "1040", "CD", "590 (85)", "490 (71)", "12", "35", "170"),
        ("G10450", "1045", "HR", "570 (82)", "310 (45)", "16", "40", "163"),
        ("G10450", "1045", "CD", "630 (91)", "530 (77)", "12", "35", "179"),
        ("G10500", "1050", "HR", "620 (90)", "340 (49.5)", "15", "35", "179"),
        ("G10500", "1050", "CD", "690 (100)", "580 (84)", "10", "30", "197"),
        ("G10600", "1060", "HR", "680 (98)", "370 (54)", "12", "30", "201"),
        ("G10800", "1080", "HR", "770 (112)", "420 (61.5)", "10", "25", "229"),
        ("G10950", "1095", "HR", "830 (120)", "460 (66)", "10", "25", "248"),
    ]

    # --- Table A-1 HTML ---
    page_html.append('  <div class="my-10 border border-gray-300 p-6 bg-white shadow-2xs rounded-xs">')
    page_html.append('    <div class="font-mono text-xs font-bold text-black uppercase mb-1 flex items-center gap-2"><span class="w-2 h-2 bg-black inline-block"></span><span class="text-gray-400">Table A.1</span>Deterministic ASTM Minimum Tensile and Yield Strength for Some Hot-Rolled (HR) and Cold-Drawn (CD) Steels</div>')
    page_html.append('    <p class="font-serif italic text-xs text-gray-500 mb-3">Estimated minimum mechanical strength values for design safety factor evaluations per ASTM A6/A568 standards.</p>')
    page_html.append('    <div class="p-3 bg-gray-50 border border-gray-200 text-xs font-serif text-gray-700 leading-relaxed mb-4 rounded-xs">')
    page_html.append('      [The strengths listed are estimated ASTM minimum values in the size range 18 to 32 mm (&frac34; to 1&frac14; in). These strengths are suitable for use with the design factor defined in Sec. 1–10, provided the materials conform to ASTM A6 or A568 requirements or are required in the purchase specifications. Remember that a numbering system is not a specification.]')
    page_html.append('    </div>')
    
    page_html.append('    <div class="overflow-x-auto relative max-w-full border border-black">')
    page_html.append('      <table class="w-full border-collapse font-mono text-xs text-left bg-white">')
    page_html.append('        <thead>')
    page_html.append('          <tr class="bg-gray-100 text-black border-b border-black">')
    page_html.append('            <th class="border border-black p-2 font-bold uppercase text-center w-12">1<br><span class="text-[11px] font-semibold text-gray-600">UNS No.</span></th>')
    page_html.append('            <th class="border border-black p-2 font-bold uppercase text-center w-24">2<br><span class="text-[11px] font-semibold text-gray-600">SAE / AISI</span></th>')
    page_html.append('            <th class="border border-black p-2 font-bold uppercase text-center w-16">3<br><span class="text-[11px] font-semibold text-gray-600">Process</span></th>')
    page_html.append('            <th class="border border-black p-2 font-bold uppercase text-right">4<br><span class="text-[11px] font-semibold text-gray-600">Tensile Str, MPa (kpsi)</span></th>')
    page_html.append('            <th class="border border-black p-2 font-bold uppercase text-right">5<br><span class="text-[11px] font-semibold text-gray-600">Yield Str, MPa (kpsi)</span></th>')
    page_html.append('            <th class="border border-black p-2 font-bold uppercase text-right">6<br><span class="text-[11px] font-semibold text-gray-600">Elongation in 2 in, %</span></th>')
    page_html.append('            <th class="border border-black p-2 font-bold uppercase text-right">7<br><span class="text-[11px] font-semibold text-gray-600">Reduction in Area, %</span></th>')
    page_html.append('            <th class="border border-black p-2 font-bold uppercase text-right">8<br><span class="text-[11px] font-semibold text-gray-600">Brinell Hardness</span></th>')
    page_html.append('          </tr>')
    page_html.append('        </thead>')
    page_html.append('        <tbody>')

    i = 0
    row_bg_toggle = 0
    while i < len(table_a1_data):
        curr = table_a1_data[i]
        # Check if next row has same UNS/SAE (pair of HR and CD)
        has_pair = (i + 1 < len(table_a1_data)) and (table_a1_data[i+1][0] == curr[0])
        bg_cls = 'bg-gray-50/70' if row_bg_toggle % 2 == 1 else 'bg-white'
        row_bg_toggle += 1

        if has_pair:
            nxt = table_a1_data[i+1]
            # First row of pair
            page_html.append(f'          <tr class="{bg_cls} border-b border-gray-200 hover:bg-yellow-50/40 transition-colors">')
            page_html.append(f'            <td class="border border-black p-2 text-center font-bold text-gray-900" rowspan="2">{curr[0]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-center font-semibold text-gray-800" rowspan="2">{curr[1]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-center font-medium text-gray-700 bg-gray-100/50">{curr[2]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800 font-medium">{curr[3]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800 font-medium">{curr[4]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800">{curr[5]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800">{curr[6]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800 font-medium">{curr[7]}</td>')
            page_html.append('          </tr>')
            # Second row of pair
            page_html.append(f'          <tr class="{bg_cls} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
            page_html.append(f'            <td class="border border-black p-2 text-center font-medium text-gray-700 bg-gray-100/50">{nxt[2]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800 font-medium">{nxt[3]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800 font-medium">{nxt[4]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800">{nxt[5]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800">{nxt[6]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800 font-medium">{nxt[7]}</td>')
            page_html.append('          </tr>')
            i += 2
        else:
            page_html.append(f'          <tr class="{bg_cls} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
            page_html.append(f'            <td class="border border-black p-2 text-center font-bold text-gray-900">{curr[0]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-center font-semibold text-gray-800">{curr[1]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-center font-medium text-gray-700 bg-gray-100/50">{curr[2]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800 font-medium">{curr[3]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800 font-medium">{curr[4]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800">{curr[5]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800">{curr[6]}</td>')
            page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800 font-medium">{curr[7]}</td>')
            page_html.append('          </tr>')
            i += 1

    page_html.append('        </tbody>')
    page_html.append('      </table>')
    page_html.append('    </div>')
    page_html.append('    <p class="font-serif text-xs text-gray-600 mt-3 pt-2 border-t border-gray-200"><span class="italic font-semibold">Source.</span> Data from 1986 SAE Handbook, p. 2.15. Adapted for mechanical design calculations.</p>')
    page_html.append('  </div>')

    # Table A-2 Data
    table_a2_data = [
        ("Aluminum (all alloys)", "10.4", "71.7", "3.9", "26.9", "0.333", "0.098", "169", "26.6"),
        ("Beryllium copper", "18.0", "124.0", "7.0", "48.3", "0.285", "0.297", "513", "80.6"),
        ("Brass", "15.4", "106.0", "5.82", "40.1", "0.324", "0.309", "534", "83.8"),
        ("Carbon steel", "30.0", "207.0", "11.5", "79.3", "0.292", "0.282", "487", "76.5"),
        ("Cast iron (gray)", "14.5", "100.0", "6.0", "41.4", "0.211", "0.260", "450", "70.6"),
        ("Copper", "17.2", "119.0", "6.49", "44.7", "0.326", "0.322", "556", "87.3"),
        ("Douglas fir", "1.6", "11.0", "0.6", "4.1", "0.33", "0.016", "28", "4.3"),
        ("Glass", "6.7", "46.2", "2.7", "18.6", "0.245", "0.094", "162", "25.4"),
        ("Inconel", "31.0", "214.0", "11.0", "75.8", "0.290", "0.307", "530", "83.3"),
        ("Lead", "5.3", "36.5", "1.9", "13.1", "0.425", "0.411", "710", "111.5"),
        ("Magnesium", "6.5", "44.8", "2.4", "16.5", "0.350", "0.065", "112", "17.6"),
        ("Molybdenum", "48.0", "331.0", "17.0", "117.0", "0.307", "0.368", "636", "100.0"),
        ("Monel metal", "26.0", "179.0", "9.5", "65.5", "0.320", "0.319", "551", "86.6"),
        ("Nickel silver", "18.5", "127.0", "7.0", "48.3", "0.322", "0.316", "546", "85.8"),
        ("Nickel steel", "30.0", "207.0", "11.5", "79.3", "0.291", "0.280", "484", "76.0"),
        ("Phosphor bronze", "16.1", "111.0", "6.0", "41.4", "0.349", "0.295", "510", "80.1"),
        ("Stainless steel (18-8)", "27.6", "190.0", "10.6", "73.1", "0.305", "0.280", "484", "76.0"),
        ("Titanium alloys", "16.5", "114.0", "6.2", "42.4", "0.340", "0.160", "276", "43.4"),
    ]

    # --- Table A-2 HTML ---
    page_html.append('  <div class="my-10 border border-gray-300 p-6 bg-white shadow-2xs rounded-xs">')
    page_html.append('    <div class="font-mono text-xs font-bold text-black uppercase mb-1 flex items-center gap-2"><span class="w-2 h-2 bg-black inline-block"></span><span class="text-gray-400">Table A.2</span>Physical Constants of Materials</div>')
    page_html.append('    <p class="font-serif italic text-xs text-gray-500 mb-4">Fundamental physical, thermodynamic, and elastic constants including modulus of elasticity, modulus of rigidity, Poisson\'s ratio, and unit weight.</p>')

    page_html.append('    <div class="overflow-x-auto relative max-w-full border border-black">')
    page_html.append('      <table class="w-full border-collapse font-mono text-xs text-left bg-white">')
    page_html.append('        <thead>')
    page_html.append('          <tr class="bg-gray-100 text-black border-b border-black">')
    page_html.append('            <th class="border border-black p-2 font-bold uppercase text-left w-48" rowspan="2">Material</th>')
    page_html.append('            <th class="border border-black p-2 font-bold uppercase text-center" colspan="2">Modulus of Elasticity <em>E</em></th>')
    page_html.append('            <th class="border border-black p-2 font-bold uppercase text-center" colspan="2">Modulus of Rigidity <em>G</em></th>')
    page_html.append('            <th class="border border-black p-2 font-bold uppercase text-center" rowspan="2">Poisson\'s Ratio <em>&nu;</em></th>')
    page_html.append('            <th class="border border-black p-2 font-bold uppercase text-center" colspan="3">Unit Weight <em>w</em></th>')
    page_html.append('          </tr>')
    page_html.append('          <tr class="bg-gray-50 text-black border-b border-black">')
    page_html.append('            <th class="border border-black p-1.5 font-bold uppercase text-right text-[11px] text-gray-600">Mpsi</th>')
    page_html.append('            <th class="border border-black p-1.5 font-bold uppercase text-right text-[11px] text-gray-600">GPa</th>')
    page_html.append('            <th class="border border-black p-1.5 font-bold uppercase text-right text-[11px] text-gray-600">Mpsi</th>')
    page_html.append('            <th class="border border-black p-1.5 font-bold uppercase text-right text-[11px] text-gray-600">GPa</th>')
    page_html.append('            <th class="border border-black p-1.5 font-bold uppercase text-right text-[11px] text-gray-600">lbf/in&sup3;</th>')
    page_html.append('            <th class="border border-black p-1.5 font-bold uppercase text-right text-[11px] text-gray-600">lbf/ft&sup3;</th>')
    page_html.append('            <th class="border border-black p-1.5 font-bold uppercase text-right text-[11px] text-gray-600">kN/m&sup3;</th>')
    page_html.append('          </tr>')
    page_html.append('        </thead>')
    page_html.append('        <tbody>')

    for r_idx, row in enumerate(table_a2_data):
        bg_cls = 'bg-gray-50/70' if r_idx % 2 == 1 else 'bg-white'
        page_html.append(f'          <tr class="{bg_cls} border-b border-gray-200 hover:bg-yellow-50/40 transition-colors">')
        page_html.append(f'            <td class="border border-black p-2 text-left font-bold text-gray-900">{row[0]}</td>')
        page_html.append(f'            <td class="border border-black p-2 text-right font-medium text-gray-800">{row[1]}</td>')
        page_html.append(f'            <td class="border border-black p-2 text-right font-medium text-gray-800">{row[2]}</td>')
        page_html.append(f'            <td class="border border-black p-2 text-right font-medium text-gray-800">{row[3]}</td>')
        page_html.append(f'            <td class="border border-black p-2 text-right font-medium text-gray-800">{row[4]}</td>')
        page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800">{row[5]}</td>')
        page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800">{row[6]}</td>')
        page_html.append(f'            <td class="border border-black p-2 text-right text-gray-800">{row[7]}</td>')
        page_html.append(f'            <td class="border border-black p-2 text-right font-medium text-gray-800">{row[8]}</td>')
        page_html.append('          </tr>')

    page_html.append('        </tbody>')
    page_html.append('      </table>')
    page_html.append('    </div>')
    page_html.append('    <p class="font-serif text-xs text-gray-600 mt-3 pt-2 border-t border-gray-200"><span class="italic font-semibold">Note.</span> Adapted from engineering materials property databases and Ashby (2005). Conversion factor: 1 Mpsi = 6.89476 GPa.</p>')
    page_html.append('  </div>')

    page_html.append('</div>')
    return '\n'.join(page_html)

def render_apa_item(author_year, title, source, url_text=None, url=None, note=None):
    h = []
    h.append('<div class="apa-reference pl-8 -indent-8 font-serif text-sm text-gray-800 leading-relaxed mb-4 hover:text-black transition-colors">')
    h.append(f'  <span class="font-medium">{html.escape(author_year)}</span> ')
    h.append(f'  <span class="italic">{html.escape(title)}.</span> ')
    h.append(f'  <span>{html.escape(source)}</span>')
    if note:
        h.append(f'  <span class="text-gray-600"> ({html.escape(note)})</span>')
    target_url = url or url_text
    if target_url:
        is_doi = "doi.org" in target_url.lower() or "doi:" in target_url.lower()
        badge_text = "[DOI]" if is_doi else "[LINK]"
        h.append(f' <a href="{html.escape(target_url)}" target="_blank" rel="noopener noreferrer" class="text-blue-700 hover:text-black font-mono text-xs font-bold underline ml-1.5 whitespace-nowrap">{badge_text}&nbsp;↗</a>')
    h.append('</div>')
    return ''.join(h)

def get_references_html(pdf_page):
    page_html = []
    
    if pdf_page == 148:
        page_html.append('<h2 class="text-2xl md:text-3xl font-bold font-mono tracking-tight mt-14 mb-4 pb-2 border-b-2 border-black" id="reference">REFERENCES</h2>')
        page_html.append('<p class="text-sm font-serif italic text-gray-600 mb-8">All references are formatted according to the American Psychological Association (APA) 7th Edition guidelines, organized systematically across research domains with verified digital identifiers and archival links.</p>')

        page_html.append('<div class="reference-category mb-8">')
        page_html.append('  <h3 class="font-mono text-xs uppercase font-bold tracking-wider text-black mb-4 pb-1.5 border-b border-gray-300 flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>1. Primary Survey & Research Data</h3>')
        page_html.append(render_apa_item(
            "Fuad, M. M., et al. (2024).",
            "Customer needs, usage behavior, and product requirement survey for semi-automated shoe cleaning machine",
            "Online survey instrument and response dataset hosted on Google Forms.",
            url_text="https://docs.google.com/forms/d/1qbd03J8L5Fd174adMUQSutuz2Fc0FPTlVtnMwFFm1lw/edit",
            url="https://docs.google.com/forms/d/1qbd03J8L5Fd174adMUQSutuz2Fc0FPTlVtnMwFFm1lw/edit",
            note="Survey Drive Link"
        ))
        page_html.append('</div>')

        page_html.append('<div class="reference-category mb-8">')
        page_html.append('  <h3 class="font-mono text-xs uppercase font-bold tracking-wider text-black mb-4 pb-1.5 border-b border-gray-300 flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>2. Institutional Demographics & Demand Forecasting (Dhaka Region)</h3>')
        
        page_html.append(render_apa_item(
            "University Grants Commission of Bangladesh. (2024).",
            "List of recognized private universities in Bangladesh",
            "UGC Institutional Directory.",
            url_text="http://www.ugc-universities.gov.bd/private-universities",
            url="http://www.ugc-universities.gov.bd/private-universities",
            note="Total institutions: 115"
        ))
        
        page_html.append(render_apa_item(
            "Bangladesh Bank. (2024).",
            "Commercial banking directory and branch network statistics: Dhaka division",
            "Central Bank of Bangladesh.",
            url_text="https://www.bb.org.bd/en/index.php",
            url="https://www.bb.org.bd/en/index.php",
            note="Total branches in Dhaka: 1,200 private bank branches"
        ))

        page_html.append(render_apa_item(
            "Ministry of Commerce & Trade Directories. (2024).",
            "Directory of multinational corporations and corporate offices operating in Dhaka",
            "Scribd Commercial Publications.",
            url_text="https://www.scribd.com/document/518600317/How-Many-Multinational-Companies-Doing-Busi",
            url="https://www.scribd.com/document/518600317/How-Many-Multinational-Companies-Doing-Busi",
            note="Total corporate enterprises: Approximately 921 companies"
        ))

        page_html.append(render_apa_item(
            "Bangladesh Bureau of Educational Information and Statistics. (2021).",
            "Bangladesh education statistics 2021",
            "BANBEIS, Ministry of Education, Government of the People's Republic of Bangladesh.",
            url_text="https://banbeis.portal.gov.bd/sites/default/files/files/banbeis.portal.gov.bd/npfblock/Bangladesh%20Education%20Statistics%202021_compressed-1-235.pdf",
            url="https://banbeis.portal.gov.bd/sites/default/files/files/banbeis.portal.gov.bd/npfblock/Bangladesh%20Education%20Statistics%202021_compressed-1-235.pdf",
            note="Total schools and colleges in Dhaka: 324"
        ))

        page_html.append(render_apa_item(
            "Kayak Lodging Database. (2024).",
            "Hotel registry and commercial accommodations directory in Dhaka metropolitan area",
            "Kayak Commercial Travel Index.",
            url_text="https://www.kayak.com/hotels/Dhaka,Bangladesh-p12960/",
            url="https://www.kayak.com/hotels/Dhaka,Bangladesh-p12960/2024-12-02/2024-12-03/2adults;map?ucs=1grdcmh&sort=rank_a",
            note="Total verified hotels: 245"
        ))

        page_html.append(render_apa_item(
            "Directorate General of Health Services. (2024, June 9).",
            "List of primary, secondary & tertiary level hospitals and clinics in Dhaka metropolitan area",
            "Hospitals & Clinics Section Unit and HSM, Health Services Division, Ministry of Health and Family Welfare.",
            url_text="http://hospitaldghs.gov.bd/list-of-2ndary-tertiary-level-hospital/",
            url="http://hospitaldghs.gov.bd/list-of-2ndary-tertiary-level-hospital/",
            note="Total registered facilities: 15 + 3 + 43 + 48 + 6 + 5 + 16 = 136 institutions"
        ))
        page_html.append('</div>')

        page_html.append('<div class="reference-category mb-8">')
        page_html.append('  <h3 class="font-mono text-xs uppercase font-bold tracking-wider text-black mb-4 pb-1.5 border-b border-gray-300 flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>3. Design Analysis & Finite Element Modeling</h3>')
        page_html.append(render_apa_item(
            "Syaifudin, A., et al. (2013).",
            "S-N curve estimation in air and corrosive environment using finite element method",
            "Prosiding Badan Kerjasama Teknik Mesin (BKSTM), Indonesia.",
            url_text="https://prosiding.bkstm.org/prosiding/2013/MAT200.pdf",
            url="https://prosiding.bkstm.org/prosiding/2013/MAT200.pdf"
        ))
        page_html.append('</div>')

    elif pdf_page == 149:
        page_html.append('<div class="reference-category mb-8">')
        page_html.append('  <h3 class="font-mono text-xs uppercase font-bold tracking-wider text-black mb-4 pb-1.5 border-b border-gray-300 flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>4. Qualitative Analysis & Joining Methodologies</h3>')
        
        page_html.append(render_apa_item(
            "Kah, P., & Martikainen, J. (2022).",
            "Joining processes and modern fabrication techniques in mechanical assemblies",
            "Journal of Advanced Joining Processes, 6, Article 100113.",
            url_text="https://doi.org/10.1016/j.jajp.2022.100113",
            url="https://doi.org/10.1016/j.jajp.2022.100113"
        ))

        page_html.append(render_apa_item(
            "Lancaster, J. F. (1999).",
            "Metallurgy of welding (6th ed.)",
            "Woodhead Publishing / Butterworth-Heinemann.",
            url_text="https://doi.org/10.1016/b978-075067509-3/50036-1",
            url="https://doi.org/10.1016/b978-075067509-3/50036-1"
        ))

        page_html.append(render_apa_item(
            "Barnes, T. A., & Pashby, I. R. (2010).",
            "Joining for lightweight vehicles and consumer product structures",
            "In Materials, Design and Manufacturing for Lightweight Vehicles (pp. 275–311). Woodhead Publishing.",
            url_text="https://doi.org/10.1533/9781845697822.2.275",
            url="https://doi.org/10.1533/9781845697822.2.275"
        ))

        page_html.append(render_apa_item(
            "Tollenaere, M. (1998).",
            "Qualitative constraints in integrated design",
            "In Integrated Design and Manufacturing in Mechanical Engineering (pp. 41–50). Springer Netherlands.",
            url_text="https://doi.org/10.1007/978-94-015-9966-5_5",
            url="https://doi.org/10.1007/978-94-015-9966-5_5"
        ))
        page_html.append('</div>')

        page_html.append('<div class="reference-category mb-8">')
        page_html.append('  <h3 class="font-mono text-xs uppercase font-bold tracking-wider text-black mb-4 pb-1.5 border-b border-gray-300 flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>5. Quantitative Materials Science, Standards & Component Evaluation</h3>')

        page_html.append(render_apa_item(
            "Callister, W. D., & Rethwisch, D. G. (2007).",
            "Materials science and engineering: An introduction (7th ed.)",
            "John Wiley & Sons."
        ))

        page_html.append(render_apa_item(
            "Radaj, D. (2017).",
            "Stresses, shrinkage, and distortion in weldments and structural joints",
            "In Welding Residual Stresses and Distortion (pp. 243–289). Elsevier.",
            url_text="https://doi.org/10.1016/b978-0-12-804176-5.00017-7",
            url="https://doi.org/10.1016/b978-0-12-804176-5.00017-7"
        ))

        page_html.append(render_apa_item(
            "Parmley, R. O. (2000).",
            "Joints, connections, and structural fasteners",
            "In Standard Handbook of Fastening and Joining (3rd ed.). McGraw-Hill.",
            url_text="https://doi.org/10.1016/b978-034071920-6/50008-x",
            url="https://doi.org/10.1016/b978-034071920-6/50008-x"
        ))

        page_html.append(render_apa_item(
            "Likert, R. (1932).",
            "A technique for the measurement of attitudes",
            "Archives of Psychology, 22(140), 1–55.",
            url_text="https://psycnet.apa.org/record/1933-01885-001",
            url="https://psycnet.apa.org/record/1933-01885-001"
        ))

        page_html.append(render_apa_item(
            "Mano, M. M., & Ciletti, M. D. (2007).",
            "Digital design and logic systems (4th ed.)",
            "Prentice Hall.",
            url_text="https://archive.org/details/digital-logic-design-4th-edition",
            url="https://archive.org/details/digital-logic-design-4th-edition"
        ))

        page_html.append(render_apa_item(
            "Ashby, M. F. (2005).",
            "Materials selection in mechanical design (3rd ed., Chapter 2, 624 p.)",
            "Butterworth-Heinemann / Elsevier Science and Technology Rights Department, Oxford."
        ))

        page_html.append(render_apa_item(
            "MatWeb LLC. (2024).",
            "AISI 1018 mild/low carbon steel, cold drawn mechanical property data sheet (Spec No. M862AN)",
            "MatWeb Material Property Data.",
            url_text="https://asm.matweb.com/search/SpecificMaterial.asp?bassnum=M862AN",
            url="https://asm.matweb.com/search/SpecificMaterial.asp?bassnum=M862AN"
        ))
        page_html.append('</div>')

    elif pdf_page == 150:
        page_html.append('<div class="reference-category mb-8">')
        page_html.append('  <h3 class="font-mono text-xs uppercase font-bold tracking-wider text-black mb-4 pb-1.5 border-b border-gray-300 flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>6. Workshop Machinery, Equipment & Tooling Depreciation</h3>')

        page_html.append(render_apa_item(
            "ClickBD Industrial Machinery. (2024).",
            "Conventional center lathe machine market quotation and capital procurement schedule (Dhaka division)",
            "ClickBD Machinery Marketplace.",
            url_text="https://www.clickbd.com/bangladesh/348275-2-pice-lathe-machine-for-sale",
            url="https://www.clickbd.com/bangladesh/348275-2-pice-lathe-machine-for-sale-call-01918-466544.html"
        ))

        page_html.append(render_apa_item(
            "Weiss Machinery Co. (2023).",
            "What is the lifespan of a lathe machine? Practical lifecycle and maintenance guide",
            "Weiss Tools Technical Journal.",
            url_text="https://cn.weiss-tools.com/blogs/what-is-the-lifespan-of-a-lathe-machine",
            url="https://cn.weiss-tools.com/blogs/what-is-the-lifespan-of-a-lathe-machine"
        ))

        page_html.append(render_apa_item(
            "Machine & Tools BD. (2024).",
            "Industrial 13mm bench drill press machine (Boky brand) technical specifications and retail pricing",
            "Machine and Tools Bangladesh.",
            url_text="https://machineandtoolsbd.com/shop/power-tools/13mm-drill-press-machine-boky-brand/",
            url="https://machineandtoolsbd.com/shop/power-tools/13mm-drill-press-machine-boky-brand/#google_vignette"
        ))

        page_html.append(render_apa_item(
            "Daraz Industrial Tools. (2024).",
            "Inverter portable electric arc welding machine (ARC-300 IGBT) technical specification and price catalog",
            "Daraz Bangladesh.",
            url_text="https://www.daraz.com.bd/products/kogeek-arc-300-welder-inverter-portable-electric-welding-machine",
            url="https://www.daraz.com.bd/products/kogeek-arc-300-welder-inverter-portable-electric-welding-machine-for-welding-working-and-electric-working-eu-plug-i375002208.html"
        ))
        page_html.append('</div>')

        page_html.append('<div class="reference-category mb-8">')
        page_html.append('  <h3 class="font-mono text-xs uppercase font-bold tracking-wider text-black mb-4 pb-1.5 border-b border-gray-300 flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>7. Raw Material Stock & Supply Costs</h3>')

        page_html.append(render_apa_item(
            "Nawabpur Metal Market. (2024a).",
            "Commercial pricing schedule for mild steel (MS) plate sheet (4 ft × 8 ft × 3 mm)",
            "Nawabpur Hardware Supplies.",
            url_text="https://nawabpur.xyz/ms-plate-sheet-4-feet-x-8-feet-x-3mm.html",
            url="https://nawabpur.xyz/ms-plate-sheet-4-feet-x-8-feet-x-3mm.html"
        ))

        page_html.append(render_apa_item(
            "Nawabpur Metal Market. (2024b).",
            "Commercial pricing schedule for stainless steel (SS 304) sheet (4 ft × 8 ft × 1 mm)",
            "Nawabpur Hardware Supplies.",
            url_text="https://nawabpur.xyz/ss-sheet-4-feet-x-8-feet-x-1mm.html",
            url="https://nawabpur.xyz/ss-sheet-4-feet-x-8-feet-x-1mm.html"
        ))

        page_html.append(render_apa_item(
            "Anhui Huixi Brush Co., Ltd. (2024).",
            "Industrial cylindrical spiral rotary cleaning roller brush (Nylon 6/6 bristles) specification and quotation",
            "Made-in-China Industrial Platform.",
            url_text="https://huixibrush.en.made-in-china.com/product/UNyaxLhdAOtW/",
            url="https://huixibrush.en.made-in-china.com/product/UNyaxLhdAOtW/China-Cylindrical-Spiral-Rotary-Cleaning-Industrial-Roller-Brush.html?pv_id=1ied6jbmn07b&faw_id=1ied6jgtd430"
        ))
        page_html.append('</div>')

        page_html.append('<div class="reference-category mb-8">')
        page_html.append('  <h3 class="font-mono text-xs uppercase font-bold tracking-wider text-black mb-4 pb-1.5 border-b border-gray-300 flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>8. Manufacturing Labor & Machinist Wage Baselines</h3>')

        page_html.append(render_apa_item(
            "Glassdoor Economic Research. (2024).",
            "Machine operator and CNC machinist average monthly salary benchmarks in Dhaka, Bangladesh",
            "Glassdoor Salary Analytics.",
            url_text="https://www.glassdoor.com/Salaries/dhaka-bangladesh-machine-operator-salary",
            url="https://www.glassdoor.com/Salaries/dhaka-bangladesh-machine-operator-salary-SRCH_IL.0,16_IM1237_KO17,33.htm"
        ))

        page_html.append(render_apa_item(
            "Bdjobs.com. (2024).",
            "Technical, vocational, and machine operator wage survey across manufacturing enterprises",
            "Bdjobs Employment Research.",
            url_text="https://www.bdjobs.com/",
            url="https://www.bdjobs.com/"
        ))
        page_html.append('</div>')

    elif pdf_page == 151:
        page_html.append('<div class="reference-category mb-8">')
        page_html.append('  <h3 class="font-mono text-xs uppercase font-bold tracking-wider text-black mb-4 pb-1.5 border-b border-gray-300 flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>9. Component Purchase & Mechanical Hardware Costs</h3>')

        page_html.append(render_apa_item(
            "Daraz Bangladesh Industrial. (2024a).",
            "0.5 modulus brass worm gear and shaft set (32mm, 60 teeth worm wheel)",
            "Daraz Mechanical Transmission Components.",
            url_text="https://www.daraz.com.bd/products/05-modulus-brass-metal-gear-shaft",
            url="https://www.daraz.com.bd/products/05-modulus-brass-metal-gear-shaft-32mm-60-teeth-worm-wheel-worm-gear-set-i246215453.html"
        ))

        page_html.append(render_apa_item(
            "Daraz Bangladesh Industrial. (2024b).",
            "Spur gear modules and steel pinion drive catalog",
            "Daraz Industrial Components Hub.",
            url_text="https://www.daraz.com.bd/catalog/?q=spur%20gear",
            url="https://www.daraz.com.bd/catalog/?q=spur%20gear"
        ))

        page_html.append(render_apa_item(
            "Daraz Electronics. (2024c).",
            "Universal AC 220V to adjustable DC 12V–24V (4.5A, 96W) multi-head converter power adapter charger",
            "Daraz Power Supplies.",
            url_text="https://www.daraz.com.bd/products/universal-ac-220v-to-adjustable-dc-power-adapter",
            url="https://www.daraz.com.bd/products/universal-ac-220v-to-adjustable-dc-12v-15v-16v-18v-19v-20v-22v-24v-45a-96w-with-8-separate-dc-converter-head-power-adapter-charger-for-775-motor-pump-laptop-notebook-power-adapter-i225294660.html"
        ))

        page_html.append(render_apa_item(
            "Fixit Hardware Bangladesh. (2024).",
            "Hexagonal bolt and nut fasteners (10mm × 40mm galvanized steel)",
            "Fixit Hardware Tools & Fasteners.",
            url_text="https://fixit.com.bd/product/10mm-x-40mm-2-pcs-packet-nut-bolt/",
            url="https://fixit.com.bd/product/10mm-x-40mm-2-pcs-packet-nut-bolt/?srsltid=AfmBOooO8HyKO0cHY6iwj9q19chgUqEtbP5kwdZ-aNgEpmad9KsPgXQR"
        ))

        page_html.append(render_apa_item(
            "HCH Bearing Industrial. (2024).",
            "Deep groove radial ball bearing 6000-2RS (10mm × 26mm × 8mm, rubber sealed chrome steel)",
            "Daraz BD Bearings & Transmission.",
            url_text="https://www.daraz.com.bd/products/6000rs-hch-10mm-x-26mm-x-8mm",
            url="https://www.daraz.com.bd/products/6000rs-hch-10mm-x-26mm-x-8mm-i337015871-s1642717459.html"
        ))

        page_html.append(render_apa_item(
            "Bemonoc Mechatronics / Ubuy. (2024).",
            "High-torque permanent magnet DC brush motor (12V, 3000 RPM micro-drive)",
            "Ubuy Bangladesh Mechatronics.",
            url_text="https://www.ubuy.com.bd/en/product/DSISOQU-bemonoc-small-dc-motor-12v",
            url="https://www.ubuy.com.bd/en/product/DSISOQU-bemonoc-small-dc-motor-12v-high-speed-3000-rpm-optional-micro-dc-brush-motor?srsltid=AfmBOor1Ls_l63U9FA_Cs8JtJq1hm7Kn2qYSysh47rxhynPI4tl_I2e3"
        ))

        page_html.append(render_apa_item(
            "Universal Shoe Care Products. (2024).",
            "Solid wax shoe polish and colorless leather maintenance oil (wax-like color repair formulation)",
            "Daraz Bangladesh Consumer Care.",
            url_text="https://www.daraz.com.bd/products/tin-box-polish-colorless-black-leather-maintenance-oil",
            url="https://www.daraz.com.bd/products/tin-box-polish-colorless-black-leather-maintenance-oil-solid-universal-shoe-polish-for-women-wax-like-color-repair-i370174056.html"
        ))
        page_html.append('</div>')

    return '\n'.join(page_html)

if __name__ == '__main__':
    print("Testing Appendix A P143:")
    print(get_appendix_a_html(143)[:300])
    print("\nTesting Appendix B P147:")
    print(get_appendix_b_html()[:300])
    print("\nTesting References P148:")
    print(get_references_html(148)[:300])
