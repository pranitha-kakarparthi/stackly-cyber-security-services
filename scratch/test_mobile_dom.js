// Test mobile layout and element presence using jsdom
const { JSDOM } = require('jsdom');
const fs = require('fs');
const path = require('path');

const files = [
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
];

let allPassed = true;

files.forEach(file => {
  const filePath = path.join(__dirname, '..', file);
  const html = fs.readFileSync(filePath, 'utf-8');
  const dom = new JSDOM(html, { runScripts: "outside-only" });
  const doc = dom.window.document;

  if (file.includes('sign-in') || file.includes('sign-up')) {
    const banner = doc.querySelector('.auth-banner-side');
    const form = doc.querySelector('.auth-form-side');
    const quote = doc.querySelector('.auth-quote-box');
    const trust = doc.querySelector('.auth-trust-list');

    if (!banner || !form || !quote || !trust) {
      console.error(`[FAIL] ${file} is missing auth components!`);
      allPassed = false;
    } else {
      console.log(`[PASS] ${file} has all auth components intact (banner, form, quote, trust list).`);
    }
  } else {
    const mobileNav = doc.querySelector('.mobile-nav-overlay');
    const servicesSubmenu = mobileNav ? mobileNav.querySelector('.mobile-submenu') : null;
    const cards = servicesSubmenu ? servicesSubmenu.querySelectorAll('.mobile-service-card') : [];

    if (!mobileNav) {
      console.error(`[FAIL] ${file} is missing .mobile-nav-overlay!`);
      allPassed = false;
    } else if (cards.length !== 6) {
      console.error(`[FAIL] ${file} mobile services dropdown has ${cards.length} cards, expected 6!`);
      allPassed = false;
    } else {
      console.log(`[PASS] ${file} mobile nav has 6 synchronized service cards in dropdown!`);
    }
  }
});

console.log("\nNode test finished. Overall:", allPassed ? "ALL PASSED" : "FAILED");

