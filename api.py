from fastapi import FastAPI
from banco import Conta
from utils import carregar_dados

app = FastAPI()

dados = carregar_dados()

if dados:
    conta = Conta(dados.get("nome", "Guilherme"), dados.get("saldo", 0))
    conta.historico = dados.get("historico", [])
    conta.saques = dados.get("saques", 0)
else:
    conta = Conta("Guilherme",2000)

@app.get("/")
def home():
    return {"mensagem": "API do banco rodando"}

@app.get("/saldo")
def ver_saldo():
    return{"saldo": conta.saldo}

@app.post("/transferir")
def transferencia(valor : float):
    if valor < 0:
        return{"error": "Valor invalido"}
    
    if valor > conta.saldo:
        return{"error": "Saldo insuficiente"}
    
    conta.Transferir(valor)
    conta.salvar()
    return{"mensagem": "Transferencia realizada", "saldo": conta.saldo}

@app.post("/deposito")
def depositar(valor : float):
    if valor < 0:
        return{"error": "Valor invalido"}

    conta.Deposito(valor)
    conta.salvar()
    return{"mensagem": "Deposito realizado", "saldo": conta.saldo}

@app.post("/saque")
def sacar(valor : float):
    if valor < 0:
        return{"error": "Valor invalido"}
    
    if valor > conta.saldo:
        return{"error": "Saldo insuficiente"}
    
    conta.saque(valor)
    conta.salvar()
    return{"mensagem": "Saque realizado", "saldo": conta.saldo}

@app.get("/historico")
def historico():
    return{"historico" : conta.historico}