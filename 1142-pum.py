#!/usr/bin/env python
# coding: utf-8

# In[13]:


n = int(input())

a = 0
for _ in range(n):
    a, b, c = a+1, a+2, a+3
    print('{} {} {} PUM'.format(a, b, c))
    a = c+1

