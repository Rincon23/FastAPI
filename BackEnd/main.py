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

acoes = {
    "CMIG4": {"Cota": 19},
    "BBSE3": {"Cota": 19},
    "TAEE11": {"Cota": 0},
    "BBAS3": {"Cota": 0},
    "DIRR3": {"Cota": 0},
    "ITSA4": {"Cota": 0},
    "BBDC4": {"Cota": 0},
    "CPLE6": {"Cota": 0},
    "PETR4": {"Cota": 0},
    "POMO4": {"Cota": 0},
    "CURY3": {"Cota": 0},
    "BRAP4": {"Cota": 0},
    "VALE3": {"Cota": 0},
    "CMIN3": {"Cota": 0},
    "MBRF": {"Cota": 0},
    "CXSE3": {"Cota": 0},
    "PSSA3": {"Cota": 0},
    "EQTL3": {"Cota": 0},
    "ABEV3": {"Cota": 0},
    "CPFE3": {"Cota": 0},
    "ITSA3": {"Cota": 0},
    "RADL3": {"Cota": 0},
    "B3SA3": {"Cota": 0},
    "WEGE3": {"Cota": 0},
    "EGIE3": {"Cota": 0},
    "AUVP11": {"Cota": 0}
}



@app.get("/acoes")
def Get_acoes():
    return acoes



    

#python -m uvicorn main:app --reload