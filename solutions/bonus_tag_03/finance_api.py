import yfinance as yf

def get_current_price(symbol):
    try:
        ticker = yf.Ticker(symbol)
        # Manchmal ist 'currentPrice' nicht verfügbar, dann nutzen wir 'regularMarketPrice' oder die History
        info = ticker.info
        price = info.get('currentPrice') or info.get('regularMarketPreviousClose')
        
        if price is None:
            # Fallback: Letzten Schlusskurs aus der History holen
            hist = ticker.history(period="1d")
            if not hist.empty:
                price = hist['Close'].iloc[-1]
        
        return round(float(price), 2) if price else None
    except Exception as e:
        print(f"Fehler beim Abruf von {symbol}: {e}")
        return None
