with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Remove duplicate hero-stage
dup_block = """/* ==========================================================================
   REFERENCE-INSPIRED KINETIC CYBER HERO STAGE
   Centered composition, ambient holographic ribbons, 3-layer kinetic typography,
   hooded cyber sentinel holding chains, pill CTAs, subtext, metrics.
   ========================================================================== */
.hero-stage {
  position: relative;
  min-height: 94vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: 2.5rem 1.25rem 5rem;
  overflow: hidden;
  text-align: center;
}

"""

if dup_block in css:
    css = css.replace(dup_block, "")
    print("Removed duplicate hero-stage block")
elif dup_block.replace('\n', '\r\n') in css:
    css = css.replace(dup_block.replace('\n', '\r\n'), "")
    print("Removed duplicate hero-stage block (CRLF)")
else:
    print("Warning: dup_block not found directly")

# 2. Update .hero-sentinel-stage margin
old_sentinel = """.hero-sentinel-stage {
  position: relative;
  width: 100%;
  max-width: 860px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
}"""

new_sentinel = """.hero-sentinel-stage {
  position: relative;
  width: 100%;
  max-width: 860px;
  margin: 2.75rem auto 0;
  display: flex;
  align-items: center;
  justify-content: center;
}"""

if old_sentinel in css:
    css = css.replace(old_sentinel, new_sentinel)
    print("Updated .hero-sentinel-stage margin")
elif old_sentinel.replace('\n', '\r\n') in css:
    css = css.replace(old_sentinel.replace('\n', '\r\n'), new_sentinel.replace('\n', '\r\n'))
    print("Updated .hero-sentinel-stage margin (CRLF)")
else:
    print("Warning: old_sentinel not found")

# 3. Update auth styles
old_auth = """.auth-banner-side {
  background: linear-gradient(145deg, #0a1122 0%, #060a14 100%);
  border-right: 1px solid var(--border-subtle);
  padding: 3.5rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
  z-index: 10;
}

.auth-brand-logo {
  height: 40px !important;
  width: auto !important;
  max-width: 170px !important;
  object-fit: contain;
  display: inline-block;
  filter: drop-shadow(0 0 12px rgba(94, 234, 212, 0.45));
  transition: transform var(--transition-fast);
}

.auth-brand-logo:hover {
  transform: scale(1.04);
}

.auth-banner-side::before {
  content: '';
  position: absolute;
  top: -20%;
  left: -20%;
  width: 140%;
  height: 140%;
  background: radial-gradient(circle at 30% 30%, rgba(0, 240, 118, 0.12) 0%, transparent 60%);
  pointer-events: none;
}

.auth-banner-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  z-index: 2;
}

.auth-banner-content {
  z-index: 2;
  margin: auto 0;
}

.auth-banner-content h1 {
  font-size: 2.25rem;
  margin-bottom: 1.25rem;
}

.auth-trust-list {
  list-style: none;
  margin: 2rem 0;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.auth-trust-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.95rem;
  color: var(--text-secondary);
}

.auth-trust-icon {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: rgba(0, 240, 118, 0.15);
  color: var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.85rem;
}

.auth-quote-box {
  background: rgba(13, 21, 39, 0.8);
  border: 1px solid var(--border-cyber);
  border-radius: var(--radius-md);
  padding: 1.25rem;
  z-index: 2;
}

.auth-quote-text {
  font-size: 0.875rem;
  font-style: italic;
  color: var(--text-secondary);
  margin-bottom: 0.5rem;
}

.auth-quote-author {
  font-size: 0.775rem;
  color: var(--primary);
  font-weight: 600;
}"""

new_auth = """.auth-banner-side {
  background: linear-gradient(145deg, #0a1122 0%, #060a14 100%);
  border-right: 1px solid var(--border-subtle);
  padding: clamp(1.5rem, 3vh, 2.5rem) clamp(1.5rem, 2.5vw, 2.75rem);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: sticky;
  top: 0;
  height: 100vh;
  max-height: 100vh;
  overflow: hidden !important;
  z-index: 10;
}

.auth-brand-logo {
  height: 38px !important;
  width: auto !important;
  max-width: 160px !important;
  object-fit: contain;
  display: inline-block;
  filter: drop-shadow(0 0 12px rgba(94, 234, 212, 0.45));
  transition: transform var(--transition-fast);
}

.auth-brand-logo:hover {
  transform: scale(1.04);
}

.auth-banner-side::before {
  content: '';
  position: absolute;
  top: -20%;
  left: -20%;
  width: 140%;
  height: 140%;
  background: radial-gradient(circle at 30% 30%, rgba(0, 240, 118, 0.12) 0%, transparent 60%);
  pointer-events: none;
}

.auth-banner-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  z-index: 2;
}

.auth-banner-content {
  z-index: 2;
  margin: auto 0;
}

.auth-banner-content h1 {
  font-size: clamp(1.4rem, 2.1vw, 1.95rem);
  line-height: 1.25;
  margin-bottom: clamp(0.5rem, 1.1vh, 0.85rem);
}

.auth-trust-list {
  list-style: none;
  margin: clamp(0.6rem, 1.2vh, 1.2rem) 0;
  display: flex;
  flex-direction: column;
  gap: clamp(0.45rem, 0.8vh, 0.7rem);
}

.auth-trust-item {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  font-size: clamp(0.8rem, 0.95vw, 0.88rem);
  color: var(--text-secondary);
}

.auth-trust-icon {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: rgba(0, 240, 118, 0.15);
  color: var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  flex-shrink: 0;
}

.auth-quote-box {
  background: rgba(13, 21, 39, 0.85);
  border: 1px solid var(--border-cyber);
  border-left: 3px solid var(--primary);
  border-radius: var(--radius-md);
  padding: clamp(0.65rem, 1.2vh, 1rem);
  z-index: 2;
  margin-top: clamp(0.4rem, 0.8vh, 0.75rem);
}

.auth-quote-text {
  font-size: clamp(0.78rem, 0.9vw, 0.85rem);
  font-style: italic;
  color: var(--text-secondary);
  line-height: 1.45;
  margin-bottom: 0.35rem;
}

.auth-quote-author {
  font-size: clamp(0.7rem, 0.8vw, 0.76rem);
  color: var(--primary);
  font-weight: 600;
  display: block;
}"""

if old_auth in css:
    css = css.replace(old_auth, new_auth)
    print("Updated auth styles")
elif old_auth.replace('\n', '\r\n') in css:
    css = css.replace(old_auth.replace('\n', '\r\n'), new_auth.replace('\n', '\r\n'))
    print("Updated auth styles (CRLF)")
else:
    print("Warning: old_auth not found")

# 4. Update media queries for hero spacing
old_mq = """  .hero-stage {
    padding: 2rem 1rem 4rem;
  }"""

new_mq = """  .hero-stage {
    padding: 3rem 1rem 4rem;
  }
  
  .hero-sentinel-stage {
    margin: 2rem auto 0;
  }"""

if old_mq in css:
    css = css.replace(old_mq, new_mq)
    print("Updated media query hero-stage")
elif old_mq.replace('\n', '\r\n') in css:
    css = css.replace(old_mq.replace('\n', '\r\n'), new_mq.replace('\n', '\r\n'))
    print("Updated media query hero-stage (CRLF)")
else:
    print("Warning: old_mq not found")

# 5. Add mobile media query for hero-sentinel-stage if not present
old_mobile_mq = """  .hero-interactive-dock {
    margin-top: 0.5rem;
  }"""

new_mobile_mq = """  .hero-stage {
    padding: 2.25rem 0.75rem 3.5rem;
  }
  
  .hero-sentinel-stage {
    margin: 1.5rem auto 0;
  }

  .hero-interactive-dock {
    margin-top: 0.5rem;
  }"""

if old_mobile_mq in css:
    css = css.replace(old_mobile_mq, new_mobile_mq)
    print("Updated mobile media query")
elif old_mobile_mq.replace('\n', '\r\n') in css:
    css = css.replace(old_mobile_mq.replace('\n', '\r\n'), new_mobile_mq.replace('\n', '\r\n'))
    print("Updated mobile media query (CRLF)")

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Saved assets/css/style.css successfully")

