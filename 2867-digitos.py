#!/usr/bin/env python
# coding: utf-8

# In[4]:


c = int(input())

for _ in range(0, c):
    n = list(map(int, input().split()))
    m = n[0]**n[1]
    print(len(str(m)))

