#!/usr/bin/env python
# coding: utf-8

# Solucion 1

# In[1]:


import time
import numpy as np


# In[2]:


costos = np.genfromtxt('costos.txt')


# In[15]:


inicio = time.time()
objetos_en_wishlist = costos[costos <=25]
inversion_total = np.sum(objetos_en_wishlist)
print('La inversion total sera de: $',inversion_total)
print('Duracion: {} segundos'.format(time.time() - inicio))


# Solucion 2

# In[19]:


with open ('costos.txt') as f:
    objetos_en_wishlist = f.read().split('\n')


# In[24]:


inicio = time.time()
precio_menor_a = []
costos = map(int, objetos_en_wishlist)
for precio in costos:
    if precio <= 25:
        precio_menor_a.append(precio)

inversion_total = np.sum(precio_menor_a)
print('La inversion total sera de: $',inversion_total)
print('Duracion: {} segundos'.format(time.time() - inicio))


# In[ ]:




