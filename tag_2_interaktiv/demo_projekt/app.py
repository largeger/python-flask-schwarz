from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Beispiel-Daten, die wir an Alpine übergeben
    tasks = [
        {"id": 1, "text": "Flask lernen", "done": False},
        {"id": 2, "text": "Alpine.js ausprobieren", "done": True},
        {"id": 3, "text": "Mittagessen kochen", "done": False}
    ]
    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
