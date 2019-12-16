# coding: utf-8

pedido, quant = input().split(" ")
pedido, quant = int(pedido), float(quant)
valor = 0

if pedido == 1:
    valor = 4.0
elif pedido == 2:
    valor = 4.5
elif pedido == 3:
    valor = 5.0
elif pedido == 4:
    valor = 2.0
elif pedido == 5:
    valor = 1.5

print('Total: R$ {:.2f}'.format(valor * quant))
