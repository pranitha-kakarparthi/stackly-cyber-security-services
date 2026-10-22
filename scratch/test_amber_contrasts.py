import sys
sys.path.append('.')
from scratch.calc_contrasts import contrast_ratio

for hex_code in ['#D97706', '#B45309', '#92400E', '#78350F']:
    cr_ivory = contrast_ratio(hex_code, '#FAF7EE')
    cr_white = contrast_ratio(hex_code, '#FFFFFF')
    print(f"{hex_code}: ivory={cr_ivory:.2f}:1  white={cr_white:.2f}:1 -> {'PASS (AAA)' if cr_ivory >= 7 else 'PASS (AA)' if cr_ivory >= 4.5 else 'FAIL'}")

