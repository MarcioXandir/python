vitoria = f'''
  \o/  
   |   |** Winner ** |
 _/ \_ 
'''
perdeu = f'''
    o  
   |\   |** Lose ** |
   |_
'''

numpa = 0
secreta = [(" __ ") for i in range(20) ]
mask = " __ "
certo = 0
acertos = 0
chances = 5
repete = ""

palavra = input("Informe a palavra: ").upper()
numpa = len(palavra)

while chances > 0 and acertos < numpa:
  print(15*"::")
  for i in range(numpa):
    
    print(secreta[i], end="")
 
  
  letra = input("\nInforme uma letra: ").upper()
  print(f'\n{15*"::"}')

  if letra in repete:
    print(f">>> A letra '({letra.upper()})' ja foi informada. Tente outra")
    chances -= 1 
    print(f"SUAS CHANCES RESTANTES: {chances} DE 5 ")
    print(f"Letras já informadas: >>>>> {repete.upper()} <<<<\n")
    print(20*'.')
    continue
  
  for i, item in enumerate(palavra):
    if letra == item:
      acertos += 1
      certo += 1
      secreta[i] = letra.upper()
     
    else:
      erro = 1
      if letra not in repete:
        repete += letra
          
  if certo == 0:
    chances -= 1
  
  certo = 0

if chances == 0:
  print("\nUma pena, vc perdeu")
  print(perdeu)

if acertos == numpa:
  print(f"\n\nParabén, vc Venceu. A palavra era {palavra.upper()}\n")
  print(vitoria)