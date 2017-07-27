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

    # print turbinas_a_la_izquierda
    index = 0
    for turbina in turbinas_a_la_izquierda:
        deficit_normalizado_en_coord = modelo.evaluar_deficit_normalizado(turbina, coord)
        u_coord = u_coord * (1 - deficit_normalizado_en_coord)
        # print turbinas_a_la_izquierda[index + 1]
        # siguiente_turbina = turbinas_a_la_izquierda[index + 1]
        # index += 1
        # deficit_normalizado_en_turbina_siguiente = modelo.evaluar_deficit_normalizado(turbina, siguiente_turbina.coord)
    return u_coord

# problema: se me va el indice
# habria que hacer algo como un u_disco = [u.coord1, u.coord2, ...] donde coord1, coord2, etc sean random

# # test
# gaussiana = Gaussiana()
# turbina_1 = Turbina_Marca(Coord(np.array([0,0,100])))
# turbina_2 = Turbina_Marca(Coord(np.array([4,0,100])))
# turbina_3 = Turbina_Marca(Coord(np.array([5,0,100])))
# parque_de_turbinas = Parque_de_turbinas([turbina_1, turbina_2, turbina_3])
# u = U()
# coord = Coord(np.array([6,0,100]))
# u.coord = calcular_u_en_coord(gaussiana, 10, coord, parque_de_turbinas)
# print u.coord
