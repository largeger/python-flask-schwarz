# 🏋️ Aufgaben Tag 5: Bilder & Deployment

## Aufgabe 1: Bild-Upload im Gästebuch 📸
**Bezieht sich auf:** Deine [**Gästebuch-App** aus Tag 4 (Aufgabe 1 & 3)](../../tag_4/aufgaben/uebungen-tag-04.md). Wir erweitern diese App, sodass Besucher optional ein Foto (z.B. ein Selfie oder ein Bild zur Nachricht) hochladen können.
1. Erweitere dein Datenbankmodell `GuestbookEntry` um ein Feld `image_file` (String, darf `nullable=True` sein).
2. Passe das Formular im Template an: Füge ein Datei-Upload-Feld (`<input type="file" name="image">`) hinzu. Wichtig: Setze `enctype="multipart/form-data"` im `<form>`-Tag!
3. Verarbeite die hochgeladene Datei in deiner Controller-Route: Nutze `secure_filename()` zur Bereinigung des Dateinamens und speichere das Bild im Verzeichnis `static/uploads/`.
4. Speichere den bereinigten Dateinamen in der Datenbank beim jeweiligen Gästebucheintrag.

---

## Aufgabe 2: Bilder im Gästebuch anzeigen 🖼️
**Bezieht sich auf:** Das Frontend deiner **Gästebuch-App**.
1. Passe das Jinja2-Template deiner Gästebuch-Ansicht so an, dass das hochgeladene Bild für jeden Eintrag angezeigt wird.
2. Falls für einen Eintrag kein Bild hochgeladen wurde, soll ein Platzhalterbild oder ein Icon (z.B. 👤) gerendert werden. Nutze hierzu eine Jinja-Bedingung (`{% if entry.image_file %}...{% else %}...{% endif %}`).

---

## Aufgabe 3: Vorbereitung fürs Deployment 📦
**Bezieht sich auf:** Deine fertige, erweiterte **Gästebuch-App** (mit Blueprint-Refactoring aus Tag 4).
1. Erstelle eine Datei `requirements.txt` im Root-Verzeichnis deines Gästebuch-Projekts mit allen installierten Paketen (`flask`, `flask-sqlalchemy`, `python-dotenv`, `gunicorn`).
2. Erstelle eine Datei `.env` (NICHT in Git einchecken!) und definiere darin deinen `SECRET_KEY` und ggf. deine Konfigurationsvariablen.
3. Lade den Key in deiner Hauptdatei `app.py` dynamisch über `os.getenv('SECRET_KEY', 'default-dev-key')`.

---

## Aufgabe 4: Containerisierung mit Docker 🐳
**Bezieht sich auf:** Deine fertige, erweiterte **Gästebuch-App**.
1. Erstelle eine Datei namens `Dockerfile` im Root-Verzeichnis deines Gästebuch-Projekts.
2. Nutze `python:3.11-slim` als Basis-Image.
3. Kopiere die `requirements.txt`, installiere die Abhängigkeiten und kopiere anschließend deinen Anwendungscode.
4. Setze den Startbefehl (CMD) auf `gunicorn --bind 0.0.0.0:8000 app:app`.
5. Erstelle eine `.dockerignore` Datei (schließe `venv/`, `.env` und die SQLite-Datenbankdatei `.db` aus).
6. Baue das Docker-Image und starte den Container lokal. Teste die Erreichbarkeit unter `http://localhost:8000`.

---

## Aufgabe 5: Das Wochen-Projekt 🏆 (Sehr Groß)
Kombiniere ALLES:
Baue eine **Reise-Tagebuch** App. Gehe dabei am besten in folgenden Schritten vor:

1. **Schritt 1: Projekt-Struktur & Blueprints**
   - Erstelle folgende Ordner: `templates/`, `static/css/`, `static/uploads/` und `blueprints/`.
   - Erstelle in `blueprints/` zwei Dateien:
     - `main.py` (für die öffentliche Ansicht der Reiseziele).
     - `admin.py` (für das Verwalten/CRUD der Reiseziele).
   - Registriere beide Blueprints in deiner zentralen `app.py`.
2. **Schritt 2: Datenbankschema entwerfen**
   - Definiere ein SQLAlchemy-Modell `TravelDestination` mit folgenden Feldern:
     - `id` (Integer, Primary Key)
     - `title` (String, Pflichtfeld)
     - `description` (Text, Pflichtfeld)
     - `date_visited` (Date, Pflichtfeld)
     - `image_file` (String, optional, für den Bildnamen)
     - `created_at` (DateTime, mit Default-Wert `datetime.utcnow`)
3. **Schritt 3: Bild-Upload absichern & implementieren**
   - Konfiguriere den Upload-Pfad und die erlaubten Dateitypen (`ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}`) in deiner `app.py`.
   - Schreibe eine Hilfsfunktion `allowed_file(filename)`.
   - Sichere hochgeladene Dateien beim Speichern im Backend ab: Nutze `secure_filename(file.filename)`, speichere sie in `static/uploads/` und lege den Dateinamen in der Spalte `image_file` ab.
4. **Schritt 4: Frontends & Jinja2 Templates erstellen**
   - Baue ein Basis-Layout (`layout.html`) mit einer Navigationsleiste.
   - Baue die öffentliche Startseite (`index.html`), die alle Reiseziele in einem schönen CSS-Grid (Karten-Layout mit Bild, Titel, Beschreibung, Reisedatum) auflistet.
   - Baue ein Admin-Dashboard (`admin.html`), das alle Einträge in einer Tabelle auflistet und Links/Buttons für "Erstellen" (Formular mit Datei-Upload), "Bearbeiten" und "Löschen" bereitstellt.
5. **Schritt 5: Validierung & Flash-Messages**
   - Prüfe bei jedem POST-Request, ob alle Pflichtfelder ausgefüllt sind.
   - Nutze Flasks `flash()` Funktion, um dem Nutzer Feedback zu geben (z.B. "Ziel erfolgreich hinzugefügt! ✈️" oder "Eintrag erfolgreich gelöscht.").
   - Stelle sicher, dass die Flash-Messages im Basis-Template über `get_flashed_messages()` gerendert werden.
6. **Schritt 6 (Optionaler Bonus): Containerisierung**
   - Erstelle ein `Dockerfile` und ein passendes `docker-compose.yml` Setup, um dein Reisetagebuch voll containerisiert mit SQLite oder PostgreSQL laufen zu lassen.


---

## Aufgabe 6: Horoskop 3.0 – Bilder & Docker 🔮🐳
Setze unser "roter Faden"-Projekt fort und mache es bereit für die Cloud!

1. **Bilder-Upload:**
   - Erweitere dein `HoroscopeLog`-Modell um ein Feld `image_file`.
   - Füge dem Horoskop-Formular ein Upload-Feld hinzu, damit User ein "Stimmungsbild" mitsenden können.
   - Speichere die Bilder in `static/uploads/`.
2. **Archiv-Upgrade:**
   - Zeige im Horoskop-Archiv die hochgeladenen Bilder in klein (Thumbnails) an.
3. **Produktions-Ready:**
   - Erstelle ein `Dockerfile` für die App.
   - Nutze `gunicorn --bind 0.0.0.0:8000 app:app` als Startbefehl.
   - Nutze eine `.env` Datei für den `SECRET_KEY`.
   - **Bonus:** Nutze eine `.dockerignore`, um die SQLite-DB und venv nicht in das Image zu kopieren.

---

## Aufgabe 7: Horoskop 4.0 – Docker Compose & PostgreSQL 🔮🐳🐘
Mache dein Horoskop-Projekt fit für größere Datenmengen und skaliere die Infrastruktur mit einer echten PostgreSQL-Datenbank über Docker Compose.

1. **Datenbank-Konfiguration anpassen:**
   - Ändere die Datenbank-Verbindung in deiner `app.py` so ab, dass sie die Umgebungsvariable `DATABASE_URL` ausliest.
   - Baue einen Fallback auf die lokale SQLite-Datenbank (`sqlite:///horoscope.db`) ein, falls `DATABASE_URL` nicht gesetzt ist.
2. **Docker Compose Setup:**
   - Erstelle eine `docker-compose.yml` im Root deines Horoskop-Projekts.
   - Definiere zwei Services: `db` (mit dem Image `postgres:15`) und `web` (dein Flask-Image, gebaut aus dem lokalen `Dockerfile`).
   - Übergebe der Flask-App über die `environment`-Sektion die `DATABASE_URL` (z.B. `postgresql://user:password@db:5432/horoscope_db`).
3. **Persistenz & Ausfallsicherheit:**
   - Richte Docker Volumes für die Postgres-Daten (`postgres_data`) und die Bilder-Uploads (`./static/uploads`) ein, damit keine Daten beim Stoppen des Containers verloren gehen.
   - Definiere einen `healthcheck` für den Postgres-Dienst und stelle über `depends_on` mit `condition: service_healthy` sicher, dass dein Web-Service erst gestartet wird, wenn die Datenbank voll einsatzbereit ist.
4. **Inbetriebnahme:**
   - Starte das Projekt mit `docker compose up --build` und teste, ob Horoskop-Einträge inklusive Bilder erfolgreich hochgeladen und in der Postgres-Datenbank persistiert werden.
