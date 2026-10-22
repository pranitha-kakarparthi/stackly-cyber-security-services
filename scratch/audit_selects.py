import glob
import re

files = glob.glob('*.html') + glob.glob('pages/*.html')

with open('scratch/selects_report.txt', 'w', encoding='utf-8') as out:
    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
        selects = re.findall(r'<select[^>]*>.*?</select>', content, re.DOTALL)
        if selects:
            out.write(f"\n=== {f} ({len(selects)} selects) ===\n")
            for s in selects:
                first_option = re.search(r'<option[^>]*>(.*?)</option>', s)
                first_opt_text = first_option.group(1) if first_option else "NONE"
                select_tag = re.search(r'<select([^>]*)>', s).group(1)
                out.write(f"  Select: {select_tag.strip()[:40]} | 1st option: {first_opt_text[:40]}\n")

print("Report written to scratch/selects_report.txt")

