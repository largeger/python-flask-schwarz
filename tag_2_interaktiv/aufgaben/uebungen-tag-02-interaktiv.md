# 🏋️ Alternative Aufgaben Tag 2: "Sprinkles" mit Alpine.js

## Aufgabe 1: Alpine.js Setup 🧪
1. Nutze dein Portfolio-Projekt aus dem regulären Tag 2.
2. Binde Alpine.js über das CDN in dein `layout.html` ein.
3. Erstelle einen Button auf der Startseite, der beim Klicken eine Nachricht anzeigt/versteckt (`x-data` und `x-show`).

---

## Aufgabe 2: Interaktive Projekt-Filter 🔍
1. Übergebe deine Projekt-Liste aus Flask an das Template.
2. Initialisiere eine Alpine-Komponente mit dieser Liste:
   ```html
   <div x-data="{ projects: {{ projects | tojson }}, filter: 'Alle' }">
   ```
3. Baue Buttons für jede Technologie (Flask, JavaScript, Python).
4. Wenn ein Button geklickt wird, soll sich die Liste der angezeigten Projekte automatisch filtern, ohne dass die Seite neu geladen werden muss.

---

## Aufgabe 3: Charakter-Zähler für Formulare ✍️
1. Erstelle ein einfaches Kontaktformular.
2. Füge ein `<textarea>` für eine Nachricht hinzu.
3. Nutze Alpine.js, um unter dem Textfeld live anzuzeigen, wie viele Zeichen der User bereits getippt hat.
4. Färbe den Zähler rot, wenn mehr als 100 Zeichen getippt wurden.

---

## Aufgabe 4: Das "Live" Dashboard 📊 (Groß)
Baue ein kleines Dashboard, das folgende interaktive Elemente enthält:
- Ein Tab-System (z.B. "Statistik", "Details", "Einstellungen"), bei dem der Inhalt wechselt, ohne die Seite neu zu laden.
- Ein Suchfeld, das eine Liste von Usern live filtert.
- Ein Modal-Fenster (Pop-up), das sich öffnet, wenn man auf einen "Info"-Button klickt, und sich schließt, wenn man außerhalb des Fensters klickt (`@click.outside`).

---

## Aufgabe 5: Der Horoskop-Client 🔮 (Fortsetzung von Tag 1)
In Tag 1 hast du eine API gebaut, die JSON-Daten für ein Horoskop liefert. Jetzt bauen wir das passende interaktive Frontend dazu!

1. **Vorbereitung:**
   - Kopiere deine Horoskop-Route (`/api/horoskop/<datum>`) in dein aktuelles Projekt (oder stelle sicher, dass sie erreichbar ist).
   - Erstelle ein Template `horoskop.html`, das von `layout.html` erbt.

2. **Alpine.js Logik:**
   - Nutze `x-data`, um den Zustand zu verwalten: `datum` (Eingabe), `result` (das vom Server geladene JSON), `loading` (Boolean).
   - Implementiere eine Funktion `fetchHoroskop()`, die:
     - `loading = true` setzt.
     - `fetch('/api/horoskop/' + this.datum)` aufruft.
     - Das Ergebnis in `this.result` speichert.
     - `loading = false` setzt.

3. **Interaktives UI:**
   - Ein `<input type="text">` (oder `date`), das via `x-model` mit `datum` verknüpft ist.
   - Ein Button, der `fetchHoroskop()` aufruft.
   - Eine Ladeanzeige (z.B. "Sterne werden befragt..."), die nur sichtbar ist, wenn `loading` true ist.
   - Wenn `result` geladen wurde: Zeige die Werte für Glück, Karma und Energie als Fortschrittsbalken oder farbige Badges an.
   - Zeige die witzige Botschaft in einer schicken Sprechblase oder Card an.

**Tipp:** Nutze `x-show="result"` oder `template x-if="result"`, um das Ergebnis erst anzuzeigen, wenn Daten vorhanden sind.
