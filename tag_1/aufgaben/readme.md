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
