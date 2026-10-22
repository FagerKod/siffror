# Resultat och kvarstående tester

De tidigare observationerna nedan kommer från projektets ursprungliga testanteckningar. De har inte körts om vid faktakontrollen den 22 oktober 2026. Skärmläsarversioner, OS-versioner, webbläsarversioner, röster och symbolinställningar saknas för de ursprungliga körningarna.

**Status: historiska observationer med ofullständig miljöinformation.** De visar vad som antecknades, inte hur alla versioner av NVDA eller VoiceOver fungerar.

## Tidigare observationer

| Testfall | VoiceOver på macOS | NVDA på Windows |
| --- | --- | --- |
| tc-01–03, grupperade och ogrupperade belopp | Samma sammanhängande belopp antecknat i alla tre fall. | Samma sammanhängande belopp antecknat i alla tre fall. |
| tc-04, grupperad identifierare | Fyra talgrupper antecknade. | Svårtolkad transkription. Kan inte användas för säker slutsats om sifferföljden. |
| tc-05, ogrupperad identifierare | Siffervis uppläsning antecknad. | Uppläsning som stort heltal antecknad. Praktisk verifierbarhet är inte testad. |
| tc-06, dold alternativ text | Beloppet antecknat en gång. | Beloppet antecknat en gång. |
| tc-07, aria-label på span | Dubbel uppläsning och ”grupp” antecknat. | Ett belopp antecknat; det visar inte vilken textrepresentation som användes. |
| tc-08, telefonnummer | Inledande nolla antecknad; den visuella gruppen 123 återgavs som ”ett tjugotre”. | Inledande nolla och gruppvis läsning antecknade. |
| tc-09, decimaler | ”noll euro komma tre ett två noll” antecknat. | ”noll komma tre ett två noll euro” antecknat. |
| tc-10, personnummerliknande sträng | Strecket saknas i transkriptionen. | Strecket återgavs som ”till”. |
| tc-11, maskering | Åtta stjärnor antecknade. | Inga asterisker antecknade. Orsaken är inte fastställd. |

De ursprungliga anteckningarna bevaras oförändrade i repots `underlag/testresultat-original.md`. Exemplen är teststrängar för uppläsning och ska inte användas för att initiera betalningar, samtal eller identifiering av personer.

## Vad resultaten inte visar

De bevisar inte att separatorer alltid är betydelselösa, att identifierare aldrig kan formateras användbart, att ett bindestreck aldrig uttalas som minus eller att teckennavigering alltid fungerar praktiskt. De visar inte heller att U+2010 skulle hjälpa eller inte hjälpa; den varianten testades inte.

För tc-06 går det inte att bevisa vilken representation som lästes enbart genom ett identiskt uttal. Teknisk inspektion och separata mekanismtester kan behövas. För tc-07 är standardfrågan redan avgjord: namngivning på ett vanligt span är förbjuden, oavsett uppläsningsresultat. [K13](kallor.html#k13)

## Återstår att verifiera

| Område | Nästa kontroll |
| --- | --- |
| Tidigare testfall tc-01–11 | Nya reproducerbara körningar med fullständig metadata. Prioritera avvikelserna men uteslut inte övriga fall. |
| tc-04 | Spara paneltext och hört tal var för sig. Rekonstruera sifferföljden utan att anta att den äldre transkriptionen var korrekt eller felhörd. |
| Teckennavigering | Kör framför allt tc-04, tc-05, tc-09, tc-10 och tc-11. Bedöm både åtkomst och praktisk användbarhet. |
| tc-12 och tc-13 | Kontrollera negativa belopp med U+002D respektive U+2212. |
| tc-14–21 | Decimaler, valutakod, telefonlänk, knapp, tabell, procent, kvadratmeter och smalt hårt mellanslag. Inga resultat finns i underlaget. |
| Symbolnivå | Kör maskering och negativa värden med dokumenterade nivåer. |
| Mobil och punktskrift | Egna körningar krävs innan slutsatserna utvidgas till dessa användningssätt. |
| Verkliga komponenter | Kontrollera även inmatning, kopiering, layout, statusändringar, nollvärden, långa värden och inledande nollor. De 21 statiska fallen täcker inte detta fullt ut. |

## Nya resultat

Inga nya skärmläsarresultat har lagts till. Använd [resultatmallen](resultatmall.html) och dokumentera en körning per miljö. Källkontroll och automatisk kodverifiering ska inte registreras som godkända uppläsningstester.
