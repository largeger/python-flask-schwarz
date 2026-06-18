# 1. Basis-Image (Schlankes Python)
FROM python:3.11-slim

# 2. Arbeitsverzeichnis setzen
WORKDIR /app

# 3. Abhängigkeiten kopieren & installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Gesamten Code kopieren (Ausschluss via .dockerignore)
COPY . .

# 5. Upload-Ordner sicherstellen
RUN mkdir -p static/uploads

# 6. Port für Gunicorn
EXPOSE 8000

# 7. Startbefehl: Gunicorn mit 1 Worker (für Demo-Persistenz im Speicher falls nötig)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "1", "app:app"]
