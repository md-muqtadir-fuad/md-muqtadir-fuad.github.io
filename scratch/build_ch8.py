# -*- coding: utf-8 -*-
import html

def clean_txt(s):
    if not s:
        return ""
    s = s.replace('\ufb01', 'fi').replace('\ufb02', 'fl').replace('\ufb03', 'ffi').replace('\ufb04', 'ffl')
    s = s.replace('\u2018', "'").replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('\ufffd', '"')
    return ' '.join(s.split())

def render_machinery_cost():
    """Renders Section 8.3.1 Cost of Machinery as a clean, structured equipment specification table."""
    h = []
    h.append('<div class="overflow-x-auto my-6 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white min-w-[700px]">')
    h.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left">Equipment / Machine</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left">Specification</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-center w-24">Lifespan</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-center w-16">Qty</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-right w-28">Unit Cost (Tk.)</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-right w-32 bg-gray-200/70">Total Cost (Tk.)</th>')
    h.append('    </tr></thead>')
    h.append('    <tbody>')
    
    machines = [
        ("Lathe Machine", "CQ6230A Single Phase Conventional Manual Lathe (4.5 feet)", "20 years", "2", "1,70,000", "3,40,000"),
        ("Drill Machine", "BOKY Bench/Pillar Drill (13mm chuck capacity)", "10 years", "1", "9,000", "9,000"),
        ("Arc Welding Machine", "ARC300 IGBT Inverter Arc Welder", "10 years", "2", "15,820", "31,640")
    ]
    
    for r_idx, (name, spec, life, qty, unit_c, tot_c) in enumerate(machines):
        bg = "bg-gray-50/70" if r_idx % 2 == 1 else "bg-white"
        h.append(f'      <tr class="{bg} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
        h.append(f'        <td class="border border-black p-2 font-bold text-black">{name}</td>')
        h.append(f'        <td class="border border-black p-2 font-sans text-xs text-gray-700">{spec}</td>')
        h.append(f'        <td class="border border-black p-2 text-center text-gray-600 font-medium">{life}</td>')
        h.append(f'        <td class="border border-black p-2 text-center font-bold">{qty}</td>')
        h.append(f'        <td class="border border-black p-2 text-right font-medium text-gray-800">{unit_c}/-</td>')
        h.append(f'        <td class="border border-black p-2 text-right font-bold text-black bg-gray-50/40">{tot_c}/-</td>')
        h.append('      </tr>')
        
    # Total row
    h.append('      <tr class="bg-gray-100 font-bold border-t-2 border-black">')
    h.append('        <td colspan="5" class="border border-black p-2.5 text-right uppercase tracking-wider text-black">Total Capital Machinery Cost</td>')
    h.append('        <td class="border border-black p-2.5 text-right font-bold text-sm bg-yellow-100/80 text-black">3,80,640/-</td>')
    h.append('      </tr>')
    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    
    # Financial terms note
    h.append('<div class="p-3 bg-gray-50 border-l-2 border-black my-4 text-xs font-mono text-gray-700 rounded-xs">')
    h.append('  <span class="font-bold text-black">Financing Terms:</span> Machinery purchased on credit at a <span class="font-bold text-black">12% annual interest rate</span> with a <span class="font-bold text-black">2% risk factor</span> over a <span class="font-bold text-black">20-year payback period</span>.')
    h.append('</div>\n')
    return '\n'.join(h)

def render_raw_material_cost():
    """Renders Section 8.3.2 Cost of Raw Material as a structured unit cost table."""
    h = []
    h.append('<div class="overflow-x-auto my-6 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white min-w-[650px]">')
    h.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left">Raw Material Item</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-center w-36">Required Qty / Unit</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-right w-36">Unit Rate (Tk.)</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-right w-36 bg-gray-200/70">Cost / Product (Tk.)</th>')
    h.append('    </tr></thead>')
    h.append('    <tbody>')
    
    items = [
        ("Mild Steel Sheet", "3 kg", "130/- per kg", "390/-"),
        ("Stainless Steel Sheet (4ft × 8ft × 1mm)", "1 sheet", "5,800/- per sheet", "5,800/-"),
        ("Nylon Brush Fiber (0.2 Nylon)", "6 units", "130/- per unit", "780/-")
    ]
    for r_idx, (name, qty, rate, cost) in enumerate(items):
        bg = "bg-gray-50/70" if r_idx % 2 == 1 else "bg-white"
        h.append(f'      <tr class="{bg} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
        h.append(f'        <td class="border border-black p-2 font-bold text-black">{name}</td>')
        h.append(f'        <td class="border border-black p-2 text-center text-gray-700">{qty}</td>')
        h.append(f'        <td class="border border-black p-2 text-right text-gray-700">{rate}</td>')
        h.append(f'        <td class="border border-black p-2 text-right font-bold text-black bg-gray-50/40">{cost}</td>')
        h.append('      </tr>')
        
    h.append('      <tr class="bg-gray-100 font-bold border-t-2 border-black">')
    h.append('        <td colspan="3" class="border border-black p-2.5 text-right uppercase tracking-wider text-black">Total Raw Material Cost per Product</td>')
    h.append('        <td class="border border-black p-2.5 text-right font-bold text-sm bg-yellow-100/80 text-black">6,970/-</td>')
    h.append('      </tr>')
    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    
    h.append('<div class="my-4 p-4 bg-gray-50 border border-gray-300 font-mono text-xs rounded-xs flex flex-col sm:flex-row justify-between items-center gap-3">')
    h.append('  <span><strong>Total Annual Raw Material Cost</strong> (for 565 units planned output):</span>')
    h.append('  <span class="text-base font-bold bg-black text-white px-3 py-1">39,38,050/- Tk.</span>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_labor_cost():
    """Renders Section 8.3.3 Cost of Labor as a clean monthly/yearly salary breakdown table."""
    h = []
    h.append('<div class="overflow-x-auto my-6 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white min-w-[650px]">')
    h.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left">Worker Role / Designation</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-center w-24">Headcount</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-right w-36">Monthly Wage / Person</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-right w-36 bg-gray-200/70">Total Monthly Cost</th>')
    h.append('    </tr></thead>')
    h.append('    <tbody>')
    
    roles = [
        ("Lathe Operator", "2", "22,500/-", "45,000/-"),
        ("Drilling & Cutting Operator", "2", "10,000/-", "20,000/-"),
        ("Welding Operator", "2", "11,000/-", "22,000/-"),
        ("Assembly Staff", "4", "9,000/-", "36,000/-"),
        ("Floor & Facility Cleaning Staff", "2", "7,000/-", "14,000/-"),
        ("Miscellaneous (15% Festival Bonus + 6% Performance Incentive)", "—", "Pooled (approx.)", "40,000/-")
    ]
    for r_idx, (role, count, wage, tot) in enumerate(roles):
        bg = "bg-gray-50/70" if r_idx % 2 == 1 else "bg-white"
        h.append(f'      <tr class="{bg} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
        h.append(f'        <td class="border border-black p-2 font-bold text-black">{role}</td>')
        h.append(f'        <td class="border border-black p-2 text-center text-gray-700 font-semibold">{count}</td>')
        h.append(f'        <td class="border border-black p-2 text-right text-gray-700">{wage}</td>')
        h.append(f'        <td class="border border-black p-2 text-right font-bold text-black bg-gray-50/40">{tot}</td>')
        h.append('      </tr>')
        
    h.append('      <tr class="bg-gray-100 font-bold border-t border-black">')
    h.append('        <td colspan="3" class="border border-black p-2 text-right uppercase tracking-wider text-black">Total Cost of Labor per Month</td>')
    h.append('        <td class="border border-black p-2 text-right font-bold text-black">1,77,000/- Tk.</td>')
    h.append('      </tr>')
    h.append('      <tr class="bg-gray-200 font-bold border-t-2 border-black">')
    h.append('        <td colspan="3" class="border border-black p-2.5 text-right uppercase tracking-wider text-black">Total Annual Labor Cost (12 Months)</td>')
    h.append('        <td class="border border-black p-2.5 text-right font-bold text-sm bg-yellow-100/80 text-black">21,24,000/- Tk.</td>')
    h.append('      </tr>')
    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_external_parts_table():
    """Table 8.1: Fully merged Purchasing Cost per Unit of Product (External Parts) across Pages 129 and 130."""
    h = []
    h.append('<div class="font-mono text-xs uppercase font-bold tracking-wider mt-8 mb-2 text-black flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>Table 8. 1: Purchasing Cost per Unit (External Parts)</div>\n')
    h.append('<div class="overflow-x-auto my-6 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white min-w-[650px]">')
    h.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left">Purchased Part</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-right w-36">Price per Unit (Tk.)</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-center w-24">Quantity</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-right w-36 bg-gray-200/70">Total Cost (Tk.)</th>')
    h.append('    </tr></thead>')
    h.append('    <tbody>')

    parts = [
        ("Spur Gear", "250", "10", "2,500"),
        ("Worm Gear", "1,270", "4", "5,080"),
        ("AC to DC Converter", "645", "1", "645"),
        ("Nut & Bolt Set", "25", "20", "500"),
        ("Ball Bearing", "99", "20", "1,980"),
        ("DC Motor (1 HP)", "4,829", "2", "9,658"),
        ("Solid Shoe Shiner", "3,000", "1", "3,000")
    ]
    for r_idx, (part, price, qty, total) in enumerate(parts):
        bg = "bg-gray-50/70" if r_idx % 2 == 1 else "bg-white"
        h.append(f'      <tr class="{bg} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
        h.append(f'        <td class="border border-black p-2 font-bold text-black">{part}</td>')
        h.append(f'        <td class="border border-black p-2 text-right text-gray-700">{price}/-</td>')
        h.append(f'        <td class="border border-black p-2 text-center text-gray-700 font-semibold">{qty}</td>')
        h.append(f'        <td class="border border-black p-2 text-right font-bold text-black bg-gray-50/40">{total}/-</td>')
        h.append('      </tr>')

    # Total row
    h.append('      <tr class="bg-gray-100 font-bold border-t-2 border-black">')
    h.append('        <td colspan="3" class="border border-black p-2.5 text-right uppercase tracking-wider text-black">Total Purchasing Cost per Unit Product</td>')
    h.append('        <td class="border border-black p-2.5 text-right font-bold text-sm bg-yellow-100/80 text-black">23,363/- Tk.</td>')
    h.append('      </tr>')
    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')

    h.append('<div class="my-4 p-4 bg-gray-50 border border-gray-300 font-mono text-xs rounded-xs flex flex-col sm:flex-row justify-between items-center gap-3">')
    h.append('  <span><strong>Total Annual External Purchasing Cost</strong> (for 565 units planned output):</span>')
    h.append('  <span class="text-base font-bold bg-black text-white px-3 py-1">1,32,00,095/- Tk.</span>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_overhead_cost_table():
    """Table 8.2: Manufacturing Overhead Cost Table on Page 130."""
    h = []
    h.append('<div class="font-mono text-xs uppercase font-bold tracking-wider mt-8 mb-2 text-black flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>Table 8. 2: Manufacturing Overhead Cost</div>\n')
    h.append('<div class="overflow-x-auto my-6 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white min-w-[650px]">')
    h.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left">Cost Item</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-center w-24">No. of Posts</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-right w-36">Monthly Salary / Rate</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-right w-36 bg-gray-200/70">Monthly Cost (Tk.)</th>')
    h.append('    </tr></thead>')
    h.append('    <tbody>')

    items = [
        ("Production Manager", "1", "30,000/-", "30,000/-"),
        ("Manufacturing Engineer", "1", "25,000/-", "25,000/-"),
        ("Quality Control Manager", "1", "20,000/-", "20,000/-"),
        ("Power & Industrial Electricity Consumption", "—", "Variable utility", "15,000/-"),
        ("Factory Facility Rent", "—", "Fixed lease", "25,000/-")
    ]
    for r_idx, (item, posts, rate, cost) in enumerate(items):
        bg = "bg-gray-50/70" if r_idx % 2 == 1 else "bg-white"
        h.append(f'      <tr class="{bg} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
        h.append(f'        <td class="border border-black p-2 font-bold text-black">{item}</td>')
        h.append(f'        <td class="border border-black p-2 text-center text-gray-700 font-semibold">{posts}</td>')
        h.append(f'        <td class="border border-black p-2 text-right text-gray-700">{rate}</td>')
        h.append(f'        <td class="border border-black p-2 text-right font-bold text-black bg-gray-50/40">{cost}</td>')
        h.append('      </tr>')

    h.append('      <tr class="bg-gray-100 font-bold border-t border-black">')
    h.append('        <td colspan="3" class="border border-black p-2 text-right uppercase tracking-wider text-black">Total Overhead per Month</td>')
    h.append('        <td class="border border-black p-2 text-right font-bold text-black">1,15,000/- Tk.</td>')
    h.append('      </tr>')
    h.append('      <tr class="bg-gray-200 font-bold border-t-2 border-black">')
    h.append('        <td colspan="3" class="border border-black p-2.5 text-right uppercase tracking-wider text-black">Total Annual Manufacturing Overhead (12 Months)</td>')
    h.append('        <td class="border border-black p-2.5 text-right font-bold text-sm bg-yellow-100/80 text-black">13,80,000/- Tk.</td>')
    h.append('      </tr>')
    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_total_manufacturing_cost_table():
    """Table 8.3: Total Manufacturing Cost Table on Page 131."""
    h = []
    h.append('<div class="font-mono text-xs uppercase font-bold tracking-wider mt-8 mb-2 text-black flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>Table 8. 3: Total Manufacturing Cost</div>\n')
    h.append('<div class="overflow-x-auto my-6 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white min-w-[500px]">')
    h.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left">Cost Component</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-right w-48 bg-gray-200/70">Annual Amount (Tk.)</th>')
    h.append('    </tr></thead>')
    h.append('    <tbody>')

    items = [
        ("Cost of Raw Material", "39,38,050"),
        ("Cost of Purchasing (External Parts)", "1,32,00,095"),
        ("Cost of Direct Labor", "21,24,000"),
        ("Manufacturing Overhead", "13,80,000")
    ]
    for r_idx, (comp, amt) in enumerate(items):
        bg = "bg-gray-50/70" if r_idx % 2 == 1 else "bg-white"
        h.append(f'      <tr class="{bg} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
        h.append(f'        <td class="border border-black p-2 font-bold text-black">{comp}</td>')
        h.append(f'        <td class="border border-black p-2 text-right font-medium text-gray-800">{amt}/-</td>')
        h.append('      </tr>')

    h.append('      <tr class="bg-gray-200 font-bold border-t-2 border-black">')
    h.append('        <td class="border border-black p-2.5 text-right uppercase tracking-wider text-black">Total Manufacturing Cost (TVC)</td>')
    h.append('        <td class="border border-black p-2.5 text-right font-bold text-base bg-yellow-100/80 text-black">2,06,42,145/- Tk.</td>')
    h.append('      </tr>')
    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_admin_cost_table():
    """Table 8.4: Administrative Cost of Personnel per Month on Page 131."""
    h = []
    h.append('<div class="font-mono text-xs uppercase font-bold tracking-wider mt-8 mb-2 text-black flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>Table 8. 4: Administrative Cost of Personnel (per Month)</div>\n')
    h.append('<div class="overflow-x-auto my-6 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white min-w-[650px]">')
    h.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left">Administrative Role</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-center w-24">No. of Posts</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-right w-36">Monthly Salary / Person</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-right w-36 bg-gray-200/70">Monthly Cost (Tk.)</th>')
    h.append('    </tr></thead>')
    h.append('    <tbody>')

    staff = [
        ("Chief Executive Officer (CEO)", "1", "60,000/-", "60,000/-"),
        ("Chief Financial Officer (CFO)", "1", "50,000/-", "50,000/-"),
        ("Chief Marketing Officer (CMO)", "1", "40,000/-", "40,000/-"),
        ("Product Development Officer", "1", "25,000/-", "25,000/-"),
        ("Administrative Clerk", "1", "10,000/-", "10,000/-")
    ]
    for r_idx, (role, posts, salary, cost) in enumerate(staff):
        bg = "bg-gray-50/70" if r_idx % 2 == 1 else "bg-white"
        h.append(f'      <tr class="{bg} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
        h.append(f'        <td class="border border-black p-2 font-bold text-black">{role}</td>')
        h.append(f'        <td class="border border-black p-2 text-center text-gray-700 font-semibold">{posts}</td>')
        h.append(f'        <td class="border border-black p-2 text-right text-gray-700">{salary}</td>')
        h.append(f'        <td class="border border-black p-2 text-right font-bold text-black bg-gray-50/40">{cost}</td>')
        h.append('      </tr>')

    h.append('      <tr class="bg-gray-100 font-bold border-t border-black">')
    h.append('        <td colspan="3" class="border border-black p-2 text-right uppercase tracking-wider text-black">Total Administrative Salary per Month</td>')
    h.append('        <td class="border border-black p-2 text-right font-bold text-black">1,85,000/- Tk.</td>')
    h.append('      </tr>')
    h.append('      <tr class="bg-gray-200 font-bold border-t-2 border-black">')
    h.append('        <td colspan="3" class="border border-black p-2.5 text-right uppercase tracking-wider text-black">Total Annual Administrative Cost (12 Months)</td>')
    h.append('        <td class="border border-black p-2.5 text-right font-bold text-sm bg-yellow-100/80 text-black">22,20,000/- Tk.</td>')
    h.append('      </tr>')
    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_total_non_manufacturing_table():
    """Table 8.5: Total Non-Manufacturing Cost (per year) on Page 132."""
    h = []
    h.append('<div class="font-mono text-xs uppercase font-bold tracking-wider mt-8 mb-2 text-black flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>Table 8. 5: Total Non-Manufacturing Cost (per Year)</div>\n')
    h.append('<div class="overflow-x-auto my-6 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white min-w-[500px]">')
    h.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left">Expense Category</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-right w-48 bg-gray-200/70">Annual Cost (Tk.)</th>')
    h.append('    </tr></thead>')
    h.append('    <tbody>')

    items = [
        ("Administration", "22,20,000"),
        ("Office Rent", "2,00,000"),
        ("Sales & Marketing", "3,00,000"),
        ("Bank Loan (Annuity Repayment)", "3,01,972"),
        ("Advancement for Factory Space", "2,00,000"),
        ("Municipal Taxes", "60,000"),
        ("Insurances", "80,000"),
        ("Commercial Utilities", "77,551")
    ]
    for r_idx, (cat, amt) in enumerate(items):
        bg = "bg-gray-50/70" if r_idx % 2 == 1 else "bg-white"
        h.append(f'      <tr class="{bg} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
        h.append(f'        <td class="border border-black p-2 font-bold text-black">{cat}</td>')
        h.append(f'        <td class="border border-black p-2 text-right font-medium text-gray-800">{amt}/-</td>')
        h.append('      </tr>')

    h.append('      <tr class="bg-gray-200 font-bold border-t-2 border-black">')
    h.append('        <td class="border border-black p-2.5 text-right uppercase tracking-wider text-black">Total Non-Manufacturing Cost (TFC)</td>')
    h.append('        <td class="border border-black p-2.5 text-right font-bold text-base bg-yellow-100/80 text-black">34,39,523/- Tk.</td>')
    h.append('      </tr>')
    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_total_yearly_cost_table():
    """Table 8.6: Total Yearly Cost on Page 133."""
    h = []
    h.append('<div class="font-mono text-xs uppercase font-bold tracking-wider mt-8 mb-2 text-black flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>Table 8. 6: Total Yearly Cost</div>\n')
    h.append('<div class="overflow-x-auto my-6 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white min-w-[500px]">')
    h.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left">Cost Classification</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-right w-48 bg-gray-200/70">Total Amount (Tk.)</th>')
    h.append('    </tr></thead>')
    h.append('    <tbody>')

    items = [
        ("Manufacturing Cost (Variable Cost, TVC)", "2,06,42,145"),
        ("Non-Manufacturing Cost (Fixed Cost, TFC)", "34,39,523")
    ]
    for r_idx, (cat, amt) in enumerate(items):
        bg = "bg-gray-50/70" if r_idx % 2 == 1 else "bg-white"
        h.append(f'      <tr class="{bg} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
        h.append(f'        <td class="border border-black p-2 font-bold text-black">{cat}</td>')
        h.append(f'        <td class="border border-black p-2 text-right font-medium text-gray-800">{amt}/-</td>')
        h.append('      </tr>')

    h.append('      <tr class="bg-gray-200 font-bold border-t-2 border-black">')
    h.append('        <td class="border border-black p-2.5 text-right uppercase tracking-wider text-black">Total Comprehensive Annual Cost</td>')
    h.append('        <td class="border border-black p-2.5 text-right font-bold text-base bg-yellow-100/80 text-black">2,40,81,668/- Tk.</td>')
    h.append('      </tr>')
    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_direct_material_cost_table():
    """Table 8.7: Direct Material Cost on Page 135."""
    h = []
    h.append('<div class="font-mono text-xs uppercase font-bold tracking-wider mt-8 mb-2 text-black flex items-center gap-2"><span class="w-2.5 h-2.5 bg-black inline-block"></span>Table 8. 7: Direct Material Cost</div>\n')
    h.append('<div class="overflow-x-auto my-6 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white min-w-[500px]">')
    h.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left">Material Cost Component</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-right w-48 bg-gray-200/70">Annual Amount (Tk.)</th>')
    h.append('    </tr></thead>')
    h.append('    <tbody>')

    items = [
        ("Cost of Raw Material", "39,38,050"),
        ("Cost of Purchasing (External Parts)", "1,32,00,095")
    ]
    for r_idx, (comp, amt) in enumerate(items):
        bg = "bg-gray-50/70" if r_idx % 2 == 1 else "bg-white"
        h.append(f'      <tr class="{bg} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
        h.append(f'        <td class="border border-black p-2 font-bold text-black">{comp}</td>')
        h.append(f'        <td class="border border-black p-2 text-right font-medium text-gray-800">{amt}/-</td>')
        h.append('      </tr>')

    h.append('      <tr class="bg-gray-200 font-bold border-t-2 border-black">')
    h.append('        <td class="border border-black p-2.5 text-right uppercase tracking-wider text-black">Total Direct Material Cost</td>')
    h.append('        <td class="border border-black p-2.5 text-right font-bold text-base bg-yellow-100/80 text-black">1,71,38,145/- Tk.</td>')
    h.append('      </tr>')
    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    return '\n'.join(h)

def render_sensitivity_summary_table():
    """Renders the final Sensitivity Summary Comparison Table with progress indicators."""
    h = []
    h.append('<div class="overflow-x-auto my-6 border border-black shadow-xs bg-white rounded-xs">')
    h.append('  <table class="w-full border-collapse border border-black font-mono text-xs text-left bg-white min-w-[650px]">')
    h.append('    <thead><tr class="bg-gray-100 text-black border-b border-black">')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left w-48">Parameter Evaluated</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-center w-28">Parameter Shift</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-center w-28">New $Q_{BEP}$</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-right w-32 bg-gray-200/70">Sensitivity ($\\Delta Q_{BEP}$)</th>')
    h.append('      <th class="border border-black p-2.5 font-bold uppercase text-left w-40">Impact Classification</th>')
    h.append('    </tr></thead>')
    h.append('    <tbody>')

    data = [
        ("Direct Material Cost", "+10%", "283 units", "25.22%", "bg-red-500", "Critical (Highest Impact)"),
        ("Administrative Fixed Cost", "+10%", "241 units", "6.64%", "bg-yellow-500", "Moderate Sensitivity"),
        ("Direct Labor Cost", "+10%", "232 units", "2.65%", "bg-blue-400", "Low Sensitivity"),
        ("Selling / Marketing Expenses", "+10%", "228 units", "0.88%", "bg-gray-400", "Minimal Sensitivity"),
        ("Market Demand Volume", "+10%", "226 units", "0.00%", "bg-gray-300", "No Impact on $Q_{BEP}$")
    ]
    for r_idx, (param, shift, new_q, sens, color_cls, impact) in enumerate(data):
        bg = "bg-gray-50/70" if r_idx % 2 == 1 else "bg-white"
        h.append(f'      <tr class="{bg} border-b border-gray-300 hover:bg-yellow-50/40 transition-colors">')
        h.append(f'        <td class="border border-black p-2.5 font-bold text-black">{param}</td>')
        h.append(f'        <td class="border border-black p-2 text-center text-gray-700 font-semibold">{shift}</td>')
        h.append(f'        <td class="border border-black p-2 text-center font-bold text-black">{new_q}</td>')
        h.append(f'        <td class="border border-black p-2 text-right font-bold text-sm text-black bg-gray-50/50">{sens}</td>')
        h.append(f'        <td class="border border-black p-2 text-xs font-semibold text-gray-800 flex items-center gap-2"><span class="w-2.5 h-2.5 rounded-full {color_cls} inline-block"></span>{impact}</td>')
        h.append('      </tr>')

    h.append('    </tbody>')
    h.append('  </table>')
    h.append('</div>\n')
    return '\n'.join(h)

def get_ch8_page_html(pdf_page):
    """
    Returns custom clean HTML for Chapter 8 pages (PDF Pages 126 to 138):
    - 126: Chapter 08 Header, 8.1 Introduction, 8.2 Demand Forecasting, 8.2.1-8.2.3
    - 127: 8.2.4 Formula & Calculations, 8.2.5 Scenario Analysis, 8.3 Manufacturing Cost overview
    - 128: 8.3.1 Machinery Specification Table, 8.3.2 Raw Material Costs
    - 129: Raw Material Totals, 8.3.3 Labor Costs Table, 8.3.4 External Parts (Unified Table 8.1)
    - 130: Page marker & continuation notice, 8.3.5 Manufacturing Overhead (Table 8.2)
    - 131: 8.3.6 Total Manufacturing Cost (Table 8.3), 8.4 Non-Manufacturing, 8.4.1 Admin (Table 8.4)
    - 132: 8.4.2 Sales & Marketing, 8.4.3 Bank Loan & Annuity, Table 8.5 Total Non-Manufacturing Cost
    - 133: 8.5 Total Yearly Cost (Table 8.6), 8.6 Break-Even Analysis Derivation
    - 134: Figure 8.1 Break-Even Analysis Chart (cleaned of OCR vector noise), 8.7 Sensitivity Intro, 8.7.1 Demand
    - 135: Demand conclusion, 8.7.2 Direct Material (Table 8.7 & Derivation), 8.7.3 Labor intro
    - 136: Labor derivation, 8.7.4 Admin derivation, 8.7.5 Selling expenses intro
    - 137: Selling expenses derivation, Sensitivity Summary Matrix Table, 8.8 Conclusion
    - 138: Page 138 Marker & transition to Chapter 09
    """
    h = []

    # --- PDF Page 126 (Report Page 106) ---
    if pdf_page == 126:
        h.append('<div class="mt-14 mb-8 pt-6 border-t-2 border-black" id="ch-08">')
        h.append('  <span class="text-xs uppercase font-mono tracking-widest bg-black text-white px-2.5 py-1 inline-block mb-3">Chapter 08</span>')
        h.append('  <h2 class="text-2xl md:text-4xl font-bold font-mono tracking-tight text-black">Cost &amp; Sensitivity Analysis</h2>')
        h.append('</div>\n')

        h.append('<h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mt-10 mb-4" id="sec-8-1"><span class="text-gray-400 mr-2">8.1</span>Introduction</h3>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Cost is deeply intertwined with product design, as design decisions significantly impact overall expenses. The primary factors shaping a product\'s economic viability are cost and revenue, with the aim of minimizing costs while maximizing profits. Conducting a cost analysis highlights a product\'s capacity to generate the desired output while remaining profitable. It also helps evaluate whether the product can reach its break-even point effectively.</p>\n')

        h.append('<h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mt-10 mb-4" id="sec-8-2"><span class="text-gray-400 mr-2">8.2</span>Forecasting Demand</h3>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4"><strong>Methodology: Proportional Scaling Approach.</strong> We utilized the Proportional Scaling Approach to forecast the one-year demand for the proposed product. This method is based on survey results and assumes that the sample accurately represents the target population. The steps of the methodology are outlined below:</p>\n')

        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-2-1"><span class="text-gray-400 mr-2">8.2.1</span>Target Population Identification</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">The total number of potential adopters for the product was identified as <strong>2,941 institutions</strong> in the target urban zone, comprising 245 Hotels, 324 Schools and Colleges, 136 Hospitals, 115 Private Universities, 1,200 Private Bank Branches, and 921 Corporate Commercial Offices.</p>\n')

        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-2-2"><span class="text-gray-400 mr-2">8.2.2</span>Survey Implementation</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">A survey was conducted among 35 individuals from corresponding institutions, which served as a representative sample of the target population. The survey revealed that <strong>80% of the respondents (28 out of 35)</strong> expressed definitive interest in adopting the product.</p>\n')

        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-2-3"><span class="text-gray-400 mr-2">8.2.3</span>Adoption Rate Calculation</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">The adoption rate was calculated using the following formulation:</p>\n')
        h.append('<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">')
        h.append(r'$$\text{Adoption Rate} = \frac{\text{Number of Positive Responses}}{\text{Total Number of Surveyed Institutions}} = \frac{28}{35} = 0.80 \text{ (80\%)}$$')
        h.append('</div>\n')
        return '\n'.join(h)

    # --- PDF Page 127 (Report Page 107) ---
    if pdf_page == 127:
        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-2-4"><span class="text-gray-400 mr-2">8.2.4</span>Demand Forecasting</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">The adoption rate was scaled up to the entire target population to estimate the total demand. The formula used was:</p>\n')
        h.append('<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">')
        h.append(r'$$\text{Forecasted Demand} = \text{Total Population} \times \text{Adoption Rate} = 2941 \times 0.80 = 2353 \text{ units}$$')
        h.append('</div>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Hence, the estimated one-year gross demand for the product is <strong>2,353 units</strong>.</p>\n')

        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-2-5"><span class="text-gray-400 mr-2">8.2.5</span>Scenario Analysis</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">To address potential variations in market conditions, sensitivity analysis was performed using different adoption scenarios:</p>\n')
        
        # 3 Scenarios Grid
        h.append('<div class="grid grid-cols-1 sm:grid-cols-3 gap-4 my-6">')
        h.append('  <div class="border border-black p-4 bg-white shadow-2xs rounded-xs">')
        h.append('    <span class="text-[10px] font-mono uppercase bg-black text-white px-2 py-0.5 inline-block font-bold mb-2">Optimistic (90%)</span>')
        h.append('    <div class="text-2xl font-bold font-mono text-black">2,118 <span class="text-xs font-normal text-gray-600">units</span></div>')
        h.append('    <div class="text-xs font-mono text-gray-500 mt-1">2353 × 0.90</div>')
        h.append('  </div>')
        h.append('  <div class="border-2 border-black p-4 bg-yellow-50/50 shadow-xs rounded-xs">')
        h.append('    <span class="text-[10px] font-mono uppercase bg-yellow-400 text-black px-2 py-0.5 inline-block font-bold mb-2">Realistic (80%)</span>')
        h.append('    <div class="text-2xl font-bold font-mono text-black">1,882 <span class="text-xs font-normal text-gray-600">units</span></div>')
        h.append('    <div class="text-xs font-mono text-gray-500 mt-1">2353 × 0.80</div>')
        h.append('  </div>')
        h.append('  <div class="border border-black p-4 bg-white shadow-2xs rounded-xs">')
        h.append('    <span class="text-[10px] font-mono uppercase bg-gray-200 text-gray-800 px-2 py-0.5 inline-block font-bold mb-2">Pessimistic (70%)</span>')
        h.append('    <div class="text-2xl font-bold font-mono text-black">1,647 <span class="text-xs font-normal text-gray-600">units</span></div>')
        h.append('    <div class="text-xs font-mono text-gray-500 mt-1">2353 × 0.70</div>')
        h.append('  </div>')
        h.append('</div>\n')

        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">In conclusion, the Proportional Scaling Approach offers a straightforward and effective means of forecasting demand using survey data. The projected realistic demand for the product in its first year is <strong>1,882 units</strong>.</p>\n')

        h.append('<h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mt-10 mb-4" id="sec-8-3"><span class="text-gray-400 mr-2">8.3</span>Manufacturing Cost</h3>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Manufacturing cost is the cost of production directly incurred during the manufacturing process. It comprises direct labor, direct material, and manufacturing overhead costs. With a projected realistic annual demand of 1,882 units, our production strategy targets capturing approximately <strong>30% market share</strong> during Year 1, establishing an annual planned sales and production volume of <strong>565 units</strong>.</p>\n')
        return '\n'.join(h)

    # --- PDF Page 128 (Report Page 108) ---
    if pdf_page == 128:
        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-3-1"><span class="text-gray-400 mr-2">8.3.1</span>Cost of Machinery</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">To manufacture the structural and mechanical elements of the machine, specific workshop equipment must be acquired:</p>\n')
        h.append(render_machinery_cost())

        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-3-2"><span class="text-gray-400 mr-2">8.3.2</span>Cost of Raw Material (per unit of product)</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Direct raw material consumption per single unit of the semi-automated shoe cleaning machine:</p>\n')
        h.append(render_raw_material_cost())
        return '\n'.join(h)

    # --- PDF Page 129 (Report Page 109) ---
    if pdf_page == 129:
        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-3-3"><span class="text-gray-400 mr-2">8.3.3</span>Cost of Labor</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Monthly and annual compensation for dedicated workshop operators and assembly technicians:</p>\n')
        h.append(render_labor_cost())

        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-3-4"><span class="text-gray-400 mr-2">8.3.4</span>Purchasing Cost per Unit of Product (External Parts)</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Off-the-shelf and outsourced electromechanical parts required per machine unit:</p>\n')
        h.append(render_external_parts_table())
        return '\n'.join(h)

    # --- PDF Page 130 (Report Page 110) ---
    if pdf_page == 130:
        h.append('<div class="p-3 bg-gray-50/80 border-l-2 border-black my-4 text-xs font-mono text-gray-600 flex items-center justify-between rounded-xs">')
        h.append('  <span>↳ <strong class="text-black">Table 8.1: External Purchasing Cost</strong> (unified on Report Page 109 above)</span>')
        h.append('  <a href="#sec-8-3-4" class="text-black font-bold hover:underline shrink-0 ml-4">↑ View Table 8.1</a>')
        h.append('</div>\n')

        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-3-5"><span class="text-gray-400 mr-2">8.3.5</span>Manufacturing Overhead Cost</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Indirect production expenses including technical supervisory personnel, utility consumption, and facility rental:</p>\n')
        h.append(render_overhead_cost_table())
        return '\n'.join(h)

    # --- PDF Page 131 (Report Page 111) ---
    if pdf_page == 131:
        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-3-6"><span class="text-gray-400 mr-2">8.3.6</span>Total Manufacturing Cost</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Aggregated direct and indirect manufacturing expenditures for the annual planned volume (565 units):</p>\n')
        h.append(render_total_manufacturing_cost_table())

        h.append('<h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mt-10 mb-4" id="sec-8-4"><span class="text-gray-400 mr-2">8.4</span>Non-Manufacturing Cost</h3>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Non-manufacturing costs encompass expenses not directly tied to shop-floor fabrication but indispensable for administrative governance, sales channels, logistics, and executive operations across the product lifecycle.</p>\n')

        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-4-1"><span class="text-gray-400 mr-2">8.4.1</span>Administrative Cost</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Monthly compensation and headcount for executive leadership and office personnel:</p>\n')
        h.append(render_admin_cost_table())
        return '\n'.join(h)

    # --- PDF Page 132 (Report Page 112) ---
    if pdf_page == 132:
        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-4-2"><span class="text-gray-400 mr-2">8.4.2</span>Sales &amp; Marketing Expense</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Commercialization and outreach budget for enterprise market penetration:</p>\n')
        h.append('<div class="grid grid-cols-1 sm:grid-cols-2 gap-4 my-4 font-mono text-xs">')
        h.append('  <div class="border border-black p-3 bg-white">')
        h.append('    <span class="font-bold block text-black mb-1">1. Marketing Manager</span>')
        h.append('    <span>Headcount: 1 Employee</span><br>')
        h.append('    <span>Monthly Salary: 20,000/- Tk.</span><br>')
        h.append('    <span class="font-bold text-black">Annual Salary: 2,40,000/- Tk.</span>')
        h.append('  </div>')
        h.append('  <div class="border border-black p-3 bg-white">')
        h.append('    <span class="font-bold block text-black mb-1">2. Advertising &amp; Campaigns</span>')
        h.append('    <span>Promotional materials, demonstrations &amp; outreach</span><br>')
        h.append('    <span class="font-bold text-black mt-2 block">Annual Budget: 60,000/- Tk.</span>')
        h.append('  </div>')
        h.append('</div>')
        h.append('<div class="p-3 bg-gray-50 border border-gray-300 font-mono text-xs flex justify-between items-center mb-6">')
        h.append('  <span>Total Annual Sales &amp; Marketing Cost:</span>')
        h.append('  <span class="font-bold text-black text-sm">3,00,000/- Tk.</span>')
        h.append('</div>\n')

        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-4-3"><span class="text-gray-400 mr-2">8.4.3</span>Bank Loan &amp; Interest</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Debt financing structure for startup capital expenditure:</p>\n')
        h.append('<div class="grid grid-cols-2 sm:grid-cols-4 gap-3 my-4 font-mono text-xs text-center">')
        h.append('  <div class="border border-black p-2.5 bg-white"><span class="text-gray-500 block text-[10px]">Total Loan</span><span class="font-bold text-sm">20,00,000/-</span></div>')
        h.append('  <div class="border border-black p-2.5 bg-white"><span class="text-gray-500 block text-[10px]">Interest Rate (i)</span><span class="font-bold text-sm">14%</span></div>')
        h.append('  <div class="border border-black p-2.5 bg-white"><span class="text-gray-500 block text-[10px]">Period (n)</span><span class="font-bold text-sm">20 Years</span></div>')
        h.append('  <div class="border border-black p-2.5 bg-yellow-50"><span class="text-gray-500 block text-[10px]">Annual Annuity (A)</span><span class="font-bold text-sm text-black">3,01,972/-</span></div>')
        h.append('</div>\n')

        h.append(render_total_non_manufacturing_table())
        return '\n'.join(h)

    # --- PDF Page 133 (Report Page 113) ---
    if pdf_page == 133:
        h.append('<h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mt-10 mb-4" id="sec-8-5"><span class="text-gray-400 mr-2">8.5</span>Total Cost</h3>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Comprehensive annual operational and production budget summary:</p>\n')
        h.append(render_total_yearly_cost_table())

        h.append('<h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mt-10 mb-4" id="sec-8-6"><span class="text-gray-400 mr-2">8.6</span>Break-Even Analysis</h3>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">The break-even point establishes the volume of production at which total revenues precisely match total fixed and variable costs.</p>\n')

        # BEP Key Metrics Cards
        h.append('<div class="grid grid-cols-2 sm:grid-cols-4 gap-3 my-4 font-mono text-xs">')
        h.append('  <div class="border border-black p-3 bg-white"><span class="text-gray-500 block text-[10px] uppercase">Fixed Cost (TFC)</span><span class="font-bold text-sm text-black">34,39,523/-</span><span class="block text-[10px] text-gray-400">6,087.65/- / unit</span></div>')
        h.append('  <div class="border border-black p-3 bg-white"><span class="text-gray-500 block text-[10px] uppercase">Variable Cost (TVC)</span><span class="font-bold text-sm text-black">2,06,42,145/-</span><span class="block text-[10px] text-gray-400">36,534.77/- / unit</span></div>')
        h.append('  <div class="border border-black p-3 bg-white"><span class="text-gray-500 block text-[10px] uppercase">Target Margin (25%)</span><span class="font-bold text-sm text-black">9,133.69/-</span><span class="block text-[10px] text-gray-400">profit / unit</span></div>')
        h.append('  <div class="border-2 border-black p-3 bg-yellow-50"><span class="text-gray-500 block text-[10px] uppercase font-bold">Selling Price (P)</span><span class="font-bold text-base text-black">51,756/-</span><span class="block text-[10px] text-gray-600">per unit</span></div>')
        h.append('</div>\n')

        # Equilibrium Formula
        h.append('<div class="math-block my-5 p-5 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">')
        h.append('  <span class="block font-mono text-xs text-gray-500 font-bold mb-2 uppercase tracking-wider">Equilibrium Formulation at Break-Even Point</span>')
        h.append(r'$$\text{Selling Price} \times Q_{BEP} = \text{Total Fixed Cost} + (\text{Variable Cost per unit} \times Q_{BEP})$$')
        h.append(r'$$51,756 \times Q_{BEP} = 3,439,523 + (36,534.77 \times Q_{BEP})$$')
        h.append(r'$$15,221.23 \times Q_{BEP} = 3,439,523 \implies Q_{BEP} = 226 \text{ units}$$')
        h.append('</div>\n')

        h.append('<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">')
        h.append('  <span class="block font-mono text-xs text-gray-500 font-bold mb-1 uppercase tracking-wider">Break-Even Payback Period</span>')
        h.append(r'$$\text{Break-Even Period} = \frac{226}{565} \times 1 \text{ year} = 0.40 \text{ years} \approx 4.8 \text{ months}$$')
        h.append('</div>\n')
        return '\n'.join(h)

    # --- PDF Page 134 (Report Page 114) ---
    if pdf_page == 134:
        # High-res Break-Even Chart without any OCR text noise
        h.append('<figure class="my-8 max-w-3xl mx-auto border-2 border-black p-5 bg-white shadow-sm hover:border-black transition-colors rounded-xs">')
        h.append('  <div class="flex justify-center p-2 bg-white">')
        h.append('    <img src="/assets/images/pd-report/figure_8_1_break_even_chart.png" alt="Figure 8. 1: Break-Even Analysis Chart" class="max-h-[420px] w-auto object-contain rounded-xs" loading="lazy" />')
        h.append('  </div>')
        h.append('  <figcaption class="text-center font-mono text-xs text-black font-bold border-t border-black pt-3 mt-3">Figure 8. 1: Break-Even Analysis Chart</figcaption>')
        h.append('  <div class="mt-3 flex flex-wrap justify-center gap-4 text-xs font-mono text-gray-600 bg-gray-50 p-2.5 rounded-xs border border-gray-200">')
        h.append('    <span><strong>Break-Even Quantity:</strong> <span class="text-black font-bold">226 units</span></span>')
        h.append('    <span>&bull;</span>')
        h.append('    <span><strong>Break-Even Horizon:</strong> <span class="text-black font-bold">0.4 years (4.8 months)</span></span>')
        h.append('    <span>&bull;</span>')
        h.append('    <span><strong>Target Sales Volume:</strong> <span class="text-black font-bold">565 units</span></span>')
        h.append('  </div>')
        h.append('</figure>\n')

        h.append('<h3 class="text-xl md:text-2xl font-bold font-mono tracking-tight mt-10 mb-4" id="sec-8-7"><span class="text-gray-400 mr-2">8.7</span>Sensitivity Analysis</h3>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Sensitivity analysis provides insight into how sensitive the break-even threshold ($Q_{BEP}$) is to individual variations in cost, revenue, and demand parameters. In this analysis, a separate <strong>10% adverse parameter shock</strong> is evaluated across each cost and operational driver to determine parameter vulnerability.</p>\n')

        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-7-1"><span class="text-gray-400 mr-2">8.7.1</span>Sensitivity of Demand</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Baseline planned production is 565 units per year. Under a 10% increase in market demand ($622$ units):</p>\n')
        h.append('<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">')
        h.append(r'$$\text{New Demand} = 565 \times 1.10 = 622 \text{ units}$$')
        h.append(r'$$51,756 \times Q_{BEP} = 3,439,523 + (36,534.77 \times Q_{BEP}) \implies Q_{BEP} = 226 \text{ units (No change)}$$')
        h.append(r'$$\Delta Q_{BEP} = 0.00\%$$')
        h.append('</div>\n')
        return '\n'.join(h)

    # --- PDF Page 135 (Report Page 115) ---
    if pdf_page == 135:
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Thus, sales demand volume does not alter the break-even quantity threshold itself; the break-even point is completely insensitive to demand changes.</p>\n')

        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-7-2"><span class="text-gray-400 mr-2">8.7.2</span>Sensitivity of Direct Material Cost</h4>\n')
        h.append(render_direct_material_cost_table())

        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Evaluating an adverse 10% surge in raw materials and purchased component costs:</p>\n')
        h.append('<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">')
        h.append(r'$$\text{New Direct Material Cost} = 17,138,145 \times 1.10 = 18,851,959.50 \text{ Tk.}$$')
        h.append(r'$$\text{New Variable Cost per unit} = 36,534.77 - \frac{17,138,145}{565} + \frac{18,851,959.50}{565} = 39,568.10 \text{ Tk.}$$')
        h.append(r'$$51,756 \times Q_{BEP} = 3,439,523 + (39,568.10 \times Q_{BEP}) \implies Q_{BEP} = 283 \text{ units}$$')
        h.append(r'$$\Delta Q_{BEP} = \frac{283 - 226}{226} \times 100\% = 25.22\%$$')
        h.append('</div>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4"><strong>Outcome:</strong> The break-even threshold is <em>critically sensitive</em> to direct material prices, requiring 57 additional units (+25.22%) to break even.</p>\n')

        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-7-3"><span class="text-gray-400 mr-2">8.7.3</span>Sensitivity of Direct Labor Cost</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Baseline annual labor expenditure is 21,24,000/- Tk. Subject to a 10% wage and bonus escalation:</p>\n')
        h.append('<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">')
        h.append(r'$$\text{New Labor Cost} = 2,124,000 \times 1.10 = 2,336,400 \text{ Tk.}$$')
        h.append(r'$$\text{New Variable Cost per unit} = \frac{20,642,145 + (2,336,400 - 2,124,000)}{565} = 36,910.70 \text{ Tk.}$$')
        h.append('</div>\n')
        return '\n'.join(h)

    # --- PDF Page 136 (Report Page 116) ---
    if pdf_page == 136:
        h.append('<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">')
        h.append(r'$$51,756 \times Q_{BEP} = 3,439,523 + (36,910.70 \times Q_{BEP}) \implies Q_{BEP} = 232 \text{ units}$$')
        h.append(r'$$\Delta Q_{BEP} = \frac{232 - 226}{226} \times 100\% = 2.65\%$$')
        h.append('</div>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4"><strong>Outcome:</strong> Break-even is moderately resilient to direct labor wage increases, causing only a 6-unit increase (+2.65%).</p>\n')

        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-7-4"><span class="text-gray-400 mr-2">8.7.4</span>Sensitivity of Administrative Fixed Cost</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Baseline annual administrative cost is 22,20,000/- Tk. Subject to a 10% administrative inflation shock:</p>\n')
        h.append('<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">')
        h.append(r'$$\text{New Administrative Cost} = 2,220,000 \times 1.10 = 2,442,000 \text{ Tk.}$$')
        h.append(r'$$\text{New Fixed Cost (TFC)} = 3,439,523 + (2,442,000 - 2,220,000) = 3,661,523 \text{ Tk.}$$')
        h.append(r'$$51,756 \times Q_{BEP} = 3,661,523 + (36,534.77 \times Q_{BEP}) \implies Q_{BEP} = 241 \text{ units}$$')
        h.append(r'$$\Delta Q_{BEP} = \frac{241 - 226}{226} \times 100\% = 6.64\%$$')
        h.append('</div>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4"><strong>Outcome:</strong> Administrative overhead exhibits a noticeable 15-unit (+6.64%) effect on break-even feasibility.</p>\n')

        h.append('<h4 class="text-lg font-bold font-mono mt-8 mb-3" id="sec-8-7-5"><span class="text-gray-400 mr-2">8.7.5</span>Sensitivity of Selling &amp; Marketing Expenses</h4>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">Baseline sales and promotion expense is 3,00,000/- Tk. With a 10% budget expansion:</p>\n')
        h.append('<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">')
        h.append(r'$$\text{New Selling Expense} = 300,000 \times 1.10 = 330,000 \text{ Tk.}$$')
        h.append(r'$$\text{New Fixed Cost (TFC)} = 3,439,523 + (330,000 - 300,000) = 3,469,523 \text{ Tk.}$$')
        h.append(r'$$51,756 \times Q_{BEP} = 3,469,523 + (36,534.77 \times Q_{BEP}) \implies Q_{BEP} = 228 \text{ units}$$')
        h.append('</div>\n')
        return '\n'.join(h)

    # --- PDF Page 137 (Report Page 117) ---
    if pdf_page == 137:
        h.append('<div class="math-block my-4 p-4 bg-gray-50/80 border border-gray-300 rounded-xs text-center shadow-2xs overflow-x-auto font-sans">')
        h.append(r'$$\Delta Q_{BEP} = \frac{228 - 226}{226} \times 100\% = 0.88\%$$')
        h.append('</div>\n')
        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4"><strong>Outcome:</strong> Commercial marketing expenses have an extremely minimal effect (+0.88%) on the break-even threshold.</p>\n')

        # Sensitivity Summary Section
        h.append('<div class="my-8 pt-6 border-t-2 border-black">')
        h.append('  <span class="text-xs uppercase font-mono tracking-widest bg-black text-white px-2 py-0.5 inline-block mb-2">Summary Matrix</span>')
        h.append('  <h4 class="text-xl font-bold font-mono tracking-tight text-black mb-3">Sensitivity Ranking Across All Cost Drivers</h4>')
        h.append('</div>\n')
        h.append(render_sensitivity_summary_table())

        h.append('<p class="text-base text-gray-800 leading-relaxed mb-4">It can be clearly observed that <strong>direct material costs exert the dominant influence</strong> on the break-even point ($+25.22\%$). The cost analysis is concerned with determining the monetary value of inputs (raw materials and purchased mechanical assemblies), called the overall cost of production, which dictates the optimum level of batch production. The comprehensive financial modeling confirms that the semi-automated shoe cleaning machine achieves financial break-even within <strong>4.8 months (226 units)</strong>, establishing robust commercial and operational feasibility.</p>\n')
        return '\n'.join(h)

    # --- PDF Page 138 (Report Page 118) ---
    if pdf_page == 138:
        h.append('<div class="p-4 bg-gray-50 border-l-2 border-black my-4 text-xs font-mono text-gray-600 rounded-xs flex items-center justify-between">')
        h.append('  <span>↳ <strong class="text-black">Chapter 08: Cost &amp; Sensitivity Analysis</strong> completed. Proceeding to Future Scope &amp; Limitations.</span>')
        h.append('  <a href="#ch-9" class="text-black font-bold hover:underline shrink-0 ml-4">Next: Chapter 09 →</a>')
        h.append('</div>\n')
        return '\n'.join(h)

    return ""
