import pyautogui as pg
import time
'''

t = pyautogui.KEYBOARD_KEYS
print(t)

p=pg.position() #mosta posição do mouse
print(p)
'''
nome_usuario = ''

def acesso_navegador(nome):
    global nome_usuario
    pg.PAUSE = 1
    pg.press('win')#pressiona tecla 'win'
    pg.write('google')#escreve 'google'
    pg.press('enter')#pressiona tecla
    time.sleep(4)
    pg.hotkey('win','up')#maximiza tela
    pg.moveTo(x=60, y=20) #>>> usuario marcio ou 

    usuario(nome)

    #pg.moveTo(x=773, y=332) >>> usuario marcio ou 
    #pg.click()
    #pg.hotkey('ctrl','n')#maximiza tela
    pg.write('https://contagem.ginfes.com.br/')#escreve 'google'
    pg.press('enter')#pressiona tecla
    time.sleep(3)
    pg.hotkey('win','up')#maximiza tela
    pg.press('enter')
    #pg.alert('Há algum aviso? ')


def usuario(nome):
    if nome == "A":
        pg.press('tab')
        pg.press('enter')

    elif nome == 'M':
        pg.press('tab')
        pg.press('tab')
        pg.press('tab')
        pg.press('tab')
        pg.press('tab')
        pg.press('tab')
        pg.press('tab')
        pg.press('tab')
        pg.press('tab')
        pg.press('tab')
        pg.press('enter')

    else:
        print('Usuario Invalido.')

def usuario_e_senha():
    pg.PAUSE = 0.5
    pg.moveTo(x=198, y=237)#betim(x=82, y=199)
    pg.click()
    pg.press('tab');pg.press('tab')
    pg.write('40525906000144');pg.press('tab')
    pg.write('27202720')
    pg.press('tab');pg.press('enter');pg.press('tab');pg.press('enter')
    pg.press('tab');pg.press('tab');pg.press('tab');pg.press('tab');pg.press('tab');
    pg.write('40525906000144');pg.press('tab');pg.press('enter')

def menu():
    m = f'''
    :::::::: Escolha o usuario:::::::
    
    (A) Ana Luiza
    (M) Marcio

    ================================= 
    '''
    print(m)
    opcao = input("Informe o Usuario: ").upper()

    return opcao

while True:
    nome_usuario = menu()
    acesso_navegador(nome_usuario)
    usuario_e_senha()

    break
else:
    print('Até logo!!!')
