from banco import Conta
from utils import Ler_Float
from utils import carregar_dados


dados = carregar_dados()

if dados:
    conta = Conta(dados.get("nome", "Guilherme"), dados.get("saldo", 0))
    conta.historico = dados.get("historico", [])
    conta.saques = dados.get("saques", 0)
else:
    conta = Conta("Guilherme", 2000)


while True:
    print("=======================")
    print("Menu\n\n")
    print("1 - Ver saldo")
    print("2 - Transferir")
    print("3 - Deposito")
    print("4 - Sacar")
    print("5 - Ver historico")
    print("6 - Sair")
    print("=======================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        conta.VerSaldo()
    
    elif opcao == "2":
       valor = Ler_Float("Valor da transferencia: R$")
       if valor is not None:
            conta.Transferir(valor)
            conta.salvar()

    elif opcao == "3":
        valor = Ler_Float("Valor do Deposito: R$")
        if valor is not None:
            conta.Deposito(valor)
            conta.salvar()

    elif opcao == "4":
        valor = Ler_Float("Valor do Saque: R$")
        if valor is not None:
            conta.saque(valor)
            conta.salvar()


    elif opcao == "5":
        conta.VerHistorico()

    elif opcao == "6":
        print("Saindo...")
        break

    else:
        print("Opção invalida")


    
