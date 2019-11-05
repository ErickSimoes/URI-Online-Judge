#!/usr/bin/env python
# coding: utf-8

# In[20]:


nums = []
positive = 0
summation = 0

for _ in range(0, 6):
    nums.append(float(input()))
    if nums[-1] > 0:
        summation += nums[-1]
        positive += 1
print("{} valores positivos".format(positive))
print("{:.1f}".format(summation/positive))

