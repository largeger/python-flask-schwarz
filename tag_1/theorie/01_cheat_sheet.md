# 🚀 Tag 1: Flask Grundlagen & Hello World

## 📖 Theorie-Impuls: Was ist ein Backend?
Ein **Backend** ist der Teil einer Webanwendung, der auf dem Server läuft. Es verwaltet Daten, verarbeitet Logik und kommuniziert mit der Datenbank.

### MVC-Architektur (Model-View-Controller)
- **Model:** Datenbank-Logik (Datenstrukturen)
- **View:** Das, was der Benutzer sieht (HTML/JSON)
- **Controller:** Die Logik dazwischen (In Flask: Die Routen/Funktionen)

---

## 🛠️ Flask Basics Cheat Sheet

### 1. Installation
```bash
pip install flask
```

### 2. Minimaler Server (`app.py`)
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
```

### 3. Routing & Parameter
```python
@app.route("/user/<name>")
def greet(name):
    return f"Hallo {name}!"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post ID: {post_id}"
```

### 4. JSON zurückgeben (APIs)
Flask konvertiert Dictionaries automatisch in JSON, wenn man sie zurückgibt (oder mit `jsonify`).
```python
@app.route("/api/data")
def get_data():
    return {
        "status": "success",
        "data": [1, 2, 3]
    }
```

---

## 🎯 Lernziele für heute
- [ ] Flask installieren und einen Server starten
- [ ] Den Unterschied zwischen Frontend und Backend erklären
- [ ] Routen mit Parametern erstellen
- [ ] Eine einfache JSON-API bauen
