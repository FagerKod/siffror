#!/usr/bin/env python3
"""Kontrollerar att testsidornas strängar innehåller exakt de tecken som avses.

Kontrollen görs på den avkodade texten, alltså på det som hamnar i DOM:en,
inte på hur den är skriven i källkoden. Kör skriptet efter varje redigering
av index.html, identifierare.html eller sammanhang.html.

    python3 verifiera.py
"""

import sys
from html.parser import HTMLParser
from pathlib import Path

# Tecken som ser ut som sina vanliga motsvarigheter i en editor. De skrivs som
# escapes här och som numeriska teckenreferenser i HTML, aldrig litteralt, för
# att de annars byts tyst ut av formaterare, editorer och klipp och klistra.
NBSP = "\u00a0"   # hårt mellanslag
NNBSP = "\u202f"  # smalt hårt mellanslag
MINUS = "\u2212"  # riktigt minustecken
SUP2 = "\u00b2"   # upphöjd tvåa

# Tecken som aldrig får stå litteralt i HTML-källkoden, med den teckenreferens
# de ska skrivas som. Kontrolleras mot råkällan, inte mot den avkodade texten.
RISKTECKEN = {
    NBSP: ("&#160;", "hårt mellanslag"),
    NNBSP: ("&#8239;", "smalt hårt mellanslag"),
    MINUS: ("&#8722;", "minustecken"),
    SUP2: ("&#178;", "upphöjd tvåa"),
    "\u2010": ("&#8208;", "bindestreck"),
    "\u2011": ("&#8209;", "hårt bindestreck"),
    "\u2013": ("&#8211;", "tankstreck"),
    "\u2014": ("&#8212;", "långt tankstreck"),
}

EXPECTED = {
    "tc-01": {"fil": "index.html", "text": f"1{NBSP}345{NBSP}876{NBSP}kr"},
    "tc-02": {"fil": "index.html", "text": "1 345 876 kr"},
    "tc-03": {"fil": "index.html", "text": "1345876 kr"},
    "tc-04": {"fil": "index.html", "text": "1234 5678 9012 3456"},
    "tc-05": {"fil": "index.html", "text": "1234567890123456"},
    "tc-06": {
        "fil": "index.html",
        "barn": [
            {"tagg": "span", "attr": {"aria-hidden": "true"},
             "text": f"1{NBSP}345{NBSP}876{NBSP}kr"},
            {"tagg": "span", "attr": {"class": "visually-hidden"},
             "text": "1345876 kr"},
        ],
    },
    "tc-07": {
        "fil": "index.html",
        "barn": [
            {"tagg": "span", "attr": {"aria-label": "1345876 kr"},
             "text": f"1{NBSP}345{NBSP}876{NBSP}kr"},
        ],
    },
    "tc-08": {"fil": "identifierare.html", "text": "070 123 45 67"},
    "tc-09": {"fil": "identifierare.html", "text": "0,3120 euro"},
    "tc-10": {"fil": "identifierare.html", "text": "19770311-0376"},
    "tc-11": {"fil": "identifierare.html", "text": "5226 **** **** 5963"},
    "tc-12": {"fil": "sammanhang.html", "text": "-134,50 kr"},
    "tc-13": {"fil": "sammanhang.html", "text": f"{MINUS}134,50 kr"},
    "tc-14": {"fil": "sammanhang.html", "text": f"1{NBSP}345{NBSP}876,50{NBSP}kr"},
    "tc-15": {"fil": "sammanhang.html", "text": "0,3120 EUR"},
    "tc-16": {"fil": "sammanhang.html", "text": "070 123 45 67"},
    "tc-17": {"fil": "sammanhang.html", "text": f"Betala 1{NBSP}345{NBSP}876{NBSP}kr"},
    "tc-18": {"fil": "sammanhang.html", "text": f"1{NBSP}345{NBSP}876{NBSP}kr"},
    "tc-19": {"fil": "sammanhang.html", "text": "12,5 %"},
    "tc-20": {"fil": "sammanhang.html", "text": f"45 m{SUP2}"},
    "tc-21": {"fil": "sammanhang.html", "text": f"1{NNBSP}345{NNBSP}876{NNBSP}kr"},
}

# Aria som testfallen kräver. Allt annat aria på teststrängarna är brus som
# kan förorena resultatet.
#
# Teknikbeskrivningar ska vara stängda details, utan aria-hidden.
TILLATNA_ARIA = {
    ("index.html", "aria-hidden", "true"),
    ("index.html", "aria-label", "1345876 kr"),
}

EXTERNT = {"script", "link", "img", "iframe", "object", "embed", "source", "video", "audio"}


class Extractor(HTMLParser):
    """Plockar ut innehållet i varje element som bär data-tc."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.fall = {}
        self.aktiv = None
        self.djup = 0
        self.barn = None
        self.aria = []
        self.teknik = []
        self.externa = []
        self.fel = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        klasser = a.get("class", "").split()
        if "teknik" in klasser:
            self.teknik.append(tag == "details" and "open" not in a and "aria-hidden" not in a)
        for namn, varde in a.items():
            if namn.startswith("aria-"):
                self.aria.append((namn, varde))
        if tag in EXTERNT:
            self.externa.append(tag)

        if "data-tc" in a:
            if self.aktiv is not None:
                self.fel.append("data-tc inuti data-tc")
            self.aktiv = {"tc": a["data-tc"], "text": [], "barn": []}
            self.djup = 0
            return

        if self.aktiv is not None:
            if self.barn is not None:
                self.fel.append(f"djupare nästling än ett steg i {self.aktiv['tc']}")
            self.djup += 1
            self.barn = {"tagg": tag, "attr": a, "text": []}

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if self.barn is not None:
            self.aktiv["barn"].append(self.barn)
            self.barn = None
            self.djup -= 1

    def handle_data(self, data):
        if self.aktiv is None:
            return
        self.aktiv["text"].append(data)
        if self.barn is not None:
            self.barn["text"].append(data)

    def handle_endtag(self, tag):
        if self.aktiv is None:
            return
        if self.djup == 0:
            self.fall[self.aktiv["tc"]] = self.aktiv
            self.aktiv = None
            return
        self.djup -= 1
        if self.barn is not None:
            self.aktiv["barn"].append(self.barn)
            self.barn = None


def kodpunkter(s):
    return " ".join("U+%04X" % ord(c) for c in s)


def stada(delar):
    """Tar bort ASCII-blanksteg i kanterna men aldrig U+00A0, som ska upptäckas."""
    return "".join(delar).strip(" \t\r\n")


def main():
    rot = Path(__file__).resolve().parent.parent / "docs" / "testfall"
    filer = sorted({v["fil"] for v in EXPECTED.values()})

    parsat = {}
    aria_funna = set()
    problem = []

    for namn in filer:
        sokvag = rot / namn
        if not sokvag.exists():
            problem.append(f"{namn}: filen saknas")
            continue
        kalla = sokvag.read_text(encoding="utf-8")

        for tecken, (entitet, beskrivning) in RISKTECKEN.items():
            if tecken in kalla:
                problem.append(
                    f"{namn}: litteralt U+{ord(tecken):04X} i källkoden, "
                    f"{beskrivning}, ska skrivas som {entitet}"
                )

        p = Extractor()
        p.feed(kalla)
        p.close()
        parsat[namn] = p

        for fel in p.fel:
            problem.append(f"{namn}: {fel}")
        for tagg in p.externa:
            problem.append(f"{namn}: elementet <{tagg}> hämtar eller kör extern resurs")
        for attrnamn, varde in p.aria:
            aria_funna.add((namn, attrnamn, varde))

        if not p.teknik:
            problem.append(f"{namn}: inga teknikrutor hittades")
        for i, varde in enumerate(p.teknik, start=1):
            if not varde:
                problem.append(
                    f"{namn}: teknikruta {i} ska vara stängd details utan aria-hidden"
                )

    okant_aria = aria_funna - TILLATNA_ARIA
    for post in sorted(okant_aria):
        problem.append(f"{post[0]}: oväntat {post[1]}=\"{post[2]}\"")
    saknat_aria = TILLATNA_ARIA - aria_funna
    for post in sorted(saknat_aria):
        problem.append(f"{post[0]}: saknar {post[1]}=\"{post[2]}\"")

    bredd = max(len(k) for k in EXPECTED)
    antal_fel = 0

    for tc in sorted(EXPECTED):
        vantat = EXPECTED[tc]
        p = parsat.get(vantat["fil"])
        fall = p.fall.get(tc) if p else None

        if fall is None:
            print(f"{tc.ljust(bredd)}  FEL   hittades inte i {vantat['fil']}")
            antal_fel += 1
            continue

        if "text" in vantat:
            fick = stada(fall["text"])
            ok = fick == vantat["text"]
            print(f"{tc.ljust(bredd)}  {'OK ' if ok else 'FEL'}   {kodpunkter(fick)}")
            if not ok:
                print(f"{' ' * bredd}        förväntat: {kodpunkter(vantat['text'])}")
                antal_fel += 1
            continue

        barn_ok = len(fall["barn"]) == len(vantat["barn"])
        rader = []
        if not barn_ok:
            rader.append(
                f"{' ' * bredd}        fel antal delelement: "
                f"{len(fall['barn'])}, förväntat {len(vantat['barn'])}"
            )
        for i, vb in enumerate(vantat["barn"]):
            if i >= len(fall["barn"]):
                break
            fb = fall["barn"][i]
            fick = stada(fb["text"])
            del_ok = fb["tagg"] == vb["tagg"] and fick == vb["text"]
            for attrnamn, attrvarde in vb["attr"].items():
                if fb["attr"].get(attrnamn) != attrvarde:
                    del_ok = False
                    rader.append(
                        f"{' ' * bredd}        del {i + 1}: {attrnamn} är "
                        f"{fb['attr'].get(attrnamn)!r}, förväntat {attrvarde!r}"
                    )
            rader.append(
                f"{' ' * bredd}        del {i + 1} <{fb['tagg']}>: {kodpunkter(fick)}"
            )
            if fick != vb["text"]:
                rader.append(
                    f"{' ' * bredd}        del {i + 1} förväntat: {kodpunkter(vb['text'])}"
                )
            barn_ok = barn_ok and del_ok

        print(f"{tc.ljust(bredd)}  {'OK ' if barn_ok else 'FEL'}")
        for rad in rader:
            print(rad)
        if not barn_ok:
            antal_fel += 1

    print()
    if problem:
        print("Strukturproblem:")
        for rad in problem:
            print(f"  {rad}")
        print()

    if antal_fel or problem:
        print(f"MISSLYCKADES: {antal_fel} testfall med fel, {len(problem)} strukturproblem")
        return 1

    teknikrutor = sum(len(p.teknik) for p in parsat.values())
    print(
        f"Allt stämmer: {len(EXPECTED)} testfall kontrollerade, "
        f"{teknikrutor} stängda teknikrutor kan öppnas av alla."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
