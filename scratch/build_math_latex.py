# -*- coding: utf-8 -*-
import re
import html

def format_math_para(full_para):
    t = full_para.strip()

    # 1. Section 7.3: Equations
    if 'Relative Emphasis Coefficient' in t and ('positive decisions' in t or 'criteria' in t):
        return (
            '<div class="math-block my-5 p-5 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            '<span class="block font-mono text-xs text-gray-500 font-bold mb-2 uppercase tracking-wider">Equation 7.1: Relative Emphasis Coefficient</span>'
            r'$$\alpha = \frac{\text{Number of positive decisions acquired by a criterion}}{\text{Total number of positive decisions}}'
            '$$</div>'
        )

    if 'properties to be maximized' in t or ('Scaled property' in t and 'Maximum value' in t):
        return (
            '<div class="math-block my-5 p-5 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            '<span class="block font-mono text-xs text-gray-500 font-bold mb-2 uppercase tracking-wider">Equation 7.2: Scaled Property (Maximization)</span>'
            r'$$\beta_{\text{max}} = \left( \frac{\text{Numerical value of the property}}{\text{Maximum value in the list}} \right) \times 100'
            '$$</div>'
        )

    if 'properties to be minimized' in t or ('Scaled property' in t and 'Minimum value' in t):
        return (
            '<div class="math-block my-5 p-5 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            '<span class="block font-mono text-xs text-gray-500 font-bold mb-2 uppercase tracking-wider">Equation 7.3: Scaled Property (Minimization)</span>'
            r'$$\beta_{\text{min}} = \left( \frac{\text{Minimum value in the list}}{\text{Numerical value of the property}} \right) \times 100'
            '$$</div>'
        )

    if 'Weighted score' in t and ('Relative Emphasis' in t or 'α' in t):
        return (
            '<div class="math-block my-5 p-5 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            '<span class="block font-mono text-xs text-gray-500 font-bold mb-2 uppercase tracking-wider">Equation 7.4: Weighted Score</span>'
            r'$$\text{Weighted Score} = \text{Relative Emphasis Coefficient } (\alpha) \times \text{Scaled Property } (\beta)'
            '$$</div>'
        )

    if 'Performance index' in t and ('Σ' in t or 'γ' in t):
        return (
            '<div class="math-block my-5 p-5 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            '<span class="block font-mono text-xs text-gray-500 font-bold mb-2 uppercase tracking-wider">Equation 7.5: Performance Index</span>'
            r'$$\text{Performance Index } (\gamma) = \sum_{i=1}^{n} (\alpha_i \cdot \beta_i)'
            '$$</div>'
        )

    # 2. Digital Logic Decisions combinations
    m_dec = re.search(r'N\s*=\s*n\s*\(\s*n\s*-\s*1\s*\)\s*/\s*2\s*=\s*(\d+)\s*\(\s*(\d+)\s*-\s*1\s*\)\s*/\s*2\s*=\s*(\d+)', t)
    if m_dec:
        n_val = m_dec.group(1)
        tot_val = m_dec.group(3)
        return (
            '<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            f'<span class="block font-mono text-xs text-gray-500 font-bold mb-1 uppercase tracking-wider">Digital Logic Decisions (n = {n_val})</span>'
            f'$$N = \\frac{{n(n-1)}}{{2}} = \\frac{{{n_val}({n_val}-1)}}{{2}} = {tot_val}$$'
            '</div>'
        )

    # 3. Adoption Rate
    if 'Adoption Rate = Number of Positive Responses' in t:
        return (
            '<div class="math-block my-5 p-5 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            '<span class="block font-mono text-xs text-gray-500 font-bold mb-2 uppercase tracking-wider">Equation 8.1: Adoption Rate Formulation</span>'
            r'$$\text{Adoption Rate} = \frac{\text{Number of Positive Responses}}{\text{Total Number of Surveyed Institutions}}'
            '$$</div>'
        )

    if 'Adoption Rate = 28/35' in t or 'Adoption Rate = 28 / 35' in t:
        return (
            '<div class="math-block my-5 p-5 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            '<span class="block font-mono text-xs text-gray-500 font-bold mb-2 uppercase tracking-wider">Empirical Adoption Rate Calculation</span>'
            r'$$\text{Adoption Rate} = \frac{28}{35} = 0.80 \ (80\%)'
            '$$</div>'
        )

    # 4. Forecasted Demand
    if 'Forecasted Demand = Total Population' in t:
        return (
            '<div class="math-block my-5 p-5 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            '<span class="block font-mono text-xs text-gray-500 font-bold mb-2 uppercase tracking-wider">Equation 8.2: Forecasted Annual Demand</span>'
            r'$$\text{Forecasted Demand} = \text{Total Population} \times \text{Adoption Rate}'
            '$$</div>'
        )

    if 'Forecasted Demand = 2941' in t:
        return (
            '<div class="math-block my-5 p-5 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            '<span class="block font-mono text-xs text-gray-500 font-bold mb-2 uppercase tracking-wider">Baseline Annual Demand Calculation</span>'
            r'$$\text{Forecasted Demand} = 2941 \times 0.8 = 2353 \text{ units}'
            '$$</div>'
        )

    # Scenario Multiplications
    m_scen = re.search(r'2353\s*[×\*]\s*(0\.[987])\s*=\s*(\d+)\s*units?', t)
    if m_scen:
        pct = int(float(m_scen.group(1)) * 100)
        label = "Optimistic" if pct == 90 else ("Realistic" if pct == 80 else "Pessimistic")
        return (
            f'<div class="math-block my-3 p-3.5 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            f'<span class="block font-mono text-xs text-gray-500 font-bold mb-1 uppercase tracking-wider">{label} Scenario ({pct}% Adoption)</span>'
            f'$$\\text{{Demand}}_{{{pct}\\%}} = 2353 \\times {m_scen.group(1)} = {m_scen.group(2)} \\text{{ units}}$$'
            '</div>'
        )

    # 5. Break-Even Equilibrium
    if re.search(r'Selling\s+price\s*[×\*]\s*Q_?BEP\s*=\s*Total\s+Fixed', t, re.I):
        return (
            '<div class="math-block my-5 p-5 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            '<span class="block font-mono text-xs text-gray-500 font-bold mb-2 uppercase tracking-wider">Equation 8.3: Break-Even Point Formulation</span>'
            r'$$\text{Selling Price} \times Q_{BEP} = \text{Total Fixed Cost} + (\text{Variable Cost per unit} \times Q_{BEP})'
            '$$</div>'
        )

    # Break-Even Substitution
    if re.search(r'51756\s*[×\*]\s*Q_?BEP\s*=\s*(\d+)\s*\+\s*\(?([\d\.]+)\s*[×\*]\s*Q_?BEP\)?', t, re.I):
        m = re.search(r'51756\s*[×\*]\s*Q_?BEP\s*=\s*(\d+)\s*\+\s*\(?([\d\.]+)\s*[×\*]\s*Q_?BEP\)?', t, re.I)
        fc = int(m.group(1))
        vc = float(m.group(2))
        return (
            '<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            f'$$51,756 \\times Q_{{BEP}} = {fc:,} + ({vc:,.2f} \\times Q_{{BEP}})$$'
            '</div>'
        )

    # QBEP Result
    m_q = re.match(r'^(Or,\s*)?Q_?BEP\s*=\s*(\d+)\s*units?\.?(\s*\(No change\))?', t, re.I)
    if m_q:
        q_val = m_q.group(2)
        extra = r' \quad \text{(No change)}' if 'No change' in t else ''
        return (
            '<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            f'$$Q_{{BEP}} = {q_val} \\text{{ units}}{extra}$$'
            '</div>'
        )

    # Break-even Period
    if 'Break-even Period' in t and ('226/565' in t or '0.4' in t):
        return (
            '<div class="math-block my-5 p-5 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            '<span class="block font-mono text-xs text-gray-500 font-bold mb-2 uppercase tracking-wider">Break-Even Payback Period</span>'
            r'$$\text{Break-Even Period} = 1 \text{ year} \times \frac{226}{565} = 0.40 \text{ year} \approx 4.8 \text{ months}'
            '$$</div>'
        )

    # Sensitivity Delta QBEP equation
    if 'Δ' in t and 'QBEP' in t and '%' in t:
        m = re.search(r'\((\d+)\s*[\-–]\s*226\)\s*/\s*226\s*\*?\s*100%', t)
        if m:
            new_q = m.group(1)
            return (
                '<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
                '<span class="block font-mono text-xs text-gray-500 font-bold mb-1 uppercase tracking-wider">Break-Even Sensitivity Index</span>'
                f'$$\\Delta Q_{{BEP}} = \\frac{{{new_q} - 226}}{{226}} \\times 100\\%$$'
                '</div>'
            )

    if re.match(r'^[=\s]*[\.\d]+\s*%', t):
        val = t.replace('=', '').strip()
        return (
            '<div class="math-block my-2 p-3 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            f'$$\\Delta Q_{{BEP}} = {val}$$'
            '</div>'
        )

    # Direct material per unit variable cost
    if 'Total variable cost will be per unit production' in t:
        return (
            '<div class="math-block my-5 p-5 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            '<span class="block font-mono text-xs text-gray-500 font-bold mb-2 uppercase tracking-wider">Adjusted Variable Cost (Direct Material +10%)</span>'
            r'$$\text{New Variable Cost per unit} = 36,534.77 - \frac{17,138,145}{565} + \frac{18,851,959.50}{565} = 39,568.10 \text{ BDT}'
            '$$</div>'
        )

    # New demand
    if 'New demand per year = 565+565*0.1= 622' in t:
        return (
            '<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            r'$$\text{New Demand} = 565 + (565 \times 0.10) = 622 \text{ units/year}'
            '$$</div>'
        )

    # Profit per unit
    if 'Profit per unit = 0.25*Variable cost' in t:
        return (
            '<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            '<span class="block font-mono text-xs text-gray-500 font-bold mb-1 uppercase tracking-wider">Target Unit Profit Margin (25%)</span>'
            r'$$\text{Profit per unit} = 0.25 \times 36,534.77 = 9,133.69 \text{ BDT}'
            '$$</div>'
        )

    # Variable cost calculation
    if 'Variable cost per unit = 20854545/565' in t:
        return (
            '<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            r'$$\text{Adjusted Variable Cost per unit} = \frac{20,854,545}{565} = 36,910.70 \text{ BDT}'
            '$$</div>'
        )

    # Stainless steel sheet dimension bullet
    if 'Stainless steel sheet (4ft×8ft×1mm)' in t:
        return f'<p class="text-base text-gray-800 leading-relaxed mb-4 font-sans">{html.escape(t)}</p>'

    # Cost parameter lines: Interest rate, repayment periods, etc.
    if any(t.startswith(k) for k in ['Interest rate', 'Repayment periods', 'Annuity', 'Fixed Cost per unit', 'Total Variable Cost', 'Total production Cost', 'Selling price per unit', 'Total revenue', 'Break-even Quantity', 'Increase of Demand', 'Total cost of direct material', 'Total cost of labor', 'Total administrative cost', 'Total selling expenses']):
        parts = t.split('=', 1)
        if len(parts) == 2:
            lbl = parts[0].strip()
            val = parts[1].strip().rstrip('/-')
            return f'<div class="my-2.5 px-4 py-2 bg-gray-50/80 border-l-4 border-black font-mono text-xs text-gray-800 flex justify-between items-center rounded-r-xs"><span>{html.escape(lbl)}</span><span class="font-bold font-sans text-sm">{html.escape(val)}</span></div>'

    # Cost totals with '/-'
    if re.match(r'^(Total\s+.*)=\s*([\d,]+)/?-?', t):
        m = re.match(r'^(Total\s+.*)=\s*([\d,]+)/?-?', t)
        return f'<div class="my-3 px-4 py-2.5 bg-gray-50 border border-gray-300 font-mono text-xs flex justify-between items-center rounded-xs"><span>{html.escape(m.group(1).strip())}</span><span class="font-bold text-black font-sans">{m.group(2).strip()} BDT</span></div>'

    # Single line equation remnants (e.g. "Or, 51756× Qbep =3439523+ (36910.7× Qbep)")
    if re.search(r'51756\s*[×\*]\s*Q_?bep', t, re.I):
        m = re.search(r'51756\s*[×\*]\s*Q_?bep\s*=\s*(\d+)\s*\+\s*\(?([\d\.]+)\s*[×\*]\s*Q_?bep\)?', t, re.I)
        if m:
            fc = int(m.group(1))
            vc = float(m.group(2))
            return (
                '<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
                f'$$51,756 \\times Q_{{BEP}} = {fc:,} + ({vc:,.2f} \\times Q_{{BEP}})$$'
                '</div>'
            )

    # Isolated value "= 25.22%" or "= 2336400/-"
    if re.match(r'^[=\s]*[\.\d]+\s*%', t):
        val = t.replace('=', '').strip()
        return (
            '<div class="math-block my-2 p-3 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">'
            f'$$\\Delta Q_{{BEP}} = {val}$$'
            '</div>'
        )

    # Default: not a special math block
    return None

def format_paragraph_with_math(full_para):
    """Formats full paragraph into display math block or semantic prose with inline math."""
    math_html = format_math_para(full_para)
    if math_html:
        return math_html

    p_esc = html.escape(full_para)
    # Convert inline math symbols
    p_esc = re.sub(r'\bQBEP\b', r'$Q_{BEP}$', p_esc)
    p_esc = re.sub(r'\bQbep\b', r'$Q_{BEP}$', p_esc)
    p_esc = re.sub(r'Δ\s*Q_?BEP', r'$\\Delta Q_{BEP}$', p_esc)
    p_esc = re.sub(r'Δ\s*Q\b', r'$\\Delta Q$', p_esc)
    p_esc = re.sub(r'\bN=n\(n-1\)/2\b', r'$N = \\frac{n(n-1)}{2}$', p_esc)

    return f'<p class="text-base text-gray-800 leading-relaxed mb-4">{p_esc}</p>'

def format_table_cell(cell_text):
    """Formats table cell or header with inline KaTeX math."""
    if not cell_text:
        return ""
    cell_esc = html.escape(cell_text).replace('\n', '<br>')

    # Replace N=n(n-1)/2 combinations in table headers
    cell_esc = re.sub(
        r'N\s*=\s*n\s*\(\s*n\s*-\s*1\s*\)\s*/\s*2\s*=\s*(\d+)\s*\(\s*(\d+)\s*-\s*1\s*\)\s*/\s*2\s*=\s*(\d+)',
        r'$N = \\frac{n(n-1)}{2} = \\frac{\1(\2-1)}{2} = \3$',
        cell_esc
    )
    # Greek symbols in headers
    cell_esc = re.sub(r'\bScore,\s*αβ\b', r'Score, $\\alpha\\beta$', cell_esc)
    cell_esc = re.sub(r'\bIndex,\s*γ\b', r'Index, $\\gamma$', cell_esc)
    cell_esc = re.sub(r'\(αβ\)', r'($\\alpha\\beta$)', cell_esc)
    cell_esc = re.sub(r'\(α\)', r'($\\alpha$)', cell_esc)
    cell_esc = re.sub(r'\(β\)', r'($\\beta$)', cell_esc)
    cell_esc = re.sub(r'\(γ\)', r'($\\gamma$)', cell_esc)
    cell_esc = re.sub(r'\bCoefficient,\s*α\b', r'Coefficient, $\\alpha$', cell_esc)
    cell_esc = re.sub(r'\bFactor\s*\(α\)\b', r'Factor ($\\alpha$)', cell_esc)

    return cell_esc
