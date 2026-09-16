import fitz
import re
import sys

doc = fitz.open(r'C:\Users\DELL\Downloads\pd_report.pdf')

def clean(s):
    s = s.replace('\ufb01', 'fi').replace('\ufb02', 'fl').replace('\ufb03', 'ffi')
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    return s

print("=== APPENDIX A QUESTIONS ===")
all_qs = []
current_q = None

for pno in range(142, 146):
    p = doc[pno]
    for b in p.get_text('blocks'):
        txt = clean(b[4].strip())
        lines = [l.strip() for l in txt.split('\n') if l.strip()]
        for line in lines:
            m = re.match(r'^(\d+)\.\s*(.*)', line)
            if m:
                if current_q:
                    all_qs.append(current_q)
                current_q = {'num': int(m.group(1)), 'text': m.group(2), 'opts': []}
            elif current_q:
                if line.startswith('o ') or line == 'o':
                    opt = line[2:].strip() if line.startswith('o ') else ''
                    if opt:
                        current_q['opts'].append(opt)
                elif current_q['opts'] and not line.startswith('Appendix') and not re.match(r'^\d+$', line):
                    # check if it's the option text when 'o' was alone
                    if current_q['opts'] and current_q['opts'][-1] == '':
                        current_q['opts'][-1] = line
                    elif line not in current_q['opts']:
                        pass
                elif not current_q['opts'] and not line.startswith('Appendix') and not re.match(r'^\d+$', line):
                    current_q['text'] += ' ' + line

if current_q:
    all_qs.append(current_q)

for q in all_qs:
    print(f"Q{q['num']:02d}: {q['text']}")
    print(f"     Options: {q['opts']}")
