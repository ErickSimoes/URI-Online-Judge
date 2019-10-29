#!/usr/bin/env python
# coding: utf-8

# In[7]:


n = int(input())
hos = ""

for _ in range(0, n):
    hos = hos + "Ho "

hos = hos[:len(hos)-1] + "!"
print(hos)

