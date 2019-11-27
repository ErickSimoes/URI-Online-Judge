#!/usr/bin/env python
# coding: utf-8

# In[1]:


c = int(input())

for _ in range(0, c):
    n = int(input())
    if n > 8000:
        print('Mais de 8000!')
    else:
        print('Inseto!')

