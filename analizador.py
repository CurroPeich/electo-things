# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 14:52:03 2018

@author: peich
"""

import openpyxl
import numpy as np
import matplotlib as mpl

wb = openpyxl.load_workbook('/home/peich/Desktop/datosElecciones/02_201606_1.xlsx')
sheet = wb['Municipios']
poblacion = sheet['F7':'F17']
censo = sheet['H7':'H17']

populatio = [1]
for rowOfCellObjects in poblacion:
    for cellObj in rowOfCellObjects:
        populatio = populatio + [cellObj.value]

census = [0]
for rowOfCellObjects in censo:
    for cellObj in rowOfCellObjects:
        census = census + [cellObj.value]

pop = np.array(populatio[1:])
cen = np.array(census[1:])

prop_ciud = cen/pop
print(prop_ciud)