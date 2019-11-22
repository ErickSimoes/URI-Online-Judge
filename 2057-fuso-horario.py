#!/usr/bin/env python
# coding: utf-8

# In[12]:


entrada = list(map(int, input().split()))

hora_local = sum(entrada)

if hora_local > 23:
    hora_local -= 24
elif hora_local < 0:
    hora_local += 24

print(hora_local)

