# -*- coding: utf-8 -*-

entrada = 0
soma_idades = 0
q_idades = 0
while True:
  entrada = int(input())
  if entrada >= 0:
    soma_idades += entrada
    q_idades +=1
  else:
    break

print('{:.2f}'.format(soma_idades/q_idades))
