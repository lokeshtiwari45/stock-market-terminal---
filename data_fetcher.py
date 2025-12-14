import yfinance as yf

def get_stock_data(symbol, period="6mo", interval="1d"):
    df = yf.download(symbol, period=period, interval=interval)
    df.dropna(inplace=True)
    return df
