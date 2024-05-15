
import time



saldo = 0
limite_saque = 3
VALOR_LIMITE_SAQUE = 500
total_sacado = 0
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
    if valor > 0:
        saldo += valor
        extrato += f'Deposito  - R$ {valor:.2f}\n'
        print("Depósito realizado com sucesso")
    else:
        print('Valor inválido, verifique o valor!!!')
        

    return saldo, extrato

def sacar(*, valor, saldo,total_sacado, limite_saque, valor_limite_saque, extrato):
    if limite_saque == 0:
        print("Número de saque excedido!!!")
    elif total_sacado + valor >= valor_limite_saque:
        print('Valor limite de saque diário foi excedido!!!')
    elif valor > saldo :
        print('Saldo insuficiente!!!')
    elif valor > 0 :
        saldo -= valor
        limite_saque -= 1
        total_sacado += valor
        extrato += f'Saque - R$ {valor:.2f}\n'
    else:
        print('Valor inválido, por favor verifique!!!')
    
    return saldo, extrato, total_sacado, limite_saque
                 




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
            valor = float(input("Digite o valor para saque: "))
            saldo, extrato,total_sacado,limite_saque = sacar( valor = valor,
                                   saldo = saldo,total_sacado=total_sacado,
                                   limite_saque= limite_saque,
                                   valor_limite_saque= VALOR_LIMITE_SAQUE, extrato=extrato)
            print(f'Seu saldo é {saldo:.2f}')
        
        if op ==3:
            visualizar_extrato(extrato)
            
    if opcao ==4:
        print('Saindo do sistema...')
        time.sleep(3)
        break