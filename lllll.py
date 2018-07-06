# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 17:46:26 2018

@author: peich
"""

import pandas as pd
import csv
import matplotlib.pyplot as mpl

import dhondt

with open('02_201606.csv', 'r') as f:
        reader = csv.reader(f)
        res = list(reader)

del res[0:5]
mat = pd.DataFrame(res[1:],columns=res[0],dtype=float,copy=True)

matpob = mat.ix[:,['Población']]
matcen = mat.ix[:,['Total_censo_electoral']]
mat['proporción'] = mat.Total_censo_electoral / mat.Población
prop = mat.ix[:,['proporción']]

mpl.scatter(matpob, prop, color='g')
mpl.xscale('log')
#mpl.xlabel()
mpl.show()

regionA = mat.loc[mat['proporción'] > 1]
regionB = mat.loc[mat['proporción'] <= 0.4]
