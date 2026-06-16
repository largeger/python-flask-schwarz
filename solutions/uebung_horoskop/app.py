from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random
import os

app = Flask(__name__)

# Datenbank-Konfiguration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'horoscopes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'sternenhimmel-123'

db = SQLAlchemy(app)

# --- MODELL ---
class HoroscopeLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    requested_date = db.Column(db.String(20), nullable=False)
    glueck = db.Column(db.Integer, nullable=False)
    karma = db.Column(db.Integer, nullable=False)
    energie = db.Column(db.Integer, nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "requested_date": self.requested_date,
            "glueck": self.glueck,
            "karma": self.karma,
            "energie": self.energie,
            "message": self.message,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

with app.app_context():
    db.create_all()

# --- DATEN ---
MESSAGES = [
    "Heute ist ein guter Tag, um eine neue Programmiersprache zu lernen. Meide jedoch Kaffeeautomaten.",
    "Die Sterne stehen günstig für ein Refactoring. Aber Vorsicht vor 'NullPointer' in deinem Liebesleben.",
    "Ein unerwarteter Pull-Request wird dein Herz erwärmen. Trage heute Blau.",
    "Dein Code wird heute beim ersten Mal kompilieren. Nutze dieses Glück weise!",
    "Ein Bug aus der Vergangenheit wird dich heute heimsuchen. Bleib ruhig und trinke Tee.",
    "Die Planeten raten: Dokumentiere deinen Code, bevor es zu spät ist.",
    "Großartige Gelegenheiten warten in Zeile 42 auf dich."
]

# --- ROUTEN ---

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/archiv")
def archiv():
    # Alle Logs absteigend sortiert laden
    logs = HoroscopeLog.query.order_by(HoroscopeLog.created_at.desc()).all()
    return render_template("archiv.html", logs=logs)

@app.route("/api/horoskop/<datum>")
def get_horoskop(datum):
    # Deterministischer Zufall pro Geburtsdatum und Kalendertag
    today_str = datetime.utcnow().strftime("%Y-%m-%d")
    seed_str = f"{datum}-{today_str}"
    gen = random.Random(seed_str)
    
    # 1. Werte generieren
    glueck = gen.randint(1, 100)
    karma = gen.randint(1, 100)
    energie = gen.randint(1, 100)
    message = gen.choice(MESSAGES)
    
    # 2. In Datenbank speichern (Tag 3 Aufgabe)
    new_log = HoroscopeLog(
        requested_date=datum,
        glueck=glueck,
        karma=karma,
        energie=energie,
        message=message
    )
    db.session.add(new_log)
    db.session.commit()
    
    # 3. Als JSON zurückgeben
    return jsonify(new_log.to_dict())

@app.route("/delete/<int:id>")
def delete_log(id):
    log = HoroscopeLog.query.get_or_404(id)
    db.session.delete(log)
    db.session.commit()
    return redirect(url_for('archiv'))

if __name__ == "__main__":
    app.run(debug=True, port=5009)
