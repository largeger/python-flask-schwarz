from flask import Flask, render_template, jsonify
from models import db, Category, Asset
from finance_api import get_current_price
import os
import json
import plotly
import plotly.express as px

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'portfolio.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def init_db():
    with app.app_context():
        db.create_all()
        if not Category.query.first():
            # Initialdaten
            c1 = Category(name="Aktien", color="#4a90e2")
            c2 = Category(name="Krypto", color="#f39c12")
            c3 = Category(name="Rohstoffe", color="#2ecc71")
            db.session.add_all([c1, c2, c3])
            db.session.commit()
            
            # Test-Assets
            a1 = Asset(symbol="AAPL", name="Apple Inc.", amount=10, category_id=c1.id)
            a2 = Asset(symbol="BTC-USD", name="Bitcoin", amount=0.5, category_id=c2.id)
            a3 = Asset(symbol="GC=F", name="Gold", amount=5, category_id=c3.id)
            db.session.add_all([a1, a2, a3])
            db.session.commit()

@app.route("/")
def dashboard():
    assets = Asset.query.all()
    portfolio_data = []
    total_value = 0
    
    # Portfolio berechnen
    for asset in assets:
        price = get_current_price(asset.symbol)
        if price:
            value = round(asset.amount * price, 2)
            total_value += value
            portfolio_data.append({
                "name": asset.name,
                "symbol": asset.symbol,
                "category": asset.category.name,
                "amount": asset.amount,
                "price": price,
                "value": value,
                "color": asset.category.color
            })
    
    # Plotly Pie Chart (Verteilung nach Kategorie)
    fig_pie = px.pie(portfolio_data, values='value', names='category', 
                     title='Diversifikation nach Kategorien',
                     color_discrete_sequence=[d['color'] for d in portfolio_data])
    graph_json = json.dumps(fig_pie, cls=plotly.utils.PlotlyJSONEncoder)
    
    # Plotly Bar Chart (Einzelwerte)
    fig_bar = px.bar(portfolio_data, x='name', y='value', color='category', 
                     title='Gesamtwert pro Asset in €')
    bar_json = json.dumps(fig_bar, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template("dashboard.html", 
                           portfolio=portfolio_data, 
                           total=round(total_value, 2),
                           pie_json=graph_json,
                           bar_json=bar_json)

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5007)
