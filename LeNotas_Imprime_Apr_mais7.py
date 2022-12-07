"""
#Faça um Programa que peça N notas de N alunos,
#calcule e armazene num vetor a média de cada aluno, 
#imprima o somente alunos com média maior ou igual a 7.0 dizendo:  APROVADO
"""
alunos = 0
media = []
todas = []
qtd_alunos = int(input('Serão quantos alunos: '))
numero_notas = int(input('Qual o numero de notas coletadas: '))
#numero_notas = 2

while alunos < qtd_alunos: # OU 3
    print(20*'::')
    nota = [int(input('Nota: ')) for i in range(numero_notas)]
    soma=0.0
    for i in nota:
        soma += float(i)
    media_aluno = soma/numero_notas
    todas.append(nota)
    media.append(media_aluno)
    alunos += 1 
else:
    [print(f'\nNotas do aluno {i+1}\n{todas[i]} média: {media[i]:.2f} - APROVADO\n') for i in range(alunos) if media[i] >= 7]
    
 