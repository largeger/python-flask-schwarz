from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

# Umgebungsvariablen laden (.env Datei)
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-dev-key')
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB Max Upload

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Sicherstellen, dass der Upload-Ordner existiert
os.makedirs(os.path.join(app.root_path, app.config['UPLOAD_FOLDER']), exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# In-Memory "Datenbank" für Demo
images = []

@app.route("/")
def index():
    return render_template("index.html", images=images)

@app.route("/upload", methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash("Keine Datei ausgewählt", "danger")
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash("Keine Datei ausgewählt", "danger")
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # In einem echten Projekt würden wir den Pfad in der DB speichern
        file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
        images.append(filename)
        flash("Bild erfolgreich hochgeladen!", "success")
        return redirect(url_for('index'))
    else:
        flash("Ungültiger Dateityp (Nur Bilder erlaubt)", "danger")
        return redirect(request.url)

if __name__ == "__main__":
    # Für die lokale Entwicklung
    app.run(debug=True, port=5005)
