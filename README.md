# Siffror och skärmläsare

Webbfördjupning till Confluence-kortguiden med krav, implementation och förväntat testresultat. Kortguiden ändras inte av webbbygget.

Webbplats: https://fagerkod.github.io/siffror/

## Innehåll

- `content/`: webbtexter om principer, exempelöversikt, utveckling och skärmläsare.
- `docs/testfall/`: tre körbara övningssidor. HTML redigeras direkt.
- `docs/examples.js`: lokal OCR- och betalningsövning utan nätverksanrop eller lagring.
- `docs/`: publiceringsmappen för GitHub Pages.
- `underlag/`: historiskt underlag utanför webbplatsen.

De äldre undersökningsfallen och resultatsidorna ingår inte i webbplatsen. Git-historiken bevarar tidigare versioner.

## Bygg och kontrollera

```sh
python3 scripts/build.py
python3 scripts/check_site.py
node scripts/test_examples.cjs
```

Byggaren använder endast Pythons standardbibliotek och omvandlar webbtexterna i `content/` till HTML. Vid ändringar i krav: uppdatera webbtext, motsvarande övning och förväntat resultat tillsammans. `scripts/verifiera.py` kör också den aktuella sidkontrollen.

```sh
python3 -m http.server 8000 --directory docs
```

Öppna http://localhost:8000/. Kopieringsknappen kräver en säker webbläsarkontext, exempelvis HTTPS eller localhost, och att webbläsaren tillåter kopiering. Fel visas i statusregionen.

Pages publicerar `main`, mappen `/docs`. Kör inte bara om byggaren efter att gamla källfiler återställts: publiceringsmappen ska bara innehålla aktuellt innehåll.

Automatiska kontroller verifierar struktur och funktion, inte faktiskt uttal. Prova även manuellt med NVDA på Windows och VoiceOver i Safari på iPhone samt vid 320 CSS-pixlars bredd och förstoring. Ingen godkänd skärmläsarkörning kan härledas enbart från kodkontrollerna.
