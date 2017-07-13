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

    for turbina in turbinas_a_la_izquierda:
        deficit_normalizado = modelo.evaluar_deficit_normalizado(turbina, coord)
        u_coord = u_coord * (1 - deficit_normalizado)
        return u_coord


    #         turbina[i] = Turbina(d_0, coord_turbina)                            # coord deben ser no normalizadas (np.array)
    #         turbina[i].calcular_c_T(c_T_table, modelo, U_disco)         # si es la primer turbina => U_disco = U_inf
    #         estela[i] = Estela(turbina[i], modelo)                      # la turbina le pasa el c_T
    #         deficit_dividido_U_inf[i] = estela[i].calcular_en_coord_selec(coord_selec)   # es el deficit generado por la estela i en la coord_selec
    # suma_deficit = np.sum(deficit_dividido_U_inf)                       # en este caso lo estoy sumando a lo bruto, en el futuro deberia haber algo de la forma:
    #                                                                     # suma_deficit = suma(deficit_dividido_U_inf)
    # return U_coord_selec

# # test
# gaussiana = Gaussiana()
# turbina_1 = Turbina_Marca(np.array([0,0,100]))
# parque_de_turbinas = Parque_de_turbinas([turbina_1])
# u = U()
# coord = np.array([3,0,100])
# u.coord = calcular_u_en_coord(gaussiana, 10, coord, parque_de_turbinas)
# print u.coord
