#!/usr/bin/env python
# coding: utf-8

# In[8]:


c = int(input())

def printImpares(x, y):
    total = 0
    i = 0
    n = x
    while i < y:
        if n%2 != 0:
            total += n
            i += 1
        n += 1
    print(total)

for _ in range(c):
    x, y = list(map(int, input().split()))
    
    printImpares(x, y)

