# 🚀 Tag 5: Upload & Container-Demo (Basis)

Dieses Demo-Projekt demonstriert die Grundlagen des Dateiuploads in Flask und die Containerisierung einer einfachen Web-Anwendung mit Docker und Docker Compose.

Die Anwendung ermöglicht es Benutzern, Bilder hochzuladen und in einer einfachen In-Memory-Galerie anzuzeigen.

---

## 🛠️ Anforderungen & Installation

### Lokal ausführen
1. Navigiere in diesen Ordner:
   ```bash
   cd tag_5/demo_projekt
   ```
2. Installiere die lokalen Abhängigkeiten aus der `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
3. Starte die Anwendung:
   ```bash
   python app.py
   ```
4. Öffne im Browser: [http://localhost:5005](http://localhost:5005)

---

## 🐳 Docker Deployment

### 1. Einzelnen Docker-Container bauen & starten
Um die Anwendung in einer isolierten Docker-Umgebung auszuführen:

1. **Docker Image bauen:**
   ```bash
   docker build -t tag5-demo-app .
   ```
2. **Container starten:**
   ```bash
   docker run -p 8000:8000 tag5-demo-app
   ```
3. Öffne im Browser: [http://localhost:8000](http://localhost:8000)

---

### 2. Starten über Docker Compose
Dieses Projekt verfügt über eine `docker-compose.yml`, die das Verzeichnis `static/uploads/` als Volume einbindet. Dadurch bleiben hochgeladene Bilder auch dann erhalten, wenn der Container gestoppt oder gelöscht wird.

1. **Docker Compose starten:**
   ```bash
   docker compose up --build
   ```
2. Öffne im Browser: [http://localhost:8000](http://localhost:8000)
3. **Beenden:**
   ```bash
   docker compose down
   ```

---

## 📂 Wichtige Dateien
*   [app.py](file:///D:/python-flask-schwarz/tag_5/demo_projekt/app.py): Hauptdatei der Flask-App mit Upload-Validierung (`secure_filename`, Dateityp-Überprüfung).
*   [Dockerfile](file:///D:/python-flask-schwarz/tag_5/demo_projekt/Dockerfile): Beschreibt das Image (Python-Umgebung, Gunicorn als WSGI-Server).
*   [docker-compose.yml](file:///D:/python-flask-schwarz/tag_5/demo_projekt/docker-compose.yml): Definiert den Web-Service und das persistente Dateivolume.
*   [templates/index.html](file:///D:/python-flask-schwarz/tag_5/demo_projekt/templates/index.html): HTML-Formular mit `enctype="multipart/form-data"` für Datei-Uploads.
