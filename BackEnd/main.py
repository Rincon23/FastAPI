from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#Permissões para sites
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"]
)

vendas = {

    1: {"item": "Lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5}

}

@app.get("/vendas")
def GetVenda():
    return vendas



    

#python -m uvicorn main:app --reload