#!/usr/bin/env python3
"""Validate links, document structure and removal of historical site content."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import sys
ROOT=Path(__file__).resolve().parent.parent/'docs'
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.ids=set();self.links=[];self.errors=[];self.h1=0;self.main=0;self.lang=None;self.labels=[];self.inputs=[];self.descriptions=[];self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang')
  if tag=='h1':self.h1+=1
  if tag=='main':self.main+=1
  if 'id' in a:
   if a['id'] in self.ids:self.errors.append('Dubbelt id '+a['id'])
   self.ids.add(a['id'])
  for key in ('href','src'):
   if key in a:self.links.append(a[key])
  if tag=='label':self.labels.append(a.get('for'))
  if tag in ('input','select'):self.inputs.append(a.get('id'))
  self.descriptions.extend(a.get('aria-describedby','').split())
  if a.get('aria-hidden')=='true' and tag!='svg':self.errors.append('Dolt innehåll utanför dekorativ ikon')
  if tag in ('span','p','div') and 'aria-label' in a and 'role' not in a:self.errors.append('Namn på generiskt element')
  if tag=='script' and a.get('src')!='../examples.js':self.errors.append('Oväntat skript')
def main():
 pages={p.resolve():Page(p.read_text()) for p in ROOT.rglob('*.html')};errors=[]
 for path,page in pages.items():
  errors.extend(f'{path.name}: {e}' for e in page.errors)
  if (page.lang,page.h1,page.main)!=('sv',1,1):errors.append(f'{path.name}: språk eller huvudstruktur')
  for field in page.inputs:
   if field not in page.labels:errors.append(f'{path.name}: fält utan etikett {field}')
  for id in page.descriptions:
   if id not in page.ids:errors.append(f'{path.name}: saknad beskrivning {id}')
  for url in page.links:
   parts=urlsplit(url)
   if parts.scheme or parts.netloc:continue
   target=(path.parent/unquote(parts.path)).resolve() if parts.path else path
   if not target.is_file():errors.append(f'{path.name}: saknas {url}')
   elif parts.fragment and target in pages and unquote(parts.fragment) not in pages[target].ids:errors.append(f'{path.name}: saknat ankare {url}')
  text=path.read_text()
  for forbidden in ('tc-0','tc-1','tc-2','resultat.html','resultatmall.html','historiska observationer','—','–'):
   if forbidden in text:errors.append(f'{path.name}: äldre innehåll eller talstreck {forbidden}')
 for name in ('resultat.html','resultatmall.html'):
  if (ROOT/name).exists():errors.append('Äldre sida finns kvar: '+name)
 if errors:print('\n'.join(errors));return 1
 print(f'OK: {len(pages)} sidor, länkar, ankare, etiketter och innehållskontroll.');return 0
if __name__=='__main__':sys.exit(main())
