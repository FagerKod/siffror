# För utvecklare

Utgå från vanlig text och tydlig HTML. Synlig information och information för hjälpmedel ska stämma överens. Undvik separata uttalsversioner av synliga tal.

## Belopp och precision

Använd samma formatterade text i gränssnittets berörda delar. Bestäm precision per uppgift. Två decimaler passar inte alla värden. Bevara tecken och enhet i texten; färg ensam räcker inte för minus.

```html
<p>Lönekonto, saldo 1 234,50 kr</p>
<p>Saldo −134,50 kr (negativt saldo)</p>
<button type="button">Betala 1 234,50 kr</button>
```

Knappens text är dess tillgängliga namn. Ingen separat uttalsversion behövs. [Prova belopp och saldo](testfall/index.html).

Intl.NumberFormat kan formatera presentationen. Ange valuta och avsedd precision. En sådan formatterare ersätter inte exakta beloppsberäkningar. I betalningsövningen bevaras inmatningen som text och beloppet hanteras som ett helt antal hundradelar.

## Nummer är strängar

OCR-nummer, kontonummer, telefonnummer och IBAN är inte tal som ska räknas med. Bevara inledande nollor och bokstäver. Normalisera endast avskiljare som formatreglerna tillåter.

```html
<label for="ocr">OCR-nummer</label>
<input id="ocr" name="ocr" type="text" inputmode="numeric">
```

inputmode ger en tangentbordshint, inte validering. IBAN behöver även bokstäver. Validera enligt tjänstens regler också på servern. [Prova redigering och kopiering](testfall/identifierare.html#ocr-exempel).

## Kontrollerade fält i React

Behåll den inmatade strängen i state och uppdatera den i onChange. Använd htmlFor och inputMode i JSX.

```jsx
const [ocr, setOcr] = useState('');

<label htmlFor="ocr">OCR-nummer</label>
<input
  id="ocr"
  name="ocr"
  type="text"
  inputMode="numeric"
  value={ocr}
  onChange={event => setOcr(event.target.value)}
/>
```

Utdraget hör hemma i en React-komponent med useState importerad. Undvik omformatering som flyttar markören medan användaren skriver. Normalisera vid ett tydligt steg och kontrollera redigering, inklistring och tomt värde. Webbplatsens körbara exempel använder HTML och JavaScript; samma HTML-semantik gäller i React.

## Ikonknappar behöver namn

Ett tillgängligt namn kan beskriva en kontrolls funktion utan att skapa en annan uttalsversion av ett synligt tal.

```html
<button type="button" aria-label="Kopiera OCR-nummer">
  <svg aria-hidden="true" focusable="false">...</svg>
</button>
```

Lägg till fungerande kopiering och synlig återkoppling i en statusregion. Visa inte att kopieringen lyckades om den misslyckades. [Prova ikonknappen](testfall/identifierare.html#ocr-exempel).

## Sammanhang och uppdateringar

Koppla etiketter till fält och använd rubriker i tabeller. Härled sammanställning och knapptext från samma aktuella data. När en åtgärd behöver bekräftas kan en synlig statusregion ge återkoppling utan fokusflytt.

```html
<p role="status"></p>
```

Skapa regionen innan texten uppdateras. Lägg inte hela gränssnittet i en live-region. En ändring behöver inte alltid annonseras automatiskt. [Prova betalningsövningen](testfall/sammanhang.html).

## Läsbarhet och kontroll

Ange svenska som sidans språk med lang="sv". Håll belopp, valuta och sammanhang begripliga. Kontrollera radbrytning, förstoring och kopiering i de faktiska komponenterna. Långa nummer får inte kapas. Visa vad maskering betyder, exempelvis ”Kort som slutar på 5963”, och lägg inte maskerade siffror i dold text.

[Primärkällorna](kallor.html) ger stöd för HTML, React, tillgängliga namn och statusmeddelanden.
