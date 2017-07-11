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
        q = 10              # division dentro de la grilla (queda hardcodeado aca adentro, habria que ver que valor de q es el ideal)
        U = []
        U_adentro_disco = np.array([])
        N = 500     # como estimo el orden?
        count = 0
        x = self.coord_selec[0]
        for i in range(N):
            rand_y = np.random.uniform(self.coord_selec[1]-(self.d_0/2), self.coord_selec[1]+(self.d_0/2))
            rand_z = np.random.uniform(self.coord_selec[2]-(self.d_0/2), self.coord_selec[2]+(self.d_0/2))
            coord_random = np.array([x, rand_y, rand_z])
            if ((rand_y-self.coord_selec[1])**2 + (rand_z-self.coord_selec[2])**2 < (self.d_0/2)**2):
                U = calcular_U_en_pto(Modelo, U_inf, coord_turbina, n, coord_random)
                U_adentro_disco = np.append(U_adentro_disco, U)
                count = count + U**2
        U_medio_disco = np.mean(U_adentro_disco)
        print(U_medio_disco)
        c_T_tab = self.c_T_tabulado(U_medio_disco)
        volume = (self.d_0)**2
        integral_U_cuadrado = (volume * count)/N
        T_turbina = c_T_tab * integral_U_cuadrado   # lo dividi por (0.5 * rho) porque luego dividire por eso
        T_disponible = (U_medio_disco)**2 * (np.pi*(self.d_0/2)**2)     # lo dividi por (0.5 * rho) porque luego multiplicare por eso
        c_T = T_turbina / T_disponible
        print ('c_T calculado:', c_T)
        print ('c_T_tab:', c_T_tab)

    def calcular_c_P(self):
        pass
