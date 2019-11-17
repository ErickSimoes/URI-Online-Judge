#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())

for i in range(1, n+1):
    if i % 2 == 0:
        print('{}^2 = {}'.format(i, i**2))

