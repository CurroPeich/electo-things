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

def dhondt(resu=res, nmunic=5063, num_seats=10):
    mat = pd.DataFrame(res[1:], columns=res[0], dtype=int)

    pueblo = mat.ix[5061:5064,4]
    votossss = mat.ix[5061:5064,13:]
    votos = votossss[votossss > 0]

    fila = pd.DataFrame(votos,dtype=int,copy=True)
    fila.columns = [str(pueblo)]

    matriz = pd.concat([pd.DataFrame([fila.ix[:,0]/(i+1)]) for i in range(num_seats)], ignore_index=True)

    for i in range(num_seats):
        matriz[matriz == matriz.max().max()] = 0
    
    matrix = matriz == 0
    resu_part = matrix.sum()
    return resu_part

def municipio(resu=res, nmunic=5063, comicio=['junio de 2016']):
    mun = pd.DataFrame(res[nmunic:nmunic+1],index=comicio,columns=res[0],
                       dtype=int,copy=True)
    return mun
    