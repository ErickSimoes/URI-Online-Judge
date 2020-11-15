# -*- coding: utf-8 -*-

array = []

for _ in range(20):
  array.append(input())

array.reverse()
n = 0

for i in array:
  print('N[{}] = {}'.format(n, i))
  n += 1