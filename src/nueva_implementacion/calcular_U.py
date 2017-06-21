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

def calcular_U(modelo, posicion_turbinas, mi_posicion):

    for i in range(mi_posicion):
        if (posicion_turbinas[i][0] < mi_posicion[0]):      # si hay turbinas a la izquierda
            estela = Estela()
