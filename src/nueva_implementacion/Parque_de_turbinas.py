from __future__ import division
# coding=utf-8

class Parque_de_turbinas(object):

    def __init__(self, turbinas):
        self.turbinas = turbinas

    def ordenar_turbinas_de_izquierda_a_derecha(self):
        turbinas_ordenadas = []
        for turbina in self.turbinas
        self.turbinas.sort(key=lambda turbina:turbina.coord[0])

    def turbinas_a_la_izquierda_de_una_coord(self, una_coord):
        turbinas_a_la_izquierda = []
        for turbina in self.turbinas:
            if (turbina.coord[0] < una_coord[0]):
                turbinas_a_la_izquierda.append(turbina)
        return turbinas_a_la_izquierda


# test:
from Turbina_Marca import Turbina_Marca
import numpy as np

turbina_0 = Turbina_Marca(np.array([0,20,10]))
turbina_1 = Turbina_Marca(np.array([20,20,10]))
turbina_2 = Turbina_Marca(np.array([40,20,10]))
parque_de_turbinas = Parque_de_turbinas([turbina_0, turbina_1, turbina_2])
turbinas_a_la_izquierda = parque_de_turbinas.turbinas_a_la_izquierda_de_una_coord(np.array([20,20,10]))
print 'ok' if turbinas_a_la_izquierda[0] == turbina_0 else 'error'
