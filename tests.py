'''import pyautogui as pg
p=pg.position() #mosta posição do mouse
print(p)
'''
import time

class Bicicletas():
    def __init__(self,marca,aro=18) -> None:
        self.marca = marca
        self.aro = aro


    def pedala(self):
  
        for i in 'PEDALANDO':
            print(f'{i} ',end='')
            
           

    def parar(self):
        print('Parando de pedalar.')
        print("Parou!!")

cros = Bicicletas('caloi')

cros.pedala()
time.sleep = 5
cros.parar()
time.sleep = 5
print(cros.marca)