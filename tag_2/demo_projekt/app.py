from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    user_name = "Lars"
    return render_template("index.html", name=user_name)

@app.route("/portfolio")
def portfolio():
    my_projects = [
        {"title": "Flask Demo", "year": 2024, "category": "Backend", "desc": "Eine einfache Flask App."},
        {"title": "Weather Tracker", "year": 2023, "category": "API", "desc": "Wetterdaten in Echtzeit."},
        {"title": "Portfolio Page", "year": 2024, "category": "Frontend", "desc": "Mein persönliches Portfolio."}
    ]
    return render_template("portfolio.html", projects=my_projects)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
