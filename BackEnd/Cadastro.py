import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS acoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT NOT NULL,
            cota REAL NOT NULL DEFAULT 0,
            quantidade INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def listar_acoes():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, ticker, cota, quantidade FROM acoes")
    rows = cursor.fetchall()
    conn.close()
    return [
        {"id": r[0], "ticker": r[1], "cota": r[2], "quantidade": r[3]}
        for r in rows
    ]

def adicionar_acao(ticker: str, quantidade: int, cota: float = 0):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO acoes (ticker, quantidade, cota) VALUES (?, ?, ?)",
        (ticker, quantidade, cota)
    )
    conn.commit()
    conn.close()
    return {"msg": f"Ação {ticker} adicionada com {quantidade} cotas"}
