#!/usr/bin/env python3
"""Build the small, documented Markdown subset used in content/. No dependencies.

Supported: headings, paragraphs, fenced code, flat lists, pipe tables, inline
code, strong text and links. Raw HTML is escaped. Not a general Markdown parser.
Test pages are maintained directly to keep their test strings stable.
"""
from pathlib import Path
import html
import re
import unicodedata

ROOT = Path(__file__).resolve().parent.parent


def slug(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def inline(text):
    tokens = []

    def token(value):
        tokens.append(value)
        return f"ZZTOKEN{len(tokens)-1}ZZ"

    text = re.sub(r"`([^`]+)`", lambda m: token("<code>" + html.escape(m[1]) + "</code>"), text)
    text = re.sub(r"\[([^\]]+)\]\((\S+?)\)(?=\s|[.,;]|$)",
                  lambda m: token('<a href="' + html.escape(m[2], quote=True) + '">' + html.escape(m[1]) + '</a>'), text)
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    for i in reversed(range(len(tokens))):
        text = text.replace(f"ZZTOKEN{i}ZZ", tokens[i])
    return text


def render(source):
    lines = source.splitlines()
    output, headings = [], []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("```"):
            code = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code.append(lines[i])
                i += 1
            output.append('<pre tabindex="0" aria-label="Kodexempel"><code>' + html.escape("\n".join(code)) + '</code></pre>')
            i += 1
            continue
        match = re.match(r"^(#{1,6}) (.+)$", line)
        if match:
            level, label = len(match[1]), match[2]
            anchor = slug(label)
            headings.append((level, label, anchor))
            output.append(f'<h{level} id="{anchor}">{inline(label)}</h{level}>')
            i += 1
            continue
        if line.startswith("| "):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                row = [cell.strip() for cell in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", cell.replace(" ", "")) for cell in row):
                    rows.append(row)
                i += 1
            label = headings[-1][1] if headings else "Tabell"
            output.append('<div class="table-scroll" role="region" tabindex="0" aria-label="Tabell: ' + html.escape(label, quote=True) + '"><table><thead><tr>')
            output.extend('<th scope="col">' + inline(cell) + '</th>' for cell in rows[0])
            output.append('</tr></thead><tbody>')
            for row in rows[1:]:
                output.append('<tr>' + ''.join('<td>' + inline(cell) + '</td>' for cell in row) + '</tr>')
            output.append('</tbody></table></div>')
            continue
        if re.match(r"^(- |\d+\. )", line):
            ordered = not line.startswith("- ")
            tag = "ol" if ordered else "ul"
            output.append(f"<{tag}>")
            pattern = r"^\d+\. (.+)$" if ordered else r"^- (.+)$"
            while i < len(lines) and (match := re.match(pattern, lines[i])):
                output.append('<li>' + inline(match[1]) + '</li>')
                i += 1
            output.append(f"</{tag}>")
            continue
        paragraph = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|```|\| |[-] |\d+\. )", lines[i]):
            paragraph.append(lines[i])
            i += 1
        output.append('<p>' + inline(' '.join(paragraph)) + '</p>')
    return '\n'.join(output), headings


def main():
    template = (ROOT / 'scripts/template.html').read_text()
    for path in sorted((ROOT / 'content').glob('*.md')):
        body, headings = render(path.read_text())
        title = headings[0][1]
        toc = ''
        if path.stem != 'index':
            entries = ''.join(f'<li><a href="#{anchor}">{html.escape(label)}</a></li>' for level, label, anchor in headings if level == 2)
            toc = '<nav class="toc" aria-label="På sidan"><strong>På sidan</strong><ul>' + entries + '</ul></nav>'
        # Insert the TOC below the introductory paragraphs, before first h2.
        if toc:
            body = body.replace('<h2 ', toc + '\n<h2 ', 1)
        page = template.replace('{{title}}', html.escape(title)).replace('{{body}}', body)
        page = page.replace('{{source}}', path.name)
        (ROOT / 'docs' / (path.stem + '.html')).write_text(page)
    (ROOT / 'docs/.nojekyll').touch()
    print('Byggde dokumentsidor från content/. Körbara exempel ligger i docs/testfall/.')


if __name__ == '__main__':
    main()

