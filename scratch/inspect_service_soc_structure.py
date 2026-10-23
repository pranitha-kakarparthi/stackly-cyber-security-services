with open('pages/service-soc.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('Total lines in service-soc.html:', len(lines))
# print lines 1 to 50
print(''.join(lines[:50]))

