import yfinance as yf

petro = yf.Ticker('PETR4.SA')

print(petro.ticker)

print(petro.actions)

print(petro.dividends)


#Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 4h, 1d, 5d, 1wk, 1mo, 3mo]
print(petro.history(start = '2025-08-01', end = '2025-10-01', interval = '1d'))

print(petro.history(period = 'max', interval = '1wk'))