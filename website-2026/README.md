# Kulé kulé Zanskar — nieuwe website

Statische site, gebouwd volgens de websitestrategie van 30 augustus 2026.
37 pagina's, geen framework, geen build-stap nodig om te publiceren.

---

## Snel bekijken

Dubbelklik **`preview.command`** (macOS). Dat start een lokale server en opent
`http://localhost:8000` in je browser. Sluit het terminalvenster om te stoppen.

Handmatig kan ook:

```bash
cd <deze map>
python3 -m http.server 8000
```

> Open `index.html` **niet** rechtstreeks met dubbelklik. De site gebruikt paden vanaf
> de root (`/zanskar/…`), zoals op een echte server. Via `file://` werken die niet.

---

## Wat er in deze map staat

```
index.html            Home
zanskar/              Bestemmingscluster — 9 pagina's
guides/               Gidsen — 5 pagina's
journeys/             Reizen — 5 pagina's
plan/                 Praktische gidsen — 9 pagina's
about/  stories/  contact/  privacy/  terms/  404.html
sitemap.xml  robots.txt

assets/site.css       Volledige stylesheet
assets/site.js        Menu, filters, formulier-prefill (13 regels logica)
assets/images/        Foto's, elk in 1800 px en 900 px
assets/routes/        De zes GPX-bestanden

build.py              Generator
content_*.py          De teksten, per cluster
OPENSTAANDE-PUNTEN.md Automatisch gegenereerde lijst van 50 gaten
```

## Teksten wijzigen

De HTML in deze map wordt **gegenereerd**. Wijzig je iets rechtstreeks in een
`index.html`, dan is het weg bij de volgende build. Pas de tekst aan in het
bijbehorende `content_*.py`-bestand en draai:

```bash
python3 build.py
```

Dat herschrijft alle pagina's, `sitemap.xml`, `robots.txt` en
`OPENSTAANDE-PUNTEN.md`.

Wil je liever helemaal niet met Python werken: draai de build één keer, gooi
`build.py` en de `content_*.py`-bestanden weg, en bewerk daarna de HTML met de
hand. Je verliest dan wel het gedeelde sjabloon — een wijziging in de footer
moet je vanaf dat moment 37 keer maken.

---

## De 50 openstaande punten

Overal waar informatie ontbreekt die alleen van de gidsen kan komen, staat een
**geel gemarkeerde tekst** op de pagina met precies wat er nodig is. Ze staan
allemaal op een rij in `OPENSTAANDE-PUNTEN.md`.

De site is bewust **niet** publicatieklaar zolang die lijst niet leeg is. Verzin
de ontbrekende feiten niet — dat is precies wat de strategie wilde vermijden.

De zwaarste blokken, in volgorde van belang:

1. **Gidsprofielen** (punten 7–21). Twee portretten, twee citaten van 150–250
   woorden uit een opgenomen interview, per gids drie onderwerpen en één verhaal.
   Zonder dit is de gidsenpagina leeg van binnen.
2. **Juridisch** (36, 38, 45–49). Wie contracteert, annulatievoorwaarden,
   bedrijfsgegevens. Dit blokkeert publicatie, niet alleen kwaliteit.
3. **Prijzen** (27, 29) voor de Tsokmichik-route en de culturele rondreis.
4. **Formulier-endpoint** (41, 42). Zonder dit komt er geen enkele aanvraag
   binnen — precies het probleem van de huidige site.
5. **Reviews** (3). De testimonial-sectie op de homepage is nu een instructie in
   plaats van een blok; publiceer hem pas als er drie echte citaten zijn.

---

## Wat er in de teksten is gecontroleerd

* **Afstanden en hoogtes van de Zangla–Phuktal-route** zijn berekend uit jouw
  eigen GPX-bestanden: 71,3 km, ongeveer 2.750 m stijging, hoogste punt circa
  5.140 m op dag 3. Dat is meteen het antwoord op de discrepantie uit de
  strategie: de live site noemde 5.100 m, de GPX zegt 5.143 m.
* **De Tsokmichik-route** staat met de cijfers uit jouw PDF van maart 2026 en
  draagt een expliciete waarschuwing dat ze nog niet tegen een GPS-spoor zijn
  gecontroleerd.
* **Regiofeiten** (inwoners 13.793 volgens de census van 2011, Padum, Zangla op
  3.931 m, Phuktal begin 15e eeuw en circa 70 monniken, de Nimmu–Padum–Darcha-weg
  van 298 km die in maart 2024 verhard werd opgeleverd maar nog geen
  all-weather verbinding is) komen uit publieke bronnen en zijn nagekeken.
* **Alt-teksten** beschrijven wat er daadwerkelijk op de foto staat, niet wat er
  zou moeten staan. Als je een foto vervangt, pas de alt-tekst mee aan.

---

## Techniek

* **Geen framework, geen JavaScript-afhankelijkheden.** De site werkt volledig
  zonder JS; het menu valt dan terug op de zichtbare navigatie.
* **Beelden** worden geserveerd op 900 px of 1800 px via `srcset`. Het hero-beeld
  laadt met `fetchpriority="high"`, de rest lazy.
* **Gestructureerde data**: `TravelAgency` op de home, `TouristTrip` op de
  reispagina's, `Person` op de gidsprofielen, `TouristAttraction` op Phuktal en
  Zangla, `FAQPage` op `/plan/faq/`.
* **Lettertypes** komen van Google Fonts. Wil je die weg (sneller, en geen
  externe request): download Familjen Grotesk en Source Serif 4, zet ze in
  `assets/fonts/` en vervang de `<link>` in `build.py` door lokale
  `@font-face`-regels in `site.css`.
* **Toegankelijkheid**: skip-link, zichtbare focusstaten, alt op elke afbeelding,
  contrast van tekst op beeld via een verloop in plaats van tekst direct op de
  foto.

## Publiceren

De huidige site draait op **GitHub Pages** (de domeinnaam wijst naar
185.199.108–111.153, de vaste adressen van GitHub Pages). Je publiceert dus door
de inhoud van je bestaande repository te vervangen en te pushen.

### Stap voor stap

1. Open de map waar je repository staat (die met de huidige `index.html` erin).
2. **Bewaar het bestand `CNAME`** dat daar staat. Dat is wat je domeinnaam aan
   GitHub Pages koppelt. In deze map zit er een met `www.kulekulezanskar.com` —
   controleer of dat overeenkomt met wat er nu in je repo staat en gebruik die
   van de repo als ze verschillen.
3. Verwijder de oude bestanden uit de repository (niet de map `.git`, niet
   `CNAME`).
4. Kopieer de volledige inhoud van `website-2026/` erin. De vier
   ontwikkelbestanden mogen mee of niet — ze doen niets op de server:
   `build.py`, de `content_*.py`, `preview.command` en
   `OPENSTAANDE-PUNTEN.md`. Ik zou ze meenemen, dan staat de bron bij het
   resultaat.
5. Committen en pushen:

   ```bash
   git add -A
   git commit -m "Nieuwe site: drie pijlers, 37 pagina's"
   git push
   ```

6. Na een minuut staat hij live op https://www.kulekulezanskar.com.

Het bestand `.nojekyll` in deze map zorgt dat GitHub de bestanden ongewijzigd
serveert in plaats van ze door Jekyll te halen. Laat het staan.

### Wat GitHub Pages níét kan

* **Geen formulierverwerking.** Het contactformulier heeft een externe dienst
  nodig — Formspree of Formcarry werken hier prima en kosten weinig. Zet het
  endpoint in `content_misc.py` en laat het naar twee adressen sturen.
* **Geen redirects.** GitHub Pages leest geen `_redirects`-bestand. Dat is hier
  geen probleem: de homepage-URL blijft dezelfde en de oude ankers
  (`/#itinerary`, `/#pricing`) worden door de server nooit gezien — die vallen
  vanzelf terug op de nieuwe homepage.

### Als je liever verhuist

Netlify of Cloudflare Pages zijn een stap eenvoudiger: map erin slepen, klaar,
en formulieren zitten er ingebouwd. Je moet dan wel de DNS-records van het
domein aanpassen, en dat is de enige stap waarbij de site even onbereikbaar kan
zijn. Niet nodig, tenzij het formulier je hoofdpijn geeft.

### Na het live zetten

1. `sitemap.xml` indienen in Google Search Console — die ontbrak volledig, en
   het is de eerste stap om te weten of de site überhaupt geïndexeerd wordt.
2. `hello@kulekulezanskar.com` aanmaken en het formulier daarop laten uitkomen.
3. Google Business Profile aanmaken.
4. De site in de Instagram-bio zetten, met een link naar `/journeys/` in plaats
   van naar de homepage.
