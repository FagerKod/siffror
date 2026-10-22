# Uppläsning och presentation av siffror

Version 2. Bygger på testresultat från VoiceOver på macOS och NVDA på Windows, se Bilaga A.

## Kortversion, gör så här

### Grundregel

**Samma sträng visas visuellt och exponeras för hjälpmedel. Vi skapar inte alternativa skärmläsartexter för att styra uttalet.**

Formatera siffror så att de är lätta att läsa visuellt. Sätt korrekt språk på sidan. Därefter är uppläsningen skärmläsarens och användarens sak.

Tester visar att tusentalsgruppering inte försämrar uppläsningen. Ett belopp som visas `1 345 876 kr` läses som ett sammanhängande värde av både VoiceOver och NVDA, oavsett om separatorn är hårt eller vanligt mellanslag. Det finns alltså inget skäl att ge hjälpmedel en egen version av talet.

### Formatera efter vad siffrorna betyder

| Typ | Gör så här | Exempel |
| --- | --- | --- |
| Belopp, saldo, antal och andra numeriska värden | Gruppera långa tal i tresiffriga grupper | `1 345 876 kr` |
| Telefonnummer | Följ etablerad svensk formatering | `070 123 45 67` |
| OCR-, konto- och referensnummer | Gruppera för visuell läsbarhet | `1234 5678 9012 3456` |
| Personnummer | Behåll vanligt bindestreck, U+002D | `19770311-0376` |
| Decimaltal | Vanligt kommatecken, ingen gruppering av decimaldelen | `0,3120 euro` |
| Årtal, versionsnummer, husnummer och liknande | Gruppera inte | `1995`, `version 2.1.4` |

Grupperingen ska vara riktiga tecken i textnoden. Skapa den inte med CSS, `letter-spacing`, `word-spacing` eller genererat innehåll, eftersom sådana mellanrum inte existerar för hjälpmedel.

För belopp kan hårt mellanslag, U+00A0, användas så att talet inte bryts över radslut. För identifierare är vanligt mellanslag lämpligare eftersom det fungerar bättre vid kopiering och inklistring.

### Detta ska du inte göra

* Inte `aria-label` på ett `span` eller annat element utan roll. Testat och underkänt: VoiceOver läser både etiketten och textinnehållet, alltså värdet två gånger, och bokstaverar dessutom enheten. NVDA ger oförutsägbart resultat.
* Inte visuellt dolda dubbletter enbart för att påverka uttalet.
* Inte alternativa Unicode-tecken, exempelvis U+2010 i stället för vanligt bindestreck.
* Inte utskrivna uttalstexter som `en miljon trehundrafyrtiofemtusen åttahundrasjuttiosex kronor` eller `ett tre fyra fem åtta sju sex`.

### Gruppera presenterat innehåll, inte redigerbara fält

Lägg som standard inte in grupperande mellanslag i ett `input` medan användaren skriver. Det påverkar markörposition, validering, `pattern`, inklistring och skärmläsarens återkoppling. Formatera värdet när det presenteras efter inmatning.

### Tänk på kopiering

Mellanslagen följer med när användaren markerar och kopierar ett grupperat OCR-nummer. En kopieringsknapp kan lämna råvärdet, men den hjälper bara den som hittar och använder den. Egna formulär som tar emot OCR- och kontonummer ska normalisera whitespace vid inklistring.

### Maskerade nummer

Skriv informationen tydligt för alla:

`Kort som slutar på 5963`

Detta är förstahandsvalet och det är ett design- och innehållsbeslut, inte en teknisk fix. Skälet är konkret: NVDA hoppar över asteriskerna helt i `5226 **** **** 5963`. Användaren hör bara de synliga siffrorna och får ingen antydan om att något är dolt.

Om den maskerade formen måste behållas visuellt hanteras det som ett dokumenterat undantag, se avsnittet Teknik för dokumenterade undantag.

### Gör sammanhanget tydligt

Undvik:

`Sparkonto 3835789 134,50 kr`

Skriv hellre:

`Sparkonto 3835789, saldo 134,50 kr`

Beskrivande ord som saldo bör vara synliga, eftersom sammanhanget hjälper alla användare.

### Deklarera rätt språk

```html
<html lang="sv">
```

Innehåll på annat språk märks upp separat. Språkdeklarationen gör att rätt talsyntes och uttalsregler används. Den garanterar inte ett visst uttal.

## Var går gränsen för vårt ansvar

Det här är riktlinjens svåraste fråga, och testerna besvarar den.

När HTML är korrekt kodad och språket deklarerat har vi gjort det som ligger inom vår kontroll. Uppläsningen skapas därefter av hjälpmedlet, talsyntesen, rösten och användarens egna inställningar. Att samma sträng låter olika i olika skärmläsare är normaltillståndet, inte ett fel.

Vi skiljer på tre nivåer.

**Nivå 1, informationen går fram men uttalas olika.** Ingen åtgärd. Uttalsskillnader mellan skärmläsare är inte vårt problem att lösa och kan inte lösas robust.

**Nivå 2, informationen finns men är svår att använda.** Åtgärda med innehåll, sammanhang och etiketter. Inte med markup som ändrar vad hjälpmedlet får. Ett långt OCR-nummer läses obegripligt i NVDA oavsett formatering, men siffrorna finns i textnoden och användaren kan läsa dem tecken för tecken.

**Nivå 3, informationen förmedlas inte alls.** Här är ett undantag motiverat. I testerna gäller det endast maskerade nummer i NVDA, där asteriskerna försvinner.

Även på nivå 3 gäller att lösningen i första hand ska ligga i innehållet. Att NVDA hoppar över asterisker beror på användarens inställning för skiljetecken, alltså på något användaren själv styr. Ett tekniskt undantag flyttar då problemet i stället för att lösa det, medan en tydligare formulering löser det för alla.

## Vad är WCAG-krav och vad är vår riktlinje

**WCAG-krav som kan beröras:**

* **1.3.1 Information och relationer.** Om relationen mellan exempelvis ett kontonummer och ett saldo bara framgår av visuell placering.
* **2.5.3 Etikett i namn.** Om ett nummer ingår i den synliga etiketten för en knapp, länk eller annan komponent.
* **3.1.1 Sidans språk** och **3.1.2 Språk för delar.**

Att ett OCR-nummer uttalas som ett stort heltal är inte ett WCAG-fel. Siffrorna finns i textnoden, de exponeras i tillgänglighetsträdet och de går att nå tecken för tecken. Att en talsyntes väljer att tolka dem som ett tal är en egenskap hos hjälpmedlet.

Resten av den här riktlinjen är interna regler och rekommendationer för ett konsekvent och robust gränssnitt.

## Varför gör vi så här

### Gruppering kostar ingenting

Den ursprungliga farhågan var att tusentalsseparatorer skulle få ett belopp att läsas som flera separata tal. Det stämmer inte. `1 345 876 kr` med U+00A0, samma sträng med vanligt mellanslag, och `1345876 kr` utan separator gav ordagrant samma uppläsning i både VoiceOver och NVDA.

Därmed finns inget skäl att ge hjälpmedel en normaliserad version av belopp. Vi slipper dubbla representationer, dubbel DOM i varje saldo och prislapp, och risken att de två versionerna glider isär över tid.

### Uttalsstyrning fungerar inte ens tekniskt

`aria-label` på ett `span` gav i VoiceOver både etiketten och textinnehållet upplästa efter varandra, med enheten bokstaverad som `k r` i den ena omgången. NVDA gav ett resultat som inte gick att härleda till någon av representationerna.

Namnet exponerades, men resultatet blev dubbel uppläsning och en oförutsägbar gruppering: VoiceOver lade in ordet "grupp" mellan de två uppläsningarna. Problemet är alltså inte att namngivning på element utan roll saknar effekt, utan att effekten inte går att förutse. Om numret dessutom ligger i en länk eller knapp riskerar en `aria-label` att den synliga texten försvinner ur det tillgängliga namnet, vilket är en 2.5.3-fråga.

### Identifierare kan inte formateras rätt

Ett sextonsiffrigt OCR-nummer testades både grupperat och ogrupperat.

Grupperat lästes det som fyra separata tal i VoiceOver och som en obegriplig blandning i NVDA. Ogrupperat lästes det siffra för siffra i VoiceOver, alltså användbart, men som ett tal i biljardklassen i NVDA.

Det finns alltså ingen formatering som ger verifierbar uppläsning i båda. Slutsatsen är att gruppering av identifierare är ett rent visuellt hjälpmedel, och att verifiering av långa sifferföljder kräver teckennavigering oavsett hur vi formaterar. Det är inte ett fel vi kan koda bort.

Gruppera därför för ögat, och lägg energin på att sammanhanget är tydligt i stället.

### Decimaler behöver inget undantag

`0,3120 euro` lästes med alla decimaler i båda skärmläsarna. NVDA läste decimaldelen siffra för siffra. Det tidigare befarade problemet, att värdet skulle läsas som `noll komma tretusenetthundratjugo`, uppstod inte.

VoiceOver placerade däremot enheten mitt i talet, mellan heltalsdel och decimaldel. Om det gäller även kronor, även för belopp över ett, och även när talet är grupperat, är det ett problem för varje prislapp och saldo med ören. Uppföljning sker i tc-14 och tc-15.

Undantaget för precisionskritiska värden finns kvar i riktlinjen som mekanism, men det finns i dagsläget inget känt fall som utlöser det. Ett undantag ska bygga på ett observerat problem, inte på en farhåga.

### Bindestreck uttalas inte som minus

Det var premissen för den gamla rekommendationen om U+2010. Den stämmer inte.

I `19770311-0376` hoppade VoiceOver över strecket helt. NVDA läste det som "till" och tolkade dessutom första delen som ett stort tal.

Ingen av uppläsningarna är särskilt användbar, men båda innehåller alla siffror, och U+2010 hade inte hjälpt. Vi behåller vanligt bindestreck, U+002D, eftersom det fungerar vid kopiering och inklistring i system som validerar personnummer.

### Etablerad telefonnummerformatering fungerar

`070 123 45 67` lästes med bibehållen inledande nolla i båda skärmläsarna. Den farhåga som fanns, att `070` skulle tolkas som talet sjuttio och nollan försvinna, besannades inte.

Grupperingen följdes däremot inte konsekvent. NVDA läste gruppvis, medan VoiceOver bröt gruppen `123` till "ett tjugotre". Alla siffror går fram i båda, men den som lyssnar efter grupper får dem inte alltid.

### Årtal och liknande

Generella nummerformaterare får inte användas blint på allt som råkar vara numeriskt. Ett årtal `1995` ska inte bli `1 995`. Samma sak gäller versionsnummer, husnummer och modellbeteckningar. Formateringen ska utgå från vad informationen betyder, inte från datatypen.

### Redigerbara inmatningsfält

Reglerna om gruppering gäller presenterat innehåll. I ett redigerbart fält kan automatisk gruppering påverka `pattern` och annan validering, flytta markören, störa inklistring, ändra värdet vid varje tangenttryckning och göra skärmläsarens återkoppling svårförutsägbar.

Om ett fält ändå behöver automatisk formatering ska det byggas som en särskild komponent och testas med tangentbord, skärmläsare, inklistring och validering.

## Teknik för dokumenterade undantag

Ett undantag införs bara när informationen inte förmedlas alls, alltså nivå 3 ovan, och när innehållsmässiga lösningar inte räcker.

Den verifierade tekniken för statiskt innehåll är:

1. den visuella representationen behålls i DOM men döljs med `aria-hidden="true"`
2. en visuellt dold alternativ representation exponeras för hjälpmedel

Detta fungerade i både VoiceOver och NVDA i testerna.

`aria-label` ska inte användas för detta. Det är underkänt i test på element utan roll, och på länkar och knappar riskerar det den synliga etiketten och därmed WCAG 2.5.3.

För interaktiva komponenter gäller alltid att den synliga etiketten ska ingå i det tillgängliga namnet.

Varje undantag dokumenteras med:

* vilken komponent eller situation det gäller
* vilken information som går förlorad utan undantaget
* varför en innehållsmässig lösning inte räcker
* vilken alternativ representation som används
* vilka hjälpmedel och versioner lösningen har testats med

## Befintlig kod

Den här riktlinjen ersätter tidigare rekommendationer om:

* Unicode-hyphen, U+2010, för att påverka uppläsning av bindestreck
* logik som tvingar fram uppläsning siffra för siffra
* separata skärmläsartexter för att styra uttalet
* normalisering av belopp för hjälpmedel

Befintliga lösningar behöver inte byggas om akut om de fungerar. Förenkla dem när komponenten ändå förändras. Ny kod följer den här riktlinjen.

## Bilaga A, testresultat

Testade med sidorna `index.html` och `identifierare.html`. All gruppering låg som riktiga tecken i textnoden, ingen CSS påverkade mellanrummen, inga script ändrade DOM efter laddning.

Uppläsningarna nedan är automatisk läsning. Teckennavigering är ännu inte testad, se Bilaga B.

### Belopp och teknik

| Id | Sträng | VoiceOver macOS | NVDA Windows |
| --- | --- | --- | --- |
| tc-01 | `1 345 876 kr` med U+00A0 | Ett sammanhängande tal | Ett sammanhängande tal |
| tc-02 | `1 345 876 kr` med U+0020 | Identiskt med tc-01 | Identiskt med tc-01 |
| tc-03 | `1345876 kr` utan separator | Identiskt med tc-01 | Identiskt med tc-01 |
| tc-06 | `aria-hidden` plus visuellt dold text | Läser den dolda texten korrekt | Läser den dolda texten korrekt |
| tc-07 | `aria-label` på `span` | Dubbel uppläsning, enheten bokstaverad som `k r` i första omgången | Oklart vilken representation som lästes |

**Slutsats.** Separatorn saknar betydelse för uppläsningen. Ingen normalisering behövs. `aria-hidden` plus visuellt dold text är den godkända undantagstekniken. `aria-label` på element utan roll är underkänt.

### Identifierare och specialtecken

| Id | Sträng | VoiceOver macOS | NVDA Windows |
| --- | --- | --- | --- |
| tc-04 | 16-siffrigt OCR i fyrgrupper | Fyra separata tal | Blandning av tal och siffror, obegriplig |
| tc-05 | Samma OCR utan gruppering | Siffra för siffra, användbart | Ett tal i biljardklassen |
| tc-08 | `070 123 45 67` | Inledande nolla bevarad, men gruppen `123` bryts: "noll sju noll ett tjugotre fyrtiofem sextiosju" | Gruppvis, inledande nolla bevarad |
| tc-09 | `0,3120 euro` | Alla decimaler upplästa, men enheten läses mitt i talet: "noll euro komma tre ett två noll" | Decimaldelen siffra för siffra, alla siffror med, enheten sist |
| tc-10 | `19770311-0376` | Strecket hoppas över | Strecket läses som "till", första delen som ett stort tal |
| tc-11 | `5226 **** **** 5963` | Åtta stjärnor upplästa, maskeringen framgår | Asteriskerna hoppas över helt, maskeringen framgår inte |

**Slutsats.** Ingen formatering av långa identifierare fungerar i båda skärmläsarna, så gruppering är ett visuellt hjälpmedel. Telefonnummer och decimaltal fungerar utan åtgärd. Bindestreck uttalas inte som minus, vilket gör den gamla U+2010-rekommendationen omotiverad. Maskerade nummer är det enda fall där information faktiskt går förlorad.

### Metadata som saknas

Skärmläsarversioner, OS-versioner, webbläsare, röst och inställning för skiljetecken är inte dokumenterade för dessa körningar. Särskilt inställningen för skiljetecken påverkar tc-11 direkt och bör fyllas i innan resultaten används som beslutsunderlag utanför teamet.

## Bilaga B, öppna frågor

**Teckennavigering är inte testad.** Hela riktlinjen vilar på att användaren kan läsa ett värde tecken för tecken när det behöver verifieras. Kör tc-04, tc-05, tc-10 och tc-11 med teckennavigering i NVDA och VoiceOver. Om det visar sig opraktiskt någonstans behöver nivåresonemanget i avsnittet om ansvarsgränsen justeras.

**Mobil är inte testad.** VoiceOver på iOS och TalkBack på Android återstår, och det är där teckennavigering är mest omständlig.

**Inställningen för skiljetecken.** tc-11 bör köras om på flera nivåer i NVDA för att se hur mycket av utfallet som styrs av användarens inställning.

**Telefonnummer i länk.** `070 123 45 67` inuti en `tel:`-länk är inte testat. Länkens tillgängliga namn och `href` spelar då in. Testas som tc-16.

**tc-04 i NVDA går inte att stämma av.** Transkriptionen ger sjutton siffror mot strängens sexton, med en extra nolla. Frågan är om NVDA producerar fel siffror eller om transkriptionen är felhörd. Kör om med talvisaren och rekonstruera siffra för siffra ur loggen. Svaret avgör om tc-04 är nivå 2, informationen finns men är svår att använda, eller nivå 3, informationen förmedlas inte alls. Slutsatserna om tc-04 står tills vidare kvar oförändrade.

**Negativa belopp är inte testade.** VoiceOver hoppade över bindestrecket helt i tc-10. Gör den samma sak i `-134,50 kr` låter ett negativt saldo exakt som ett positivt, vilket vore nivå 3. Testas som tc-12 med vanligt bindestreck och tc-13 med riktigt minustecken, U+2212. Det är det enda fall där avvisningen av alternativa Unicode-tecken kan behöva ett undantag, eftersom tecknet där bär betydelse och inte bara form.

**Punktskriftsdisplay är inte testad.** Det är den kanal där gruppering av identifierare faktiskt kan vara mer än ett visuellt hjälpmedel, eftersom läsaren där rör sig över tecknen med fingret i stället för att lyssna. Det berör direkt slutsatsen i avsnittet **Identifierare kan inte formateras rätt**, som i dag bygger enbart på uppläsning.
