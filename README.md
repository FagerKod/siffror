# Siffror och tal med skärmläsare

En gemensam vägledning med delar för testare och utvecklare, kompletterad med 21 testfall, testmanual, resultatmall och källgranskning.

## Redigera och kontrollera

Dokumentens källor finns i `content/`. Kör efter redigering:

```sh
python3 scripts/build.py
python3 scripts/verifiera.py
python3 scripts/check_site.py
```

Byggaren kräver Python 3.8 eller senare och inga paket. Den stöder en avgränsad Markdown-dialekt: rubriker, stycken, kodblock, platta listor, tabeller, länkar, fetstil och inline-kod. Lägg inte in rå HTML eller nästlade listor i dokumentkällorna.

Testsidornas HTML i `docs/testfall/` redigeras direkt. Bevara exakta teckenreferenser och test-ID:n. `scripts/verifiera.py` kontrollerar de ursprungliga strängarna och testmekanismerna. Det är inte ett uppläsningstest.

## Öppna lokalt

```sh
python3 -m http.server 8000 --directory docs
```

Öppna `http://localhost:8000/`. HTML-filerna kan också öppnas direkt utan server. Inga externa typsnitt, skript eller analysverktyg används.

## GitHub Pages

Allt publicerbart material finns i `docs/`, inklusive `.nojekyll`. Välj Settings → Pages → Deploy from a branch → main → /docs och spara när sidan ska publiceras. GitHub Pages kan användas från ett privat repo med en plan som stöder det; annars behövs ett offentligt repo. Ändra inte repots synlighet utan ägarens beslut.

Pages-webbplatsen kan bli offentlig även om repot är privat. Nuvarande underlag i `underlag/` ingår inte i webbplatsen. Förväntad adress efter aktivering är `https://fagerkod.github.io/siffror/`; adressen är inte ett påstående om att publicering har genomförts.

Källor: [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) och [publiceringskälla](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Ursprung och status

Utgår från den lokala riktlinjen version 2 och befintliga testfall. Originalriktlinje och originalobservationer bevaras i `underlag/` som historik, inte aktuell vägledning.

Version 3 är faktakontrollerad 2026-10-22. Se `content/kallor.md` för rättelser och primärkällor. Nya praktiska skärmläsarkörningar återstår. Inga syntetiska eller automatiskt antagna uppläsningsresultat har lagts till.
