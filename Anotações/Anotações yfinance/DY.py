import yfinance as yf
import pandas as pd

# Ticker da PETR4
acao = yf.Ticker("PETR4.SA")

# Último preço
preco = acao.history(period="1d")["Close"].iloc[-1]

# Histórico de dividendos
dividendos = acao.dividends

# Dividendos pagos nos últimos 12 meses
ultimos_12m = dividendos[dividendos.index > (dividendos.index[-1] - pd.DateOffset(years=1))].sum()

# Calcula o DY
dy = (ultimos_12m / preco) * 100

print(f"Preço PETR4: R$ {preco:.2f}")
print(f"Dividendos últimos 12 meses: R$ {ultimos_12m:.2f}")
print(f"Dividend Yield PETR4: {dy:.2f}%")
