menu = """ 
##### SEJA BEM VINDO #####
..........................
(S) SAQUE
(E) EXTRATO
(D) DEPOSITO
(N) CADASTRA CLIENTE
(C) CADASTRA C.C.
(T) CONSULTA C.C.
(Q) SAIR 
..........................
##########################
"""

#separar em funcões: sacar, depositar,estrato
saldo = 0

qtd_saques = 3
limite_valor = 500

saques_realizados = [] #extrato
depositos_realizados = []#depositos q foram feitos

cc = []
cadastro_clientes = []

def deposito(saldo, valor, depositos_realizados):
    saldo += valor
    depositos_realizados.append(valor)

    print(f'Valor deposito REALIZADO. Seu saldo atual é: R${saldo:7.2f}')
    input('Pressione ENTER para continuar')
    return saldo, depositos_realizados

def saque(saldo,valor,saques_realizados,limite_valor):
    global qtd_saques#estou colocando essa aqui como global, daí não irei coloca-la como argumento
    if valor > limite_valor or valor > saldo or valor <= 0:
        print(f'Valor Inválido. Saque deve ser Máximo de R$ 500,00 e Mínimo R$ 1,00. Seu saldo atual: R$ {saldo}')
        input('Pressione ENTER para continuar')
    else:
                # armazenar saques em variavel e pode ser exibido em extrato
        qtd_saques -= 1
        saldo -= valor
        saques_realizados.append(valor)
        print('Seu Saque foi liberado!')
        input('Pressione ENTER para prosseguir.')

    return saldo, saques_realizados

def extrato(saldo):
    print('\n\n..........INICIO EXTRATO.........')
    if saldo == 0:
        print('Não houve movimentações em conta.')
    print('\nDEPÓSITOS')

    [print(f' + R${i:10.2f}') for i in depositos_realizados]
    print('SAQUES')
    [print(f' - R${i:10.2f}') for i in saques_realizados]
            
    # no fim o saldo atual formato R$ XXX.XX # print(extrato)
    print(f'\nSeu saldo atual é: {saldo:10.2f}')
    print('...........FIM Extrato...........')

    input('\n\nPressione ENTER para prosseguir.')

def cad_cliente():
    cli_cpf = int(input('Informe o cpf do cliente, somente numeros: '))
    cli_nome = input('Informe o nome cliente: ')
    cli_endereco = input('Informe o endereço do cliente: ')
    cli_dt_nascimento = input('informe a data de nascimento: ')

    return cli_cpf, cli_nome, cli_dt_nascimento, cli_endereco

def cadastro_cc(cadastro_clientes,cc):
    agencia = '0001'
    numero_cc = len(cc)+1
    cpf_correntista = cadastro_clientes[0]
    nome_correntista = cadastro_clientes[1]
    print('conta corrente criada!')

    return numero_cc,agencia,nome_correntista,cpf_correntista

def mostra_cc(cc):
    for i in range(len(cc)):
        print(f'CPF: {cc[i][3]}')
        print(f'CC: {cc[i][0]}')
        print(f'Agência: {cc[i][1]}')
        print(f'Correntista: {cc[i][2]}')





while True:
    print(menu)
    opcao = input("Escolha opção desejada: ").upper()
    if opcao == 'Q':
        print("Obrigado por usar nossos serviços!!")
        break
    
    elif opcao == "N":
        cadastro_clientes = cad_cliente()
        dados_cc = cadastro_cc(cadastro_clientes,cc)
        cc.append(dados_cc)

    elif opcao == "C":
        cadastro_cc(cc=cc,cadastro_clientes=cadastro_clientes)

    elif opcao == 'T':
        mostra_cc(cc)
    
    elif opcao == 'D':
        valor = float(input("Informe o valor de deposito: "))
        # depositos somente positivos,
        if valor < 0:
            print('valor negativo é invalido para depósito.')
            input('PRESSIONE ENTER PRA CONTINUAR')

        else:
            # deverão ser armazenados em variavel
            saldo, depositos_realizados = deposito(saldo, valor, depositos_realizados) #,saldo,depositos_realizados)

    elif opcao == 'E':
        #listar todos depositos e saques realizados na conta.

        extrato(saldo)

    elif opcao == 'S':
        if qtd_saques == 0:
            print("Seu Limite diário de 3 saques foi excedido")
            #input('Pressione ENTER para prosseguir.')
        else:
            # caso não haja saldo, msg de falta de saldo
            valor = float(input('Informe o valor de saque: '))
            saldo, saques_realizados = saque(saldo=saldo,valor=valor,saques_realizados=saques_realizados,limite_valor=limite_valor)


    else:
        print('Opção invalida!')
