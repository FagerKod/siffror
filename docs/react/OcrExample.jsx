import { useEffect, useId, useRef, useState } from 'react';

export default function OcrExample() {
  const id = useId();
  const inputRef = useRef(null);
  const revision = useRef(0);
  const [ocr, setOcr] = useState('0012 3456 7890');
  const [error, setError] = useState('');
  const [status, setStatus] = useState('');

  useEffect(() => {
    if (error) inputRef.current?.focus();
  }, [error]);
  const [copying, setCopying] = useState(false);

  // Formatövning, inte kontroll av kontrollsiffra eller mottagare.
  function validate(value) {
    if (!value.trim()) return 'Ange ett OCR-nummer. Tomt är inte noll.';
    if (!/^[0-9 \u00a0\u202f]+$/.test(value)) {
      return 'Använd endast siffror och mellanslag i denna övning.';
    }
    return '';
  }

  function change(event) {
    revision.current += 1;
    setOcr(event.target.value); // Behåll texten och markörpositionen.
    setError('');
    setStatus('');
  }

  function check(event) {
    event.preventDefault();
    const message = validate(ocr);
    setError(message);
    setStatus('');
    if (message) {
      return;
    }
    const normalized = ocr.replace(/[ \u00a0\u202f]/g, '');
    setStatus(`Formatet är godkänt för övningen. Utan mellanslag: ${normalized}. Kontrollsiffra och mottagare har inte kontrollerats.`);
  }

  async function copy() {
    if (copying) return;
    const message = validate(ocr);
    setError(message);
    setStatus('');
    if (message) {
      return;
    }
    const copiedValue = ocr;
    const copiedRevision = revision.current;
    setCopying(true);
    try {
      await navigator.clipboard.writeText(copiedValue);
      // Bekräfta inte ett gammalt värde om användaren hunnit redigera.
      if (revision.current === copiedRevision) {
        setStatus('OCR-numret har kopierats, inklusive mellanslag.');
      }
    } catch {
      if (revision.current === copiedRevision) {
        setStatus('Kopieringen lyckades inte. Markera och kopiera texten i fältet manuellt.');
      }
    } finally {
      setCopying(false);
    }
  }

  return (
    <section aria-labelledby={`${id}-title`}>
      <h2 id={`${id}-title`}>OCR och kopiering</h2>
      <form onSubmit={check} noValidate>
        <label htmlFor={`${id}-ocr`}>OCR-nummer</label>
        <p id={`${id}-help`}>
          Använd exempeluppgifter. Mellanslag tillåts som avskiljare.
          Övningen kontrollerar bara format, inte kontrollsiffra eller mottagare.
        </p>
        <input
          ref={inputRef}
          id={`${id}-ocr`}
          name="ocr"
          type="text"
          inputMode="numeric"
          value={ocr}
          onChange={change}
          aria-describedby={`${id}-help ${id}-error`}
          aria-invalid={error ? true : undefined}
        />
        <p id={`${id}-error`}>{error}</p>
        <button type="submit">Kontrollera format</button>
        <button
          type="button"
          aria-label="Kopiera OCR-nummer"
          aria-disabled={copying || undefined}
          onClick={copy}
        >
          <svg aria-hidden="true" focusable="false" width="24" height="24"
            viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <rect x="8" y="8" width="12" height="13" rx="2" />
            <path d="M15 8V3H3v13h5" />
          </svg>
        </button>
      </form>
      <p role="status">{status}</p>
    </section>
  );
}
