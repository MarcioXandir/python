menu = """ 
=========== MENU ===========
    (S) SAQUE
    (E) EXTRATO
    (D) DEPOSITO
    (C) CADASTRAR CLIENTE
    (G) GERAR C.C.
    (M) MOSTRAR C.C.
    (Q) SAIR
............................
============================
"""

saldo = 0
qtd_saques = 3
limite_valor = 500
saques_realizados = [] 
depositos_realizados = []
cc = []
cadastro_clientes = []

def msg_salta_linha():
    input('PRESSIONE ENTER PARA CONTINUAR!')

def deposito(saldo, valor, depositos_realizados):
    saldo += valor
    depositos_realizados.append(valor)
    print(f'Valor deposito REALIZADO. Seu saldo atual é: R${saldo:7.2f}')
    msg_salta_linha()
    return saldo, depositos_realizados

def saque(*,saldo,valor,qtd_saques,saques_realizados,limite_valor):
    if valor > limite_valor or valor > saldo or valor <= 0:
        print(f'Valor Inválido. Saque deve ser Máximo de R$ 500,00 e Mínimo R$ 1,00. Seu saldo atual: R$ {saldo}')
        msg_salta_linha()
    else:
        qtd_saques -= 1
        saldo -= valor
        saques_realizados.append(valor)
        print('Seu Saque foi liberado!')
        msg_salta_linha()
    return saldo, saques_realizados,qtd_saques

def extrato(saldo,/,depositos_realizados,saques_realizados):
    print('\n\n..........INICIO EXTRATO.........')
    if saldo == 0:
        print('Não houve movimentações em conta.')
    print('\nDEPÓSITOS')
    [print(f'\t+ R${i:.2f}') for i in depositos_realizados]
    print('SAQUES')
    [print(f'\t- R${i:.2f}') for i in saques_realizados]        
    # no fim o saldo atual formato R$ XXX.XX # print(extrato)
    print(f'\nSeu saldo atual é:\t{saldo:.2f}')
    print('...........FIM Extrato...........')
    msg_salta_linha()

def cadastrar_cliente(cli_cpf):
    cli_nome = input('Informe o nome COMPLETO do cliente: ')
    cli_endereco = input('Informe o endereço (ex.: said mansur, 17 - Ingá - Betim/MG): ')
    cli_dt_nascimento = input('Data de nascimento (dd/mm/aaaa): ')        
    return {'cpf':cli_cpf,'nome':cli_nome,'data nascimento':cli_dt_nascimento,'endereco':cli_endereco}
            
def gerar_conta_corrente(conta):
    correntista = conta
    agencia = '0001'
    numero_cc = len(cc)+1
    nova_conta = dict(cpf=correntista,agencia=agencia,numero_cc=numero_cc)
    return nova_conta
          
def filtra_cc(item,cc):
    for i in cc:
        if i['cpf'] == item['cpf']:
            print(f'Agência: {i["agencia"]} \nC/C.: {i["numero_cc"]}')
        
def mostra_cc(cc):
    for i, item in enumerate(cadastro_clientes):
        print(f"{(12*'=')} CORRENTISTA {(12*'=')}")
        print(f'CPF: {cadastro_clientes[i]["cpf"]}')
        print(f"Nome: {cadastro_clientes[i]['nome']}")
        print(f"Data Nascimento: {cadastro_clientes[i]['data nascimento']}")
        print(f'Endereço: {cadastro_clientes[i]["endereco"]}\n')
        print(f"Conta(s) {(20*'.')}")
        filtra_cc(item=item,cc=cc)
        print(30*'.')
        print(f"{(40*'=')}\n\n")


while True:
    print(menu)
    opcao = input("Escolha opção desejada: ").upper()
    if opcao == 'Q':
        print("Obrigado por usar nossos serviços!!")
        break
    
    elif opcao == "C":
        cli_cpf = input('Informe o cpf do cliente, somente numeros: ')
        for i in range(len(cadastro_clientes)):
            if cli_cpf == cadastro_clientes[i]['cpf']:
                print(f"\nCPF JÁ CADASTRADO PARA O CLIENTE DE NOME: {cadastro_clientes[i]['nome']}")
                input('Pressione Enter para continuar!')
                break
        else:
            dados = (cadastrar_cliente(cli_cpf))
            cadastro_clientes.append(dados)
    
    elif opcao == 'M':
        mostra_cc(cc)

    elif opcao == 'G':
        cliente_nova_cc = input('Informe CPF cliente para nova CC: ')
        for i in range(len(cadastro_clientes)):
            if cliente_nova_cc == cadastro_clientes[i]['cpf']:
                dadoscc = gerar_conta_corrente(conta=cliente_nova_cc) #entrei com cpf digitado paralá dentro criar o dict e retorna-lo feito
                cc.append(dict(dadoscc))
                print('\nCONTA CRIADA!')
                print(f"\nCorrentista: {dadoscc['cpf']} \nAgencia: {dadoscc['agencia']} \nConta Corrente nº:{dadoscc['numero_cc']}\n")
                msg_salta_linha()
                break
        else:
            print('cliente precisa ser cadastrado primeiro.')
                  
    elif opcao == 'D':
        valor = float(input("Informe o valor de deposito: "))
        # depositos somente positivos,
        if valor < 0:
            print('valor negativo é invalido para depósito.')
            msg_salta_linha()

        else:
            # deverão ser armazenados em variavel
            saldo, depositos_realizados = deposito(saldo, valor, depositos_realizados) #,saldo,depositos_realizados)

    elif opcao == 'E':
        #listar todos depositos e saques realizados na conta.
        extrato(saldo,depositos_realizados=depositos_realizados,saques_realizados=saques_realizados)

    elif opcao == 'S':
        if qtd_saques == 0:
            print("Seu Limite diário de 3 saques foi excedido")
            msg_salta_linha()
            #input('Pressione ENTER para prosseguir.')
        else:
            # caso não haja saldo, msg de falta de saldo
            valor = float(input('Informe o valor de saque: '))
            saldo, saques_realizados,qtd_saques = saque(saldo=saldo,valor=valor,qtd_saques=qtd_saques,saques_realizados=saques_realizados,limite_valor=limite_valor)
    else:
        print('Opção invalida!')