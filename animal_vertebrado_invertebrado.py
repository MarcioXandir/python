a = input()
b = input()
c = input()

if a == 'vertebrado':
    if b == 'ave':
        if c == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if c == 'onivoro':
            print('homem')
        else:
            print('vaca')

    ''' 
    TODO Crie as condições necessárias para definir o tipo de animal possível seguindo
    o esquema da imagem.
    TODO Imprima, de acordo com as condições, o animal identificado.
    '''
elif a == 'invertebrado':
    if b == 'inseto':
        if c == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if c == 'hematofago':
            print('sanguesuga')
        else:
            print('minhoca')
