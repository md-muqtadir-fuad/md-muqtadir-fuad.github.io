import re

with open('blog-semi-automated-shoe-cleaning-machine.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 1. Check Chapter 6 tables
assert 'Qualitative Analysis of Material Selection for Different Sections' in html_content
assert 'Qualitative Analysis of Manufacturing Process Selection' in html_content
assert 'Qualitative Analysis of Parts Joining Method Selection' in html_content

# Check that Table 6.2 has Make/Outsource badges
assert '>Make<' in html_content
assert '>Outsource<' in html_content

# Check that Table 6.3 has Permanent/Temporary badges
assert '>Permanent<' in html_content
assert '>Temporary<' in html_content

# 2. Check Digital Logic tables
dl_headers = re.findall(r'Number of Positive Decisions,\s*\$N = \\frac\{n\(n-1\)\}\{2\}', html_content)
print(f"Found {len(dl_headers)} Digital Logic two-tier headers with KaTeX formula!")
assert len(dl_headers) == 10, f"Expected 10 DL headers, found {len(dl_headers)}"

# Check Table 7.4 has 45 decision columns
assert '>45</th>' in html_content
assert 'Relative Emphasis ($\\alpha$)' in html_content

# 3. Check Performance Index tables
pi_headers = re.findall(r'Weighting Factor \(\$\\alpha\$\)', html_content)
print(f"Found {len(pi_headers)} Performance Index two-tier headers with KaTeX formula!")
assert len(pi_headers) == 10, f"Expected 10 PI headers, found {len(pi_headers)}"

# Check Table 7.5 candidate materials
assert 'AISI 316 Stainless Steel' in html_content
assert 'AISI 347 Annealed Stainless Steel' in html_content
assert '1045 Carbon Steel' in html_content

# Check Scaled (beta) and Score (alphabeta)
assert r'Scaled ($\beta$)' in html_content
assert r'Score ($\alpha\beta$)' in html_content
assert r'Performance Index ($\gamma = \sum \alpha\beta$)' in html_content

# Check Table 7.12 has both parts merged
assert 'Abrasion Resistance' in html_content
assert 'Flexibility' in html_content
assert 'Water Resistance' in html_content
assert 'Durability' in html_content

# Check no bell \x07 or backspace \x08
assert '\x07' not in html_content
assert '\x08' not in html_content

print("ALL VERIFICATIONS PASSED IN GENERATED HTML!")
