# 1. Basis Image
FROM python:3.11-slim

# 2. Arbeitsverzeichnis im Container setzen
WORKDIR /code

# 3. System-Abhängigkeiten (optional, falls benötigt)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#    build-essential \
#    && rm -rf /var/lib/apt/lists/*

# 4. Pip Upgrade & Requirements
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 5. Datein kopieren
COPY . .

# 6. Umgebungsvariablen setzen
# ENV PYTHONPATH=/code
# ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1

# 7. Port freigeben
EXPOSE 8000

# 8. Startbefehl
# Wir nutzen die explizite Bindung
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "1", "app:app"]
