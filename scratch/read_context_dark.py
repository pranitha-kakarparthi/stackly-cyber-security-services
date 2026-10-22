with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

targets = [370, 1410, 1495, 1630, 1790, 1980, 2685, 2745]
for t in targets:
    start = max(0, t - 3)
    end = min(len(lines), t + 12)
    print(f"\n=== CONTEXT AROUND LINE {t} ===")
    for i in range(start, end):
        print(f"{i+1:4}: {lines[i]}", end='')

