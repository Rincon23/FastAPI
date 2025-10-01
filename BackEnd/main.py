from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Cadastro import init_db, listar_acoes, adicionar_acao

app = FastAPI()

# Permissões CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"]
)

# Inicia o Banco de dados
init_db()

# Rota para listar ações
@app.get("/acoes")
def get_acoes():
    return listar_acoes()

# Rota para adicionar uma ação
@app.post("/acoes/add/{ticker}/{quantidade}")
def add_acao(ticker: str, quantidade: int):
    return adicionar_acao(ticker, quantidade)
