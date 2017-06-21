from __future__ import division
# coding=utf-8

from Modelo_2 import Modelo
import numpy as np
from numpy import exp
from Case_2 import Case
from Turbina_2 import Turbina
# from cart2pol import cart2pol
# from Coordenadas import Coordenadas
# from Coordenadas_Norm import Coordenadas_Norm



class Estela(object):

    def __init__(self, turbina, modelo):
        self.turbina = turbina
        self.modelo = modelo
        self.c_T = turbina.calcular_c_T(c_T_table, modelo, U_x, q)

    def calcularme(self, mi_posicion, L_x, q_x, L, q):    # caja de volumen (2L) * (2L) * L_x
        x = np.linspace(0, L_x, q_x)
        y = np.linspace(-L, L, q)
        z = np.linspace(-L, L, q)
        for i in range(len(x)):
            for j in range(len(y)):
                for k in range(len(z)):
                    coord = np.array([turbina.x_h, turbina.y_h + y[i], turbina.z_h + z[j]])
                    deficit_dividido_U_inf[i, j, k] = modelo.evalDeficitNorm(coord,c_T)
