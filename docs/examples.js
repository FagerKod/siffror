'use strict';
// Presentation examples only. No requests, persistence or real payments.
function normalizeOcr(raw) {
  if (!raw.trim()) return {error: 'Ange ett OCR-nummer. Tomt är inte noll.'};
  if (!/^[0-9 \u00a0\u202f]+$/.test(raw)) return {error: 'Använd endast siffror och mellanslag i denna övning.'};
  return {value: raw.replace(/[ \u00a0\u202f]/g, '')};
}
function parseAmount(raw) {
  const text = raw.trim();
  if (!text) return {error: 'Ange ett belopp.', empty: true};
  // Optional, consistent thousands grouping; at most two decimal digits.
  if (!/^(?:\d+|\d{1,3}(?:[ \u00a0\u202f]\d{3})+)(?:[,.]\d{1,2})?$/.test(text)) {
    return {error: 'Ange ett positivt belopp med högst två decimaler och korrekt tusentalsgruppering.'};
  }
  const [whole, fraction = ''] = text.replace(/[ \u00a0\u202f]/g, '').split(/[,.]/);
  const cents = BigInt(whole) * 100n + BigInt(fraction.padEnd(2, '0'));
  if (cents === 0n) return {error: 'Beloppet måste vara större än noll.'};
  if (cents > 99999999999n) return {error: 'Ange högst 999 999 999,99 i denna övning.'};
  return {cents};
}
function formatAmount(cents, currency) {
  const whole = (cents / 100n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
  return `${whole},${(cents % 100n).toString().padStart(2, '0')} ${currency === 'EUR' ? 'EUR' : 'kr'}`;
}
function initExamples() {
  const byId = id => document.getElementById(id);
  const ocrForm = byId('ocr-form');
  if (ocrForm) {
    byId('ocr-fields').disabled = false; byId('copy-ocr').disabled = false;
    const input = byId('ocr'), error = byId('ocr-error'), status = byId('ocr-status');
    input.addEventListener('input', () => {
      byId('ocr-preview').textContent = input.value || 'Ingen uppgift angiven';
      error.textContent = ''; status.textContent = ''; input.removeAttribute('aria-invalid');
    });
    ocrForm.addEventListener('submit', event => {
      event.preventDefault();
      const result = normalizeOcr(input.value);
      error.textContent = result.error || '';
      if (result.error) {
        input.setAttribute('aria-invalid', 'true'); status.textContent = ''; input.focus();
      } else {
        input.removeAttribute('aria-invalid');
        status.textContent = `Formatet är godkänt för övningen. Utan mellanslag: ${result.value}. Kontrollsiffra och mottagare har inte kontrollerats.`;
      }
    });
    byId('copy-ocr').addEventListener('click', async () => {
      const text = input.value;
      if (normalizeOcr(text).error) { status.textContent = 'Fyll i ett OCR-nummer med enbart siffror och mellanslag före kopiering.'; return; }
      try {
        await navigator.clipboard.writeText(text);
        status.textContent = 'OCR-numret har kopierats. Klistra in i jämförelsefältet för att kontrollera.';
      } catch (_) {
        status.textContent = 'Kopieringen lyckades inte. Markera och kopiera texten i OCR-fältet manuellt.';
      }
    });
  }
  const form = byId('payment-form');
  if (form) {
    byId('payment-fields').disabled = false;
    const amount = byId('amount'), account = byId('account'), currency = byId('currency');
    const summary = byId('payment-summary'), button = byId('pay'), error = byId('payment-error'), status = byId('payment-status');
    function update() {
      error.textContent = ''; status.textContent = ''; amount.removeAttribute('aria-invalid');
      const result = parseAmount(amount.value);
      if (result.error) {
        summary.textContent = `Betalning från ${account.value}: ${result.empty ? 'Belopp saknas' : 'Beloppet behöver kontrolleras'} (${currency.value}).`;
        button.textContent = 'Kontrollera betalningsuppgifterna';
      } else {
        const formatted = formatAmount(result.cents, currency.value);
        summary.textContent = `Betalning från ${account.value}: ${formatted}`;
        button.textContent = `Betala ${formatted}`;
      }
    }
    amount.addEventListener('input', update);
    account.addEventListener('change', update);
    currency.addEventListener('change', update);
    form.addEventListener('submit', event => {
      event.preventDefault();
      const result = parseAmount(amount.value);
      if (result.error) {
        error.textContent = result.error; amount.setAttribute('aria-invalid', 'true'); status.textContent = ''; amount.focus();
      } else {
        error.textContent = ''; amount.removeAttribute('aria-invalid');
        status.textContent = `Övningen är klar. Betalning från ${account.value}: ${formatAmount(result.cents, currency.value)}. Ingen betalning har genomförts.`;
      }
    });
    update();
  }
}
if (typeof document !== 'undefined') initExamples();
if (typeof module !== 'undefined') module.exports = {normalizeOcr, parseAmount, formatAmount};
