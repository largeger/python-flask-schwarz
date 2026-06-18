from flask import Flask
import os
from models import db

def create_app():
    """App Factory Pattern (Best Practice für Flask 3.x)"""
    app = Flask(__name__)
    
    # --- KONFIGURATION (via Environment Variables) ---
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key')
    # Datenbank-URL von Docker-Compose übernehmen (mit Fallback auf SQLite für lokale Entwicklung)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///travel_journal.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/uploads')

    # --- INITIALISIERUNG ---
    db.init_app(app)
    
    # Sicherstellen, dass Upload-Ordner existiert
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # --- BLUEPRINTS REGISTRIEREN ---
    from blueprints.journal import journal_bp
    app.register_blueprint(journal_bp)

    # Datenbank-Tabellen beim Start erstellen (falls nicht vorhanden)
    with app.app_context():
        db.create_all()

    return app

# Gunicorn sucht standardmäßig nach 'app'
app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=8000)
