#!/usr/bin/env python
# coding: utf-8

# In[9]:


tomadas = input().split()
n_tomadas = int(tomadas[0])

for i in range(1, 4):
    n_tomadas += int(tomadas[i]) - 1

print(n_tomadas)

