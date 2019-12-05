#!/usr/bin/env python
# coding: utf-8

# In[3]:


n = int(input())

hobbits = 0
humanos = 0
elfos = 0
anoes = 0
magos = 0

for _ in range(0, n):
    raca = input().split()[1]
    if raca == 'X':
        hobbits += 1
    elif raca == 'H':
        humanos += 1
    elif raca == 'E':
        elfos += 1
    elif raca == 'A':
        anoes += 1
    elif raca == 'M':
        magos += 1

print(hobbits, 'Hobbit(s)')
print(humanos, 'Humano(s)')
print(elfos, 'Elfo(s)')
print(anoes, 'Anao(s)')
print(magos, 'Mago(s)')

