# 📝 Tag 4: Formulare & Blueprints

## 📖 Theorie-Impuls: GET vs. POST
- **GET:** Daten werden in der URL übertragen (sichtbar). Gut für Suchen oder Filter.
- **POST:** Daten werden im Request-Body übertragen (unsichtbar). Gut für Passwörter, neue Posts oder Dateiuploads.

---

## 🛠️ Forms & Blueprints Cheat Sheet

### 1. Daten aus Formularen empfangen
```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Logik hier...
        return redirect(url_for('home'))
    return render_template('login.html')
```

### 2. Blueprints (Struktur für große Apps)
In `auth.py`:
```python
from flask import Blueprint
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "Login Seite"
```
In `app.py`:
```python
from auth import auth
app.register_blueprint(auth, url_prefix='/auth')
```

### 3. Flash Messages (Feedback für User)
```python
from flask import flash

flash("Erfolgreich gespeichert!", "success")
```
Im Template:
```html
{% with messages = get_flashed_messages(with_categories=true) %}
  {% for category, message in messages %}
    <div class="alert alert-{{ category }}">{{ message }}</div>
  {% endfor %}
{% endwith %}
```

---

## 🎯 Lernziele für heute
- [ ] Den Unterschied zwischen GET und POST verstehen
- [ ] Daten aus einem HTML-Formular verarbeiten
- [ ] Benutzerfeedback mit Flash-Messages geben
- [ ] Eine App mit Blueprints in Module unterteilen
