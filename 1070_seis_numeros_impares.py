#!/usr/bin/env python
# coding: utf-8

# In[3]:


x = int(input())
i=0

while i < 6:
    if x % 2 != 0:
        print(x)
        i = i + 1
    x = x + 1

