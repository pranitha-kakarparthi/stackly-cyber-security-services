with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line_num in [1200, 1577, 1616, 1681, 2330, 2475]:
    if line_num <= len(lines):
        print(f"--- Line {line_num} ---")
        print(''.join(lines[max(0, line_num-3):min(len(lines), line_num+4)]))

