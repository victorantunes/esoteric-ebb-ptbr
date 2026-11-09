import re
_ph = re.compile(r'\{[^}]*\}|\$[A-Za-z_]+')
_tag = re.compile(r'<(/?)([A-Za-z]+)[^>]*>')
def _balanced(s):
    st = []
    for m in _tag.finditer(s):
        if m.group(1) == '':
            st.append(m.group(2).lower())
        else:
            if not st or st.pop() != m.group(2).lower(): return False
    return not st
def serious(en, pt):
    """True se a tradução pode quebrar o jogo (placeholders diferentes ou tags desbalanceadas)."""
    if sorted(_ph.findall(en)) != sorted(_ph.findall(pt)): return True
    if _balanced(en): return not _balanced(pt)
    return sorted(re.findall(r'<[^>]*>', en)) != sorted(re.findall(r'<[^>]*>', pt))
def cosmetic(en, pt):
    return sorted(re.findall(r'<[^>]*>', en)) != sorted(re.findall(r'<[^>]*>', pt))
