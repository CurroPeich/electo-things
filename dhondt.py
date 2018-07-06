# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:36:26 2018

@author: peich
"""

import pandas as pd

"""construya la matriz d'Hondt"""
list_of_parties = ['PRD','ARV','PSI','PNR']
list_of_votes = [2015,1786,1540,1223]
resu = pd.DataFrame(list_of_votes)
rest = resu.T
rest.columns = list_of_parties
matriz = pd.concat([pd.DataFrame([rest.ix[0,:]/(i+1)],columns=rest.columns) for i in range(12)], ignore_index=True)

"""calcule los diputados correspondientes"""
for i in range(12):
    matriz[matriz == matriz.max().max()] = 0
    
matrix = matriz == 0
resu_part = matrix.sum()


def apply_dhondt(
        list_of_parties=['PRD','ARV','PSI','PNR'], 
        list_of_votes=[2015,1786,1540,1223], 
        num_of_chairs=12):
    """
    list_of_parties:    ['PRD','ARV','PSI','PNR']
    list_of_votes: [2015,1786,1540,1223]
    num_of_chairs: 12

    output: (DataFrame)
        PRD    4
        ARV    3
        PSI    3
        PNR    2
        dtype: int64
    """
    resu = pd.DataFrame(list_of_votes)
    rest = resu.T
    rest.columns = list_of_parties
    # TODO: Refactor this sheit    
    matriz = pd.concat(
        [pd.DataFrame([rest.ix[0,:]/(i+1)],columns=rest.columns) 
            for i in range(num_of_chairs)],
        ignore_index=True)
    
    for i in range(num_of_chairs):
        matriz[matriz == matriz.max().max()] = 0
    
    matrix = matriz == 0
    res = matrix.sum()
    
    return res
    