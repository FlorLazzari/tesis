from __future__ import division
# coding=utf-8

import numpy as np
from numpy import exp

class Turbina(object):

    def __init__(self, d_0, coord):
        self.d_0 = d_0
        self.coord = coord
        self.c_T = None

    def c_T_tabulado(self):
        pass

    def generar_coord_random(self):
        N = 500     # como estimo el orden?
        coord_random_arreglo = []
        for i in range(N):
            rand_y = np.random.uniform(self.coord[1]-(self.d_0/2), self.coord[1]+(self.d_0/2))
            rand_z = np.random.uniform(self.coord[2]-(self.d_0/2), self.coord[2]+(self.d_0/2))
            coord_random = Coord([self.coord[0], rand_y, rand_z])
            coord_random_arreglo.append(coord_random)
        return coord_random_arreglo

    def calcular_c_T(self, Modelo, U_inf, coord, coord_random):
        q = 10              # division dentro de la grilla (queda hardcodeado aca adentro, habria que ver que valor de q es el ideal)
        U = []
        U_adentro_disco = np.array([])
        count = 0
        if ((coord_random[1]-self.coord[1])**2 + (coord_random[2]-self.coord[2])**2 < (self.d_0/2)**2):
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
