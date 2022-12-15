menu = """ 
##### SEJA BEM VINDO #####
..........................
(S) SAQUE
(E) EXTRATO
(D) DEPOSITO
(C) CADASTRAR CLIENTE
(G) GERAR C.C.
(M) MOSTRAR C.C.
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

def msg_salta_linha():
    print('\n>>>>>>>>>>>>>>>>>>>>>>>>\nPRESSIONE ENTER PARA CONTINUAR!')
    input()

def deposito(saldo, valor, depositos_realizados):
    saldo += valor
    depositos_realizados.append(valor)

    print(f'Valor deposito REALIZADO. Seu saldo atual é: R${saldo:7.2f}')
    msg_salta_linha()
    return saldo, depositos_realizados

def saque(saldo,valor,saques_realizados,limite_valor):
    global qtd_saques#estou colocando essa aqui como global, daí não irei coloca-la como argumento
    if valor > limite_valor or valor > saldo or valor <= 0:
        print(f'Valor Inválido. Saque deve ser Máximo de R$ 500,00 e Mínimo R$ 1,00. Seu saldo atual: R$ {saldo}')
        msg_salta_linha()
    else:
                # armazenar saques em variavel e pode ser exibido em extrato
        qtd_saques -= 1
        saldo -= valor
        saques_realizados.append(valor)
        print('Seu Saque foi liberado!')
        msg_salta_linha()

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

    msg_salta_linha()

def cadastrar_cliente(cli_cpf):
    cli_nome = input('Informe o nome cliente: ')
    cli_endereco = input('Informe o endereço do cliente: ')
    cli_dt_nascimento = input('informe a data de nascimento: ')        
    return cli_cpf, cli_nome, cli_dt_nascimento, cli_endereco             
            
def gerar_conta_corrente(conta):
    correntista = conta
    agencia = '0001'
    numero_cc = len(cc)+1
    nova_conta = dict(correntista=correntista,agencia=agencia,numero_cc=numero_cc)


    return nova_conta
          
def mostra_cc(cc):
    for i in range(len(cc)):
        
        print(f'CPF: {cc[i]["correntista"]}')
        print(f'Nome: {cadastro_clientes[i][1]}')
        print(f'Data Nascimento: {cadastro_clientes[i][2]}')
        print(f'Endereço: {cadastro_clientes[i][3]}')
        aux = cc[i]['correntista']
        #print(cadastro_clientes)
        #print(type(cadastro_clientes))
        #print(len(cadastro_clientes))
        
        print(20*'.')
        print(f"CC: {cc[i]['agencia']}")
        print(f"Agência: {cc[i]['numero_cc']}")
        #for i2 in range(len(cc)):
        #    if cc[]['correntista'] == aux:
        print(20*'-')
#        msg_salta_linha()

while True:
    print(menu)
    opcao = input("Escolha opção desejada: ").upper()
    if opcao == 'Q':
        print("Obrigado por usar nossos serviços!!")
        break
    
    elif opcao == "C":
        cli_cpf = input('Informe o cpf do cliente, somente numeros: ')

        for i in range(len(cadastro_clientes)):
            #print(f'todo cadastro cliente: {cadastro_clientes}') # 1 indice com 4 registros
            #print(f'cadastro_clientes indice [i]: {cadastro_clientes[i]}')#1 indice com 4 registros
            #print(f'cadastro_clientes indice [i][0]: {cadastro_clientes[i][0]}')# mostra o indice 0 do 1 registro>> : 11
            #input('enter')
            if cli_cpf == cadastro_clientes[i][0]:
                print(f'CPF JÁ CADASTRADO PARA O CLIENTE DE NOME: {cadastro_clientes[i][1]}')
                input()
                break
        else:
            dados = (cadastrar_cliente(cli_cpf))
            cadastro_clientes.append(dados)
    
    elif opcao == 'M':
        mostra_cc(cc)

    elif opcao == 'G':
        cliente_nova_cc = input('Informe CPF cliente para nova CC: ')

        for i in range(len(cadastro_clientes)):
            if cliente_nova_cc == cadastro_clientes[i][0]:
                dadoscc = gerar_conta_corrente(conta=cliente_nova_cc) #entrei com cpf digitado paralá dentro criar o dict e retorna-lo feito
                cc.append(dict(dadoscc))
                print('\nCONTA CRIADA!')
                print(f"\n\nCorrentista: {dadoscc['correntista']} \nAgencia: {dadoscc['agencia']} \nConta Corrente nº:{dadoscc['numero_cc']},")
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

        extrato(saldo)

    elif opcao == 'S':
        if qtd_saques == 0:
            print("Seu Limite diário de 3 saques foi excedido")
            msg_salta_linha()

            #input('Pressione ENTER para prosseguir.')
        else:
            # caso não haja saldo, msg de falta de saldo
            valor = float(input('Informe o valor de saque: '))
            saldo, saques_realizados = saque(saldo=saldo,valor=valor,saques_realizados=saques_realizados,limite_valor=limite_valor)

    else:
        print('Opção invalida!')