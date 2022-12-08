numpa = 0
secreta = [" __ "," __ "," __ "," __ "," __ "," __ "," __ "," __ "," __ "," __ "," __ "," __ "," __ "," __ "," __ "," __ "," __ "," __ "," __ "," __ ",]
mask = " __ "
certo = 0
acertos = 0
chances = 5
repete = ""

import os
palavra = str(input("Informe a palavra: "))

palavra = palavra.upper()
for i,item in enumerate(palavra):
  numpa += 1

os.system('clear')

while chances > 0 and acertos < numpa:
  for i in range(numpa):
    print(secreta[i], end="")

  print()
  print()

  print("CHANCES FALTANTES: ", chances)
  
  print('Letras informadas: ', repete.upper(),' ')
  print()
#  pause = input()
  letra = input("Informe a letra: ")
  letra = letra.upper()
  if letra in repete:
    print("A letra", ' { ',letra.upper(),' }', " ja foi informada. ")
    input("PRESSIONE <Enter> ")
    chances -= 1
    os.system('clear')
    continue
  
  for i, item in enumerate(palavra):
    if letra == item:
      acertos += 1
      certo += 1
      secreta[i] = letra.upper()
    #  if letra in repete:
     #   continue
      #else:
       # repete += letra
      
    else:
      erro = 1
      if letra not in repete:
        repete += letra
       
  
  if certo == 0:
    chances -= 1
  
  certo = 0
  os.system('clear')

if chances == 0:
  print("Uma pena, vc perdeu")

if acertos == numpa:
  print("Parabén, vc Venceu. A palavra é ")
  print('{ ',palavra.upper(),' }')
  print()
  print()
  for i in range(numpa):
    print('  \o/  ')
    print('   |   ')
    print(' _/ \_ ')
    print()