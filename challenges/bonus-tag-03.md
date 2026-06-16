# Projekt-Aufgabe: WealthWise – Der intelligente Investment-Tracker

## 1. Szenario und Zielsetzung
Finanzielle Freiheit durch Überblick! Sie sollen ein professionelles Dashboard zur Verwaltung eines Investment-Portfolios entwickeln. Während Tag 3 die Grundlagen von Datenbanken behandelt hat, geht dieses Projekt einen Schritt weiter: Wir nutzen **komplexe Beziehungen** (One-to-Many), integrieren **Echtzeit-Finanzdaten** und visualisieren das Portfolio mit interaktiven Charts.

Die Anwendung "WealthWise" erlaubt es Nutzern, verschiedene Assets (Aktien, Kryptowährungen, Gold) zu erfassen, deren aktuellen Wert über eine API abzurufen und die Wertentwicklung sowie die Diversifikation grafisch darzustellen.

---

## 2. Projektarchitektur & Struktur
Das Projekt soll eine saubere Trennung von Modellen und Logik aufweisen:

```text
wealthwise_tracker/
│
├── app.py                 # Hauptanwendung & Routen
├── models.py              # Datenbank-Modelle (SQLAlchemy)
├── finance_api.py         # Logik für API-Abrufe (yfinance)
├── requirements.txt       # Projektspezifische Abhängigkeiten
│
├── static/
│   └── css/
│       └── style.css      # Custom Styling
│
└── templates/
    ├── layout.html        # Basis-Layout
    └── dashboard.html     # Das Haupt-Dashboard
```

---

## 3. Detaillierte Anforderungen

### Teil A: Fortgeschrittenes Datenbank-Design (`models.py`)
Erstellen Sie eine Datenbankstruktur mit **Beziehungen**:
1. **Modell `Category`:** (z.B. "Aktien", "Krypto", "Rohstoffe")
   - `id`, `name`, `color` (Hex-Code für Charts).
2. **Modell `Asset`:**
   - `id`, `symbol` (z.B. AAPL, BTC-USD), `name`, `amount` (Menge im Besitz).
   - **Relationship:** Jedes Asset gehört zu einer `Category` (ForeignKey).
3. **Modell `PriceHistory` (Optional/Bonus):**
   - Speichert historische Preise für ein Asset, um Trends zu zeigen.

### Teil B: Externe Daten-Integration (`finance_api.py`)
Hier nutzen wir eine neue Library: **`yfinance`**.
1. Schreiben Sie eine Funktion `get_current_price(symbol)`, die mithilfe von `yfinance` den aktuellsten Kurs abruft.
2. Implementieren Sie ein Error-Handling für Symbole, die nicht gefunden werden.

### Teil C: Das Flask-Backend (`app.py`)
1. **Initialisierung:** Erstellen Sie beim Start der App die Datenbank und legen Sie Standard-Kategorien an.
2. **Portfolio-Berechnung:** 
   - Loop über alle Assets in der DB.
   - Rufe aktuellen Preis via API ab.
   - Berechne den Gesamtwert (`amount * price`).
3. **Daten-Übergabe:** Übergeben Sie die berechneten Werte und die Kategorien an das Template.

### Teil D: Interaktive Visualisierung (Plotly)
Anstatt statischer Bilder (Matplotlib) nutzen wir **Plotly** für interaktive Web-Charts.
1. Erstellen Sie ein **Pie-Chart**, das die Verteilung des Portfolios nach Kategorien zeigt.
2. Erstellen Sie ein **Bar-Chart**, das den Gesamtwert pro Asset anzeigt.
3. Wandeln Sie die Plotly-Charts in JSON um (`plotly.utils.PlotlyJSONEncoder`), um sie im Template mit `Plotly.newPlot()` anzuzeigen.

---

## 4. Bonus-Herausforderung (Optional)
- **Caching:** Da API-Abrufe langsam sind, speichern Sie die abgerufenen Preise für 10 Minuten in einer temporären Variable oder einer Cache-Tabelle.
- **Transaktions-Historie:** Erstellen Sie ein drittes Modell `Transaction`, um Käufe und Verkäufe zu protokollieren und den durchschnittlichen Kaufpreis zu berechnen.

---

## 5. Neue Python-Libraries
Für dieses Projekt müssen Sie folgende Module installieren und nutzen:
- `yfinance` (Finanzdaten-Schnittstelle)
- `plotly` (Interaktive Diagramme)

---

## 6. Bewertungskriterien
- **ORM-Beziehungen:** Korrekte Umsetzung der One-to-Many Beziehung zwischen Kategorie und Asset.
- **API-Stabilität:** Die App darf nicht abstürzen, wenn das Internet weg ist oder ein falsches Symbol eingegeben wird.
- **Frontend-Integration:** Saubere Einbindung der Plotly-Skripte im HTML-Template.
- **Code-Struktur:** Logische Trennung der Funktionen (API-Logik vs. Datenbank-Modelle).

---

**Viel Erfolg beim Aufbau von WealthWise! 📈💰**
