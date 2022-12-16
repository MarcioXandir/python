listas = ['coco',{'nome': 'marcio','idade':44},12,{'num':2222,'frutas':{0:'manga',1:'jaboticaba'}}]
#print(listas)
voga = 'aeiou'
aux = ''

for i in listas[-1]['frutas'][1]:
    if i in voga:
        aux += i
print(f"Vogais encontradas em :{listas[-1]['frutas'][1]} {set(aux)}")
