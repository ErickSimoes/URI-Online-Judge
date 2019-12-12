#!/usr/bin/env python
# coding: utf-8

# In[11]:


n = int(input())

lista = [0, 1]
fibo = 0

while len(lista) < n:
    fibo = lista[-1] + lista[-2]
    lista.append(fibo)

print(str(lista).replace('[', '').replace(',', '').replace(']', ''))

