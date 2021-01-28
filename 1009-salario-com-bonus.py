# -*- coding: utf-8 -*-

nome = input()
salario = input()
vendas = input()

salario, vendas = float(salario), float(vendas)

print("TOTAL = R$ %.2f" % float(salario + (vendas*0.15)))
