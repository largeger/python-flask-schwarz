# STACKIT Deployment Guide: Flask-Anwendung im Web bereitstellen

Diese Anleitung beschreibt den vollständigen Prozess, um eine Flask-Anwendung aus einem STACKIT Git-Repository zu bauen und auf einer STACKIT Compute Engine VM im Internet verfügbar zu machen.

---

## 📋 Das Gesamtbild
```text
[ Phase 1: Code ] ──> [ Phase 2: STACKIT Git Action ] ──> [ Phase 3: Registry ] ──> [ Phase 4: STACKIT VM ]
```

---

## Phase 1: Code-Basis vorbereiten
Stellen Sie sicher, dass sich die folgenden drei Dateien im Hauptverzeichnis Ihres STACKIT Git-Repositorys befinden:

### 1. `app.py` (Flask Anwendung)
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    # Wichtig: host='0.0.0.0' macht die App im Container-Netzwerk erreichbar
    app.run(host='0.0.0.0', port=5000)
```

### 2. `requirements.txt` (Abhängigkeiten)
```text
Flask==3.0.3
```

### 3. `Dockerfile` (Bauanleitung)
```dockerfile
FROM python:3.9-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

---

## Phase 2: Automatischer Build (STACKIT Git Actions)

### 1. Secrets im Git-Repository hinterlegen
Navigieren Sie in Ihrem STACKIT Git-Repository zu **Settings > Secrets** und fügen Sie folgende Variablen hinzu:
![img.png](assets/git_secrets.png)
* `REGISTRY_URL`: Die Adresse Ihrer STACKIT Registry (z. B. `registry.onstackit.cloud`).
* `REGISTRY_USER`: Ihre STACKIT-E-Mail-Adresse.
* `REGISTRY_PASSWORD`: Ihr persönliches **CLI-Secret**. (Zu finden im STACKIT Portal der Container Registry oben rechts unter *User Profile -> CLI Secret*).

![User Profile](assets/user_profile_cli_pwd.png)

### 2. Workflow-Datei anlegen
Erstellen Sie in Ihrem Repository die Ordnerstruktur `.forgejo/workflows/` und legen Sie darin die Datei `build-and-push.yaml` an:

```yaml
name: Build and Push Flask App

on:
  push:
    branches:
      - main

jobs:
  build-and-push:
    # Wichtig: Nutzen Sie das für Ihre STACKIT-Umgebung gültige Runner-Label
    runs-on: stackit-ubuntu-22  # Nutzt den STACKIT-Standard-Runner
    # sonst üblicherweise: runs-on: ubuntu-20.04 
    steps:
      - name: Code auschecken
        uses: actions/checkout@v4

      - name: Bei STACKIT Registry anmelden
        uses: docker/login-action@v3
        with:
          registry: ${{ secrets.REGISTRY_URL }}
          username: ${{ secrets.REGISTRY_USER }}
          password: ${{ secrets.REGISTRY_PASSWORD }}

      - name: Docker Image bauen und pushen
        uses: docker/build-push-action@v5
        with:
          context: .
          file: ./Dockerfile
          push: true
          tags: |
            ${{ secrets.REGISTRY_URL }}/ihr-projekt/flask-app:latest
```
`ihr-projekt` ist der Name des in der STACKIT Container Registry verwendeten Projekts.

Sobald Sie diese Datei in den `main`-Branch pushen, baut die STACKIT Git Action Ihr Image automatisch und legt es in der Registry ab.

---

## Phase 3: STACKIT VM & Firewall vorbereiten

### 1. VM & IP einrichten
1. Erstellen Sie eine Ubuntu-VM in der **STACKIT Compute Engine**.
2. Bestellen Sie im STACKIT Portal eine **Public IP** (Öffentliche IP) und weisen Sie diese Ihrer VM zu.

### 2. Security Groups (Firewall) anpassen
Navigieren Sie im Portal zu **Network > Security Groups** der VM und fügen Sie zwei **Ingress-Regeln (Inbound)** hinzu:
* **Regel 1 (SSH):** TCP | Port `22` | Source: `0.0.0.0/0` (oder Ihre eigene Heim-IP)
* **Regel 2 (HTTP):** TCP | Port `80` | Source: `0.0.0.0/0` (für den öffentlichen Web-Zugriff)

---

## Phase 4: Deployment & Start via PuTTY

### 1. Verbindung mit PuTTY aufbauen
1. Wandeln Sie Ihren privaten SSH-Schlüssel (`.pem`) mithilfe von **PuTTYgen** in das `.ppk`-Format um.
2. Öffnen Sie **PuTTY**, hinterlegen Sie die `.ppk`-Datei unter *Connection > SSH > Auth > Credentials* und verbinden Sie sich mit `ubuntu@IHRE_OEFFENTLICHE_VM_IP`.

### 2. Docker auf der VM installieren
Führen Sie im PuTTY-Terminal folgende Befehle aus:
```bash
sudo apt-get update
sudo apt-get install -y docker.io
```

### 3. An der STACKIT Registry anmelden
Melden Sie sich mit Ihren Zugangsdaten an (Nutzen Sie Ihr **CLI-Secret** als Passwort. In PuTTY fügen Sie es mit einem einfachen **Rechtsklick** ein):
```bash
sudo docker login registry.onstackit.cloud
```

### 4. Container im Hintergrund starten
Laden Sie das Image herunter und starten Sie es. Die Port-Weiterleitung `-p 80:5000` sorgt dafür, dass Anfragen aus dem Internet (Port 80) an Flask (Port 5000) weitergeleitet werden.
Die URI setzt sich zusammen aus der STACKIT Registry URL und dem dort gewählten Projektnamen: 

![Registry Project Name](assets/cloud_registry_project_name.png)
```bash
sudo docker run -d -p 80:5000 registry.onstackit.cloud/python-flask/flask-projekt/flask-app:latest
```

---

## 🎉 Live-Test
Öffnen Sie einen Webbrowser auf Ihrem PC und rufen Sie Ihre App auf:
`http://IHRE_OEFFENTLICHE_VM_IP`

Sie sollten nun die Meldung **"Hello, World!"** sehen. Ihre Anwendung ist erfolgreich im Web verfügbar.
