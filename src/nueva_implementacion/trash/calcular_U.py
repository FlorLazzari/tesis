from __future__ import division
# coding=utf-8

from Modelo_2 import Modelo
import numpy as np
from numpy import exp
from Case_2 import Case
from integrar_disco_monte_carlo import integrar_disco_monte_carlo


# posicion_turbinas = {0: np.array([x_0, y_0, z_0])}     np.array?? que me conviene?
# debo numerarlas de izquierda a derecha sino todo el script no tiene sentido
# mi_posicion = np.array([x_0, y_0, z_0])

def calcular_U(modelo, posicion_turbinas, coord_selec):

    for i in range(mi_posicion):
        if (coord_turbina[i][0] < coord_selec[0]):      # si hay turbinas a la izquierda
            turbina = Turbina()
            turbina.calcular_c_T()
            estela = Estela()                               # calcula estela unicamente en el pto
