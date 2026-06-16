from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# 1. Datenbank-Konfiguration
# Wir nutzen SQLite und speichern die Datei im aktuellen Verzeichnis
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'members.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 2. Modell-Definition
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Member {self.name}>'

# 3. Datenbank initialisieren (beim ersten Start)
with app.app_context():
    db.create_all()
    # Falls die DB leer ist, Testdaten hinzufügen
    if not Member.query.first():
        m1 = Member(name="Alice", role="Developer")
        m2 = Member(name="Bob", role="Designer")
        db.session.add_all([m1, m2])
        db.session.commit()

# --- ROUTEN ---

# READ: Alle Mitglieder anzeigen
@app.route("/")
def index():
    members = Member.query.all()
    return render_template("index.html", members=members)

# CREATE: Ein neues Mitglied hinzufügen (via GET Parameter für Demo-Zwecke)
@app.route("/add/<name>/<role>")
def add_member(name, role):
    new_member = Member(name=name, role=role)
    db.session.add(new_member)
    db.session.commit()
    return redirect(url_for('index'))

# UPDATE: Status umschalten
@app.route("/toggle/<int:id>")
def toggle_status(id):
    member = Member.query.get_or_404(id)
    member.is_active = not member.is_active
    db.session.commit()
    return redirect(url_for('index'))

# DELETE: Mitglied löschen
@app.route("/delete/<int:id>")
def delete_member(id):
    member = Member.query.get_or_404(id)
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=5003)
