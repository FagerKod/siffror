# Källor och faktakontroll

Faktakontrollerad 22 oktober 2026 mot primärkällor från W3C, WHATWG, NV Access, Apple, Google, Unicode och Ecma. Utgångspunkt: den mer utvecklade lokala versionen av riktlinje 2 samt projektets testkod och anteckningar.

Standardtexter avgör vad attribut och kriterier betyder. Produktmanualer beskriver kommandon och inställningar. Ingen av dessa källtyper bevisar ett visst svenskt uttal av våra teststrängar; sådana påståenden kräver dokumenterade praktiska tester.

## Rättelser och avgränsningar

| Påstående eller instruktion i underlaget | Resultat av granskningen |
| --- | --- |
| Korrekt HTML och språk betyder att vårt ansvar är färdigt | För kategoriskt. Tillgänglighetsstöd och praktisk åtkomst måste också bedömas. K3. |
| Alla separatorer ger samma uppläsning | Begränsat till antecknade körningar av tc-01–03. U+202F och andra miljöer är inte därmed verifierade. |
| Ingen formatering av identifierare kan fungera i båda skärmläsarna | Kan inte härledas från två testvarianter och ofullständigt dokumenterade miljöer. Ersatt med uppgiftsbaserad bedömning. |
| Alla siffror finns i textnoden, alltså är åtkomsten tillräcklig | Inte visat. Teckengranskning och praktisk verifiering återstår. |
| aria-label på span är opålitligt | Starkare och mer precis regel: namngivning är förbjuden för elementets implicita roll. K13. |
| CSS-genererat innehåll når inte hjälpmedel | Fel som generell regel. F87 är indraget. CSS-avstånd ska skiljas från genererat textinnehåll. K14. |
| Bindestreck uttalas inte som minus och U+2010 skulle inte hjälpa | Utfallet är kontext- och miljöberoende; U+2010 testades inte. U+2212 är ett riktigt matematiskt minustecken. K15. |
| Alla alternativa Unicode-tecken ska undvikas | Ersatt med semantiskt lämpliga tecken, formatkrav och tester. Ett generellt förbud skulle även träffa riktiga minustecken och hårda mellanslag. |
| Asteriskerna försvann på grund av NVDA:s symbolnivå | Möjlig förklaring, inte konstaterad orsak när inställningen saknas. K1. |
| Dold text plus aria-hidden är en generellt godkänd undantagsteknik | Mekanismen kräver likvärdig information, rätt användning och tester i sitt sammanhang. K18. |
| Kopiering får alltid med båda textversionerna | Beror på konstruktion, markering och miljö. Nu en kontrollpunkt, inte ett universellt resultat. |
| NVDA+Numpad 1/2/3 granskar tecken | Fel för stationär standardlayout. Kommandona är Numpad 1/2/3 utan NVDA. K1. |
| VO+Högerpil stegar tecken | Beskriver inte generellt teckennavigering; i text är det ett ordkommando. K20–21. |
| VO+W verifierar hela ett grupperat nummer | Bokstavering gäller aktuellt ord. Alla grupper måste granskas. K20. |
| VoiceOvers skiljeteckennivå finns under Tal | Aktuell guide anger Utförlighet, Text. K2. |
| TalkBacks läskontroller öppnas med upp och höger | Rättat till upp–ned eller ned–upp; därefter väljs Tecken. K23. |
| Talvisaren är en exakt utskrift av hur talsyntesen uttalar talet | Otillräckligt underlag för uttalsanalys. Text och hört tal hålls isär. |
| De äldre testfallen ska inte köras om | Rättat. Fullständigt dokumenterade omkörningar behövs för reproducerbart beslutsunderlag. |
| Om testaren inte kan skriva numret ur minnet fungerar inte teckennavigering | Ersatt med att skriva under granskningen och slutföra en realistisk uppgift. |
| Teknikrutorna ska döljas för alla hjälpmedelsanvändare | Ersatt med stängda details-element som alla kan öppna efter sin observation. Teststrängarna är bevarade. |

## K1

[NVDA User Guide](https://api.nvaccess.org/documentation/userGuide.html). Avsnitten Browse Mode, Reviewing Text, Punctuation/Symbol Level och Speech Viewer. Den lästa guiden anger NVDA 2026.2; använd guiden för installerad version vid avvikelser.

## K2

[Apple om skiljetecken i VoiceOver](https://support.apple.com/en-euro/guide/voiceover/vod1f1248b5e/mac). Inställningar och egna skiljeteckengrupper.

## K3

[WCAG 2.2](https://www.w3.org/TR/WCAG22/). Normativa kriterier och avsnitt 5.2.4 om tillgänglighetsstöd. Vägledningen gör ingen fullständig WCAG- eller EN 301 549-granskning av en produkt.

## K4

[Understanding 1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html). Samband och struktur ska kunna uppfattas även utan den visuella presentationen.

## K5

[Understanding 1.3.2 Meaningful Sequence](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence.html). Meningsbärande läsordning.

## K6

[Understanding 1.4.1 Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html). Färg får inte vara enda visuella informationsbärare.

## K7

[Understanding 2.5.3 Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html). Synlig textetikett och tillgängligt namn på kontroller. Avser inte ett krav på identiskt hörbart uttal.

## K8

[Understanding 3.1.1 Language of Page](https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html). Sidans språk ger förutsättningar för språkanpassad presentation.

## K9

[Understanding 3.1.2 Language of Parts](https://www.w3.org/WAI/WCAG22/Understanding/language-of-parts.html). Språkbyten och undantag.

## K10

[Understanding 4.1.3 Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html). Omfattar statusmeddelanden enligt kriteriets definition, inte varje DOM-ändring.

## K11

[Understanding 1.4.10 Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html). Förstoring och smala vyer utan informationsförlust.

## K12

[ECMA-402, utgåva 13](https://402.ecma-international.org/13.0/). NumberFormat och precision. Ger ingen garanti för identisk talsyntesutdata.

## K13

[ARIA in HTML, avsnitt 4.1](https://www.w3.org/TR/html-aria/#naming). Förbud mot namngivning på roller som inte får namnges; exemplen omfattar span, div och p.

## K14

[W3C:s indragna felexempel F87](https://www.w3.org/WAI/WCAG21/Techniques/failures/F87). CSS-genererat innehåll innebär inte alltid ett WCAG-fel. Rekommendationen att använda riktig text här är ett robusthetsval.

## K15

[Unicode FAQ om skiljetecken och symboler](https://www.unicode.org/faq/punctuation_symbols.html). U+002D, U+2010 och U+2212 har olika definierade funktioner. Teckendefinitionerna säger inte hur en svensk röst uttalar varje sammanhang.

## K16

[HTML Standard om input type number](https://html.spec.whatwg.org/multipage/input.html#number-state-(type=number)). Skiljer numeriska värden från identifierare med siffror.

## K17

[HTML Standard om inputmode](https://html.spec.whatwg.org/multipage/interaction.html#attr-inputmode). Hint om lämplig inmatningsmekanism.

## K18

[WAI-ARIA 1.2 om aria-hidden](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden) och [ARIA in HTML](https://www.w3.org/TR/html-aria/). Döljning, likvärdig information och restriktioner för fokuserbara element.

## K19

[Apple om textpanel och punktskriftspanel](https://support.apple.com/en-euro/guide/voiceover/unac078/mac). Panelerna är stöd vid observation, inte dokumentation av våra utförda tester.

## K20

[Apple om textkommandon](https://support.apple.com/guide/voiceover/text-commands-cpvokys06/mac). Ord, tecken, bokstavering och modifierare.

## K21

[Apple om att läsa text](https://support.apple.com/guide/voiceover/read-text-vo2706/mac). Textgranskning; välj dokumentation för den macOS-version som används. Praktisk åtkomst till våra teststrängar återstår att testa.

## K22

[Apple om VoiceOver-rotorn på iPhone och iPad](https://support.apple.com/en-ca/111796). Granularitet och nästa/föregående objekt.

## K23

[Google om TalkBacks läskontroller](https://support.google.com/accessibility/android/answer/6007066?hl=en). Val av teckengranularitet och navigeringsgester.

## Så hålls innehållet aktuellt

Ändra rekommendationer när nya reproducerbara fynd motiverar det. Lägg nya observationer under Resultat med testversion och miljö. Ett påstående om vad en viss kombination faktiskt säger ska alltid gå att skilja från standardens krav och vår rekommenderade arbetspraxis.
