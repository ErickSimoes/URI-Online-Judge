#!/usr/bin/env python
# coding: utf-8

# In[6]:


comidas = list(map(int, input().split()))
pedidos = list(map(int, input().split()))

insatisfeitos = 0

for i in range(0, 3):
    if pedidos[i] > comidas[i]:
        insatisfeitos = insatisfeitos + (pedidos[i]-comidas[i])

print(insatisfeitos)

