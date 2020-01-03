# -*- coding: utf-8 -*-

n = int(input())

horas = int(n / 3600)
minutos = int((n - (horas * 3600)) / 60)
segundos = int(n % 60)

print('{}:{}:{}'.format(horas, minutos, segundos))
