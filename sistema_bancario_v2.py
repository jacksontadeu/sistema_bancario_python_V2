
import time


valor = 0
saldo = 0
LIMITE_SAQUE = 3
VALOR_LIMITE_SAQUE = 500
extrato = ""

def menu():
    print("***********Sistema Bancário*************")
    print('''
          (1) Cadastrar Cliente
          (2) Cadastrar Conta
          (3) Operações da Conta
          (4) Sair do sistema
          ''')
    

def operacoes():
    print('''
          (1) Depositar
          (2) Sacar
          (3) Extrato da Conta
          ''')
    
def depositar(valor, saldo, extrato, /):
    if valor <= 0:
        print('Valor inválido, verifique o valor!!!')
    else:
        saldo += valor
        extrato += f'Deposito  - R$ {valor:.2f}\n'
        print("Depósito realizado com sucesso")

    return saldo, extrato

def sacar()

def visualizar_extrato(extrato):
    print("******************EXTRATO*************")
    print(extrato)
    print(f"Saldo atual R$ {saldo:.2f}")
    print("***************************************")








while True:
    menu()
    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        print('opcao 1')

    if opcao == 2:
        print('opcao 2')

    if opcao == 3:
        operacoes()
        op = int(input('Digite a operação: '))

        if op == 1:
            valor = float(input('Digite o valor do depósito: '))
            saldo, extrato = depositar(valor,saldo, extrato)
            print(f'Seu saldo é {saldo:.2f}')
        if op == 2:
            print('Saque')
        
        if op ==3:
            visualizar_extrato(extrato)
            
    if opcao ==4:
        print('Saindo do sistema...')
        time.sleep(3)
        break