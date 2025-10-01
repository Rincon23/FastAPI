import yfinance as yf

dowload = yf.download(["WEGE3.SA", "PETR4.SA", 'VALE3.SA'], start = '2023-01-01', end= '2023-10-01', group_by = 'ticker')

print(dowload)