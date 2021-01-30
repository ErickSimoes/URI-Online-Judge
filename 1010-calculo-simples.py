# -*- coding: utf-8 -*-

c1, n1, v1 = input().split(" ")
c2, n2, v2 = input().split(" ")

n1, v1, n2, v2 = float(n1), float(v1), float(n2), float(v2)

p1 = n1 * v1
p2 = n2 * v2

print("VALOR A PAGAR: R$ %.2f" % float(p1 + p2))
