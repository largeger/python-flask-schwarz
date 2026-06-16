from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Datenbank-Konfiguration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'library.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- MODELLE (1:n Beziehung) ---

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # Beziehung: Ein Autor hat viele Bücher
    # 'backref' erlaubt es uns, vom Buch-Objekt via .author auf den Autor zuzugreifen
    books = db.relationship('Book', backref='author', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Author {self.name}>'

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    # Fremdschlüssel: Verweist auf die Author-ID
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

# Datenbank initialisieren
with app.app_context():
    db.create_all()
    # Testdaten, falls leer
    if not Author.query.first():
        a1 = Author(name="J.K. Rowling")
        a2 = Author(name="George R.R. Martin")
        db.session.add_all([a1, a2])
        db.session.commit()
        
        b1 = Book(title="Harry Potter und der Stein der Weisen", author_id=a1.id)
        b2 = Book(title="Harry Potter und die Kammer des Schreckens", author_id=a1.id)
        b3 = Book(title="A Game of Thrones", author_id=a2.id)
        db.session.add_all([b1, b2, b3])
        db.session.commit()

# --- ROUTEN ---

@app.route("/")
def index():
    authors = Author.query.all()
    return render_template("index.html", authors=authors)

@app.route("/author/<int:author_id>")
def author_details(author_id):
    author = Author.query.get_or_404(author_id)
    # Wir können dank 'relationship' einfach auf .books zugreifen
    return render_template("author_details.html", author=author)

# Hilfs-Routen zum Hinzufügen (da wir Forms erst an Tag 4 lernen)
@app.route("/add_author/<name>")
def add_author(name):
    new_author = Author(name=name)
    db.session.add(new_author)
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/add_book/<int:author_id>/<title>")
def add_book(author_id, title):
    new_book = Book(title=title, author_id=author_id)
    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for('author_details', author_id=author_id))

@app.route("/delete_author/<int:id>")
def delete_author(id):
    author = Author.query.get_or_404(id)
    db.session.delete(author)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=5008)
