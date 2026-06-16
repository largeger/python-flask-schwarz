# 🏋️ Aufgaben Tag 3: Datenbanken & CRUD

## Aufgabe 1: Datenbank Setup ⚙️
1. Installiere `flask-sqlalchemy`.
2. Erstelle eine Flask-App mit einer SQLite-Datenbank.
3. Definiere ein Modell `Task`:
   - `id`: Integer, Primary Key
   - `content`: String (nicht leerbar)
   - `is_completed`: Boolean (Standard: False)
4. Erstelle die Datenbank-Datei (`db.create_all()`).

---

## Aufgabe 2: Daten manuell hinzufügen ✍️
Nutze die Python-Konsole (oder ein kleines Skript), um:
1. Drei verschiedene Aufgaben in die Datenbank zu speichern.
2. Alle Aufgaben wieder auszugeben (`Task.query.all()`).
3. Nur die erste Aufgabe auszugeben.

---

## Aufgabe 3: Die ToDo-Liste im Browser 🌐
1. Erstelle eine Route `/tasks`, die alle Aufgaben aus der Datenbank lädt.
2. Übergib diese Aufgaben an ein Template `tasks.html`.
3. Zeige die Aufgaben in einer Liste an. Wenn `is_completed` True ist, streiche den Text durch (HTML: `<s>`).

---

## Aufgabe 4: Buch-Katalog 📚 (Groß)
Erstelle ein neues Modell `Book` mit Titel, Autor und Seitenanzahl.
1. Baue eine API-Route `/api/books`, die alle Bücher als JSON zurückgibt.
2. Baue eine Route `/api/books/add`, die per GET-Parameter (z.B. `/api/books/add?title=Python&author=Lars`) ein neues Buch speichert.
3. Baue eine Route `/api/books/delete/<int:id>`, die ein Buch anhand seiner ID löscht.

Tipp für JSON-Umwandlung von Objekten:
```python
@app.route("/api/books")
def get_books():
    books = Book.query.all()
    return {"books": [{"title": b.title, "author": b.author} for b in books]}
```

---

## Aufgabe 5: Das Horoskop-Archiv 🔮 (Fortsetzung von Tag 1 & 2)
Bisher wurden deine Horoskope nur zufällig generiert und waren nach einem Seiten-Refresh weg. Jetzt machen wir sie persistent!

1. **Datenmodell erstellen:**
   - Erstelle ein Modell `HoroscopeLog`.
   - Felder: `id`, `requested_date` (String), `glueck` (Integer), `karma` (Integer), `energie` (Integer), `message` (Text), `created_at` (DateTime, Standard: `datetime.utcnow`).

2. **Speicher-Logik:**
   - Passe deine Horoskop-API-Route (`/api/horoskop/<datum>`) an.
   - Jedes Mal, wenn ein neues Horoskop generiert wird, speichere es zusätzlich als neuen Eintrag in der Datenbank.

3. **Das Archiv-Frontend:**
   - Erstelle eine Route `/horoskop/archiv`.
   - Lade alle gespeicherten Horoskope aus der Datenbank (sortiert nach `created_at` absteigend).
   - Zeige sie in einer schönen Liste oder Tabelle an, damit man sehen kann, welche Vorhersagen bisher getroffen wurden.

4. **Lösch-Funktion (Optional):**
   - Füge einen Button neben jedem Archiv-Eintrag hinzu, um alte Vorhersagen aus der Datenbank zu löschen.

**Tipp für DateTime:**
```python
from datetime import datetime
created_at = db.Column(db.DateTime, default=datetime.utcnow)
```
