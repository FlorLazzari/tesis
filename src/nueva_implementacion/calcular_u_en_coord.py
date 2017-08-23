from __future__ import division
# coding=utf-8

from Modelo_2 import Modelo
from Gaussiana_2 import Gaussiana
from Parque_de_turbinas import Parque_de_turbinas
from Turbina_Marca import Turbina_Marca
from U import U
from Coord import Coord
import numpy as np
from numpy import exp


def calcular_u_en_coord(modelo, u_inf, coord, parque_de_turbinas):

    u_coord = u_inf
    turbinas_a_la_izquierda = parque_de_turbinas.turbinas_a_la_izquierda_de_una_coord(coord)
    deficit_normalizado_en_coord = []
# el parque ya esta inicializado, el c_T de la primera turbina esta calculado
    index = 0
# el for no deberia incluir a la primera turbina
    for turbina in turbinas_a_la_izquierda:
        turbina.generar_coord_random()
        # ahora calculo la contribucion de cada turbina a la izquierda en las coord_random

        q = 10              # division dentro de la grilla (queda hardcodeado aca adentro, habria que ver que valor de q es el ideal)
        U = []
        U_adentro_disco = np.array([])
        count = 0
        for coord_random in coord_random_arreglo:
            if ((coord_random[1]-self.coord[1])**2 + (coord_random[2]-self.coord[2])**2 < (self.d_0/2)**2):
                deficit_normalizado_en_coord_random = modelo.evaluar_deficit_normalizado(turbina, coord_random)
                u_coord = u_coord * (1 - deficit_normalizado_en_coord_random)
                U = u_coord

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

        turbina.calcular_c_T(gaussiana, u_inf, coord_turbina, n)
        # u_coord = u_coord * (1 - deficit_normalizado_en_coord)
        print "index =", index
        print 'deficit_normalizado_en_coord_por_[index] =', deficit_normalizado_en_coord[index]
        index = index + 1

    # return u_coord

# problema: se me va el indice
# habria que hacer algo como un u_disco = [u.coord1, u.coord2, ...] donde coord1, coord2, etc sean random

from Turbina_Paper import Turbina_Paper
# # test
gaussiana = Gaussiana()
turbina_1 = Turbina_Paper(Coord(np.array([0,0,100])))
turbina_2 = Turbina_Paper(Coord(np.array([4,0,100])))
turbina_3 = Turbina_Paper(Coord(np.array([5,0,100])))
parque_de_turbinas = Parque_de_turbinas([turbina_1, turbina_2, turbina_3])
u_inf = 10
parque_de_turbinas.inicializar_parque(u_inf)
u = U()
coord = Coord(np.array([6,0,100]))
u.coord = calcular_u_en_coord(gaussiana, u_inf, coord, parque_de_turbinas)
# print u.coord
