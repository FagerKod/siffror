# Siffror och tal med skärmläsare

Gemensam vägledning för testare och utvecklare. Version 3, 22 oktober 2026.

**Visa siffror och tal som vanlig, läsbar text. Låt samma text vara tillgänglig för hjälpmedel. Skapa inte alternativa uttal med `aria-label`, dolda dubbletter eller utskrivna sifferord.**

Skärmläsare behöver inte läsa ett värde med samma ord, pauser eller gruppering. Det viktiga är att användaren får rätt information: hela värdet eller sifferföljden, dess betydelse och det sammanhang som behövs. När exakta siffror behövs ska de också gå att kontrollera.

Vägledningen gäller svenska webbgränssnitt. Den beskriver vår rekommenderade arbetspraxis. Standardkrav är särskilt utpekade och källbelagda. Tidigare testobservationer finns separat under [Resultat](resultat.html); de är inte garantier för andra miljöer.

## Gemensam grundprincip

### Vad betyder att allt ska bli uppläst

Ett saldo på `1 234,50 kr` får läsas som ett sammanhängande belopp. Siffrorna behöver inte uttalas en i taget. Ett telefonnummer får läsas siffervis eller gruppvis, så länge hela numret går att uppfatta och verifiera, inklusive den inledande nollan.

Det är informationen som ska komma fram. Ett mellanrum behöver inte sägas som ”mellanslag”. Ett kommatecken kan förmedlas genom ett begripligt decimaluttryck. Däremot får `−134,50 kr` inte uppfattas som ett positivt saldo, och en maskerad kortuppgift får inte uppfattas som ett fullständigt kortnummer.

När användaren behöver den exakta representationen, exempelvis ett OCR-nummer eller alla visade decimaler, räcker det inte att siffrorna finns någonstans i koden. Kontrollera att de faktiskt går att läsa och verifiera med hjälpmedlet.

### Vad vi styr och vad användaren styr

Vi styr innehåll, textordning, språkangivelse, HTML-struktur, namngivning av kontroller och om information döljs för hjälpmedel. Skärmläsare, webbläsare, talsyntes, röst och inställningar påverkar hur informationen presenteras. Skiljeteckennivån kan exempelvis påverka vilka symboler som sägs. [K1](kallor.html#k1) [K2](kallor.html#k2)

Vi ska inte bygga en egen uttalsversion för varje röst. Vi ska heller inte avfärda ett användningsproblem bara för att HTML-koden ser korrekt ut. Börja med tydligare synligt innehåll och rätt struktur när information är svår att förstå.

## För testare

### Vad ska gå att uppfatta

Tabellen beskriver vad som ska gå att kontrollera. Exemplen är inga manus för exakt uppläsning.

| Typ av information | Exempel | Kontrollera detta |
| --- | --- | --- |
| Belopp och saldo | `1 234,50 kr` | Rätt storlek, decimalvärde, valuta och vilket saldo eller belopp det gäller. ”Femtio öre” kan förmedla decimaldelen utan att siffrorna sägs separat. |
| Negativa värden | `−134,50 kr` | Det framgår att värdet är negativt. Färg ensam får inte bära betydelsen. |
| Antal | `1 234 deltagare` | Rätt antal och vad som räknas. Annan gruppering i talet är inte i sig ett fel. |
| Decimaler och precision | `0,3120 euro` | Rätt decimalvärde. Alla visade decimaler, inklusive slutnollan, går att kontrollera om precisionen behöver verifieras. |
| Telefonnummer | `070 123 45 67` | Hela sifferföljden i rätt ordning, inklusive inledande nolla. Kontrollera även landsnummer när det visas. |
| OCR och kontonummer | `1234 5678 9012 3456` | Varje siffra går att verifiera. Kontrollera kopiering separat om uppgiften ska användas vidare. |
| Personnummer och andra identifierare | `19770311-0376` | Hela identifieraren kan kontrolleras. Skilj på formatavskiljare och tecken som faktiskt skiljer två identifierare åt. |
| Maskerade nummer | `Kort som slutar på 5963` | De synliga siffrorna och att resten inte visas framgår. Dolda siffror ska inte avslöjas för hjälpmedel. |
| Procent och mått | `12,5 %`, `45 m²` | Talet och enhetens betydelse framgår. Kvadratmeter får inte bli meter. |
| Årtal och versioner | `1995`, `2.1.4` | Rätt år eller versionsbeteckning kan identifieras. Kräv inte ett bestämt sätt att säga årtalet. |

`0,312` och `0,3120` har samma matematiska värde, men den skrivna precisionen kan vara viktig. Bedöm både värdet och möjligheten att granska representationen när uppgiften kräver det.

### Så bedömer du ett resultat

1. Läs innehållet i sitt sammanhang med skärmläsarens vanliga läsning. Kontrollera värde, tecken, enhet och vilken uppgift siffrorna hör till.
2. Navigera direkt till innehållet. För länkar, knappar och fält kontrollerar du även vad som hörs när de får fokus. Vanlig statisk text behöver inte vara nåbar med Tab.
3. Om exakta siffror är otydliga, använd ord- eller teckennavigering. Kontrollera hela följden, inte bara början och slutet. Notera om detta krävs för att lösa uppgiften och hur väl det fungerar.
4. Vid en avvikelse: spara miljö, textunderlag, det faktiskt hörda talet och navigeringssättet. Jämför sedan relevanta inställningar och andra stödda miljöer.

| Utfall | Bedömning och nästa steg |
| --- | --- |
| Olika uttal, samma begripliga information | Godtagbart för denna kontroll. Ingen ändring behövs enbart för att få likadant uttal. |
| Exakt följd går att kontrollera, men arbetet är omständligt | Dokumentera användbarheten. Teckennavigering är ett möjligt arbetssätt, inte ett automatiskt frikort. Bedöm det mot användarens uppgift. |
| En siffra, ett tecken eller ett sammanhang saknas eller blir fel | Registrera en avvikelse och utred orsaken. Godkänn inte med hänvisning enbart till att originaltexten finns i DOM. |
| Underlaget är ofullständigt eller utfallet går inte att reproducera | Markera ”Ej bedömt” eller ”Behöver utredas”. Gissa inte ett godkänt resultat. |

För ett vanligt saldo bör värde och valuta vara begripliga vid normal läsning. För en lång identifierare kan mer detaljerad granskning behövas. Detta är vår bedömningsprincip, inte en regel i WCAG om ett visst antal tangenttryckningar.

### Vad är ett WCAG-fel

Ett annorlunda uttal visar inte i sig att ett WCAG-kriterium är brutet. Ett problem behöver kopplas till vad som faktiskt saknas eller är fel. WCAG anger inte ett gemensamt uppläsningsmanus för tal. Tekniken måste samtidigt ha tillgänglighetsstöd i de miljöer som lösningen förlitar sig på. [K3](kallor.html#k3)

| Kriterium | Exempel på vad du undersöker |
| --- | --- |
| 1.3.1 Information och relationer | Kan belopp kopplas till rätt konto, tabellrubrik eller fältetikett? [K4](kallor.html#k4) |
| 1.3.2 Meningsfull ordning | Är textens och strukturens läsordning korrekt när ordningen påverkar betydelsen? [K5](kallor.html#k5) |
| 1.4.1 Användning av färg | Visas negativt eller positivt värde på annat sätt än enbart med färg? [K6](kallor.html#k6) |
| 2.5.3 Etikett i namn | Ingår en knapps eller länks synliga textetikett i dess tillgängliga namn? Kravet gäller inte all statisk text. [K7](kallor.html#k7) |
| 3.1.1 och 3.1.2 Språk | Är sidans språk och relevanta språkbyten angivna? [K8](kallor.html#k8) [K9](kallor.html#k9) |
| 3.3.2 och 4.1.2 Formulär och kontroller | Finns begripliga etiketter och instruktioner, samt korrekt namn, roll och värde? [K3](kallor.html#k3) |
| 4.1.3 Statusmeddelanden | Kan hjälpmedel presentera en relevant statusuppdatering utan att flytta fokus? [K10](kallor.html#k10) |

Om en talsyntes flyttar ett valutaord i talet är det inte automatiskt ett fel i sidans läsordning enligt 1.3.2. Undersök både kod, exponering och användarens upplevelse innan du anger orsak och kriterium.

För konkreta kommandon och dokumentation av en körning, se [Testmanual](testmanual.html).

## För utvecklare

### Börja med vanlig text och tydligt sammanhang

```html
<html lang="sv">
<!-- Sidans övriga struktur utelämnad i exemplet. -->
<p>Sparkonto 3835789, saldo 1&#160;234,50 kr</p>
<p>Kort som slutar på 5963</p>
<a href="tel:+46701234567">070 123 45 67</a>
<button type="button">Betala 1&#160;234,50 kr</button>
```

Exemplen visar markupmönster. Lägg knappens faktiska funktion i applikationen. Använd tabellrubriker när uppgifterna presenteras i en datatabell, och synliga, kopplade etiketter för inmatningsfält.

`lang="sv"` ger hjälpmedlet möjlighet att välja svenska uttalsregler. Det garanterar inte en viss röst eller uppläsning. Märk upp verkliga språkbyten; byt inte språk på ett tal för att få ett önskat uttal. Undantagen i 3.1.2 omfattar bland annat egennamn och tekniska termer. [K8](kallor.html#k8) [K9](kallor.html#k9)

### Formatera efter betydelse

| Information | Rekommenderad implementation |
| --- | --- |
| Belopp och antal | Använd en gemensam formatterad text med avsedd gruppering, decimaler och enhet. |
| Telefon, OCR och konto | Bevara som strängar. Välj gruppering som passar respektive identifierare och användningssätt; fyrgrupper är ingen universell regel. |
| Personnummer | Bevara den avsedda identifieraren och tecknen enligt systemets formatregler. Byt inte bindestreck till andra tecken enbart för uttalets skull. |
| Årtal, version och husnummer | Använd inte generell tusentalsgruppering. |
| Maskering | Förklara synligt vad som visas, exempelvis ”Kort som slutar på 5963”. Exponera aldrig de maskerade siffrorna i en dold text. |

Vanligt mellanslag U+0020, hårt mellanslag U+00A0 och smalt hårt mellanslag U+202F ska inte antas ge identisk uppläsning överallt. Välj utifrån läsbarhet, radbrytning och kopiering, och testa den faktiska utdata som komponenten ger.

Hårda mellanslag kan hålla ihop delar av ett värde, men långa obrutna strängar får inte leda till att innehåll klipps bort eller hindrar reflow. Kontrollera små vyer och förstoring. [K11](kallor.html#k11)

`Intl.NumberFormat` kan användas för lokalanpassad presentation. Ange avsedd precision: formatinställningar kan avrunda och ändra antalet visade decimaler. Återanvänd resultatet som text i gränssnittet, inte som en separat skärmläsarversion. [K12](kallor.html#k12)

```javascript
const formatSEK = new Intl.NumberFormat("sv-SE", {
  style: "currency",
  currency: "SEK",
  minimumFractionDigits: 2,
  maximumFractionDigits: 2
});

saldoElement.textContent = formatSEK.format(1234.5);
```

Exemplet förutsätter att `saldoElement` är ett befintligt element och att två decimaler är rätt för uppgiften. Det är en presentationsfunktion, inte en lösning för exakta finansiella beräkningar. Skicka inte OCR-nummer eller andra identifierare genom talformatteraren.

### Använd inte ARIA för att regissera uttalet

På vanliga `span`, `div` och `p` förbjuder de implicita rollerna namngivning med `aria-label` och `aria-labelledby`. Att en viss kombination ändå läser etiketten gör inte koden korrekt. Lägg inte till en roll enbart för att kringgå detta. [K13](kallor.html#k13)

På en knapp eller länk kan `aria-label` vara tillåtet, men ska inte användas som ett uttalsmanus. Den synliga textetiketten ska ingå i det tillgängliga namnet. Behåll därför normalt knappens eller länkens text som namn. Detta är inget generellt förbud mot ARIA; exempelvis kan `aria-describedby` koppla en hjälpinstruktion till ett fält. [K7](kallor.html#k7)

Skapa inte en synlig sträng och en dold, siffervis eller normaliserad dubblett som standardlösning. En sådan konstruktion ger två representationer att hålla synkroniserade och behöver särskild kontroll av kopiering, sökning, tal och punktskrift.

### CSS och betydelsebärande tecken

Lägg tal, enheter och betydelsebärande tecken i HTML-texten. CSS-avstånd som `letter-spacing` skapar inte nya tecken i textnoden. Däremot är påståendet att CSS-genererat innehåll aldrig når skärmläsare fel: stödet har förbättrats och det gamla WCAG-felexemplet F87 är indraget. Vår rekommendation är ändå att hålla uppgiften som vanlig text, bland annat för granskning och kopiering. [K14](kallor.html#k14)

Förväxla inte bindestreck med matematiskt minus. U+002D kan ha båda funktionerna; U+2212 är uttryckligen ett minustecken. U+2212 är därför inte ett otillåtet ”uttalsknep”. Välj ett semantiskt lämpligt tecken och testa uppläsning och datautbyte. Ingen av kodpunkterna garanterar ett visst uttal. [K15](kallor.html#k15)

Om ett negativt saldo är svårt att uppfatta, kan ett synligt förtydligande som ”Negativt saldo” hjälpa alla. Använd bara formuleringar som stämmer med verksamhetens betydelse; negativt saldo och skuld är inte alltid utbytbara begrepp.

### Inmatning och kopiering

Använd normalt `type="text"` för sifferidentifierare och `type="tel"` för telefoninmatning. `type="number"` är avsett för numeriska värden, inte varje sträng som består av siffror. `inputmode` ger en tangentbordshint, inte validering. [K16](kallor.html#k16) [K17](kallor.html#k17)

```html
<label for="ocr">OCR-nummer</label>
<p id="ocr-hjalp">Du kan klistra in numret med mellanslag.</p>
<input id="ocr" name="ocr" type="text"
       inputmode="numeric" aria-describedby="ocr-hjalp">
```

Hjälptexten i exemplet förutsätter att applikationen verkligen accepterar mellanslag. Implementera normalisering och validering även på serversidan. Ta bara bort avskiljare som formatet tillåter; använd inte en generell funktion som raderar alla icke-siffror. Bevara inledande nollor och betydelsebärande tecken.

Vår standard är att inte lägga in grupperingsmellanslag vid varje tangenttryckning. Om automatisk formatering behövs, kontrollera redigering mitt i värdet, markörposition, inklistring, felmeddelanden och skärmläsarens återkoppling.

En kopieringsknapp kan kopiera ett korrekt råvärde. Det är en extra hjälp, inte en ersättning för läsbar text. Kontrollera också vanlig markering och kopiering. Meddela resultatet av kopieringen tillgängligt, och visa inte ”Kopierat” om kopieringen misslyckas.

### Uppdateringar och undantag

Ett belopp som ändras behöver inte alltid annonseras automatiskt. När ändringen är ett statusmeddelande, exempelvis resultatet av en beräkning, behöver det kunna förmedlas utan att fokus flyttas. En synlig statusregion kan användas för detta. `aria-live` styr annonsering av ändringar, inte uttalet av siffror. [K10](kallor.html#k10)

Tekniska undantag kräver ett dokumenterat problem och prövas först när tydligare synlig text och struktur inte räcker. Om synligt innehåll döljs med `aria-hidden="true"` måste likvärdig information och funktion fortfarande nå hjälpmedel. Dölj inte fokuserbara kontroller eller deras föräldrar. [K18](kallor.html#k18)

Ett undantag ska beskriva problemet, varför en innehållslösning inte räcker, den exakta alternativa representationen och testade miljöer. Kontrollera synlig text, tillgängligt namn, teckennavigering, kopiering och relevanta punktskriftsflöden. Ett lyckat test av dubbletttekniken för ett belopp bevisar inte att den passar alla identifierare eller kontroller.

## När är arbetet klart

Testare och utvecklare ska kunna svara ja på följande i de överenskomna testmiljöerna:

- Samma korrekta uppgift visas och exponeras för hjälpmedel, utan en särskild uttalsversion.
- Hela värdet eller identifieraren och nödvändigt sammanhang går att uppfatta och kontrollera.
- Negativt tecken, decimaler, valuta, enhet och eventuell maskering förmedlas när de behövs.
- Länkar, knappar, tabeller och fält fungerar i sina respektive användningssätt.
- Skillnader i uttal har skilts från informationsförlust och praktiska användningsproblem.
- Resultatet är dokumenterat med miljö och inställningar. Kvarstående avvikelser är uttryckliga.

Se [Testfall](testfall.html), [Testmanual](testmanual.html), [Resultat](resultat.html) och [Källor och faktakontroll](kallor.html).
