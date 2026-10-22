# -*- coding: utf-8 -*-
import os

from generate_role_views import ciso_html, soc_html, client_html
from generate_subpage_modules import (
    threats_html,
    vulnerabilities_html,
    firewall_html,
    incidents_html,
    compliance_html,
    reports_html,
    users_html
)

with open('pages/dashboard.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Locate topbar end
main_start_tag = '<main class="dash-content" role="main">'
topbar_end = orig.find(main_start_tag)
if topbar_end == -1:
    raise ValueError("Could not find main start tag in dashboard.html")

header_part = orig[:topbar_end + len(main_start_tag) + 1]

# Ensure dash-drawer-backdrop is in header_part
if 'dash-drawer-backdrop' not in header_part:
    layout_tag = '<div class="dashboard-layout">'
    header_part = header_part.replace(layout_tag, layout_tag + '\n    <!-- Mobile Drawer Backdrop -->\n    <div class="dash-drawer-backdrop" id="dash-drawer-backdrop" aria-hidden="true"></div>\n')

# Locate footer start
footer_tag = '</main>'
footer_start = orig.rfind(footer_tag)
if footer_start == -1:
    raise ValueError("Could not find closing main tag in dashboard.html")

footer_part = orig[footer_start:]

# Assemble module-overview
overview_html = f"""
        <!-- MODULE 1: OPERATIONS OVERVIEW (3 DEDICATED ROLE DASHBOARDS, 8 SECTIONS EACH) -->
        <div class="dash-module-section active" id="module-overview">
{ciso_html}
{soc_html}
{client_html}
        </div>
"""

# Combine all parts
new_dashboard = (
    header_part
    + overview_html
    + threats_html
    + vulnerabilities_html
    + firewall_html
    + incidents_html
    + compliance_html
    + reports_html
    + users_html
    + "\n      "
    + footer_part
)

with open('pages/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(new_dashboard)

print(f"Successfully assembled new dashboard.html! Total length: {len(new_dashboard)} characters.")

