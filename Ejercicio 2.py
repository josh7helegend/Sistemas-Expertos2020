#!/usr/bin/env python
# coding: utf-8

# Optimizacion de Codigo, Ejemplo 1: Identificacion de Ventas en un periodo
# Generar metricas de desempeño es una tarea muy frecuente en cualquier ambito de negocio, el siguiente codigo fue escrito para identificar qué libros fueron vendidos a partir de un listado especifico:

# In[25]:


import time
import pandas as pd
import numpy as np


# In[5]:


with open('libros_24_meses.txt') as f:
    periodo24_ventas_libros = f.read().split('\n')
    
with open('catalogo_libros.txt') as f:
    catalogo_libros = f.read().split('\n')


# In[6]:


inicio = time.time()
libros_vendidos = []

for libro in periodo24_ventas_libros:
    if libro in catalogo_libros:
        libros_vendidos.append(libro)

print(len(libros_vendidos))
print('Duracion: {} segundos'.format(time.time() - inicio))


# Propuesta de optimizacion 1: utilizar operaciones con vectores en lugar de estructuras de control repetitivas cuando esto sea posible; para este escenario se propone evaluar el uso del metodo intersect1d de la libreria numpy para que nos permita obtener la interseccion de ambos dataset:

# In[7]:


inicio = time.time()
libros_vendidos = np.intersect1d(periodo24_ventas_libros, catalogo_libros)
print(len(libros_vendidos))
print('Duracion: {} segundos'.format(time.time() - inicio))


# Propuesta de optimizacion 2: Para esta solucion se opto por convertir los archivos .txt a sets de datos y luego se procedio a utilizar el metodo intersection de python.

# In[35]:


with open('libros_24_meses.txt') as f:
    periodo24_ventas_libros = set([line.rstrip('\n') for line in f])
    
with open('catalogo_libros.txt') as f:
    catalogo_libros = set([line.rstrip('\n') for line in f])


# In[36]:


inicio = time.time()
libros_vendidos = periodo24_ventas_libros.intersection(catalogo_libros)
print(len(libros_vendidos))
print('Duracion: {} segundos'.format(time.time() - inicio))


# In[ ]:




