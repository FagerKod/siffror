#!/usr/bin/env python3
"""Check local links, fragments, document structure and contextual test markup."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import sys

ROOT = Path(__file__).resolve().parent.parent / 'docs'


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links, self.tests, self.errors = set(), [], {}, []
        self.h1 = self.main = 0
        self.lang = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html': self.lang = a.get('lang')
        if tag == 'h1': self.h1 += 1
        if tag == 'main': self.main += 1
        if 'id' in a:
            if a['id'] in self.ids: self.errors.append('Dubbelt id: ' + a['id'])
            self.ids.add(a['id'])
        for name in ['href', 'src']:
            if name in a: self.links.append(a[name])
        if 'data-tc' in a:
            if a['data-tc'] in self.tests: self.errors.append('Dubbelt test-ID')
            self.tests[a['data-tc']] = (tag, a)
        if tag == 'script': self.errors.append('Oväntat script')


def main():
    pages = {p.resolve(): Page(p.read_text()) for p in ROOT.rglob('*.html')}
    errors = []
    for path, page in pages.items():
        errors.extend(str(path.relative_to(ROOT)) + ': ' + e for e in page.errors)
        if (page.lang, page.h1, page.main) != ('sv', 1, 1):
            errors.append(f'{path.name}: fel språk, h1 eller main')
        for url in page.links:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc: continue
            target = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            if not target.is_file(): errors.append(f'{path.name}: saknas {url}')
            elif parts.fragment and target in pages and unquote(parts.fragment) not in pages[target].ids:
                errors.append(f'{path.name}: saknat ankare {url}')
    context = pages[(ROOT / 'testfall/sammanhang.html').resolve()]
    for tc, tag, attr, value in [('tc-16', 'a', 'href', 'tel:+46701234567'),
                                 ('tc-17', 'button', 'type', 'button'),
                                 ('tc-18', 'td', 'class', 'teststrang')]:
        found_tag, attrs = context.tests.get(tc, ('', {}))
        if found_tag != tag or attrs.get(attr) != value:
            errors.append('Fel testsemantik: ' + tc)
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'OK: {len(pages)} sidor, interna länkar, ankare, språk, huvudstruktur och kontextfall.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
