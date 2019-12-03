#!/usr/bin/env python
# coding: utf-8

# In[15]:


e, d = list(map(int, input().split()))

if e >= d:
    print('Eu odeio a professora!')
else:
    if d - e >= 3:
        print('Muito bem! Apresenta antes do Natal!')
    else:
        print('Parece o trabalho do meu filho!')
        
        if (e + 2) < 24:
            print('TCC Apresentado!')
        else:
            print('Fail! Entao eh nataaaaal!')

