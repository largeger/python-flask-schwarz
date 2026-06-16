# Projekt-Aufgabe: Interaktiver Movie-Explorer "Cinemania" mit Flask & Alpine.js

## 1. Szenario und Zielsetzung
Sie sollen einen Prototyp für eine moderne Streaming-Plattform-Übersicht ("Cinemania") entwickeln. Der Fokus liegt diesmal auf einem exzellenten Nutzererlebnis durch **Progressive Enhancement**. Die Anwendung soll die strukturellen Stärken von **Jinja2** (Server-Side Rendering) mit der Leichtigkeit von **Alpine.js** (Client-Side Interactivity) kombinieren.

Ziel ist es, eine Filmdatenbank zu visualisieren, in der Nutzer in Echtzeit suchen, filtern und eine persönliche Merkliste (Watchlist) verwalten können – alles auf einer Seite, ohne nervige Seiten-Refreshes.

---

## 2. Projektarchitektur & Struktur
Das Projekt soll folgende Ordnerstruktur aufweisen:

```text
cinemania_explorer/
│
├── app.py                 # Flask-Anwendung mit Routen
├── static/
│   ├── css/
│   │   └── style.css      # Design & Layout
│   └── img/               # Platzhalter für Filmposter (optional)
│
└── templates/
    ├── layout.html        # Basis-Layout (Vererbung)
    ├── partials/          # (Optional) Kleinere Template-Stücke
    │   └── movie_card.html
    └── index.html         # Die Hauptseite (Movie-Explorer)
```

---

## 3. Detaillierte Anforderungen

### Teil A: Backend & Daten (`app.py`)
1. **Datenquelle:** Erstellen Sie eine Liste von mindestens 10-15 Filmen. Jeder Film sollte folgende Attribute haben:
   - `id` (Eindeutige ID)
   - `title` (Titel)
   - `year` (Erscheinungsjahr)
   - `genre` (z.B. Action, Sci-Fi, Drama, Komödie)
   - `rating` (0.0 bis 10.0)
   - `image_url` (Nutzen Sie Platzhalter-URLs wie `https://picsum.photos/seed/{id}/200/300`)
   - `description` (Ein kurzer Teaser-Text)

2. **Routen:**
   - `/`: Rendert die `index.html` und übergibt die Filmdaten als Liste an Jinja2.

### Teil B: Struktur & Design (Jinja2 & CSS)
1. **Layout-System:** Nutzen Sie Template-Vererbung (`extends`). Das Layout soll eine moderne, dunkle Navigationsleiste und einen Footer enthalten.
2. **Movie-Cards:** Erstellen Sie ein Grid-Layout. Jede Karte soll das "Poster", den Titel, das Genre und das Rating (vielleicht als Sterne-Symbole) anzeigen.
3. **Styling:** Nutzen Sie CSS-Variablen für ein konsistentes Farbschema (z.B. Dark-Mode: Hintergrund dunkles Grau, Akzentfarbe Gold oder Neon-Blau).

### Teil C: Interaktivität (Alpine.js - "The Pro Layer")
Hier wird die App "lebendig". Die gesamte Film-Liste soll in einer Alpine-Komponente verwaltet werden.

1. **Echtzeit-Suche:** Implementieren Sie ein Suchfeld. Während der Nutzer tippt, sollen die Movie-Cards, die nicht zum Titel passen, sofort ausgeblendet werden (Nutzen Sie `x-model` und `x-show`).
2. **Genre-Filter:** Erstellen Sie Buttons oder ein Dropdown für die Genres. Ein Klick filtert die Ansicht sofort.
3. **Persönliche Watchlist:**
   - Jeder Film hat einen "Hinzufügen"-Button.
   - Die Watchlist wird lokal im Browser-Zustand (`x-data`) verwaltet.
   - Zeigen Sie in der Navigationsleiste einen Counter an (z.B. "Watchlist: 3"), der sich sofort aktualisiert.
4. **Quick-View Modal:** Beim Klick auf eine Karte soll sich ein Modal-Fenster öffnen, das die `description` und weitere Details zum Film anzeigt (Nutzen Sie `x-show` und `@click.outside`).

---

## 4. Bonus-Herausforderung (Optional)
- **Sortierung:** Implementieren Sie eine Sortierfunktion (z.B. "Neueste zuerst" oder "Bestbewertete zuerst").
- **Persistence:** Speichern Sie die Watchlist im `localStorage`, sodass die Auswahl auch nach einem Neuladen der Seite erhalten bleibt.

---

## 5. Bewertungskriterien
- **Saubere Trennung:** Jinja2 für die initiale Auslieferung der Daten, Alpine.js für die Interaktion.
- **UX-Details:** Reibungslose Übergänge (Transitions) beim Ein-/Ausblenden von Karten (Tipp: `x-transition`).
- **Code-Struktur:** Korrekte Nutzung von `tojson`, um die Python-Liste sicher an das JavaScript-Objekt in Alpine.js zu übergeben.
- **Design:** Ein ansprechendes, "App-artiges" Interface.

---

**Viel Erfolg beim Bau von Cinemania! 🍿🎬**
