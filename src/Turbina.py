from __future__ import division
# coding=utf-8

import numpy as np
from numpy import exp
from Case_2 import Case
from integrar_disco_monte_carlo import integrar_disco_monte_carlo

# from cart2pol import cart2pol
# from Coordenadas import Coordenadas
# from Coordenadas_Norm import Coordenadas_Norm

# parametro global de "presicion"
q = 10

class Turbina(object):

    def __init__(self, d_0, x_h, y_h, z_h):
        self.d_0 = d_0
        self.x_h = x_h
        self.y_h = y_h
        self.z_h = z_h

    def calcular_c_T(self, c_T_table, modelo, U_x):
        # U_x = debe ser una matriz de U en un x fijo para "y" y "z" en el rango que
        # vamos a estudiar a continuacion

        U_x = calcular_U(modelo, posicion_turbinas, mi_posicion)

        # rho = densidad del aire
        # At sea level and at 15 C air has a density of approximately 1.225 kg/m3
        rho = 1.225
        y = np.linspace(-d_0/2, d_0/2, q)
        z = np.linspace(-d_0/2, d_0/2, q)
        U = np.zeros((q, q))
        for i in range(len(y)):
            for j in range(len(z)):
                if (y[i]**2 + z[i]**2 < (d_0/2)**2):
                    coord = np.array([x_h, y_h + y[i], z_h + z[j]])
                    deficit_dividido_U_inf[i, j] = modelo.evalDeficitNorm(coord,c_T)
                    U[i,j] = U_x[i,j] * (1 - deficit_dividido_U_inf[i,j])
        U_mean = np.mean(U)  # promedio sobre el disco

        # saldra de calcular el U dependiendo del modelo y la distribucion de turbinas
        # U_mean debe ser un valor entero, por lo tanto lo redondeo
        c_T_tab = tabla[round(U_mean,0)] # podria usarse interpolacion para mejorar la tabla
        n = 2# como estimo el orden de n?
        f = # saldra del modelo
        T = integrar_disco_monte_carlo(n,f,d_0)
        c_T_mean = T / (0.5 * rho * (U_mean)**2 * (pi*(d_0/2)**2) )


    def calcular_c_P(self):
        pass
