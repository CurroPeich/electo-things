# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 17:46:26 2018

@author: peich
"""

import pandas as pd
import csv
import matplotlib.pyplot as mpl

with open('02_201606.csv', 'r') as f:
        reader = csv.reader(f)
        res = list(reader)

del res[0:5]
mat = pd.DataFrame(res[1:], columns=res[0], dtype=int)

pueblo = mat.ix[5063,4]
votossss = mat.ix[5063,13:]
votos = votossss[votossss > 0]

fila = pd.DataFrame(votos,dtype=int,copy=True)
fila.columns = [str(pueblo)]


num_seats = 10
matriz = pd.concat([pd.DataFrame([fila.ix[:,0]/(i+1)]) for i in range(num_seats)], ignore_index=True)

for i in range(num_seats):
    matriz[matriz == matriz.max().max()] = 0
    
matrix = matriz == 0
resu_part = matrix.sum()

#def votos_munic(frame,nfil):
#    votosmun = frame.ix[nfil,13:]
#    return votosmun
