# Testfall för uppläsning

Testsviten innehåller 21 jämförelsefall. Test-ID:n, siffersträngar, separatorer och de prövade HTML-elementen är bevarade från originalet. Sidornas instruktioner och navigering har uppdaterats i version 3.

## Tre testsidor

- [Del ett — belopp och identifierare, tc-01 till tc-07](testfall/index.html)
- [Del två — telefonnummer, decimaler och maskering, tc-08 till tc-11](testfall/identifierare.html)
- [Del tre — tecken och sammanhang, tc-12 till tc-21](testfall/sammanhang.html)

Läs [testmanualen](testmanual.html) innan du börjar. Använd [resultatmallen](resultatmall.html) för en körning per miljö.

## Vad jämförs

| Testfall | Innehåll |
| --- | --- |
| tc-01–03 | Samma belopp med hårt mellanslag, vanligt mellanslag och utan gruppering. |
| tc-04–05 | Samma 16-siffriga identifierare med och utan gruppering. |
| tc-06 | Synlig text med aria-hidden och en visuellt dold dubblett. En mekanismjämförelse, inte rekommenderad standardlösning. |
| tc-07 | aria-label på span. Avsiktligt felaktig ARIA-användning för observation, aldrig en godkänd implementationsmall. |
| tc-08–11 | Telefonnummer, decimalvärde, personnummerliknande sträng och maskerat nummer. |
| tc-12–13 | Negativa belopp med U+002D respektive U+2212. |
| tc-14–15 | Grupperat decimalbelopp och valutakod. |
| tc-16–18 | Telefonlänk, betalningsknapp utan funktion och belopp i tabell. |
| tc-19–21 | Procent, kvadratmeter och smalt hårt mellanslag. |

Teststrängarna är endast till för observation. Aktivera inte telefonlänken. De är inte validerade som verkliga OCR-, kort- eller personnummer.

## Tekniska detaljer finns för alla

Varje fall har en stängd detaljruta. Öppna den efter att du dokumenterat uppläsningen. Rutorna är tillgängliga även för den som använder skärmläsare; de är inte dolda med aria-hidden.

Detaljrutorna visar faktisk markup. Teststrängen ändras inte när en ruta öppnas. Ingen JavaScript-kod körs på testsidorna.

## Vad sviten inte täcker

Sviten är ett stöd för undersökning, inte en fullständig kravgranskning. Komplettera i tjänstens riktiga gränssnitt med inmatning, kopiering, statusändringar, zoom, små vyer, relevanta gränsvärden, mobil och punktskrift.
