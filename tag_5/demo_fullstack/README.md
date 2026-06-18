# 🌍 Tag 5: Multi-Container Fullstack Demo (Postgres & Docker Compose)

Dieses Demo-Projekt zeigt eine voll funktionsfähige, datenbankgestützte Reise-Tagebuch-Anwendung (Travel Log). Sie basiert auf professionellen Best Practices für Flask 3.x, PostgreSQL und Docker Compose Orchestrierung.

## 🛠️ Features & Architektur
- **App Factory Pattern:** Strukturierte App-Instanziierung über `create_app()` in [app.py](file:///D:/python-flask-schwarz/tag_5/demo_fullstack/app.py).
- **Blueprints:** Aufteilung der Routen in Module unter `blueprints/journal.py`.
- **Datenpersistenz:** Speicherung von Reise-Einträgen in PostgreSQL und hochgeladenen Fotos in `static/uploads/`.
- **Orchestrierung:** Abgestimmter Multi-Container-Start über Docker Compose.

---

## 💻 1. Lokale Ausführung (SQLite-Fallback)
Um die App schnell lokal zu testen, ohne Postgres oder Docker zu installieren, greift das Projekt automatisch auf SQLite zurück:

1. Navigiere in diesen Ordner:
   ```bash
   cd tag_5/demo_fullstack
   ```
2. Installiere die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```
3. Starte den Flask-Entwicklungsserver:
   ```bash
   python app.py
   ```
4. Öffne im Browser: [http://localhost:8000](http://localhost:8000)

---

## 🐳 2. Docker Compose Deployment (Produktion/Postgres)
Für das vollwertige Multi-Container-Setup (Flask-Webserver + PostgreSQL-Datenbank):

1. **Docker Compose starten:**
   ```bash
   docker compose up --build
   ```
   *Hinweis: Der Webserver wartet dank des in Docker Compose definierten `healthcheck` (über `pg_isready`) und der Abhängigkeit `condition: service_healthy` automatisch, bis die PostgreSQL-Datenbank vollständig hochgefahren ist und Verbindungen akzeptiert.*

2. Öffne im Browser: [http://localhost:8000](http://localhost:8000)
3. **Beenden & Aufräumen:**
   ```bash
   docker compose down
   ```

---

## 📂 Wichtige Komponenten und Dateien
- [app.py](file:///D:/python-flask-schwarz/tag_5/demo_fullstack/app.py): App Factory und Initialisierung von Flask-SQLAlchemy.
- [models.py](file:///D:/python-flask-schwarz/tag_5/demo_fullstack/models.py): Das relationale Datenmodell für Tagebucheinträge.
- [blueprints/journal.py](file:///D:/python-flask-schwarz/tag_5/demo_fullstack/blueprints/journal.py): Der Blueprint für alle Reise-Routen und Logik (Upload-Validierung & CRUD-Aktionen).
- [docker-compose.yml](file:///D:/python-flask-schwarz/tag_5/demo_fullstack/docker-compose.yml): Definiert den Web- und den Datenbank-Container, Netzwerke, Volumes (für Bilder und Datenbank-Daten) sowie Startabhängigkeiten.
- [Dockerfile](file:///D:/python-flask-schwarz/tag_5/demo_fullstack/Dockerfile): Beschreibt den Container-Build und führt die App unter dem produktiven WSGI-Server **Gunicorn** aus.
