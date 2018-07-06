# -*- coding: utf-8 -*-
"""
EL LIMPIATABLAS

Created on Thu Jun 14 17:44:33 2018

@author: peich
"""

import csv
import pandas as pd


def abredatos(archivo='02_201606.csv'):
    with open(archivo, 'r') as f:
        reader = csv.reader(f)
        res = list(reader)
        
    return res



def abrepanda(res):
    pd.dataframe(res,)
    return b
    
