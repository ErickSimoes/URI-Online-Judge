#!/usr/bin/env python
# coding: utf-8

# In[7]:


n = int(input())

for _ in range(0, n):
    x = int(input())
    if x == 0:
        print('NULL')
    else:
        if x % 2 == 0:
            resultado = 'EVEN'
        else:
            resultado = 'ODD'
    
        if x > 0:
            result = resultado + ' POSITIVE'
        else:
            result = resultado + ' NEGATIVE'
        print(result)

