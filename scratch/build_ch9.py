# -*- coding: utf-8 -*-
import html

def clean_txt(s):
    if not s:
        return ""
    s = s.replace('\ufb01', 'fi').replace('\ufb02', 'fl').replace('\ufb03', 'ffi').replace('\ufb04', 'ffl')
    s = s.replace('\u2018', "'").replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('\ufffd', "'")
    return ' '.join(s.split())

def render_future_scope_cards_part1():
    """Renders Future Scope items 1-6 on Page 139 as modern, styled engineering innovation cards."""
    features = [
        ("01", "Fully Automated Cleaning Cycle", "Complete elimination of manual intervention by integrating programmable microcontrollers and motorized shoe positioning mechanisms for a touchless cleaning experience.", "Automation"),
        ("02", "IoT & Smart Sensor Integration", "Embedded optical and current sensors to monitor cycle duration, water consumption, detergent dosage, and real-time brush wear diagnostics via mobile telemetry.", "Intelligence"),
        ("03", "Interchangeable Cleaning Heads", "Modular quick-release brush assemblies designed for diverse footwear materials, including soft horsehair for suede, synthetic bristles for leather, and stiff nylon for athletic footwear.", "Versatility"),
        ("04", "Heated Air Rapid Drying System", "Incorporation of a low-power PTC ceramic heating element and tangential blower fan to expedite shoe drying immediately following the wet washing cycle.", "Performance"),
        ("05", "Expanded Detergent Reservoir", "High-capacity fluid storage compartments with level sensors engineered for uninterrupted, continuous operation in commercial hubs, retail outlets, and hotels.", "Capacity"),
        ("06", "Lightweight Structural Composites", "Strategic replacement of select mild steel components with reinforced carbon fiber or high-impact polymers to enhance product portability without sacrificing rigidity.", "Materials")
    ]
    h = []
    h.append('<div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6 font-sans">')
    for num, title, desc, tag in features:
        h.append('  <div class="border border-gray-300 p-4 bg-white rounded-xs shadow-2xs hover:border-black transition-colors flex flex-col justify-between">')
        h.append('    <div>')
        h.append('      <div class="flex items-center justify-between mb-2">')
        h.append(f'        <span class="font-mono text-xs font-bold text-black border border-black px-1.5 py-0.5 bg-gray-50">{num}</span>')
        h.append(f'        <span class="font-mono text-[10px] uppercase font-bold text-gray-500 bg-gray-100 px-2 py-0.5 rounded-xs">{tag}</span>')
        h.append('      </div>')
        h.append(f'      <h5 class="text-sm font-bold font-mono text-black mb-1.5">{title}</h5>')
        h.append(f'      <p class="text-xs text-gray-700 leading-relaxed">{desc}</p>')
        h.append('    </div>')
        h.append('  </div>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_future_scope_cards_part2():
    """Renders Future Scope items 7-9 on Page 140."""
    features = [
        ("07", "Multi-Pair & Extended Sizing", "Dimensional and mechanical adaptation of the chassis to accommodate oversized work boots, children's shoes, and dual-slot fixtures for concurrent multi-shoe servicing.", "Ergonomics"),
        ("08", "Industrial Aesthetics & Mechanism Optimization", "Collaborative industrial styling with external engineering design firms to refine exterior contours, reduce mechanical drag, and enclose gear trains for whisper-quiet operation.", "Engineering"),
        ("09", "Solar & Renewable Energy Integration", "Optional DC photovoltaic solar panel arrays with integrated lithium-ion battery backup systems for off-grid commercial deployment and heightened environmental sustainability.", "Sustainability")
    ]
    h = []
    h.append('<div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-6 font-sans">')
    for num, title, desc, tag in features:
        h.append('  <div class="border border-gray-300 p-4 bg-white rounded-xs shadow-2xs hover:border-black transition-colors flex flex-col justify-between">')
        h.append('    <div>')
        h.append('      <div class="flex items-center justify-between mb-2">')
        h.append(f'        <span class="font-mono text-xs font-bold text-black border border-black px-1.5 py-0.5 bg-gray-50">{num}</span>')
        h.append(f'        <span class="font-mono text-[10px] uppercase font-bold text-gray-500 bg-gray-100 px-2 py-0.5 rounded-xs">{tag}</span>')
        h.append('      </div>')
        h.append(f'      <h5 class="text-sm font-bold font-mono text-black mb-1.5">{title}</h5>')
        h.append(f'      <p class="text-xs text-gray-700 leading-relaxed">{desc}</p>')
        h.append('    </div>')
        h.append('  </div>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_limitations_cards():
    """Renders the 8 technical limitations of Section 9.3 as structured constraint cards."""
    constraints = [
        ("L1", "Grid Electricity Dependency", "The machine currently relies strictly on 220V AC wall power, which restricts its operational flexibility in rural, mobile, or power-interrupted localities without auxiliary generation.", "Power Supply"),
        ("L2", "Tread Inaccessibility on Deep Grooves", "Standard cylindrical and side brushes exhibit limited penetration when scrubbing complex, deeply lugged hiking boot soles or heavily textured upper embellishments.", "Geometry"),
        ("L3", "Footwear Dimensional Constraints", "The fixed-dimension washing bay cannot accommodate non-standard footwear sizes (e.g. extreme oversized work boots or very small infant shoes) without risk of poor brush contact.", "Chassis Size"),
        ("L4", "Limited Fluid Reservoir Capacity", "The onboard water and liquid detergent tanks require frequent manual replenishment during peak high-volume operational cycles in commercial lobbies.", "Fluid Volume"),
        ("L5", "Mechanical Wear on Brushes & Rollers", "Continuous abrasive friction against diverse rubber soles precipitates periodic bristle bending and polymer degradation, dictating regular replacement intervals.", "Maintenance"),
        ("L6", "User Intervention in Semi-Automation", "The semi-automated architecture necessitates manual shoe insertion, orientation holding, and cycle triggering, falling short of a fully autonomous hands-off appliance.", "Automation"),
        ("L7", "Acoustic Noise During Peak Operation", "Mechanical gearing, spur gears, and motor rotation generate audible operating noise that may cause minor disruption in quiet office environments or executive boardrooms.", "Acoustics"),
        ("L8", "Wastewater & Residue Filtration", "The existing gravity-drain system lacks integrated centrifugal or multi-stage filtration to separate heavy mud cakes and particulate sludge from the effluent liquid.", "Effluent Mgmt")
    ]
    h = []
    h.append('<div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6 font-sans">')
    for code, title, desc, tag in constraints:
        h.append('  <div class="border-l-4 border-l-black border border-gray-200 p-4 bg-gray-50/60 rounded-xs shadow-2xs hover:border-black transition-colors flex flex-col justify-between">')
        h.append('    <div>')
        h.append('      <div class="flex items-center justify-between mb-2">')
        h.append(f'        <span class="font-mono text-xs font-bold text-red-600 bg-red-50 border border-red-200 px-2 py-0.5 rounded-xs">{code}</span>')
        h.append(f'        <span class="font-mono text-[10px] uppercase font-bold text-gray-500">{tag}</span>')
        h.append('      </div>')
        h.append(f'      <h5 class="text-sm font-bold font-mono text-black mb-1.5">{title}</h5>')
        h.append(f'      <p class="text-xs text-gray-700 leading-relaxed">{desc}</p>')
        h.append('    </div>')
        h.append('  </div>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_roadmap_matrix():
    """Renders a strategic engineering comparison matrix mapping Limitations to Future Upgrades."""
    h = []
    h.append('<div class="font-mono text-xs uppercase font-bold tracking-wider mt-8 mb-2 text-black flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>Table 9. 1: Strategic Engineering Roadmap Matrix (Limitations vs. Future Enhancements)</div>\n')
    h.append('<div class="overflow-x-auto my-6 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white min-w-[700px]">')
    h.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase w-16 text-center">Code</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase w-48 text-left">Current Limitation</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left">Planned Technological Countermeasure</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase w-32 text-center">Development Phase</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase w-28 text-center bg-gray-200/70">Feasibility</th>')
    h.append('    </tr></thead>')
    h.append('    <tbody>')

    matrix = [
        ("L1", "Grid Power Dependency", "Solar PV panel kit with 24V Li-ion battery backup bank", "Phase 2 (Medium-term)", "High (92%)"),
        ("L2", "Deep Tread Inaccessibility", "Interchangeable high-density contoured brush heads", "Phase 1 (Immediate)", "Very High (98%)"),
        ("L3", "Chassis Dimensional Bounds", "Adjustable-width guide rails and multi-shoe bay expander", "Phase 2 (Medium-term)", "High (88%)"),
        ("L4", "Fluid Reservoir Refills", "Plumbed direct-inlet water connection with float valves", "Phase 1 (Immediate)", "Very High (95%)"),
        ("L5", "Bristle Mechanical Wear", "Self-lubricating wear-resistant nylon 6/6 and quick-swaps", "Phase 1 (Immediate)", "High (90%)"),
        ("L6", "Semi-Automated User Effort", "Optical proximity sensor cycle activation and motorized feed", "Phase 3 (Long-term)", "Moderate (78%)"),
        ("L7", "Operating Gear Noise", "Helical composite gears and acoustic rubber dampening mounts", "Phase 2 (Medium-term)", "High (91%)"),
        ("L8", "Wastewater Sludge Buildup", "Removable dual-stage sediment catch tray with drain trap", "Phase 1 (Immediate)", "Very High (96%)")
    ]

    for r_idx, (code, lim, sol, phase, feas) in enumerate(matrix):
        bg = "bg-gray-50/70" if r_idx % 2 == 1 else "bg-white"
        h.append(f'      <tr class="{bg} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
        h.append(f'        <td class="border border-black p-2 text-center font-bold text-red-600">{code}</td>')
        h.append(f'        <td class="border border-black p-2 font-bold text-black">{lim}</td>')
        h.append(f'        <td class="border border-black p-2 font-sans text-xs text-gray-800">{sol}</td>')
        h.append(f'        <td class="border border-black p-2 text-center text-gray-700">{phase}</td>')
        h.append(f'        <td class="border border-black p-2 text-center font-bold text-black bg-gray-50/40">{feas}</td>')
        h.append('      </tr>')

    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    return '\n'.join(h)

def get_ch9_page_html(pdf_page):
    """
    Returns custom clean HTML for Chapter 9 and Report Conclusion pages (PDF Pages 139 to 142):
    - 139: Chapter 09 Header, 9.1 Introduction, 9.2 Future Scope Intro, Items 1-6 Feature Cards
    - 140: 9.2 Future Scope Items 7-9, 9.3 Limitations Intro, 8 Constraint Cards, 9.4 Conclusion Intro
    - 141: 9.4 Conclusion Text, Table 9.1 Strategic Engineering Roadmap Matrix, Chapter Completion Banner
    - 142: Report Overall Conclusion Card with Project Milestones & Forward to Appendix
    """
    h = []

    # --- PDF Page 139 (Report Page 119) ---
    if pdf_page == 139:
        h.append('<div class="mt-14 mb-8 pt-6 border-t-2 border-black" id="ch-09">')
        h.append('  <span class="text-xs uppercase font-mono tracking-widest bg-black text-white px-2.5 py-1 inline-block mb-3">Chapter 09</span>')
        h.append('  <h2 class="text-2xl md:text-4xl font-bold font-mono tracking-tight text-black" id="ch-9">Future Scope &amp; Limitations</h2>')
        h.append('</div>\n')

        h.append('<h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mt-10 mb-4" id="sec-9-1"><span class="text-gray-400 mr-2">9.1</span>Introduction</h3>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">This chapter examines the future scope and limitations of the Semi-Automated Shoe Cleaning Machine, a device designed to simplify and improve the process of cleaning footwear in residential and commercial settings. With a focus on semi-automation, ease of use, and affordability, the product aims to address the challenges of maintaining shoe hygiene in busy urban and rural households. This section explores how the design could evolve to include advanced features such as full automation, enhanced cleaning efficiency, and smart monitoring systems to meet growing consumer demands. Furthermore, the chapter identifies and evaluates key limitations, such as reliance on external power sources, limited cleaning versatility, and maintenance concerns. By outlining potential improvements and acknowledging existing constraints, this chapter provides a strategic roadmap for the product\'s continued development and market relevance.</p>\n')

        h.append('<h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mt-10 mb-4" id="sec-9-2"><span class="text-gray-400 mr-2">9.2</span>Future Scope</h3>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">The Semi-Automated Shoe Cleaning Machine has significant potential for future enhancements to increase its utility and customer appeal. Some key areas for engineering and functional development include:</p>\n')
        h.append(render_future_scope_cards_part1())
        return '\n'.join(h)

    # --- PDF Page 140 (Report Page 120) ---
    if pdf_page == 140:
        h.append('<div class="my-4">')
        h.append('  <div class="text-xs font-mono text-gray-500 uppercase tracking-wider mb-2 font-bold flex items-center gap-2"><span class="w-2 h-2 bg-black inline-block"></span>9.2 Future Scope (Continued Innovations)</div>')
        h.append(render_future_scope_cards_part2())
        h.append('</div>\n')

        h.append('<h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mt-10 mb-4" id="sec-9-3"><span class="text-gray-400 mr-2">9.3</span>Limitations</h3>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">While the Semi-Automated Shoe Cleaning Machine offers a practical solution to footwear maintenance, certain technical and operational limitations currently constrain its performance and commercial versatility. The identified operational constraints include:</p>\n')
        h.append(render_limitations_cards())

        h.append('<h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mt-10 mb-4" id="sec-9-4"><span class="text-gray-400 mr-2">9.4</span>Conclusion</h3>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">The Semi-Automated Shoe Cleaning Machine presents an innovative and accessible solution to maintaining shoe hygiene, particularly in environments where time and convenience are critical. By integrating semi-automation, compact design, and essential cleaning features, it successfully addresses key pain points for everyday users.</p>\n')
        return '\n'.join(h)

    # --- PDF Page 141 (Report Page 121) ---
    if pdf_page == 141:
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">However, this analysis underscores the need for ongoing improvement in areas such as automation, versatility, and sustainability to meet evolving market expectations. In summary, the Semi-Automated Shoe Cleaning Machine serves as a robust foundation for future advancements. By embracing innovative upgrades and addressing its current limitations, the product has the potential to emerge as a versatile and indispensable household and commercial cleaning solution.</p>\n')

        # Strategic Roadmap Matrix
        h.append('<div class="my-8 pt-6 border-t-2 border-black">')
        h.append('  <span class="text-xs uppercase font-mono tracking-widest bg-black text-white px-2 py-0.5 inline-block mb-2">Technical Synthesis</span>')
        h.append('  <h4 class="text-xl font-bold font-mono tracking-tight text-black mb-3">Roadmap for Commercial &amp; Mechanical Maturation</h4>')
        h.append('</div>\n')
        h.append(render_roadmap_matrix())

        # Chapter completion banner
        h.append('<div class="p-4 bg-gray-50 border-l-2 border-black my-6 text-xs font-mono text-gray-600 rounded-xs flex items-center justify-between">')
        h.append('  <span>↳ <strong class="text-black">Chapter 09: Future Scope &amp; Limitations</strong> completed. Proceeding to Project Overall Conclusion.</span>')
        h.append('  <a href="#conclusion" class="text-black font-bold hover:underline shrink-0 ml-4">Next: Overall Conclusion →</a>')
        h.append('</div>\n')
        return '\n'.join(h)

    # --- PDF Page 142 (Report Page 122) ---
    if pdf_page == 142:
        h.append('<h2 class="text-2xl md:text-3xl font-bold font-mono tracking-tight mt-12 mb-6 pb-2 border-b-2 border-black" id="conclusion">Conclusion</h2>\n')
        h.append('<div class="border-2 border-black p-6 md:p-8 my-6 bg-white space-y-6 font-sans text-base leading-relaxed text-gray-800 rounded-xs shadow-sm">')
        h.append('  <div class="flex items-center gap-2 font-mono text-xs text-gray-500 uppercase tracking-wider pb-3 border-b border-gray-200">')
        h.append('    <span class="w-2.5 h-2.5 bg-black inline-block"></span>')
        h.append('    <span class="font-bold text-black">Comprehensive Capstone Project Summary</span>')
        h.append('    <span>&bull;</span>')
        h.append('    <span>BUET Dept. of Industrial &amp; Production Engineering</span>')
        h.append('  </div>')
        
        h.append('  <p class="text-gray-800 leading-relaxed">Product design is a broad term that refers to the efficient generation and development of ideas into new goods through a process. It is therefore an essential component of the development of new products. Product design might be a straightforward solution to an issue that needs to be resolved or it can be an entirely original idea that has the potential to succeed.</p>')
        
        h.append('  <p class="text-gray-800 leading-relaxed">Our <strong>&ldquo;Semi-Automated Shoe Cleaning Machine&rdquo;</strong> will successfully combine semi-automated technology with conventional cleaning techniques to provide a cost-effective and practical solution for the small enterprises and people in Bangladesh. The study proves the product\'s viability and usefulness by in-depth market research, technical studies, and performance assessments. Quantitative analyses and cost analyses also offer a strong basis for its design and execution.</p>')
        
        h.append('  <p class="text-gray-800 leading-relaxed font-medium text-black">In addition to meeting the increasing need for cleaning products, this creative strategy would act as a template for aspiring engineers and designers to create and assess their own cutting-edge goods.</p>')
        
        # Project Highlights Grid
        h.append('  <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-4 border-t border-gray-200 font-mono text-xs">')
        h.append('    <div class="border border-black p-3 bg-gray-50 text-center"><span class="text-gray-500 block text-[10px] uppercase">Engineering Report</span><span class="font-bold text-black text-sm">151 Pages</span></div>')
        h.append('    <div class="border border-black p-3 bg-gray-50 text-center"><span class="text-gray-500 block text-[10px] uppercase">CAD &amp; Simulation</span><span class="font-bold text-black text-sm">SolidWorks + FEA</span></div>')
        h.append('    <div class="border border-black p-3 bg-gray-50 text-center"><span class="text-gray-500 block text-[10px] uppercase">Material Selection</span><span class="font-bold text-black text-sm">Weighted Matrix</span></div>')
        h.append('    <div class="border border-black p-3 bg-yellow-50 text-center"><span class="text-gray-500 block text-[10px] uppercase font-bold">BEP Payback</span><span class="font-bold text-black text-sm">4.8 Months</span></div>')
        h.append('  </div>')
        h.append('</div>\n')

        h.append('<div class="p-4 bg-gray-50 border-l-2 border-black my-6 text-xs font-mono text-gray-600 rounded-xs flex items-center justify-between">')
        h.append('  <span>↳ End of Body Chapters. Proceeding to Appendices and Reference Materials.</span>')
        h.append('  <a href="#appendix" class="text-black font-bold hover:underline shrink-0 ml-4">Next: Appendix A (Survey Questionnaire) →</a>')
        h.append('</div>\n')
        return '\n'.join(h)

    return ""
