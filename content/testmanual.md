# Testmanual för siffror och tal

Version 3, 22 oktober 2026. Använd [vägledningen för testare](vagledning.html#for-testare) för bedömningen. Här finns arbetsgången och kommandon för att undersöka uppläsningen.

## Förbered en körning

Anteckna datum, testsidans version eller commit, testare, operativsystem, webbläsare, skärmläsare, talsyntes, röst, språk, tangentbordslayout och relevanta inställningar. Ange versioner för programmen samt skiljeteckennivå och eventuella egna uttalsregler.

Bestäm testmiljöerna utifrån tjänstens användare och support. Tidigare observationer omfattar NVDA på Windows och VoiceOver på macOS men saknar fullständig miljöinformation. Planera nya dokumenterade körningar; gamla resultat ersätter inte verifiering i den miljö som nu ska stödjas. Mobil och punktskrift behöver egna körningar om slutsatserna ska omfatta dem.

## Håll isär tre sorters underlag

- **Källtext:** vad sidan innehåller och exponerar, inklusive exakta siffror och tecken.
- **Talvisare eller textpanel:** den text som hjälpmedlet visar som stöd för talet. Spara den utan omskrivning.
- **Hört tal:** vad rösten faktiskt uttalar. Anteckna det separat; vid svårtolkade resultat kan en inspelning av testmaterialet behövas.

En textpanel är inte en ljudinspelning. Dra inte slutsatsen att en talsyntes uttalade alla siffror korrekt enbart från paneltexten. Om det hörda talet och paneltexten skiljer sig, bevara båda uppgifterna.

NVDA:s talvisare finns under Verktyg i NVDA-menyn. VoiceOvers textpanel finns i VoiceOver-verktyg, Visuellt, Paneler och menyer. Öppna verktyget med `VO+Fn+F8`; Fn kan bero på tangentbordsinställning. [K1](kallor.html#k1) [K19](kallor.html#k19)

## Kör varje testfall

1. Låt de tekniska detaljerna vara stängda. Läs sidan med vanlig löpande läsning och dokumentera utfallet.
2. Navigera till testfallet via rubriken och vidare till teststrängen. Dokumentera detta separat.
3. För länk och knapp: kontrollera även vid tangentbordsfokus och relevant länk- eller knapplista. Aktivera inte testtelefonlänken. Testknappen genomför ingen betalning.
4. För tabellen: läs först normalt, sedan med hjälpmedlets tabellnavigering. Kontrollera kopplingen till rubriken.
5. Kontrollera exakta sifferföljder med tecken- eller ordgranskning. Skriv ner följden medan du granskar; detta är inget minnestest.
6. Öppna tekniska detaljer efteråt och jämför med källtexten. Klassificera enligt vägledningen och notera kvarstående osäkerhet.

Testa i första hand tc-04, tc-05, tc-10 och tc-11 med detaljerad granskning. Lägg till tc-09 för slutnollan och tc-12/tc-13 för negativa värden. Kontrollera sedan återstående fall och de verkliga komponenterna i tjänsten.

## NVDA på Windows

I bläddringsläge används `H` för nästa rubrik och vänster/höger pil för textens tecken. `NVDA+Mellanslag` växlar bläddrings- och fokusläge. Fokusläge är inte ett extra testläge för vanliga statiska stycken.

För granskningsmarkören gäller följande standardkommandon. Numpad används med Num Lock av.

| Åtgärd | Stationär layout | Bärbar layout |
| --- | --- | --- |
| Föregående tecken | `Numpad 1` | `NVDA+Vänsterpil` |
| Aktuellt tecken | `Numpad 2` | `NVDA+Punkt` |
| Nästa tecken | `Numpad 3` | `NVDA+Högerpil` |

Dubbeltryck på kommandot för aktuellt tecken ger teckenbeskrivning. `NVDA+P` ändrar symbolnivå. Vid utredning av maskering eller tecken: jämför Något och Alla och logga varje körning separat. Egna tangentbindningar kan skilja sig. [K1](kallor.html#k1)

## VoiceOver på macOS

`VO` är vald VoiceOver-modifierare, vanligtvis Control+Option eller Caps Lock. Navigera till texten och interagera vid behov med `VO+Skift+Nedåtpil`.

| Åtgärd | Kommando |
| --- | --- |
| Läs aktuellt ord | `VO+W` |
| Bokstavera aktuellt ord | `VO+W` två gånger |
| Fonetisk bokstavering | `VO+W` tre gånger |
| Läs aktuellt tecken | `VO+C` |
| Läs nästa eller föregående ord i text | `VO+Högerpil` eller `VO+Vänsterpil` |

Bokstavering gäller aktuellt ord, inte säkert hela ett nummer med mellanrum. Granska därför samtliga grupper. [K20](kallor.html#k20)

Apples aktuella läsguide anger höger/vänster pil för tecken i text. Utfallet på webben beror även på textinteraktion, Quick Nav och markörläge. Kontrollera att kommandot verkligen flyttar ett tecken i den aktuella Safari-miljön; anteckna metoden om det inte fungerar. `VO+Högerpil` är inte ett generellt kommando för nästa tecken. [K21](kallor.html#k21)

Skiljetecken styrs i VoiceOver-verktyg under Utförlighet, Text. Menynamnen kan variera med språk och version. Anteckna vald nivå och eventuella anpassningar. [K2](kallor.html#k2)

## VoiceOver på iPhone och iPad

Gå till teststrängen. Vrid två fingrar som ett vred och välj Tecken i rotorn. Svep nedåt med ett finger för nästa tecken och uppåt för föregående. Om Tecken saknas, kontrollera rotorinställningarna. Granska hela följden och dokumentera hur navigationen fungerade. [K22](kallor.html#k22)

## TalkBack på Android

Gå till teststrängen. Växla läskontroll genom att svepa upp och sedan ned, eller ned och sedan upp, i en sammanhängande enfingerrörelse. Välj Tecken. Svep ned för nästa tecken och upp för föregående. Anpassade gester och enhetsversion kan påverka kommandona. [K23](kallor.html#k23)

## Dokumentera och bedöm

Använd [resultatmallen](resultatmall.html). Håll separata rader för löpande läsning, navigerad läsning och detaljerad granskning. Notera om värdet gick att återge korrekt, vilka tecken som var otydliga, hur mycket extra arbete som krävdes och om uppgiften gick att slutföra.

En ovan testares misslyckande bevisar inte att teckennavigering är omöjlig. Kontrollera kommandon och ta vid behov hjälp av en van användare. Samtidigt får en tekniskt möjlig men orimligt svår väg inte döljas bakom ett enkelt ”godkänt”.

Ingen fast tidsgräns eller viss ordalydelse gäller som generellt WCAG-krav. Bedöm uppgiften, och skilj observation, användbarhetsbedömning och konstaterad kravavvikelse åt.
