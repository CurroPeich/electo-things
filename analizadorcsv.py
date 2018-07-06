# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 15:44:12 2018

@author: peich
"""

import numpy as np
import matplotlib.pyplot as mpl
import csv

with open('02_201606.csv', 'r') as f:
    reader = csv.reader(f)
    res2016 = list(reader)



#fila = res2016[5]
#columna = [list(i) for i in zip(*a)][64]
#c = res2016[2][:]
#print(fila)
#print(columna)

"""Selecciona las filas y/o columnas de interés"""
columna5 = [list(i) for i in zip(*res2016)][5]
columna7 = [list(i) for i in zip(*res2016)][7]

"""Borra las sobras que no son números"""
del(columna5[0:6])
del(columna7[0:6])

"""Convierte los str en float"""
pob = [float(i) for i in columna5]
cen = [float(i) for i in columna7]

"""Pasa a numPy.array"""
pobar = np.array(pob)
cenar = np.array(cen)

"""Define las magnitudes derivadas"""
prop_ciud = cenar/pobar

mpl.scatter(pobar,prop_ciud)
mpl.xlabel('Población')
mpl.xscale('log')
mpl.ylabel('Censo/Población')
mpl.show()