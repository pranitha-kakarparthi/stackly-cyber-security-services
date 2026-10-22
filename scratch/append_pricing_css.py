with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

pricing_css = '''
/* ==========================================================================
   PRICING DETAILED COMPARISON MATRIX - PERFECT REALIGNMENT
   ========================================================================== */
.pricing-comparison-wrap {
  background: var(--surface-card);
  border: 1px solid var(--border-cyber);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
  overflow-x: auto;
  position: relative;
  margin-top: 1.5rem;
}

.pricing-comparison-table {
  width: 100%;
  min-width: 780px;
  border-collapse: separate;
  border-spacing: 0;
  text-align: left;
}

.pricing-comparison-table th,
.pricing-comparison-table td {
  padding: 1.15rem 1.4rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  vertical-align: middle;
}

.pricing-comparison-table thead th {
  background: #090e1c;
  color: var(--text-primary);
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: -0.01em;
  padding: 1.5rem 1.4rem;
  border-bottom: 2px solid var(--border-cyber);
}

.pricing-comparison-table thead th:first-child {
  border-top-left-radius: var(--radius-md);
  text-align: left;
  width: 34%;
}

.pricing-comparison-table thead th:not(:first-child) {
  text-align: center;
  width: 22%;
}

.pricing-comparison-table thead th:last-child {
  border-top-right-radius: var(--radius-md);
}

.pricing-comparison-table tbody tr:hover td {
  background: rgba(255, 255, 255, 0.02);
}

.pricing-comparison-table td:not(:first-child) {
  text-align: center;
  color: var(--text-secondary);
  font-size: 0.925rem;
}

.pricing-comparison-table td:first-child {
  color: var(--text-primary);
  font-weight: 600;
  font-size: 0.95rem;
}

/* Highlighted Popular Column: Advanced SOC 24/7 */
.pricing-comparison-table th.col-highlight,
.pricing-comparison-table td.col-highlight {
  background: rgba(94, 234, 212, 0.04);
  border-left: 1px solid rgba(94, 234, 212, 0.25);
  border-right: 1px solid rgba(94, 234, 212, 0.25);
}

.pricing-comparison-table th.col-highlight {
  background: rgba(94, 234, 212, 0.09);
  border-top: 2px solid var(--primary);
  position: relative;
}

.col-badge-popular {
  display: inline-block;
  font-size: 0.68rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 0.2rem 0.6rem;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  color: #030508;
  border-radius: var(--radius-full);
  margin-bottom: 0.45rem;
}

.pricing-table-cta {
  padding-top: 1.5rem !important;
  border-bottom: none !important;
  text-align: center;
}
'''

if '.pricing-comparison-table' not in css:
    css += pricing_css
    with open('assets/css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added pricing comparison CSS to style.css")
else:
    print("Pricing comparison CSS already present in style.css")

