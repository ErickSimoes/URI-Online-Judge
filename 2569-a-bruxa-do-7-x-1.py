# -*- coding: utf-8 -*-

entrada = input().replace('7', '0').split()
a, o, b = int(entrada[0]), entrada[1], int(entrada[2])
calc = 0

if o == '+':
  calc = a + b
else:
  calc = a * b

calc = int(str(calc).replace('7', '0'))

print(calc)
