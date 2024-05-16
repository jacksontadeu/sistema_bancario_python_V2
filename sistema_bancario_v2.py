
import time

AGENCIA ="0001"

saldo = 0
limite_saque = 3
VALOR_LIMITE_SAQUE = 500
total_sacado = 0
extrato = ""
usuarios = []
contas =[]
numero_conta = 0


def menu():
    print("***********Sistema Bancário*************")
    print('''
          (1) Cadastrar Cliente
          (2) Cadastrar Conta
          (3) Listar Contas
          (4) Operações da Conta
          (0) Sair do sistema
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
    

def cadastrar_usuarios(usuarios):
    cpf = input('Digite o CPF: ')
    usuario = verificar_cpf(cpf, usuarios)
    if usuario:
        print("Usuário já cadastrado!!!")
        return
    elif len(cpf) == 11:
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input('Digite a data de nascimento (dd/mm/aaaa): ')
        endereco = input('Digite o endereco(logradouro,numero,bairro,cidade/estado): ')
        usuarios.append({"nome": nome,"cpf":cpf,"data_nascimento":data_nascimento,"endereco": endereco})
    else:
        print('CPF inválido!!!')
        return
        
    print('Usuário cadastrado com sucesso!!!')


def verificar_cpf(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None


def criar_conta(agencia,numero_conta, usuarios):
    cpf = input("Digite o CPF: ")
    usuario = verificar_cpf(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        conta =  {"agencia":agencia, "numero_conta": numero_conta, "usuario":usuario}
        return conta

    print("Usuário não encontrado!!!")


def listar_contas(contas):
    
    for conta in contas:
        linha = f"""\
              Agência: {conta['agencia']}
              Conta..: {conta['numero_conta']}
              Cliente: {conta['usuario']['nome']}
        """
        print(linha)
        print('*******************************************')
        




while True:
    menu()
    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        cadastrar_usuarios(usuarios)

    elif opcao == 2:
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA,numero_conta, usuarios)
        if conta:
            contas.append(conta)
            

    elif opcao == 3:
        listar_contas(contas)


    elif opcao == 4:
        operacoes()
        op = int(input('Digite a operação: '))

        if op == 1:
            valor = float(input('Digite o valor do depósito: '))
            saldo, extrato = depositar(valor,saldo, extrato)
            print(f'Seu saldo é {saldo:.2f}')

        elif op == 2:
            valor = float(input("Digite o valor para saque: "))
            saldo, extrato,total_sacado,limite_saque = sacar( valor = valor,
                                   saldo = saldo,total_sacado=total_sacado,
                                   limite_saque= limite_saque,
                                   valor_limite_saque= VALOR_LIMITE_SAQUE, extrato=extrato)
            print(f'Seu saldo é {saldo:.2f}')
        
        elif op ==3:
            visualizar_extrato(extrato)
            
    elif opcao ==0:
        print('Saindo do sistema...')
        time.sleep(3)
        break