#!/usr/bin/env python
# coding: utf-8

# In[8]:


n, g = list(map(int, input().split()))

runas = dict()

for i in range(0, n):
    entry = input().split()
    runas[entry[0]] = int(entry[1])

input()
x = input().split()

total = 0
for runa in x:
    total += runas[runa]

print(total)
if total >= g:
    print('You shall pass!')
else:
    print('My precioooous')

