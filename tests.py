saldo = 1000
qtd_saques = 3
limite_valor = 500
saques_realizados = [] #extrato

import pyautogui as pg
#depositos_realizados = []#depositos q foram feitos
#cc = []
#clientes = []'''
'''
def saque(saldo,valor,saques_realizados,qtd_saques,limite_valor):
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

valor = float(input('Informe o valor de saque: '))
saldo, saques_realizados = saque(saldo=saldo,valor=valor,saques_realizados=saques_realizados,qtd_saques=qtd_saques,limite_valor=limite_valor)

'''
p=pg.position() #mosta posição do mouse
print(p)