import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def generate_sales_data(n_rows=5000):
    # Datumsbereich
    dates = pd.date_range(end=pd.Timestamp.now(), periods=n_rows, freq='H')
    
    # Kategorien mit Wahrscheinlichkeiten
    categories = ['Elektronik', 'Bekleidung', 'Wohnen', 'Sport', 'Bücher']
    probs = [0.35, 0.25, 0.2, 0.1, 0.1]
    
    data = {
        'Bestelldatum': np.random.choice(dates, n_rows),
        'Produktkategorie': np.random.choice(categories, n_rows, p=probs),
        'Menge': np.random.randint(1, 6, n_rows),
        'Einzelpreis': np.random.normal(50, 30, n_rows),
        'Kundensegment': np.random.choice(['Neukunde', 'Bestandskunde', 'VIP'], n_rows)
    }
    
    df = pd.DataFrame(data)
    
    # Ausreißer und NaNs
    df.loc[df.sample(frac=0.02).index, 'Menge'] = 50
    df.loc[df.sample(frac=0.02).index, 'Einzelpreis'] = np.nan
    
    # Preise absichern
    df['Einzelpreis'] = df['Einzelpreis'].clip(lower=5)
    
    return df

def clean_and_prepare_data(df):
    # NaNs füllen
    df['Einzelpreis'] = df.groupby('Produktkategorie')['Einzelpreis'].transform(lambda x: x.fillna(x.median()))
    
    # Extremwerte begrenzen
    df.loc[df['Menge'] > 20, 'Menge'] = 20
    
    # Feature Engineering
    df['Gesamtumsatz'] = df['Menge'] * df['Einzelpreis']
    df['Monat'] = df['Bestelldatum'].dt.to_period('M').astype(str)
    
    return df

def get_kpis(df):
    if df.empty:
        return {"umsatz": 0, "bestellungen": 0, "aov": 0, "top_kat": "N/A"}
    
    return {
        "umsatz": round(df['Gesamtumsatz'].sum(), 2),
        "bestellungen": len(df),
        "aov": round(df['Gesamtumsatz'].mean(), 2),
        "top_kat": df.groupby('Produktkategorie')['Gesamtumsatz'].sum().idxmax()
    }

def generate_plots(df):
    if df.empty:
        return "", ""

    # 1. Trend-Linie
    plt.figure(figsize=(10, 4))
    trend = df.groupby('Monat')['Gesamtumsatz'].sum()
    trend.plot(kind='line', marker='o', color='#4a90e2')
    plt.title("Monatlicher Umsatztrend")
    plt.grid(True, alpha=0.3)
    
    # Bonus: Regression
    try:
        x = np.arange(len(trend))
        y = trend.values
        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)
        plt.plot(x, p(x), "r--", alpha=0.8, label="Trend")
    except:
        pass
        
    trend_plot = fig_to_base64(plt)

    # 2. Kategorie-Verteilung
    plt.figure(figsize=(6, 6))
    df.groupby('Produktkategorie')['Gesamtumsatz'].sum().plot(kind='pie', autopct='%1.1f%%', colors=['#50e3c2', '#ffce54', '#4a90e2', '#e74c3c', '#9b59b6'])
    plt.title("Umsatz nach Kategorie")
    plt.ylabel("")
    
    dist_plot = fig_to_base64(plt)
    
    return trend_plot, dist_plot

def fig_to_base64(plt_obj):
    img = io.BytesIO()
    plt_obj.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt_obj.close()
    return plot_url
