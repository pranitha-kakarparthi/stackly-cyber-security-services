with open('assets/css/dashboard.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line_num in [521, 556, 728]:
    if line_num <= len(lines):
        print(f"--- Line {line_num} ---")
        print(''.join(lines[max(0, line_num-3):min(len(lines), line_num+4)]))

