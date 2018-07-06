# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:15:28 2018

@author: peich
"""

import numpy as np
import matplotlib.pyplot as mpl
import csv
from matplotlib import colors

def abredatos(archivo='02_201606.csv'):
    with open(archivo, 'r') as f:
        reader = csv.reader(f)
        res = list(reader)
    return res

def abredatos1(archivo='02_201606.csv'):
    res = []    
    with open(archivo, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            res.append(list(row))
    return resa

def columna(ncol,archivo='02_201606.csv'):
    with open(archivo, 'r') as f:
        reader = csv.reader(f)
        res = list(reader)    
    col = [list(i) for i in zip(*res)][ncol]
    del(col[0:6])
    colflo = [float(i) for i in col]
    arraycol = np.array(colflo)
    return arraycol

def sacafila(nfil):
    fila = res[nfil]
    del(fila[0:7])
    filflo = [float(i) for i in fila]
    nombrefila = np.array(filflo)
    return nombrefila
    
def graf1(x,y,archivo='02_201606.csv'):
    with open(archivo, 'r') as f:
        reader = csv.reader(f)
        res = list(reader)
    columnax = [list(i) for i in zip(*res)][x]
    del(columnax[0:6])
    xflo = [float(i) for i in columnax]
    xar = np.array(xflo)
    columnay = [list(i) for i in zip(*res)][y]
    del(columnay[0:6])
    yflo = [float(i) for i in columnay]
    yar = np.array(yflo)
    mpl.scatter(xar,yar)
    mpl.xlabel(res[5][x])
    mpl.ylabel(res[5][y])    
    mpl.xscale('log')
    mpl.yscale('log')
    mpl.yticks([0.1,1,10,100,1000,10000,100000])
    mpl.show()


def graf2(x,y1,y2,archivo='02_201606.csv'):
    with open(archivo, 'r') as f:
        reader = csv.reader(f)
        res = list(reader)
    columnax = [list(i) for i in zip(*res)][x]
    del(columnax[0:6])
    xflo = [float(i) for i in columnax]
    xar = np.array(xflo)
    columnay1 = [list(i) for i in zip(*res)][y1]
    del(columnay1[0:6])
    y1flo = [float(i) for i in columnay1]
    y1ar = np.array(y1flo)
    columnay2 = [list(i) for i in zip(*res)][y2]
    del(columnay2[0:6])
    y2flo = [float(i) for i in columnay2]
    y2ar = np.array(y2flo)
    mpl.scatter(xar,y1ar,c=(0,1,0))
    mpl.scatter(xar,y2ar,c=(1,0,0))
    mpl.xlabel(res[5][x])
    mpl.ylabel(res[5][y1]+' (verde) y '+res[5][y2]+' (rojo)')    
    mpl.xscale('log')
    mpl.yscale('log')
    mpl.yticks([0.1,1,10,100,1000,10000,100000])
    mpl.show()


def semilog(x,y):
    mpl.scatter(x,y)
    mpl.xscale('log')
    mpl.show()

def loglog(x,y):
    mpl.scatter(x,y)
    mpl.xscale('log')
    mpl.yscale('log')
    mpl.show()
    