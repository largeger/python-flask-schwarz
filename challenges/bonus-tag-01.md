# Projekt-Aufgabe: E-Commerce Analytics Dashboard mit Flask, Pandas, NumPy & Matplotlib

## 1. Szenario und Zielsetzung
Ein mittelständisches E-Commerce-Unternehmen ("ShopifyPlus-Analyzer") benötigt ein internes Web-Dashboard zur Visualisierung und Analyse seiner Verkaufsdaten. Da die IT-Abteilung Ressourcen sparen möchte, soll ein Prototyp vollständig in Python umgesetzt werden.

Ihre Aufgabe ist es, eine eigenständige Web-Anwendung mit **Flask** zu entwickeln. Die Daten sollen mithilfe von **NumPy** realistisch simuliert, mit **Pandas** aggregiert und analysiert, und mit **Matplotlib** visuell aufbereitet werden.

---

## 2. Projektarchitektur & Struktur
Das Projekt soll folgende Ordnerstruktur aufweisen:

```text
ecommerce_dashboard/
│
├── app.py                 # Hauptanwendung (Flask-Routen und Logik)
├── data_analytics.py      # Daten-Generierung und Pandas-Analyse
├── README.md              # Dokumentation (wird hier erstellt)
│
├── static/
│   └── css/
│       └── style.css      # Optional: Minimales Styling
│
└── templates/
    └── dashboard.html     # HTML-Template für das Dashboard
```

---

## 3. Detaillierte Anforderungen
### Teil A: Daten-Simulation & -Verarbeitung (`data_analytics.py`)

#### 1. Daten-Generierung (NumPy):
- Schreiben Sie eine Funktion `generate_sales_data(n_rows=5000)`, die ein künstliches Verkaufs-Dataset für das aktuelle/vergangene Jahr generiert.
- Folgende Spalten müssen erzeugt werden:
  - `Bestelldatum`: Ein Zeitraum über die letzten 12 Monate (`pd.date_range`).
  - `Produktkategorie`: Zufällige Auswahl aus `['Elektronik', 'Bekleidung', 'Wohnen', 'Sport', 'Bücher']` mit vordefinierten Wahrscheinlichkeiten (z.B. Elektronik ist beliebter als Bücher).
  - `Menge`: Ganzzahlen zwischen 1 und 5 (Nutzen Sie `np.random.randint` oder Ähnliches).
  - `Einzelpreis`: Normalverteilte Preise um einen Mittelwert (z.B. $\mu = 50$, $\sigma = 30$), abgesichert gegen negative Werte.
  - `Kundensegment`: Zufällige Zuordnung (`['Neukunde', 'Bestandskunde', 'VIP']`).
- Fügen Sie absichtlich ca. 2% künstliche Ausreißer oder Extremwerte (z.B. extrem hohe Mengen) sowie vereinzelte NaN-Werte in die Spalte Einzelpreis ein, um reale Daten zu simulieren.


#### 2. Datenbereinigung & Feature Engineering (Pandas):
- Schreiben Sie eine Funktion `clean_and_prepare_data(df)`, die:
  - Fehlende Werte (`NaN`) in `Einzelpreis` durch den Median der jeweiligen Produktkategorie ersetzt.
  - Extremwerte (z.B. Mengen > 20) filtert oder auf ein Maximum begrenzt.
  - Eine neue Spalte Gesamtumsatz berechnet ($Menge \times Einzelpreis$).
  - Eine neue Spalte `Monat` im Format `YYYY-MM` extrahiert.

#### 3. Metriken & Aggregationen:
- Erstellen Sie eine Funktion `get_kpis(df)`, die ein Dictionary mit folgenden Kennzahlen zurückgibt:
  - Gesamter Umsatz des Unternehmens.
  - Anzahl der Bestellungen.
  - Durchschnittlicher Warenkorbwert (Average Order Value).
  - Top-Produktkategorie nach Umsatz.

### Teil B: Daten-Visualisierung (Matplotlib)
Erstellen Sie in `data_analytics.py` eine Funktion `generate_plots(df, category_filter=None)`, die Diagramme generiert. Wenn ein Filter gesetzt ist, sollen die Diagramme entsprechend angepasst werden.
1. Trend-Linie: Monatlicher Gesamtumsatz im Zeitverlauf.
2. Kategorie-Verteilung: Ein Bar- oder Pie-Chart, das den Umsatzanteil der Produktkategorien zeigt.
3. Wichtig für Flask: Die Diagramme dürfen nicht auf der Festplatte gespeichert werden. Nutzen Sie `io.BytesIO` und das base64-Modul, um die Diagramme als Base64-Strings direkt in das HTML-Template einzubetten (`data:image/png;base64,...`).

### Teil C: Web-Anwendung (Flask in `app.py`)
1. Routen-Struktur:
   - `/` (Dashboard-Hauptseite): Lädt die Daten, berechnet die globalen KPIs, generiert die Grafiken und rendert das Template `dashboard.html`.
   - `/filter` (POST- oder GET-Request): Ermöglicht dem Nutzer, die Daten über ein Dropdown-Menü nach Produktkategorie oder Kundensegment zu filtern. Nach dem Filtern werden die KPIs und Diagramme nur für diese Teilmenge neu berechnet.
2. State-Management: Da die Daten dynamisch generiert werden, sollten Sie die Daten entweder einmalig beim Start der App generieren und global im Speicher halten (für diesen Prototyp ausreichend).
 
## Teil D: HTML-Template (`templates/dashboard.html`)
- Erstellen Sie ein sauberes Dashboard-Layout.
- Anzeigen der 4 Haupt-KPIs in strukturierten Boxen.
- Ein Formular mit einer Dropdown-Auswahl für die Filterung (inklusive einer Option "Alle Kategorien").
- Einbetten der beiden Matplotlib-Diagramme mittels `<img src="data:image/png;base64,{{ plot_data }}">`.

--- 

## 4. Bonus-Herausforderung (Optional)
Nutzen Sie NumPy (`np.polyfit` und `np.poly1d`), um auf dem monatlichen Umsatztrend eine einfache lineare Regressionsgerade (Trendlinie) zu berechnen und diese gestrichelt im Matplotlib-Umsatzdiagramm anzuzeigen, um eine Prognose für die kommenden Monate zu visualisieren.

---

## 5. BewertungskriterienCode-Qualität:
- Trennung von Datenlogik (`data_analytics.py`) und Web-Logik (`app.py`).
- Korrekter Umgang mit Pandas: Effiziente Nutzung von `.groupby(`), `.fillna()` und Vektoroperationen statt Schleifen.
- Fehlerfreiheit: Keine Abstürze bei extremen Filtereinstellungen (z.B. wenn für einen Filter keine Daten existieren).
- Visualisierung: Korrekte Beschriftung der Achsen, Legenden und saubere Konvertierung in Base64.
