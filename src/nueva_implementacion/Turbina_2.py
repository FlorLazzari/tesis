from __future__ import division
# coding=utf-8

import numpy as np
from numpy import exp
from integrar_disco_monte_carlo import integrar_disco_monte_carlo
from calcular_U_en_pto import calcular_U_en_pto


class Turbina(object):

    def __init__(self, d_0, coord_selec):
        self.d_0 = d_0
        self.coord_selec = coord_selec

    def c_T_tabulado(self):
        pass

    def calcular_c_T(self, Modelo, U_inf, coord_turbina, n):
        # rho = densidad del aire
        # At sea level and at 15 C air has a density of approximately 1.225 kg/m3
        q = 10              # division dentro de la grilla
        rho = 1.225
        U = []
        U_adentro_disco = np.array([])
        for i in np.linspace(self.coord_selec[1]-(self.d_0/2), self.coord_selec[1]+(self.d_0/2), q):
            for j in np.linspace(self.coord_selec[2]-(self.d_0/2), self.coord_selec[2]+(self.d_0/2), q):
                if ((i-self.coord_selec[1])**2 + (j-self.coord_selec[2])**2 < (self.d_0/2)**2):
                    U = calcular_U_en_pto(Modelo, U_inf, coord_turbina, n, self.coord_selec)
                    # para el caso mas sencillo (donde no hay turbina a la izq) vale esto, sino
                    # saldra de calcular el U dependiendo del modelo y la distribucion de turbinas etc.
                    U_adentro_disco = np.append(U_adentro_disco, U)
        U_medio_disco = np.mean(U_adentro_disco)
        print(U_medio_disco)
        # U_mean debe ser un valor entero, por lo tanto lo redondeo
        c_T_tab = self.c_T_tabulado(U_medio_disco)

        # podria usarse interpolacion para mejorar la tabla
        # n = 2# como estimo el orden de n?
        # f = # saldra del modelo
        # T = integrar_disco_monte_carlo(n,f,d_0)
        # c_T_medio = T / (0.5 * rho * (U_medio_disco)**2 * (pi*(d_0/2)**2) )


    def calcular_c_P(self):
        pass
