import yfinance as yf

# Ação PETR4
acao = yf.Ticker("PETR4.SA")

# Cotação atual (último fechamento disponível)
preco = acao.history(period="1d")["Close"].iloc[-1]

print(f"Cotação atual PETR4: R$ {preco:.2f}")