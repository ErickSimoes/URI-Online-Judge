# coding: utf-8

n = int(input())

cedulas = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0]

def cResto(cedula, n):
    qC = 0
    if n / cedula >= 1:
        qC = n//cedula
        n -= qC*cedula
    return qC, n

print(n)

for x in cedulas:
    q, n = cResto(x, n)
    print('{:.0f} nota(s) de R$ {:.0f},00'.format(q, x))
