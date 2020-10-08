#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np
import time

inicio = time.time()
DNNA=np.random.normal(loc=500,scale=30,size=10000000)
SVMQ=0


for valor in DNNA:
    if valor <=500000:
        SVMQ+=valor
        

print('La sumatoria de los numeros menores a 500,000 es:',SVMQ)
print('Duracion: {} segundos'.format(time.time() - inicio))


# In[ ]:




