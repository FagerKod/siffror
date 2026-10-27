import { useEffect, useId, useRef, useState } from 'react';

function parseAmount(raw) {
  const text = raw.trim();
  if (!text) return { error: 'Ange ett belopp.', empty: true };
  if (!/^(?:\d+|\d{1,3}(?:[ \u00a0\u202f]\d{3})+)(?:[,.]\d{1,2})?$/.test(text)) {
    return { error: 'Ange ett positivt belopp med högst två decimaler och korrekt tusentalsgruppering.' };
  }
  const [whole, fraction = ''] = text.replace(/[ \u00a0\u202f]/g, '').split(/[,.]/);
  const cents = BigInt(whole) * 100n + BigInt(fraction.padEnd(2, '0'));
  if (cents === 0n) return { error: 'Beloppet måste vara större än noll.' };
  if (cents > 99999999999n) return { error: 'Ange högst 999 999 999,99.' };
  return { cents };
}

function formatAmount(cents, currency) {
  const whole = (cents / 100n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
  const decimals = (cents % 100n).toString().padStart(2, '0');
  return `${whole},${decimals} ${currency === 'EUR' ? 'EUR' : 'kr'}`;
}

export default function PaymentExample() {
  const id = useId();
  const amountRef = useRef(null);
  const [account, setAccount] = useState('Lönekonto');
  const [amount, setAmount] = useState('1 234,50');
  const [currency, setCurrency] = useState('SEK');
  const [error, setError] = useState('');
  const [status, setStatus] = useState('');

  useEffect(() => {
    if (error) amountRef.current?.focus();
  }, [error]);

  // Härled presentationen från samma state, inte separata kopior i state.
  const result = parseAmount(amount);
  const formatted = result.error ? null : formatAmount(result.cents, currency);
  const summary = formatted
    ? `Betalning från ${account}: ${formatted}`
    : `Betalning från ${account}: ${result.empty ? 'Belopp saknas' : 'Beloppet behöver kontrolleras'} (${currency}).`;

  function clearFeedback() {
    setError('');
    setStatus('');
  }

  function submit(event) {
    event.preventDefault();
    if (result.error) {
      setError(result.error);
      setStatus('');
      return;
    }
    setError('');
    setStatus(`Övningen är klar. ${summary}. Ingen betalning har genomförts.`);
  }

  return (
    <section aria-labelledby={`${id}-title`}>
      <h2 id={`${id}-title`}>Betalningsövning</h2>
      <p>Ingen betalning genomförs. Inga uppgifter skickas eller sparas.</p>
      <form onSubmit={submit} noValidate>
        <label htmlFor={`${id}-account`}>Från konto</label>
        <select id={`${id}-account`} name="account" value={account}
          onChange={event => { setAccount(event.target.value); clearFeedback(); }}>
          <option value="Lönekonto">Lönekonto</option>
          <option value="Sparkonto">Sparkonto</option>
        </select>
        <label htmlFor={`${id}-amount`}>Belopp</label>
        <p id={`${id}-help`}>
          Ange ett positivt belopp med högst två decimaler, exempelvis 1 234,50.
          Högst 999 999 999,99. Mellanslag får gruppera tusental.
        </p>
        <input ref={amountRef} id={`${id}-amount`} name="amount"
          type="text" inputMode="decimal" value={amount}
          onChange={event => { setAmount(event.target.value); clearFeedback(); }}
          aria-describedby={`${id}-help ${id}-error`}
          aria-invalid={error ? true : undefined}
        />
        <p id={`${id}-error`}>{error}</p>
        <label htmlFor={`${id}-currency`}>Valuta</label>
        <select id={`${id}-currency`} name="currency" value={currency}
          onChange={event => { setCurrency(event.target.value); clearFeedback(); }}>
          <option value="SEK">SEK</option>
          <option value="EUR">EUR</option>
        </select>
        <p>{summary}</p>
        <button type="submit">
          {formatted ? `Betala ${formatted}` : 'Kontrollera betalningsuppgifterna'}
        </button>
      </form>
      <p role="status">{status}</p>
    </section>
  );
}
