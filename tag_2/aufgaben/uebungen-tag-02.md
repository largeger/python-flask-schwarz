# 🏋️ Aufgaben Tag 2: Jinja2 & Styling

## Aufgabe 1: Die erste Vorlage 📄
1. Erstelle einen Ordner `templates` in deinem Projekt.
2. Erstelle darin eine Datei `index.html`.
3. Passe deine Flask-Route `/` so an, dass sie `render_template('index.html')` nutzt.
4. Übergib eine Variable `name` an das Template und zeige sie mit `{{ name }}` an.

---

## Aufgabe 2: Layout & Vererbung 🏗️
1. Erstelle eine `layout.html` mit einem HTML5-Grundgerüst.
2. Nutze `{% block content %}{% endblock %}` im Body.
3. Erstelle `index.html` und `ueber_mich.html`, die beide von `layout.html` erben.
4. Füge eine Navigation (Bootstrap oder einfaches CSS) in das Layout ein, die zwischen beiden Seiten verlinkt.

---

## Aufgabe 3: Dynamische Portfolio-Liste 📂
Erstelle eine Liste von Dictionaries in Python:
```python
projects = [
    {"name": "E-Commerce", "year": 2023, "tech": "Flask"},
    {"name": "Wetter App", "year": 2024, "tech": "JavaScript"},
    {"name": "KI Chatbot", "year": 2024, "tech": "Python"}
]
```
1. Übergib diese Liste an ein Template `projekte.html`.
2. Nutze eine `{% for %}` Schleife, um jedes Projekt in einer schicken Card oder Tabellenzeile anzuzeigen.
3. Nutze ein `{% if %}`, um Projekte aus dem Jahr 2024 fett zu markieren oder mit einem Badge "NEU" zu versehen.

---

## Aufgabe 4: Styling mit CSS 💅 (Groß)
1. Erstelle den Ordner `static/css` und darin `style.css`.
2. Binde die CSS-Datei in deinem `layout.html` mit `url_for` ein.
3. Style dein Portfolio:
   - Eine zentrierte Navbar.
   - Ein ansprechendes Grid-Layout für deine Projekte.
   - Ein schicker Footer.
4. Füge ein Profilbild in `static/img/` hinzu und binde es auf der "Über mich" Seite ein.
