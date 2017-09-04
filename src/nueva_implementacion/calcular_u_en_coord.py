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
    print u_coord
    for turbina in turbinas_a_la_izquierda:
        deficit_normalizado_en_coord = modelo.evaluar_deficit_normalizado(turbina, coord)
        u_coord = u_coord * (1 - deficit_normalizado_en_coord)
    return u_coord
