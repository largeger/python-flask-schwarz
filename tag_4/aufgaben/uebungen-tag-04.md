# 🏋️ Aufgaben Tag 4: Formulare & Feedback

## Aufgabe 1: Das Gästebuch 📖
1. Erstelle ein Modell `GuestbookEntry` (Name, Nachricht, Datum).
2. Erstelle eine Route `/gaestebuch`, die alle Einträge anzeigt.
3. Füge auf dieser Seite ein HTML-Formular hinzu, um neue Einträge zu erstellen (POST).
4. Nutze `flash()`, um dem User zu sagen, dass sein Eintrag erfolgreich war.

---

## Aufgabe 2: Passwort-Check 🔐
1. Baue eine Login-Seite `/login`.
2. Wenn das Passwort "geheim123" ist, leite den User auf eine Seite `/geheimnis` weiter.
3. Wenn das Passwort falsch ist, nutze `flash()` mit der Kategorie `danger`, um eine Fehlermeldung anzuzeigen.

---

## Aufgabe 3: Refactoring mit Blueprints 🏗️
Nimm deine App aus Aufgabe 1.
1. Erstelle eine Datei `main.py` und definiere darin einen Blueprint für die öffentlichen Seiten (`/`, `/gaestebuch`).
2. Erstelle eine Datei `admin.py` und definiere darin einen Blueprint für Admin-Zwecke (z.B. `/admin/delete/<id>`).
3. Registriere beide Blueprints in deiner zentralen `app.py`.

---

## Aufgabe 4: Der Event-Planer 📅 (Groß)
Da der Blog bereits im Demo-Projekt behandelt wurde, baust du nun einen Event-Planer.
1. Erstelle ein Modell `Event` (Titel, Ort, Datum, Beschreibung).
2. Erstelle eine Seite zum Anlegen von Events. Nutze ein Formular mit:
   - `<input type="text">` für Titel und Ort.
   - `<input type="date">` für das Datum.
   - `<textarea>` für die Beschreibung.
3. Implementiere eine Validierung:
   - Titel und Ort dürfen nicht leer sein.
   - Die Beschreibung muss mindestens 20 Zeichen lang sein.
4. Zeige alle geplanten Events auf einer Übersichtsseite in chronologischer Reihenfolge an.

---

## Aufgabe 5: Horoskop 2.0 – Das Formular 🔮 (Fortsetzung)
In den letzten Tagen haben wir das Horoskop über URLs oder JavaScript (Alpine) gesteuert. Heute nutzen wir ein klassisches Server-Side Formular.

1. **Eingabe-Formular:**
   - Erstelle eine Route `/horoskop/neu`.
   - Baue ein HTML-Formular, in dem der User seinen Namen und sein Geburtsdatum eingeben kann.
2. **Verarbeitung (POST):**
   - Wenn das Formular abgeschickt wird, generiere im Backend das Horoskop (nutze deine Logik aus den Vortagen).
   - Speichere die Anfrage in deiner `HoroscopeLog` Datenbank (aus Tag 3).
3. **Feedback:**
   - Nutze `flash()`, um eine Erfolgsmeldung anzuzeigen.
   - Leite den User auf eine Detailseite weiter, die nur sein gerade generiertes Horoskop anzeigt.
