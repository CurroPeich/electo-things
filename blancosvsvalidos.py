# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 20:08:58 2018

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
columnax = [list(i) for i in zip(*res2016)][9]
columnay = [list(i) for i in zip(*res2016)][11]

"""Borra las sobras que no son números"""
del(columnax[0:6])
del(columnay[0:6])

"""Convierte los str en float"""
validos = [float(i) for i in columnax]
blancos = [float(i) for i in columnay]

"""Pasa a numPy.array"""
valar = np.array(validos)
blaar = np.array(blancos)

"""Define las magnitudes derivadas"""
prop_bla = blaar/valar

mpl.scatter(valar,prop_bla)
mpl.xlabel('Votos válidos')
mpl.xscale('log')
mpl.ylabel('Proporción de votos blancos')
mpl.show()