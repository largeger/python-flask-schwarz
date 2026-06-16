# 🎨 Tag 2: Jinja2 Templating & Static Files

## 📖 Theorie-Impuls: Warum Templates?
Anstatt HTML als lange Strings in Python-Funktionen zu schreiben, nutzen wir **Jinja2 Templates**. Das trennt Logik (Python) von Design (HTML).

### Template Vererbung
Wir erstellen ein `layout.html` mit dem Grundgerüst (Navbar, Footer) und "befüllen" es in anderen Dateien.

---

## 🛠️ Jinja2 Cheat Sheet

### 1. Variablen ausgeben
```html
<h1>Hallo {{ name }}!</h1>
```

### 2. Kontrollstrukturen
```html
{% if user.is_logged_in %}
  <p>Willkommen zurück!</p>
{% else %}
  <p>Bitte logge dich ein.</p>
{% endif %}

<ul>
{% for item in items %}
  <li>{{ item }}</li>
{% endfor %}
</ul>
```

### 3. Template Vererbung
`layout.html`:
```html
<html>
<body>
  {% block content %}{% endblock %}
</body>
</html>
```

`index.html`:
```html
{% extends "layout.html" %}
{% block content %}
  <h1>Startseite</h1>
{% endblock %}
```

### 4. Statische Dateien (CSS, Bilder)
Ordnerstruktur:
```
/static
  /css
    style.css
/templates
  index.html
```
Einbinden in HTML:
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

---

## 🎯 Lernziele für heute
- [ ] Den `templates/` Ordner nutzen
- [ ] Variablen an HTML übergeben
- [ ] Schleifen und Bedingungen in Jinja2 anwenden
- [ ] `url_for` für statische Dateien nutzen
