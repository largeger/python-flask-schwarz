from flask import Blueprint, render_template, request, redirect, url_for, flash

blog_bp = Blueprint('blog', __name__)

# Simulierter Datenspeicher
posts = [
    {"id": 1, "title": "Erster Beitrag", "content": "Willkommen in unserem Blog!"},
    {"id": 2, "title": "Flask Tipps", "content": "Nutze Blueprints für bessere Struktur."}
]

@blog_bp.route("/")
def list_posts():
    return render_template("blog.html", posts=posts)

@blog_bp.route("/neu", methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        # Daten aus dem Formular holen
        title = request.form.get('title')
        content = request.form.get('content')

        # Einfache Validierung
        if not title or not content:
            flash("Bitte alle Felder ausfüllen!", "danger")
        else:
            # Neuen Post hinzufügen
            new_id = len(posts) + 1
            posts.append({"id": new_id, "title": title, "content": content})
            flash("Beitrag erfolgreich erstellt!", "success")
            return redirect(url_for('blog.list_posts'))

    return render_template("create_post.html")
