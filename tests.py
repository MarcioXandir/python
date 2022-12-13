def deposito(valor, saldo,extrato):
    saldo += valor
    extrato = valor
    return saldo, extrato



v = 1000
s = 0
ext = 0

saldo, extrato = deposito(v,s,ext)

print(saldo, extrato)
