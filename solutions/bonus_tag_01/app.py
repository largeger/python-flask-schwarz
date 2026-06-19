from flask import Flask, render_template, request
from data_analytics import generate_sales_data, clean_and_prepare_data, get_kpis, generate_plots

app = Flask(__name__)

# Daten einmalig beim Start generieren
raw_data = generate_sales_data()
df_master = clean_and_prepare_data(raw_data)

@app.route("/", methods=['GET', 'POST'])
def dashboard():
    category_filter = request.args.get('category', 'Alle')
    segment_filter = request.args.get('segment', 'Alle')
    
    # Filtern
    df_filtered = df_master.copy()
    if category_filter != 'Alle':
        df_filtered = df_filtered[df_filtered['Produktkategorie'] == category_filter]
    if segment_filter != 'Alle':
        df_filtered = df_filtered[df_filtered['Kundensegment'] == segment_filter]
        
    # Analyse
    kpis = get_kpis(df_filtered)
    trend_plot, dist_plot = generate_plots(df_filtered)
    
    # Optionen für Dropdowns
    categories = ['Alle'] + sorted(df_master['Produktkategorie'].unique().tolist())
    segments = ['Alle'] + sorted(df_master['Kundensegment'].unique().tolist())
    
    return render_template("dashboard.html", 
                           kpis=kpis, 
                           trend_plot=trend_plot, 
                           dist_plot=dist_plot,
                           categories=categories,
                           segments=segments,
                           selected_cat=category_filter,
                           selected_seg=segment_filter)

if __name__ == "__main__":
    app.run(debug=True, port=5005)
