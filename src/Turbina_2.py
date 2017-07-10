from __future__ import division
# coding=utf-8

import numpy as np
from numpy import exp
from Case_2 import Case
from integrar_disco_monte_carlo import integrar_disco_monte_carlo

# from cart2pol import cart2pol
# from Coordenadas import Coordenadas
# from Coordenadas_Norm import Coordenadas_Norm


turbina[i] = Turbina(d_0, coord_turbina)                            # coord deben ser no normalizadas (np.array)
turbina[i].calcular_c_T(c_T_table, modelo, U_disco)         # si es la primer turbina => U_disco = U_inf

q = 10

class Turbina(object):

    def __init__(self, d_0, coord_turbina):
        self.d_0 = d_0
        self.coord_turbina[0] = x_h
        self.coord_turbina[1] = y_h
        self.coord_turbina[2] = z_h

    def calcular_c_T(self, c_T_tab, modelo, U_disco):
        # rho = densidad del aire
        # At sea level and at 15 °C air has a density of approximately 1.225 kg/m3
        rho = 1.225
        y = np.linspace( y_h-(d_0/2), y_h+(d_0/2), q)
        z = np.linspace( z_h-(d_0/2), z_h+(d_0/2), q)
        U = np.zeros((q, q))
        U_adentro_disco = np.array([])
        for i in range(len(y)):
            for j in range(len(z)):
                if (y[i]**2 + z[j]**2 < (d_0/2)**2):
                    U[i,j] = U_disco                        # para el caso mas sencillo (donde no hay turbina a la izq) vale esto, sino
                                                            # saldra de calcular el U dependiendo del modelo y la distribucion de turbinas etc.
                    U_adentro_disco = np.append(U_adentro_disco, U_[i,j])
        U_medio_disco = np.mean(U_adentro_disco)
        # U_mean debe ser un valor entero, por lo tanto lo redondeo
        c_T_tab = tabla[round(U_mean,0)] # podria usarse interpolacion para mejorar la tabla
        n = 2# como estimo el orden de n?
        f = # saldra del modelo
        T = integrar_disco_monte_carlo(n,f,d_0)
        c_T_medio = T / (0.5 * rho * (U_medio_disco)**2 * (pi*(d_0/2)**2) )


    def calcular_c_P(self):
        pass
