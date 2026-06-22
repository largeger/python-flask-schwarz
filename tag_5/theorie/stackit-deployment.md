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

---

## Phase 5: Vollautomatische Aktualisierung via Push-Trigger (mit verschlüsseltem SSH-Key)

In dieser Phase fügen wir der STACKIT Git Action den finalen Schritt hinzu. Sobald Sie Code in den `main`-Branch pushen, verbindet sich der Runner automatisch per passwortgeschütztem SSH-Schlüssel mit Ihrer VM, beendet die alte Version und startet die neu gebaute Flask-Anwendung.

---

### 1. Secrets im Git-Repository ergänzen
Navigieren Sie in Ihrem STACKIT Git-Repository zu **Settings > Secrets** und fügen Sie die folgenden vier Variablen für den Server-Zugriff hinzu:

* `SSH_HOST`: Die öffentliche IP-Adresse Ihrer STACKIT VM.
* `SSH_USER`: Der Benutzername Ihrer VM (Standard bei STACKIT Ubuntu-VMs: `ubuntu`).
* `SSH_PRIVATE_KEY`: Der **vollständige Inhalt** Ihrer ursprünglichen `.pem`-Datei (inklusive der Zeilen `-----BEGIN OPENSSH PRIVATE KEY-----` und `-----END OPENSSH PRIVATE KEY-----`).
* `SSH_PASSPHRASE`: Das Passwort (die Passphrase), mit dem Ihr privater SSH-Schlüssel verschlüsselt ist.

![additional_secrets.png](assets/additional_secrets.png)

---

### 2. Die finale Workflow-Datei anpassen
Ersetzen Sie den Inhalt Ihrer Datei `.forgejo/workflows/build-and-push.yaml` durch den folgenden vollständigen Code. Der Deployment-Schritt nutzt die hinterlegten Secrets und führt die Befehle direkt auf Ihrer VM aus.
Außerdem enthält sie ein paar kleinere Optimierungen (z.B. das Speichern des Pfades zum Container Registry Image in einer Variablen)

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

    # Zentrale Definition des Image-Pfads für das gesamte Skript
    env:
      IMAGE_PATH: ${{ secrets.REGISTRY_URL }}/python-hello/flask-app:latest

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
          tags: ${{ env.IMAGE_PATH }}

      - name: Deployment auf VM ausführen
        uses: appleboy/ssh-action@v1.0.3
        with:
          host: ${{ secrets.SSH_HOST }}
          username: ${{ secrets.SSH_USER }}
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          passphrase: ${{ secrets.SSH_PASSPHRASE }}
          envs: IMAGE_PATH
          script: |
            # 1. Bei STACKIT Registry einloggen
            echo "${{ secrets.REGISTRY_PASSWORD }}" | sudo docker login ${{ secrets.REGISTRY_URL }} --username "${{ secrets.REGISTRY_USER }}" --password-stdin
            
            # 2. Laufenden Container stoppen und entfernen (falls vorhanden)
            sudo docker stop flask-app-container || true
            sudo docker rm flask-app-container || true
            
            # 3. Altes Image löschen, um Speicherplatz zu sparen
            sudo docker rmi $IMAGE_PATH || true 
            
            # 4. Neues Image aus der STACKIT Registry ziehen
            sudo docker pull $IMAGE_PATH
            
            # 5. Container mit festem Namen und Auto-Restart starten
            sudo docker run -d \
              --name flask-app-container \
              --restart always \
              -p 80:5000 \
              $IMAGE_PATH 
```

---

### 🎉 Live-Test nach dem Push
Nehmen Sie eine kleine Änderung in Ihrer `app.py` vor (z. B. den Text zu *"Hello, STACKIT World!"* ändern) und pushen Sie die Änderung in Ihr Repository. 

Verfolgen Sie den Fortschritt unter **Actions** in Ihrem Git-Repository. Sobald die Pipeline grün leuchtet, aktualisiert sich Ihre App unter `http://IHRE_OEFFENTLICHE_VM_IP` ohne manuelles Zutun.

![workflow_run.png](assets/workflow_run.png)