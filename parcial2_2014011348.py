#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import time

#En esta seccion se establece la variable de tiempo y la funcion que generara los numeros aleatorios y su distribucion normal
inicio = time.time()
DNNA=np.random.normal(loc=500,scale=30,size=10000000) 

#En esta seccion inicia la iteracion de datos mediante la estructura de control for
SVMQ=0
for valor in DNNA:
    if valor <=500000:
        SVMQ+=valor
        
print('La sumatoria de los numeros menores a 500,000 es:',SVMQ)
print('Duracion: {} segundos'.format(time.time() - inicio))


# In[2]:


import numpy as np
import time

#En esta seccion se establece la variable de tiempo y la funcion que generara los numeros aleatorios y su distribucion normal
inicio = time.time()
DNNA=np.random.normal(loc=500,scale=30,size=10000000)

#En esta seccion inicia la iteracion de datos mediante 
SVMQ=DNNA[DNNA<=500000]
SVMQ=np.sum(SVMQ)

print('La sumatoria de los numeros menores a 500,000 es:',SVMQ)
print('Duracion: {} segundos'.format(time.time() - inicio))


# DNNA=Distrbucion normal de numeros aleatorios SVQM=Sumatoria de valores menores a quinientos mil
