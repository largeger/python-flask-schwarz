from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
from models import db, TravelEntry
import os

# Blueprint Definition (Modularisierung aus Tag 4)
journal_bp = Blueprint('journal', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@journal_bp.route('/')
def index():
    # READ: Alle Einträge absteigend sortiert laden (Tag 3)
    entries = TravelEntry.query.order_by(TravelEntry.created_at.desc()).all()
    return render_template('index.html', entries=entries)

@journal_bp.route('/add', methods=['POST'])
def add_entry():
    # CREATE: Formularverarbeitung (Tag 4)
    title = request.form.get('title')
    destination = request.form.get('destination')
    body = request.form.get('body')
    file = request.files.get('image')

    # Einfache Validierung
    if not title or not destination:
        flash("Titel und Ziel sind Pflichtfelder!", "danger")
        return redirect(url_for('journal.index'))

    filename = None
    # FILE UPLOAD: Handling von Bildern (Tag 5)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    # In DB speichern
    new_entry = TravelEntry(
        title=title,
        destination=destination,
        body=body,
        image_file=filename
    )
    db.session.add(new_entry)
    db.session.commit()

    flash("Reise erfolgreich hinzugefügt! ✈️", "success")
    return redirect(url_for('journal.index'))

@journal_bp.route('/delete/<int:id>', methods=['POST'])
def delete_entry(id):
    # DELETE: Eintrag entfernen
    entry = TravelEntry.query.get_or_404(id)

    # Optional: Bild auch vom Filesystem löschen
    if entry.image_file:
        img_path = os.path.join(current_app.config['UPLOAD_FOLDER'], entry.image_file)
        if os.path.exists(img_path):
            os.remove(img_path)

    db.session.delete(entry)
    db.session.commit()

    flash("Eintrag gelöscht.", "info")
    return redirect(url_for('journal.index'))
