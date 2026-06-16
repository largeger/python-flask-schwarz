# 🗄️ Tag 3: Datenbanken mit Flask-SQLAlchemy

## 📖 Theorie-Impuls: Was ist ein ORM?
Ein **Object-Relational Mapper** (ORM) erlaubt es uns, Datenbanktabellen als Python-Klassen zu behandeln.
- **Klasse** = Tabelle
- **Objekt** = Tabellenzeile (Datensatz)
- **Attribut** = Spalte

---

## 🛠️ SQLAlchemy Cheat Sheet (Vollständig)

### 1. Setup & Konfiguration
```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLite: sqlite:///pfad/zur/datei.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)
```

### 2. Ein Modell definieren
Jede Tabelle wird als Klasse definiert, die von `db.Model` erbt.
```python
class User(db.Model):
    # Spalten definieren
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)

    # Hilfreich für Debugging in der Konsole
    def __repr__(self):
        return f'<User {self.username}>'
```

### 3. Spaltentypen & Parameter
Häufig genutzte Typen:
- `db.Integer`, `db.String(size)`, `db.Text`, `db.Float`, `db.Boolean`, `db.DateTime`

Wichtige Parameter:
- `primary_key=True`: Eindeutige ID.
- `unique=True`: Wert darf nur einmal vorkommen.
- `nullable=False`: Feld darf nicht leer sein (Pflichtfeld).
- `default=Value`: Standardwert.

### 4. CRUD Operationen (Die 4 Basics)

#### CREATE (Erstellen)
```python
new_user = User(username='lars', email='lars@dev.de')
db.session.add(new_user)
db.session.commit()
```

#### READ (Lesen/Suchen)
```python
all_users = User.query.all()
first_user = User.query.first()
# Suchen nach ID (liefert 404 Fehler, falls nicht gefunden)
user = User.query.get_or_404(1)
# Filtern
devs = User.query.filter_by(role='admin').all()
```

#### UPDATE (Aktualisieren)
```python
user = User.query.get(1)
user.username = 'neuer_name' # Einfach Attribut ändern
db.session.commit()          # Und commiten
```

#### DELETE (Löschen)
```python
user = User.query.get(1)
db.session.delete(user)
db.session.commit()
```

### 5. Beziehungen (1:n - One-to-Many)
Ein Autor kann viele Bücher schreiben:
```python
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    # backref fügt dem Buch-Objekt .author hinzu
    books = db.relationship('Book', backref='author', lazy=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    # Fremdschlüssel (author.id klein schreiben!)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
```

---

## ⚠️ Troubleshooting & Tipps

### Der App-Kontext
Befehle wie `db.create_all()` müssen innerhalb des Flask-Kontexts laufen:
```python
with app.app_context():
    db.create_all()
```

### Datenbank zurücksetzen
Änderst du das Modell, lösche die `.sqlite` Datei und starte `db.create_all()` neu.

---

## 🎯 Lernziele für heute
- [ ] Flask-SQLAlchemy Basis-Setup beherrschen
- [ ] Modelle mit `db.Model` und `__repr__` erstellen
- [ ] Alle CRUD-Operationen sicher anwenden
- [ ] Beziehungen (ForeignKey) verstehen und nutzen
