# -*- coding: utf-8 -*-
import html

def clean_txt(s):
    if not s:
        return ""
    s = s.replace('\ufb01', 'fi').replace('\ufb02', 'fl').replace('\ufb03', 'ffi').replace('\ufb04', 'ffl')
    s = s.replace('\u2018', "'").replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('\ufffd', '"')
    return ' '.join(s.split())

def render_table_3_1():
    """Renders the complete, unified Table 3.1: Relationship Explanation across all 8 customer requirements."""
    h = []
    h.append('<div class="overflow-x-auto my-6 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white min-w-[760px]">')
    h.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left w-48">Customer Requirement</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left w-48">Engineering Requirement</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-center w-32">Relationship</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left">Explanation</th>')
    h.append('    </tr></thead>')
    h.append('    <tbody>')

    # All 8 customer requirements and their 32 engineering relationship mappings
    requirements = [
        ("Easy to Operate", [
            ("Chamber Assembly", "Strong", "Three different chambers allow us to operate the cleaning process more precisely."),
            ("Vibrating Plate", "Moderate", "This segment ensures the shining process more significantly.")
        ]),
        ("Portability", [
            ("Chamber Assembly", "Strong", "Chamber assembly has made the product more compacted which enhances the product portability."),
            ("Manufacturing Cost", "Moderate", "The presence of separate chamber for separate process increases the manufacturing cost slightly.")
        ]),
        ("Automation", [
            ("Cleaning Design", "Strong", "An improved cleaning design ensures effective automation of the process."),
            ("Roller Brush", "Strong", "Proper functionality of roller brush improves the process automation significantly."),
            ("Vibrating Plate", "Strong", "Improved functionality of vibrating plate improves the process automation significantly."),
            ("Operational Cost", "Weak", "Ensuring self-automated process slightly increases the operational cost."),
            ("Manufacturing Cost", "Strong", "Implementing automated processes tends to raise manufacturing cost.")
        ]),
        ("Eco-Friendly", [
            ("Brush Material", "Strong", "Selecting eco-friendly materials for brushes reduces environmental impact."),
            ("Shiner", "Moderate", "Choosing eco-friendly materials for shiner promotes sustainability while maintaining effective performance.")
        ]),
        ("Operating Speed", [
            ("Strength of Body", "Weak", "A higher operating speed can slightly strain body's strength."),
            ("Manufacturing Cost", "Moderate", "Increasing operating speed may raise manufacturing cost."),
            ("Operational Cost", "Moderate", "Increasing operating speed may raise operational cost."),
            ("Roller Brush", "Moderate", "Operating speed of roller brush influences its cleaning efficiency."),
            ("Cleaning Design", "Moderate", "The design of a cleaning system is optimized for operational speed to maximize efficiency."),
            ("Shiner", "Moderate", "The operating speed of a shiner affects its polishing effectiveness.")
        ]),
        ("Effectiveness", [
            ("Brush Material", "Strong", "The choice of brush material significantly impacts its effectiveness, influencing durability, compatibility."),
            ("Manufacturing Cost", "Moderate", "Enhancing effectiveness typically results in increased manufacturing cost."),
            ("Operational Cost", "Moderate", "Improving effectiveness typically results in increased operational cost."),
            ("Roller Brush", "Strong", "Different types of roller brush enhance effectiveness by catering to specific cleaning needs."),
            ("Cleaning Design", "Strong", "Different cleaning design ensures effectiveness while minimizing time and effort."),
            ("Shiner", "Strong", "A shiner provides effectiveness by utilizing specialized ingredients that create a protective layer, enhance shine and repel dirt.")
        ]),
        ("Low Cost", [
            ("Brush Material", "Moderate", "Using lower cost material reduces overall expenses."),
            ("Manufacturing Cost", "Strong", "Manufacturing cost can be minimized through efficient process and the use of lower cost material."),
            ("Operational Cost", "Moderate", "Minimizing operational cost leads to lower overall cost."),
            ("Cleaning Design", "Strong", "An effective cleaning design minimizes resource consumption which ensures lowering of overall costs."),
            ("Chamber Assembly", "Moderate", "Chamber assembly can lead to lower cost by reducing number of components needed and minimizing assembly time.")
        ]),
        ("Good Stability", [
            ("Strength of Body", "Strong", "The strength of body ensures good stability by providing necessary support and resistance to external forces."),
            ("Vibrating Plate", "Strong", "A vibrating plate contributes to good stability by distributing weight evenly."),
            ("Roller Brush", "Moderate", "A roller brush partially provides good stability by maintaining consistent contact with surfaces."),
            ("Chamber Assembly", "Moderate", "Chamber assembly contributes to good stability by securely integrating components.")
        ])
    ]

    for cr_name, rows in requirements:
        for r_idx, (er_name, rel, exp) in enumerate(rows):
            rel_badge = ""
            if rel == "Strong":
                rel_badge = '<span class="px-2 py-0.5 bg-black text-white text-[10px] uppercase font-mono font-bold tracking-wider inline-block">Strong</span>'
            elif rel == "Moderate":
                rel_badge = '<span class="px-2 py-0.5 bg-gray-200 text-gray-800 text-[10px] uppercase font-mono font-bold tracking-wider inline-block">Moderate</span>'
            else:
                rel_badge = '<span class="px-2 py-0.5 border border-gray-400 text-gray-600 text-[10px] uppercase font-mono font-bold tracking-wider inline-block">Weak</span>'

            h.append('      <tr class="border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
            if r_idx == 0:
                h.append(f'        <td rowspan="{len(rows)}" class="border border-black p-3 font-bold text-gray-900 bg-gray-50/80 align-top">{cr_name}</td>')
            h.append(f'        <td class="border border-black p-2.5 font-semibold text-black">{er_name}</td>')
            h.append(f'        <td class="border border-black p-2.5 text-center">{rel_badge}</td>')
            h.append(f'        <td class="border border-black p-2.5 text-gray-700 font-sans text-xs leading-relaxed">{exp}</td>')
            h.append('      </tr>')

    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_qfd_legends():
    """Renders the House of Quality notation and scoring legends as clean side-by-side cards."""
    h = []
    h.append('<div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-8">')
    
    # 1. Relationships Card
    h.append('  <div class="border border-black p-5 bg-white shadow-2xs rounded-xs">')
    h.append('    <div class="flex items-center gap-2 border-b border-black pb-2 mb-3">')
    h.append('      <span class="w-3 h-3 bg-black inline-block"></span>')
    h.append('      <h4 class="font-mono text-xs uppercase font-bold tracking-wider text-black">QFD Matrix Relationships</h4>')
    h.append('    </div>')
    h.append('    <p class="font-sans text-xs text-gray-600 mb-3">Defines the impact of engineering specifications on customer requirements.</p>')
    h.append('    <table class="w-full border-collapse border border-black font-mono text-xs text-left">')
    h.append('      <thead><tr class="bg-gray-100 border-b border-black">')
    h.append('        <th class="border border-black p-2 font-bold uppercase">Relationship Level</th>')
    h.append('        <th class="border border-black p-2 font-bold uppercase text-center w-24">Weight Value</th>')
    h.append('      </tr></thead>')
    h.append('      <tbody>')
    h.append('        <tr class="border-b border-gray-300 hover:bg-yellow-50/40">')
    h.append('          <td class="border border-black p-2 font-bold text-black flex items-center gap-2"><span class="px-2 py-0.5 bg-black text-white text-[10px] uppercase">Strong</span></td>')
    h.append('          <td class="border border-black p-2 text-center font-bold text-base text-black bg-gray-50/60">9</td>')
    h.append('        </tr>')
    h.append('        <tr class="border-b border-gray-300 hover:bg-yellow-50/40">')
    h.append('          <td class="border border-black p-2 font-semibold text-gray-800 flex items-center gap-2"><span class="px-2 py-0.5 bg-gray-200 text-gray-800 text-[10px] uppercase">Moderate</span></td>')
    h.append('          <td class="border border-black p-2 text-center font-semibold text-sm text-gray-800 bg-gray-50/60">3</td>')
    h.append('        </tr>')
    h.append('        <tr class="border-b border-gray-300 hover:bg-yellow-50/40">')
    h.append('          <td class="border border-black p-2 text-gray-700 flex items-center gap-2"><span class="px-2 py-0.5 border border-gray-400 text-gray-600 text-[10px] uppercase">Weak</span></td>')
    h.append('          <td class="border border-black p-2 text-center font-medium text-sm text-gray-700 bg-gray-50/60">1</td>')
    h.append('        </tr>')
    h.append('        <tr class="border-b border-gray-300 hover:bg-yellow-50/40">')
    h.append('          <td class="border border-black p-2 text-gray-500 italic">No Relationship</td>')
    h.append('          <td class="border border-black p-2 text-center text-gray-400 text-sm bg-gray-50/60">0</td>')
    h.append('        </tr>')
    h.append('      </tbody>')
    h.append('    </table>')
    h.append('  </div>')

    # 2. Correlations Card
    h.append('  <div class="border border-black p-5 bg-white shadow-2xs rounded-xs">')
    h.append('    <div class="flex items-center gap-2 border-b border-black pb-2 mb-3">')
    h.append('      <span class="w-3 h-3 bg-black inline-block"></span>')
    h.append('      <h4 class="font-mono text-xs uppercase font-bold tracking-wider text-black">Roof Technical Correlations</h4>')
    h.append('    </div>')
    h.append('    <p class="font-sans text-xs text-gray-600 mb-3">Inter-parameter correlations between engineering requirements.</p>')
    h.append('    <table class="w-full border-collapse border border-black font-mono text-xs text-left">')
    h.append('      <thead><tr class="bg-gray-100 border-b border-black">')
    h.append('        <th class="border border-black p-2 font-bold uppercase text-center w-20">Symbol</th>')
    h.append('        <th class="border border-black p-2 font-bold uppercase">Correlation Type</th>')
    h.append('      </tr></thead>')
    h.append('      <tbody>')
    h.append('        <tr class="border-b border-gray-300 hover:bg-yellow-50/40">')
    h.append('          <td class="border border-black p-2 text-center font-bold text-sm bg-gray-100 font-mono">+ +</td>')
    h.append('          <td class="border border-black p-2 font-bold text-black">Strongly Positive</td>')
    h.append('        </tr>')
    h.append('        <tr class="border-b border-gray-300 hover:bg-yellow-50/40">')
    h.append('          <td class="border border-black p-2 text-center font-bold text-sm bg-gray-50 font-mono">+</td>')
    h.append('          <td class="border border-black p-2 font-semibold text-gray-800">Positive</td>')
    h.append('        </tr>')
    h.append('        <tr class="border-b border-gray-300 hover:bg-yellow-50/40">')
    h.append('          <td class="border border-black p-2 text-center text-gray-400 font-mono">&mdash;</td>')
    h.append('          <td class="border border-black p-2 text-gray-500 italic">No Relation</td>')
    h.append('        </tr>')
    h.append('        <tr class="border-b border-gray-300 hover:bg-yellow-50/40">')
    h.append('          <td class="border border-black p-2 text-center font-bold text-sm bg-gray-50 font-mono">-</td>')
    h.append('          <td class="border border-black p-2 font-medium text-gray-800">Negative</td>')
    h.append('        </tr>')
    h.append('        <tr class="border-b border-gray-300 hover:bg-yellow-50/40">')
    h.append('          <td class="border border-black p-2 text-center font-bold text-sm bg-gray-100 font-mono">- -</td>')
    h.append('          <td class="border border-black p-2 font-bold text-black">Strongly Negative</td>')
    h.append('        </tr>')
    h.append('      </tbody>')
    h.append('    </table>')
    h.append('  </div>')

    h.append('</div>\n')
    return '\n'.join(h)

def get_ch3_page_html(pdf_page):
    """
    Returns custom clean HTML for Chapter 3 pages (PDF Pages 46 to 54):
    - 46: Chapter Title & Section 3.1 Introduction
    - 47: Section 3.2 Customer Requirements & Table 3.1 (Complete Unified Table)
    - 48..52: Table 3.1 continuation notices (silencing broken fragment tables)
    - 53: Section 3.3 House of Quality (High-res diagram + clean legends)
    - 54: Section 3.4 Conclusion
    """
    h = []

    # --- PDF Page 46 (Report Page 26) ---
    if pdf_page == 46:
        h.append('<div class="mt-14 mb-8 pt-6 border-t-2 border-black" id="ch-03">')
        h.append('  <span class="text-xs uppercase font-mono tracking-widest bg-black text-white px-2.5 py-1 inline-block mb-3">Chapter 03</span>')
        h.append('  <h2 class="text-2xl md:text-4xl font-bold font-mono tracking-tight text-black">Incorporating the Voice of Customer in Product Design with Quality Function Deployment (QFD)</h2>')
        h.append('</div>\n')

        h.append('<h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mt-10 mb-4" id="sec-3-1"><span class="text-gray-400 mr-2">3.1</span>Introduction</h3>\n')

        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">According to the Japanese, Quality Function Deployment (QFD) is "Listen to the voice of the market (customers)," which refers to understanding the design problem to create a high-quality product. One must comprehend the design problem thoroughly. The process of turning user requests and requirements into a technical description of what has to be created is known as Quality Function Deployment, or QFD. The goal of QFD is to create a product that meets the customer\'s exact needs, rather than focusing on the builder\'s existing skills or knowledge.</p>\n')

        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">In QFD, multi-skilled teams work together to understand customer needs and define technical requirements for each stage. The key benefits of QFD include a strong focus on customer needs, ensuring that products are developed based on what the customer values rather than depending solely on technical expertise. QFD promotes teamwork by bringing together multi-skilled teams, which enhances a deeper understanding of the project requirements. This approach also improves production efficiency and helps reduce development time and costs. The QFD process emphasizes listening to customers, refining specifications, and assessing how well both the company and competitors meet customer expectations.</p>\n')

        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Since we have already collected customer needs by conducting the customer survey, the next step in the QFD technique is to evaluate the importance of each of the customers\' requirements (out of a 10 scale). This is accomplished by generating a weighting factor.</p>\n')
        return '\n'.join(h)

    # --- PDF Page 47 (Report Page 27) ---
    if pdf_page == 47:
        h.append('<h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mt-10 mb-4" id="sec-3-2"><span class="text-gray-400 mr-2">3.2</span>Customer Requirement and Engineering Requirement</h3>\n')

        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">In order to meet the customer requirements, the necessary engineering requirements and their relationship is depicted in the following table:</p>\n')

        h.append('<div class="font-mono text-xs uppercase font-bold tracking-wider mt-8 mb-2 text-black flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>Table 3. 1: Relationship Explanation</div>\n')

        h.append(render_table_3_1())
        return '\n'.join(h)

    # --- PDF Pages 48 to 52 (Report Pages 28 to 32) ---
    if 48 <= pdf_page <= 52:
        rep_p = pdf_page - 20
        h.append(f'<div class="p-3 bg-gray-50/80 border-l-2 border-black my-4 text-xs font-mono text-gray-600 flex items-center justify-between rounded-xs">')
        h.append(f'  <span>↳ <strong class="text-black">Table 3.1: Relationship Explanation</strong> (continuation on Report Page {rep_p}; fully unified on Report Page 27 above)</span>')
        h.append(f'  <a href="#sec-3-2" class="text-black font-bold hover:underline shrink-0 ml-4">↑ View Table 3.1</a>')
        h.append('</div>\n')
        return '\n'.join(h)

    # --- PDF Page 53 (Report Page 33) ---
    if pdf_page == 53:
        h.append('<h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mt-10 mb-4" id="sec-3-3"><span class="text-gray-400 mr-2">3.3</span>Quality Function Deployment\'s House of Quality</h3>\n')

        # High-Resolution House of Quality Diagram
        h.append('<figure class="my-8 max-w-4xl mx-auto border-2 border-black p-4 bg-white shadow-sm hover:border-black transition-colors rounded-xs">')
        h.append('  <div class="flex flex-col items-center justify-center p-2 bg-white overflow-x-auto">')
        h.append('    <img src="/assets/images/pd-report/page_053_img_1_516.png" alt="Figure 3. 1: House of Quality" class="w-full max-h-[650px] object-contain rounded-xs border border-gray-200" loading="lazy" />')
        h.append('    <div class="mt-3 text-center">')
        h.append('      <a href="/assets/images/pd-report/page_053_img_1_516.png" target="_blank" class="inline-flex items-center gap-1.5 text-xs font-mono text-gray-600 hover:text-black hover:underline border border-gray-300 px-3 py-1 bg-gray-50 rounded-xs">')
        h.append('        <span>🔍 View Full-Resolution House of Quality Matrix</span>')
        h.append('      </a>')
        h.append('    </div>')
        h.append('  </div>')
        h.append('  <figcaption class="text-center font-mono text-xs text-black font-bold border-t border-black pt-3 mt-3">Figure 3. 1: House of Quality</figcaption>')
        h.append('</figure>\n')

        # Legends Card
        h.append(render_qfd_legends())
        return '\n'.join(h)

    # --- PDF Page 54 (Report Page 34) ---
    if pdf_page == 54:
        h.append('<h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mt-10 mb-4" id="sec-3-4"><span class="text-gray-400 mr-2">3.4</span>Conclusion</h3>\n')

        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">QFD gives a deeper understanding of the problem. It helps to build up consensus within an organization on the measurement systems and performance specifications that represent the demands of the customers. Strategically designed to enhance competitiveness for a company, QFD also identifies and prioritizes actions needed to satisfy the expressed and implied needs of the customer. We were able to develop our QFD process in relatively quick fashion because we were under a very tight schedule&mdash;normally, QFD is a very involved, lengthy process. Although this apparently slows down the design phase, time utilized at the front end in gathering information saves time further down the process.</p>\n')
        return '\n'.join(h)

    return ""
