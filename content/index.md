# Siffror och skärmläsare

Fördjupning och praktiska exempel för testare och React-utvecklare. Utgå från kortguiden i Confluence och prova hur samma information fungerar med din skärmläsare.

**Samma korrekta information ska vara tillgänglig visuellt och för hjälpmedel. Olika uttal är okej om uppgiften går att förstå, kontrollera och använda.**

## Välj ett område

| Område | Det får du prova |
| --- | --- |
| [Belopp och saldo](testfall/index.html) | Belopp, minus, noll, saknad uppgift, decimaler och flera konton. |
| [Nummer och inmatning](testfall/identifierare.html) | OCR, kontonummer, IBAN, telefonnummer, maskering och kopiering. |
| [Komponenter och ändrade värden](testfall/sammanhang.html) | En betalningsövning med konto, belopp, valuta och tillgänglig återkoppling. |

## Så använder du sidan

1. Läs kravet och vad exemplet ska förmedla.
2. Starta NVDA på Windows eller VoiceOver på iPhone. Följ [kom igång med skärmläsare](testmanual.html).
3. Läs och använd det fungerande exemplet. Kontrollera informationen och funktionen, inte ett bestämt uttal.
4. Öppna HTML-exemplet och läs förklaringen för utvecklare.

Exemplen använder påhittade uppgifter och genomför inga betalningar. Inmatningen behandlas endast på sidan och sparas inte. Använd exempeluppgifter när du provar. Telefonlänken kan öppna telefonens samtalsfunktion; du behöver inte ringa för att testa den.

## Från kortguide till fördjupning

Confluence är den kortfattade guiden med krav, implementation och förväntat testresultat. Här finns samma principer omsatta i exempel och övningar. [Översikten](testfall.html) visar vilket exempel som hör till vilket krav. [För utvecklare](vagledning.html) förklarar HTML, React och formatering.

Sidan visar implementationsmönster. Ett visst uttal eller ett godkänt resultat i din miljö är inte utlovat. Lyssna och kontrollera med de versioner, röster och inställningar som ska stödjas i tjänsten.
