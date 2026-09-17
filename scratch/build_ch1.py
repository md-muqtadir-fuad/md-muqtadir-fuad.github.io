# -*- coding: utf-8 -*-
import html


def _list_html(items, columns=False):
    grid = " grid grid-cols-1 sm:grid-cols-2 gap-x-6" if columns else ""
    out = [f'<ul class="mt-3 ml-5 list-disc space-y-1.5 text-sm text-gray-800{grid}">']
    for item in items:
        out.append(f'  <li class="pl-1 leading-relaxed">{html.escape(item)}</li>')
    out.append('</ul>')
    return '\n'.join(out)


def _feature_list_html(items):
    out = ['<ul class="mt-3 space-y-2 text-sm text-gray-800">']
    for item in items:
        if ':' in item:
            label, detail = item.split(':', 1)
            body = f'<strong class="text-black">{html.escape(label)}:</strong>{html.escape(detail)}'
        else:
            body = html.escape(item)
        out.append('  <li class="flex gap-2.5 leading-relaxed">')
        out.append('    <span class="mt-2 h-1.5 w-1.5 shrink-0 bg-black" aria-hidden="true"></span>')
        out.append(f'    <span>{body}</span>')
        out.append('  </li>')
    out.append('</ul>')
    return '\n'.join(out)


def _proposal_card(number, title, overview, components, features, target_market, operation=None, selected=False):
    border = 'border-2 border-black' if selected else 'border border-gray-300'
    badge = 'Selected proposal' if selected else 'Product concept'
    out = [f'<section class="my-7 bg-white {border} shadow-2xs" id="sec-1-2-{number}">']
    out.append('  <div class="flex flex-col gap-3 border-b border-black bg-gray-50 p-5 sm:flex-row sm:items-start sm:justify-between">')
    out.append('    <div class="flex items-start gap-3">')
    out.append(f'      <span class="inline-flex h-8 w-8 shrink-0 items-center justify-center bg-black font-mono text-xs font-bold text-white">{number:02d}</span>')
    out.append('      <div>')
    out.append(f'        <p class="font-mono text-[10px] font-bold uppercase tracking-widest text-gray-500">Proposal {number:02d}</p>')
    out.append(f'        <h4 class="mt-0.5 text-lg font-bold text-black md:text-xl">{html.escape(title)}</h4>')
    out.append('      </div>')
    out.append('    </div>')
    badge_class = 'bg-black text-white' if selected else 'border border-gray-300 bg-white text-gray-600'
    out.append(f'    <span class="shrink-0 px-2 py-1 font-mono text-[10px] font-bold uppercase tracking-wider {badge_class}">{badge}</span>')
    out.append('  </div>')
    out.append('  <div class="p-5 md:p-6">')
    out.append(f'    <p class="text-base leading-relaxed text-gray-800">{html.escape(overview)}</p>')
    if operation:
        out.append(f'    <p class="mt-4 text-sm leading-relaxed text-gray-700">{html.escape(operation)}</p>')
    out.append('    <div class="mt-6 grid grid-cols-1 gap-5 lg:grid-cols-2">')
    out.append('      <div class="border border-gray-200 bg-gray-50/70 p-4">')
    out.append('        <h5 class="font-mono text-xs font-bold uppercase tracking-wider text-black">Main components</h5>')
    out.append(_list_html(components, columns=len(components) > 5))
    out.append('      </div>')
    out.append('      <div class="border border-gray-200 bg-gray-50/70 p-4">')
    out.append('        <h5 class="font-mono text-xs font-bold uppercase tracking-wider text-black">Notable features</h5>')
    out.append(_feature_list_html(features))
    out.append('      </div>')
    out.append('    </div>')
    out.append('    <div class="mt-5 border-l-4 border-black bg-gray-100/80 px-4 py-3">')
    out.append('      <p class="font-mono text-[10px] font-bold uppercase tracking-widest text-gray-500">Target market</p>')
    out.append(f'      <p class="mt-1 text-sm leading-relaxed text-gray-800">{html.escape(target_market)}</p>')
    out.append('    </div>')
    out.append('  </div>')
    out.append('</section>')
    return '\n'.join(out)


def get_ch1_html():
    proposals = [
        {
            'number': 1,
            'title': 'Multifunctional Canal & River Cleaning Machine',
            'overview': (
                'This concept removes waste from rivers, canals, and drainage systems to reduce water pollution, '
                'protect aquatic life, prevent blockages and flooding, and support safer water supplies.'
            ),
            'components': ['Waste-carrying conveyor', 'Disinfectant sprayer', 'Carrier vehicle'],
            'features': [
                'Collects solid and semi-solid waste floating on the water.',
                'Automates the waste-collection conveyor.',
                'Stores collected waste in an ejectable, transportable basket.',
                'Uses a remotely controlled carrier vehicle.',
                'Allows the sprayer, conveyor, and carrier vehicle to operate independently.',
            ],
            'target_market': (
                'Government organizations such as city corporations, municipalities, and water-management '
                'authorities, as well as non-government organizations working to prevent water pollution and '
                'maintain ecological balance.'
            ),
        },
        {
            'number': 2,
            'title': 'Multi-Functional Cleaner',
            'overview': (
                'A single machine designed to handle several cleaning operations, reducing the need to purchase '
                'and store separate devices for different household cleaning tasks.'
            ),
            'components': [
                'Motors and rotating shafts', 'Brush rollers', 'Polishing and mopping pad', 'Detergent sprayer',
                'Water tank', 'Suction nozzle', 'Vacuum chamber with exhaust port', 'Power source',
            ],
            'features': [
                'Versatility: Performs several cleaning operations with one machine.',
                'Wet and dry cleaning: Adapts to the cleaning method required by the situation.',
                'Ergonomics: Supports comfortable operation.',
                'Accessories: Uses detachable parts for easier handling and task-specific setup.',
            ],
            'target_market': (
                'Busy households, working professionals, elderly users seeking convenience, apartment residents '
                'with limited storage, and pet owners who need frequent floor-cleaning solutions.'
            ),
        },
        {
            'number': 3,
            'title': 'Pedal-Powered Dishwasher',
            'overview': (
                'A manually operated dishwasher that cleans dishes without electricity by using two '
                'counter-rotating discs around a stationary rack.'
            ),
            'operation': (
                'Pedal motion is transferred through a rack-and-pinion mechanism to a vertical shaft. The shaft '
                'rotates the internal and external discs in opposite directions, creating water jets around dishes '
                'held in a rack that exposes most surfaces to the flow.'
            ),
            'components': ['Container', 'Internal and external rotating discs', 'Rack', 'Shaft', 'Gear system', 'Pedal and sprockets'],
            'features': [
                'Uses a simple mechanical system.',
                'Provides a low-cost design.',
                'Can use pedal power, with an optional motor.',
                'Targets a capacity of at least 30 dishes or plates in approximately 10 minutes.',
            ],
            'target_market': (
                'Households and restaurants, particularly busy restaurants that need to clean dishes quickly and '
                'consistently between service cycles.'
            ),
        },
        {
            'number': 4,
            'title': 'Semi-Automated Shoe Cleaning Machine',
            'overview': (
                'A faster and more convenient way to clean and polish shoes at building entrances or designated '
                'cleaning zones, helping prevent dirt transfer and reducing manual cleaning effort.'
            ),
            'operation': (
                'An adjustable drawer-like sole-cleaning chamber uses high-speed roller brushes to remove debris. '
                'Multi-axis synthetic brushes clean the shoe upper, while a spring-mounted sponge on a vibrating '
                'plate follows the shoe surface during polishing.'
            ),
            'components': ['Shoe-sole cleaning chamber', 'Brush-cleaning chamber', 'Shoe-shining chamber'],
            'features': [
                'Provides adjustable brushes for cleaning and polishing.',
                'Applies polishing spray automatically.',
                'Reduces manual shoe-cleaning effort.',
                'Cleans and shines both the upper and sole.',
                'Removes dry or wet dirt from the sole.',
                'Supports a cleaner and more hygienic environment.',
            ],
            'target_market': (
                'Corporate offices, hotels, transportation hubs, healthcare facilities, retail spaces, luxury '
                'residences, government buildings, and event venues where cleanliness, convenience, and a '
                'professional appearance matter.'
            ),
            'selected': True,
        },
    ]

    out = []
    out.append('<div class="mt-14 mb-8 border-t-2 border-black pt-6" id="ch-01">')
    out.append('  <span class="mb-3 inline-block bg-black px-2.5 py-1 font-mono text-xs uppercase tracking-widest text-white">Chapter 01</span>')
    out.append('  <h2 class="font-mono text-2xl font-bold tracking-tight text-black md:text-4xl">Introduction</h2>')
    out.append('</div>')
    out.append('<h3 class="mt-10 mb-4 font-mono text-xl font-bold tracking-tight md:text-2xl" id="sec-1-1"><span class="mr-2 text-gray-400">1.1</span>Product Design</h3>')
    out.append('<div class="border border-gray-300 bg-white p-5 md:p-6">')
    out.append('  <p class="text-base leading-relaxed text-gray-800">Product design is the process of creating new products or services, or improving existing ones, through strategic and tactical activities focused on customer needs and market demand. A design must balance its goals and constraints while accounting for aesthetic, functional, economic, and social considerations.</p>')
    out.append('  <p class="mt-4 text-base leading-relaxed text-gray-800">Effective product design combines ergonomics, usability, and manufacturing feasibility. It uses analysis and problem-solving to translate user needs into an engineered solution, balancing the factors that shape how a product looks, works, is produced, and interacts with its environment.</p>')
    out.append('  <div class="mt-5 grid grid-cols-1 gap-3 font-mono text-xs sm:grid-cols-3">')
    for item in ('Ergonomics', 'Usability', 'Manufacturing feasibility'):
        out.append(f'    <div class="border border-black bg-gray-50 px-3 py-2 text-center font-bold uppercase tracking-wide">{item}</div>')
    out.append('  </div>')
    out.append('</div>')
    out.append('<h3 class="mt-12 mb-3 font-mono text-xl font-bold tracking-tight md:text-2xl" id="sec-1-2"><span class="mr-2 text-gray-400">1.2</span>Proposed Product Ideas</h3>')
    out.append('<p class="mb-6 text-base leading-relaxed text-gray-800">The team initially proposed four product concepts for Product Design Sessional-I.</p>')
    for proposal in proposals:
        out.append(_proposal_card(**proposal))
    out.append('<h3 class="mt-12 mb-4 font-mono text-xl font-bold tracking-tight md:text-2xl" id="sec-1-3"><span class="mr-2 text-gray-400">1.3</span>Selected Proposal</h3>')
    out.append('<div class="border-2 border-black bg-gray-50 p-5 md:p-6">')
    out.append('  <div class="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">')
    out.append('    <div>')
    out.append('      <p class="font-mono text-[10px] font-bold uppercase tracking-widest text-gray-500">Final concept</p>')
    out.append('      <h4 class="mt-1 text-xl font-bold text-black">Semi-Automated Shoe Cleaning Machine</h4>')
    out.append('    </div>')
    out.append('    <span class="bg-black px-3 py-1.5 font-mono text-xs font-bold uppercase tracking-wider text-white">Proposal 04</span>')
    out.append('  </div>')
    out.append('  <p class="mt-4 text-base leading-relaxed text-gray-800">After reviewing the four ideas with the course teachers, the fourth proposal was approved as the team project.</p>')
    out.append('</div>')
    out.append('<h4 class="mt-8 mb-3 font-mono text-lg font-bold" id="sec-1-3-1"><span class="mr-2 text-gray-400">1.3.1</span>Reasons for Selection</h4>')
    out.append('<p class="text-base leading-relaxed text-gray-800">The selected concept serves corporate offices, hotels, transportation hubs, and other high-traffic facilities where clean footwear supports a professional appearance and better hygiene. It saves time for staff, visitors, and guests by cleaning and polishing footwear with minimal manual effort. The combination of convenience, cleanliness, and a distinctive product concept gives the machine strong potential to attract customer and market interest.</p>')
    return '\n'.join(out)
