import json

class Conta:
    LIMITE_SAQUE = 4
    VALOR_LIMITE = 500
    
    def salvar(self):
        dados = {
            "nome": self.nome,
            "saques": self.saques,
            "saldo": self.saldo,
            "historico": self.historico
        }

        with open("historico.json", "w")as f:
            json.dump(dados, f, indent=4)



    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo
        self.historico = []
        self.saques = 0

    def VerSaldo(self):
        print(f'Seu saldo atual é de: R${self.saldo:.2f}')

    def Transferir(self, valor):
        if valor > self.saldo:
            print("Saldo insuficinte")
            return
        
        self.saldo -= valor
        self.historico.append(f'-Transferencia: R${valor:.2f}')
        print("Transferencia realizada")
        print(f"Seu saldo atual é de: R${self.saldo:.2f}")

    def Deposito(self, valor):
        if valor <= 0:
            print("Deposito deve ser maior que R$0.00")
            return
        
        self.saldo += valor
        self.historico.append(f'+Deposito: R${valor:.2f}')
        print("Deposito realizado")
        print(f"Seu saldo atual é de: R${self.saldo:.2f}")

    def saque(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
            return
        
        self.saldo -= valor
        self.historico.append(f'-Saque: R${valor:.2f}')
        print("Saque realizado")
        print(f"Seu saldo atual é de: R${self.saldo:.2f}")

    def VerHistorico(self):
        if not self.historico:
            print("Nenhuma movimentação")
        else:
            print("Historico")
            for item in self.historico:
                print(item)