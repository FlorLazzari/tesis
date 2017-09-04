from __future__ import division
# coding=utf-8

import numpy as np
from numpy import exp
from Coord import Coord
from U_inf import U_inf

class Turbina(object):

    def __init__(self, d_0, coord):
        self.d_0 = d_0
        self.coord = coord
        self.c_T = None
        self.estela_de_otras_turbinas = []

    def c_T_tabulado(self):
        pass

    def generar_coord_random(self):
        N = 5     # como estimo el orden?
        coord_random_arreglo = []
        for i in range(N):
            rand_y = np.random.uniform(self.coord.y-(self.d_0/2), self.coord.y+(self.d_0/2))
            rand_z = np.random.uniform(self.coord.z-(self.d_0/2), self.coord.z+(self.d_0/2))
            coord_random = Coord(np.array([self.coord.x, rand_y, rand_z]))
            coord_random_arreglo = np.append(coord_random_arreglo, coord_random)
        return coord_random_arreglo




    def calcular_c_T(estela, coord_random_adentro_disco, u_inf, cantidad_turbinas_izquierda_de_selec):
    #     - cantidad_adentro_disco = len(coord_random_adentro_disco)
    #     - cantidad_turbinas_izquierda_de_selec = len(estela)/cantidad_adentro_disco
    #     - self.merge_estela(estela, cantidad_adentro_disco, cantidad_turbinas_izquierda_de_selec)
    #     - u_inf_arreglo = calcular u_inf en cada coord_random_arreglo (podria ser usando el modelo del log dado en U() )
    #     - restar la estela total a la u_inf en todo el u_inf_arreglo
    #     - hacer el montecarlo con el u_inf_arreglo
    #     - obtener el c_T
    #
        cantidad_adentro_disco = len(coord_random_adentro_disco)
        self.merge_estela(estela, cantidad_adentro_disco, cantidad_turbinas_izquierda_de_selec)
        u_inf_arreglo = U_inf()



    # def calcular_c_T(self, cantidad_adentro_disco, cantidad_turbinas_izquierda_de_selec):
    #     q = 10              # division dentro de la grilla (queda hardcodeado aca adentro, habria que ver que valor de q es el ideal)
    #     U = []
    #     U_adentro_disco = np.array([])
    #     N = 500     # como estimo el orden?
    #     count = 0
    #     # primero mergeo las estelas de todas las turbinas
    #     merge_estela(self.estela_de_otras_turbinas, cantidad_adentro_disco, cantidad_turbinas_izquierda_de_selec)
    #
    #         self.estela_de_otras_turbinas
    #         U =
    #         U_adentro_disco = np.append(U_adentro_disco, U)
    #         count = count + U**2
    #     U_medio_disco = np.mean(U_adentro_disco)
    #     print(U_medio_disco)
    #     c_T_tab = self.c_T_tabulado(U_medio_disco)
    #     volume = (self.d_0)**2
    #     integral_U_cuadrado = (volume * count)/N
    #     T_turbina = c_T_tab * integral_U_cuadrado   # lo dividi por (0.5 * rho) porque luego dividire por eso
    #     T_disponible = (U_medio_disco)**2 * (np.pi*(self.d_0/2)**2)     # lo dividi por (0.5 * rho) porque luego multiplicare por eso
    #     c_T = T_turbina / T_disponible
    #     print ('c_T calculado:', c_T)
    #     print ('c_T_tab:', c_T_tab)

    # def calcular_c_T(self, Modelo, U_inf, coord, n):
    #     q = 10              # division dentro de la grilla (queda hardcodeado aca adentro, habria que ver que valor de q es el ideal)
    #     U = []
    #     U_adentro_disco = np.array([])
    #     N = 500     # como estimo el orden?
    #     count = 0
    #     x = self.coord[0]
    #     for i in range(N):
    #         rand_y = np.random.uniform(self.coord[1]-(self.d_0/2), self.coord[1]+(self.d_0/2))
    #         rand_z = np.random.uniform(self.coord[2]-(self.d_0/2), self.coord[2]+(self.d_0/2))
    #         coord_random = np.array([x, rand_y, rand_z])
    #         if ((rand_y-self.coord[1])**2 + (rand_z-self.coord[2])**2 < (self.d_0/2)**2):
    #             U = calcular_U_en_pto(Modelo, U_inf, coord_turbina, n, coord_random)
    #             U_adentro_disco = np.append(U_adentro_disco, U)
    #             count = count + U**2
    #     U_medio_disco = np.mean(U_adentro_disco)
    #     print(U_medio_disco)
    #     c_T_tab = self.c_T_tabulado(U_medio_disco)
    #     volume = (self.d_0)**2
    #     integral_U_cuadrado = (volume * count)/N
    #     T_turbina = c_T_tab * integral_U_cuadrado   # lo dividi por (0.5 * rho) porque luego dividire por eso
    #     T_disponible = (U_medio_disco)**2 * (np.pi*(self.d_0/2)**2)     # lo dividi por (0.5 * rho) porque luego multiplicare por eso
    #     c_T = T_turbina / T_disponible
    #     print ('c_T calculado:', c_T)
    #     print ('c_T_tab:', c_T_tab)

    # def calcular_c_P(self):
    #     pass
