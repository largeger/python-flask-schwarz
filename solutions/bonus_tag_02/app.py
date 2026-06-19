from flask import Flask, render_template

app = Flask(__name__)

MOVIES = [
    {"id": 1, "title": "Inception", "year": 2010, "genre": "Sci-Fi", "rating": 8.8, "desc": "Ein Dieb, der Geheimnisse aus Träumen stiehlt."},
    {"id": 2, "title": "The Dark Knight", "year": 2008, "genre": "Action", "rating": 9.0, "desc": "Batman kämpft gegen den Joker."},
    {"id": 3, "title": "Interstellar", "year": 2014, "genre": "Sci-Fi", "rating": 8.6, "desc": "Eine Reise durch ein Wurmloch."},
    {"id": 4, "title": "Pulp Fiction", "year": 1994, "genre": "Crime", "rating": 8.9, "desc": "Verwobene Geschichten aus der Unterwelt."},
    {"id": 5, "title": "Fight Club", "year": 1999, "genre": "Drama", "rating": 8.8, "desc": "Ein Büroangestellter gründet einen Fight Club."},
    {"id": 6, "title": "Matrix", "year": 1999, "genre": "Sci-Fi", "rating": 8.7, "desc": "Die Realität ist eine Simulation."},
    {"id": 7, "title": "Gladiator", "year": 2000, "genre": "Action", "rating": 8.5, "desc": "Ein General wird zum Gladiator."},
    {"id": 8, "title": "Se7en", "year": 1995, "genre": "Crime", "rating": 8.6, "desc": "Ein Serienmörder nutzt die sieben Todsünden."},
    {"id": 9, "title": "The Lion King", "year": 1994, "genre": "Animation", "rating": 8.5, "desc": "Ein junger Löwe wird König."},
    {"id": 10, "title": "Parasite", "year": 2019, "genre": "Drama", "rating": 8.6, "desc": "Eine arme Familie infiltriert eine reiche."}
]

@app.route("/")
def index():
    return render_template("index.html", movies=MOVIES)

if __name__ == "__main__":
    app.run(debug=True, port=5006)
