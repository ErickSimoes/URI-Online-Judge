# -*- coding: utf-8 -*-

n, w = map(int, input().split())

for _ in range(n):
  entrada = input()
  last_space = entrada.rfind(' ')
  if int(entrada[last_space:]) >  w:
    print(entrada[:last_space])
