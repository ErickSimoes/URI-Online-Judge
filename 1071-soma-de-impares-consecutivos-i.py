#!/usr/bin/env python
# coding: utf-8

# In[19]:


n = int(input())
m = int(input())

total = 0
if n > m:
    n, m = m, n

for i in range(n+1, m):
    if i%2 != 0:
        total += i
print(total)

