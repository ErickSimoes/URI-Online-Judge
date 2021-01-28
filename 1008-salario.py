# -*- coding: utf-8 -*-

numero = input()
h_trabalho = input()
custo = input()

numero, h_trabalho, custo = int(numero), float(h_trabalho), float(custo)

print("NUMBER = " + str(numero))
print("SALARY = U$ %.2f" % (h_trabalho * custo))
