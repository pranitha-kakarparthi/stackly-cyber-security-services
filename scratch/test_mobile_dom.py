import glob
import os
import re

files = [
    'index.html',
    'pages/about.html',
    'pages/services.html',
    'pages/pricing.html',
    'pages/contact.html',
    'pages/service-soc.html',
    'pages/service-pentest.html',
    'pages/service-cloud-security.html',
    'pages/service-incident-response.html',
    'pages/service-vulnerability-management.html',
    'pages/service-compliance.html',
    'pages/sign-in.html',
    'pages/sign-up.html'
]

all_passed = True

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    if 'sign-in' in f or 'sign-up' in f:
        has_banner = 'class="auth-banner-side"' in c
        has_form = 'class="auth-form-side"' in c
        has_quote = 'class="auth-quote-box"' in c
        has_trust = 'class="auth-trust-list"' in c
        passed = has_banner and has_form and has_quote and has_trust
        if not passed:
            all_passed = False
        print(f"[{'PASS' if passed else 'FAIL'}] {f} has full auth components intact (banner={has_banner}, form={has_form}, quote={has_quote}, trust={has_trust})")
    else:
        has_overlay = 'class="mobile-nav-overlay"' in c
        has_btn = 'class="mobile-dropdown-btn' in c
        service_cards = len(re.findall(r'class="mobile-service-card\b', c))
        passed = has_overlay and has_btn and service_cards == 6
        if not passed:
            all_passed = False
        print(f"[{'PASS' if passed else 'FAIL'}] {f} mobile drawer (overlay={has_overlay}, toggle_btn={has_btn}, service_cards={service_cards}/6)")

print("\nOVERALL TEST STATUS:", "ALL PASSED!" if all_passed else "SOME FAILED!")

