listas = ['coco',{'nome': 'marcio','idade':44},12,{'num':2222,'frutas':{0:'manga',1:'jaboticaba'}}]
#print(listas)
#print(listas[3]['frutas'][0])
#print(listas[::-1])
print(listas)

print(f"{listas[-1]['frutas'][1]} ",end='') # jaboticaba
print(listas[-1]['frutas'][0])#manga

voga = 'aeiou'
aux = ''

for i in listas[-1]['frutas'][1]:
    if i in voga:
        aux += i
print(f"Vogais encontradas em :{listas[-1]['frutas'][1]} {set(aux)}")



