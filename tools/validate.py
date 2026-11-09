#!/usr/bin/env python3
"""Valida a pasta PortugueseBR contra a pasta Official do jogo.

Uso:
    python tools/validate.py "<pasta Localization do jogo>"

Verifica, para cada CSV:
  - mesmas chaves, na mesma ordem, que Official/
  - texto vazio (cai no FallbackLanguage = EN)
  - tags e placeholders divergentes ({0}, $VAR, <i>, <color=...>)
Sai com código 1 se houver problema de chave/ordem ou tag/placeholder.
"""
import csv, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tagrule import serious

csv.field_size_limit(10**9)
HERE = os.path.dirname(os.path.abspath(__file__))
PT_DIR = os.path.join(HERE, '..', 'PortugueseBR')


def read(path):
    with open(path, encoding='utf-8', newline='') as fh:
        return [r for r in csv.reader(fh) if r]


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    official = os.path.join(sys.argv[1], 'Official')
    bad = empty = total = 0
    for fn in sorted(os.listdir(PT_DIR)):
        if not fn.endswith('.csv'):
            continue
        en = read(os.path.join(official, fn))
        pt = read(os.path.join(PT_DIR, fn))
        en_hdr = en[0]
        col = en_hdr.index('EN')  # texto em inglês
        if [r[0] for r in en[1:]] != [r[0] for r in pt[1:]]:
            print(f'{fn}: chaves/ordem diferem de Official')
            bad += 1
            continue
        for e, p in zip(en[1:], pt[1:]):
            total += 1
            src, dst = e[col], p[-1]
            if not dst.strip():
                if src.strip():
                    empty += 1
                continue
            if serious(src, dst):
                bad += 1
                print(f'{fn}: tag/placeholder divergente em {e[0]}')
    print(f'linhas: {total} | vazias (usam EN): {empty} | problemas: {bad}')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
