# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 17:51:14 2018

@author: peich
"""

def votos_efectivos(partido):
    return float(partido.votos) / float(partido.escaños + 1)


class partido(object):
    def __init__(self, n, v, e):
        self.nombre = n
        self.votos = v
        self.escaños = e

    def votos_efectivos(self):
        return float(self.votos) / float(self.escaños + 1)
 
    def asigna_escaño(self):
        self.escaños += 1


class elecciones(object):
    def __init__(self, lista_de_partidos, lista_de_votos, escanos_en_disputa):
        self.partidos = []
        self.escanos_en_disputa = escanos_en_disputa
        for nombre, voto in zip(lista_de_partidos, lista_de_votos):
            self.partidos.append(partido(nombre,voto,0))

    def reparte_escaños(self):   
        while(self.escanos_en_disputa):
            self.partidos = sorted(self.partidos, key = lambda partido: votos_efectivos(partido), reverse=True)
            partido_ganador = self.partidos[0]           
            partido_ganador.asigna_escaño()
            self.partidos[0] = partido_ganador
            self.escanos_en_disputa -= 1

    def resultado(self):
        self.reparte_escaños()
        for partido in sorted(self.partidos, key = lambda partido: -1 * partido.escaños):
            print("{escaños} para el {partido}".format(
                partido=partido.nombre, escaños=str(partido.escaños)
            ))
