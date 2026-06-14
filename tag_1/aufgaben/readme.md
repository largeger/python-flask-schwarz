# 🏋️ Aufgaben Tag 1: Flask Grundlagen

## Aufgabe 1: Der erste Server 🍦
Erstelle eine Datei `app.py`.
1. Installiere Flask mit `pip install flask`.
2. Erstelle eine Flask-App, die auf der Route `/` den Text "Hallo Bootcamp!" zurückgibt.
3. Starte den Server im Debug-Modus.

---

## Aufgabe 2: Begrüßungs-Komitee 🤝
Erweitere deine App um folgende Routen:
1. `/begruessung/<name>`: Gibt "Hallo [Name], schön dass du da bist!" zurück.
2. `/alter/<int:jahre>`: Gibt "Du bist [Jahre] Jahre alt." zurück.
3. `/umdrehen/<wort>`: Gibt das Wort rückwärts zurück (Tipp: `wort[::-1]`).

---

## Aufgabe 3: Mini-Rechenzentrum 🔢
Erstelle eine Route `/rechner/<int:a>/<int:b>`, die ein JSON-Objekt mit folgendem Inhalt zurückgibt:
- `summe`: a + b
- `differenz`: a - b
- `produkt`: a * b
- `quotient`: a / b (Vorsicht bei b=0!)

---

## Aufgabe 4: Profil-API 👤 (Groß)
Stell dir vor, du baust ein Backend für eine Social Media App.
Erstelle eine Route `/api/profil/<username>`.
- Wenn der Username "admin" ist, gib ein JSON mit Admin-Daten zurück (Name, Rolle: Admin, Status: Aktiv).
- Wenn der Username "gast" ist, gib ein JSON mit eingeschränkten Daten zurück.
- Für alle anderen Usernamen gib eine Nachricht zurück: "Benutzer nicht gefunden", und nutze den HTTP Status Code 404.

Tipp für Status Codes:
```python
return {"error": "not found"}, 404
```

---

## Aufgabe 5: Der Horoskop-Generator 🔮 (Große Aufgabe)
Baue eine API, die basierend auf einem Geburtsdatum die Zukunft vorhersagt!

**Endpunkt:** `/api/horoskop/<datum>`

**Anforderungen:**
1. Der Endpunkt nimmt ein Datum entgegen (z.B. `12.06.1990`).
2. Er generiert drei zufällige Werte zwischen **1 und 100** für:
   - `glueck`
   - `karma`
   - `energie`
3. Er wählt eine zufällige witzige Nachricht aus einer Liste von mindestens 5 Horoskop-Messages aus.
4. Die Antwort soll ein **JSON-Objekt** sein.

**Beispiel-Response:**
```json
{
  "datum": "12.06.1990",
  "glueck": 87,
  "karma": 12,
  "energie": 99,
  "botschaft": "Heute ist ein guter Tag, um eine neue Programmiersprache zu lernen. Meide jedoch Kaffeeautomaten."
}
```

**Tipps:**
- Importiere das `random` Modul.
- Nutze `random.randint(1, 100)` für die Werte.
- Nutze `random.choice(meine_liste)` für die Botschaft.
