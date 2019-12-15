#!/usr/bin/env python
# coding: utf-8

# In[11]:


d = {
    'vertebrado ave carnivoro ': 'aguia',
    'vertebrado ave onivoro ': 'pomba',
    'vertebrado mamifero onivoro ': 'homem',
    'vertebrado mamifero herbivoro ': 'vaca',
    'invertebrado inseto hematofago ': 'pulga',
    'invertebrado inseto herbivoro ': 'lagarta',
    'invertebrado anelideo hematofago ': 'sanguessuga',
    'invertebrado anelideo onivoro ': 'minhoca'
}

key = ''

for _ in range(3):
    key += input() + ' '
print(d[key])

