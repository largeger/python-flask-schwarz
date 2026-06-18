# 🚀 Tag 5: Dateiuploads & Deployment

## 📖 Theorie-Impuls: Sicherheit beim Upload
Dateien von Benutzern sind ein Sicherheitsrisiko. Wir müssen:
1. Den Dateinamen säubern (`secure_filename`).
2. Den Dateityp prüfen (z.B. nur `.jpg`, `.png`).
3. Die Dateigröße limitieren.

---

## 🛠️ Upload & Deployment Cheat Sheet

### 1. Dateiupload Konfiguration
```python
import os
from werkzeug.utils import secure_filename

app.config['UPLOAD_FOLDER'] = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
```

### 2. File im POST-Request verarbeiten
```python
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "Keine Datei"
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "Datei gespeichert!"
```

### 3. Wichtige Deployment-Schritte
- **Umgebungsvariablen:** Nutze `python-dotenv` für `SECRET_KEY` und `DATABASE_URL`.
- **WSGI Server:** Nutze `gunicorn` anstelle des Flask-Debug-Servers.
  ```bash
  gunicorn app:app
  ```
- **Requirements:** Erstelle eine `requirements.txt`.
  ```bash
  pip freeze > requirements.txt
  ```

### 4. Containerisierung mit Docker 🐳
Ein Dockerfile beschreibt die Umgebung für deine App:

```dockerfile
# 1. Basis-Image (Python)
FROM python:3.11-slim

# 2. Arbeitsverzeichnis erstellen
WORKDIR /app

# 3. Abhängigkeiten kopieren & installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Den restlichen Code kopieren
COPY . .

# 5. Startbefehl (Gunicorn)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
```

**Wichtige Docker-Befehle:**
- Image bauen: `docker build -t meine-flask-app .`
- Container starten: `docker run -p 8000:8000 meine-flask-app`

### ⚠️ Profi-Tipp: Der Build-Kontext & Startbefehl
Ein häufiger Fehler (`ModuleNotFoundError`) entsteht durch einen falschen Startpunkt des Builds oder falsche Modulnamen.

**Die goldene Regel:**
1. Wechsle immer erst in das Verzeichnis, das dein `Dockerfile` enthält.
2. Verwende deine Hauptdatei `app.py` und binde sie über `app:app` in Gunicorn ein.

```bash
# 1. In den Projektordner gehen
cd tag_5/demo_projekt

# 2. Image bauen
docker build -t meine-flask-app .

# 3. Container starten
docker run -p 8000:8000 meine-flask-app
```

**Verifizierung:** Falls es immer noch klemmt, kannst du mit `docker run --rm meine-flask-app ls -R /code` prüfen, ob deine Dateien wirklich dort gelandet sind, wo Gunicorn sie erwartet.

---

### 5. Multi-Container-Orchestrierung mit Docker Compose 🐳🐘

Wenn deine App eine externe Datenbank (wie PostgreSQL) benötigt, verwaltest du beide Services am besten über Docker Compose in einer `docker-compose.yml` Datei.

**Vorteile:**
1. Kein manuelles Erstellen und Verlinken von virtuellen Docker-Netzwerken.
2. Automatischer Start aller benötigten Services mit einem einzigen Befehl.
3. Einfache Konfiguration von Volumes zur permanenten Datenspeicherung (Datenpersistenz).

**Beispiel `docker-compose.yml` (Flask + Postgres):**
```yaml
services:
  # --- DATENBANK SERVICE (Postgres) ---
  db:
    image: postgres:15
    container_name: travel_db
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: travel_journal
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck: # Prüft regelmäßig, ob der Postgres-Server bereit ist
      test: ["CMD-SHELL", "pg_isready -U user -d travel_journal"]
      interval: 5s
      timeout: 5s
      retries: 5

  # --- WEB APP SERVICE (Flask) ---
  web:
    build: .
    container_name: travel_app
    ports:
      - "8000:8000"
    environment:
      # Hostname entspricht dem Namen des Services ("db")
      DATABASE_URL: postgresql://user:password@db:5432/travel_journal
      SECRET_KEY: super-geheim-123
    depends_on:
      db:
        condition: service_healthy # Startet erst, wenn db als "healthy" eingestuft ist
    volumes:
      # Persistierung hochgeladener Bilder auf dem Host-Rechner
      - ./static/uploads:/app/static/uploads

volumes:
  postgres_data:
```

**Wichtige Docker Compose Befehle:**
*   Services bauen und starten: `docker compose up --build`
*   Services im Hintergrund starten: `docker compose up -d`
*   Container stoppen und Netzwerke/Container löschen: `docker compose down`

---

### 6. Dynamische Datenbankverbindung (SQLite & Postgres Fallback) 💾

Damit deine Anwendung sowohl lokal (direkt auf deinem PC mit SQLite) als auch innerhalb der Docker Compose Umgebung (mit Postgres) lauffähig ist, solltest du deine Datenbankverbindung in `app.py` dynamisch über Umgebungsvariablen steuern:

```python
import os
from flask import Flask
from models import db

app = Flask(__name__)

# Wenn DATABASE_URL existiert (Docker), nutzen wir PostgreSQL.
# Falls nicht (lokale Entwicklung), weichen wir automatisch auf SQLite aus.
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 
    'sqlite:///travel_journal.db'
)
```

---

## 🎯 Lernziele für heute
- [ ] Bilder sicher auf den Server hochladen und verarbeiten
- [ ] Die Dateipfade in der Datenbank speichern und im HTML referenzieren
- [ ] Eine `requirements.txt` und `.env` für die Deployment-Vorbereitung erstellen
- [ ] Eine Flask-Anwendung mithilfe eines `Dockerfile` containerisieren
- [ ] Das Konzept eines WSGI-Servers (`gunicorn`) verstehen
- [ ] Mehrere Container (Web-App & Datenbank) über Docker Compose orchestrieren

