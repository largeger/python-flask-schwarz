from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# 1. Einfache Route (Statisch)
@app.route("/")
def home():
    return "<h1>Willkommen zum Tag 1 Demo Projekt!</h1><p>Gehe zu /api/info für ein JSON Beispiel.</p>"

# 2. Route mit URL-Parametern (Dynamisch)
@app.route("/greet/<name>")
def greet(name):
    return f"Hallo {name.capitalize()}! Dies ist eine dynamische Route."

# 3. Route mit Typprüfung (Integer)
@app.route("/double/<int:number>")
def double(number):
    result = number * 2
    return f"Das Doppelte von {number} ist {result}."

# 4. JSON API Endpunkt
@app.route("/api/info")
def get_info():
    # Flask konvertiert Dictionaries automatisch in JSON
    return {
        "framework": "Flask",
        "tag": 1,
        "themen": ["Routing", "Parameter", "JSON"],
        "status": "online"
    }

# 5. Route mit Query-Parametern (z.B. /search?q=flask)
@app.route("/search")
def search():
    query = request.args.get('q', 'nichts')
    return f"Du hast nach '{query}' gesucht."

if __name__ == "__main__":
    # debug=True erlaubt automatisches Neuladen bei Codeänderungen
    app.run(debug=True, port=5000)
