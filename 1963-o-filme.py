#!/usr/bin/env python
# coding: utf-8

# In[9]:


a, b = list(map(float, input().split()))

print('{:.2f}%'.format(((b*100)/a)-100))

