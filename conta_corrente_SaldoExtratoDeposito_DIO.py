menu = """ 
##### SEJA BEM VINDO #####
..........................
(S) SAQUE
(E) EXTRATO
(D) DEPOSITO
(Q) SAIR 
..........................
##########################
"""
saldo = 0
saques_realizados = []
depositos_realizados = []
qtd_Saques = 3

while True:
    print(menu)
    opcao = input("Escolha opção desejada: ").upper()
    if opcao == 'Q':
        print("Obrigado por usar nossos serviços!!")
        break

    elif opcao == 'D':
        deposito = float(input("Informe o valor de deposito: "))
        # depositos somente positivos,
        if deposito < 0:
            print('valor negativo é invalido para depósito.')
            input('PRESSIONE ENTER PRA CONTINUAR')
        else:
            # deverão ser armazenados em variavel
            depositos_realizados.append(deposito)
            saldo += deposito
            print(f'Valor deposito REALIZADO. Seu saldo atual é: R${saldo:7.2f}')
            input('Pressione ENTER para continuar')

    elif opcao == 'E':
        #listar todos depositos e saques realizados na conta.
        print('\n\n..........INICIO EXTRATO.........')
        if saldo == 0:
            print('Não houve movimentações em conta.')
        print('\nDEPÓSITOS')
        for i in depositos_realizados:
            print(f' + R${i:10.2f}')
        print('SAQUES')
        for i in saques_realizados:
            print(f' - R${i:10.2f}')

        # no fim o saldo atual formato R$ XXX.XX # print(extrato)
        print(f'\nSeu saldo atual é: {saldo:10.2f}')
        print('...........FIM Extrato...........')

        input('\n\nPressione ENTER para prosseguir.')

    elif opcao == 'S':
        #limite de 3 saques diarios e 500 por saque
        if qtd_Saques == 0:
            print("Seu Limite diário de 3 saques foi excedido")
            input('Pressione ENTER para prosseguir.')
        else:
            # caso não haja saldo, msg de falta de saldo
            valor_saque_unitario = float(input('Valor para saque: '))
            if valor_saque_unitario > 500 or valor_saque_unitario > saldo or valor_saque_unitario <= 0:
                print(f'Valor Inválido. Saque deve ser Máximo de R$ 500,00 e Mínimo R$ 1,00. Seu saldo atual: R$ {saldo}')
                input('Pressione ENTER para continuar')

            else:
                # armazenar saques em variavel e pode ser exibido em extrato
                qtd_Saques -= 1
                saldo -= valor_saque_unitario
                saques_realizados.append(valor_saque_unitario)
                print('Seu Saque foi liberado!')
                input('Pressione ENTER para prosseguir.')
    else:
        print('Opção invalida!')
