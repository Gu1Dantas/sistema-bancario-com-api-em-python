import json

def Ler_Float(mensagem):
    try:
        return float(input(mensagem))
    except ValueError:
        print("Digite um valor valido")
        return None
    
def carregar_dados():
    try:
        with open("historico.json", "r")as f:
            return json.load(f)
    except FileNotFoundError:
        return None