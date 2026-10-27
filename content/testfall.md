# Krav och praktiska exempel

Varje exempel följer kortguiden: krav, implementation och förväntat testresultat. Börja med den uppgift som du utvecklar eller testar.

## Hitta rätt exempel

| Krav i kortguiden | Exempel på webbplatsen | Förväntad information eller funktion |
| --- | --- | --- |
| Begripliga belopp och saldo | [Belopp och konto](testfall/index.html#belopp) | Rätt belopp, decimalvärde, valuta och konto. |
| Negativt skiljs från positivt | [Negativt saldo](testfall/index.html#minus) | Värdet uppfattas som negativt vid vanlig läsning. |
| Noll, saknad uppgift och laddning skiljs åt | [Tre olika tillstånd](testfall/index.html#tillstand) | Saknad eller ännu inte hämtad information blir inte noll. |
| Nödvändig precision bevaras | [Decimaler](testfall/index.html#precision) | Rätt värde och möjlighet att granska alla nödvändiga decimaler. |
| OCR, konto och IBAN bevaras | [Nummer och inmatning](testfall/identifierare.html#ocr-exempel) | Hela följden, inklusive nollor och bokstäver, går att kontrollera. |
| Telefonnummer går att använda | [Telefonlänk](testfall/identifierare.html#telefon) | Samma nummer visas och används i länkmålet. |
| Maskering är begriplig | [Kortets sista siffror](testfall/identifierare.html#maskering) | Det framgår att endast de sista siffrorna visas. |
| Enhet och betydelse framgår | [Ränta och datum](testfall/index.html#betydelse) | Årsränta, procentenheter och bokföringsdag går att skilja åt. |
| Information fungerar i komponenter | [Kontotabell](testfall/index.html#konton) och [betalningsövning](testfall/sammanhang.html#betalning) | Rubriker, etiketter och knappnamn ger rätt sammanhang. |
| Ändrade värden är aktuella överallt | [Betalningsövning](testfall/sammanhang.html#betalning) | Fält, sammanställning och knapptext stämmer efter ändringen. |
| Kopiering och redigering fungerar | [OCR-fält och kopieringsknapp](testfall/identifierare.html#ocr-exempel) | Inledande nollor bevaras, markören fungerar och tomt blir inte noll. |

## Bedöm det du hör

| Observation | Bedömning |
| --- | --- |
| Telefonnumret läses i grupper eller decimaldelen som ören | Okej om rätt information går att förstå och kontrollera. |
| Ett långt OCR-nummer behöver teckennavigering | Kan vara okej om hela numret går att kontrollera praktiskt. |
| Ett vanligt saldo kräver teckennavigering för att förstås | Behöver utredas. |
| Minus, en siffra eller nödvändigt sammanhang saknas | Inte godkänt för den aktuella kontrollen. |
| Talvisaren visar rätt text men det hörda talet är oklart | Behöver utredas. Talvisaren räcker inte som underlag. |

## Prova även gränsfallen

Klistra in ett OCR-nummer med inledande nolla och mellanslag. Redigera mitt i fältet och töm det. Kopiera till ett annat fält och jämför. Byt konto, belopp och valuta i betalningsövningen. Använd smal skärm och förstoring och kontrollera att hela uppgiften går att nå.

Exemplen ersätter inte testning av bankens faktiska komponenter, formatregler och flöden. Anteckna testdata, produktversion, operativsystem, webbläsare, skärmläsare, röst, relevanta inställningar och ditt resultat.
