import yfinance as yf

petro = yf.Ticker('PETR4.SA')

print(petro.financials)

print(petro.institutional_holders)