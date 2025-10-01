import yfinance as yf

petro = yf.Ticker('PETR4.SA')

print(petro.info['dividendRate'])