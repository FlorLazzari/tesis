from __future__ import division
# coding=utf-8

import numpy as np

# es la estela sobre un disco
class Estela(object):
    def __init__(self, arreglo, cantidad_coords_adentro_disco, cantidad_turbinas_izquierda):
        self.arreglo = arreglo
        self.cantidad_coords_adentro_disco = cantidad_coords_adentro_disco
        self.cantidad_turbinas_izquierda = cantidad_turbinas_izquierda
        self.mergeada = None

    def merge(self):
        self.mergeada = np.zeros(self.cantidad_coords_adentro_disco)
        # print self.cantidad_coords_adentro_disco
        # print self.cantidad_turbinas_izquierda

        for i in range(self.cantidad_coords_adentro_disco):
            for j in range(self.cantidad_turbinas_izquierda):
                self.mergeada[i] += self.arreglo[i + self.cantidad_coords_adentro_disco*j]
