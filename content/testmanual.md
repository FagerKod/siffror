# Prova med skärmläsare

Använd NVDA med en stödd webbläsare på Windows eller VoiceOver med Safari på iPhone. Välj svensk röst och anteckna versioner och inställningar om du dokumenterar ett resultat. Kommandona nedan avser standardinställningar.

## NVDA på Windows

Starta NVDA och öppna ett av [exemplen](testfall.html). NVDA-tangenten är vanligtvis Insert eller Caps Lock beroende på inställning.

| Gör så här | Kontrollera |
| --- | --- |
| Tryck H i bläddringsläge för nästa rubrik. Läs vidare med nedåtpil. | Beloppets värde, valuta och sammanhang framgår. |
| Använd vänster och höger pil i texten. | Hela numret går att granska tecken för tecken när det behövs. |
| Använd Tab till fält och knappar. | Etikett, roll, värde och knappens funktion framgår. Statisk text behöver inte nås med Tab. |
| Växla vid behov med NVDA+Mellanslag. | Bläddringsläge används för läsning och fokusläge för inmatning. |
| Använd Ctrl+Alt+piltangenter i kontotabellen. | Beloppet kan kopplas till rätt rad och kolumn. |

Fyll i OCR-fältet, redigera mitt i numret och töm det. Prova sedan betalningsövningen och lyssna efter återkoppling när du aktiverar knappen. NVDA:s talvisare under Verktyg kan hjälpa vid dokumentation, men lyssna också på det faktiska talet.

## VoiceOver på iPhone

Slå på VoiceOver under Inställningar, Hjälpmedel, VoiceOver. Öppna sidan i Safari.

1. Svep åt höger med ett finger för att gå framåt genom innehållet. Svep åt vänster för att gå tillbaka.
2. Använd rotorns Rubriker för att hitta ett exempel. Vrid två fingrar som ett vred, välj Rubriker och svep uppåt eller nedåt.
3. Gå till numret. Välj Tecken i rotorn och svep nedåt för nästa tecken, uppåt för föregående. Kontrollera alla grupper. Om Tecken saknas, lägg till det i rotorinställningarna.
4. Markera ett fält eller en knapp och dubbeltryck för att aktivera. Prova inmatning, kopiering och betalningsövningens återkoppling.

För ett vanligt saldo ska informationen vara begriplig vid vanlig läsning. Teckennavigering är främst ett stöd för att kontrollera exakta följder eller precision. Den ersätter inte ett begripligt saldo.

## Vad räknas som ett bra resultat

Rätt uppgift går att förstå, nödvändiga detaljer går att kontrollera och uppgiften går att genomföra. Annan gruppering, pauser eller ord som ”femtio öre” är inte i sig fel.

Om minus, siffror eller sammanhang saknas ska det utredas. Notera vilken navigering du använde och vad du faktiskt hörde. Ändra inte inställningar utan att notera det. Bedöm även om det är praktiskt rimligt att kontrollera uppgiften.

## Dokumentera vid behov

Anteckna exemplet och testdata, sidans version, datum, operativsystem, webbläsare, skärmläsare, röst, språk och symbolnivå. Beskriv vad du gjorde, vad du hörde och om informationen gick att förstå och kontrollera. Håll text från talvisaren och hört tal åtskilda.

Det finns inget gemensamt uppläsningsmanus som alla röster måste följa. [Bedömningsöversikten](testfall.html#bedom-det-du-hor) sammanfattar vad som är okej och vad som behöver utredas.

## Kommandon och produktmanualer

[NVDA:s användarhandbok](https://api.nvaccess.org/documentation/userGuide.html) beskriver bläddringsläge, textgranskning och tabellnavigering. [Apples guide till VoiceOver-rotorn](https://support.apple.com/en-ca/111796) beskriver rubriker, tecken och gester. Anpassade kommandon kan skilja sig från exemplen här.
