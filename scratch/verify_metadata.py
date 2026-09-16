import json
import re

def check_file_metadata(filepath):
    print(f"\n==================== Checking {filepath} ====================")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Canonical
    if '<link rel="canonical"' in content:
        print("PASSED: Canonical link found.")
    else:
        print("FAILED: Canonical link missing.")

    # Primary Meta
    for tag in ['name="title"', 'name="description"', 'name="keywords"', 'name="author"', 'name="robots"']:
        if tag in content:
            print(f"PASSED: Found {tag}")
        else:
            print(f"FAILED: Missing {tag}")

    # Open Graph
    for og in ['property="og:type"', 'property="og:url"', 'property="og:title"', 'property="og:description"', 'property="og:image"']:
        if og in content:
            print(f"PASSED: Found {og}")
        else:
            print(f"FAILED: Missing {og}")

    # Twitter
    for tw in ['name="twitter:card"', 'name="twitter:title"', 'name="twitter:description"']:
        if tw in content:
            print(f"PASSED: Found {tw}")
        else:
            print(f"FAILED: Missing {tw}")

    # JSON-LD
    json_ld_matches = re.findall(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', content, re.DOTALL)
    if json_ld_matches:
        for idx, j_str in enumerate(json_ld_matches):
            try:
                parsed = json.loads(j_str)
                print(f"PASSED: JSON-LD #{idx+1} parsed successfully! @type: {parsed.get('@type')}")
            except Exception as e:
                print(f"FAILED: JSON-LD #{idx+1} parse error: {e}")
    else:
        print("FAILED: No JSON-LD found.")

if __name__ == '__main__':
    check_file_metadata('blog-semi-automated-shoe-cleaning-machine.html')
    check_file_metadata('blog-badhan.html')
