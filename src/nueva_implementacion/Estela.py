from __future__ import division
import numpy as np
# coding=utf-8

# es la estela sobre un disco
class Estela(object):
    def __init__(self, arreglo, cantidad_coords_adentro_disco, cantidad_turbinas_izquierda):
        self.arreglo = arreglo
        self.cantidad_coords_adentro_disco = cantidad_coords_adentro_disco
        self.cantidad_turbinas_izquierda = cantidad_turbinas_izquierda
        self.mergeada = None

    """
    Utilizo los tres metodos de superposicion de estelas que utiliza el paper
    'Limitations to the validity of single wake superposition in wind
    farm yield assessment'
    """

    def merge(self, metodo):

        self.mergeada = np.zeros(self.cantidad_coords_adentro_disco)

        if (metodo=='linear'):
            for i in range(self.cantidad_coords_adentro_disco):
                for j in range(self.cantidad_turbinas_izquierda):
                    # print 'self.arreglo[i + self.cantidad_coords_adentro_disco*j] = ',self.arreglo[i + self.cantidad_coords_adentro_disco*j]
                    self.mergeada[i] += self.arreglo[i + self.cantidad_coords_adentro_disco*j]

        elif (metodo=='rss'):

            for i in range(self.cantidad_coords_adentro_disco):
                suma = 0
                for j in range(self.cantidad_turbinas_izquierda):
                    suma += (self.arreglo[i + self.cantidad_coords_adentro_disco*j])**2
                self.mergeada[i] = (suma)**0.5

        elif (metodo=='largest'):

            if self.cantidad_turbinas_izquierda != 0:
                for i in range(self.cantidad_coords_adentro_disco):
                    grupo = np.zeros(self.cantidad_turbinas_izquierda)
                    for j in range(self.cantidad_turbinas_izquierda):
                        grupo[j] = self.arreglo[i + self.cantidad_coords_adentro_disco*j]
                    self.mergeada[i] = np.max(grupo)

#
#
# # test
# cant_coords_adentro_disco =  5
# cant_turbinas_izquierda = 3
# arreglo = np.array([3,3,3,3,3,1,1,1,1,1,2,2,2,2,2])
# estela_1 = Estela(arreglo, cant_coords_adentro_disco, cant_turbinas_izquierda)
# estela_1.merge('linear')
# print estela_1.mergeada
#
# estela_2 = Estela(arreglo, cant_coords_adentro_disco, cant_turbinas_izquierda)
# estela_2.merge('rss')
# print estela_2.mergeada
#
# estela_3 = Estela(arreglo, cant_coords_adentro_disco, cant_turbinas_izquierda)
# estela_3.merge('largest')
# print estela_3.mergeada
