from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# DB Instanz initialisieren
db = SQLAlchemy()

class TravelEntry(db.Model):
    """Datenmodell für ein Reisetagebuch-Eintrag (Postgres-kompatibel)"""
    __tablename__ = 'travel_entries'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(100), nullable=True) # Speichert nur den Dateinamen
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<TravelEntry {self.title}>"
