from __future__ import division
import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
# coding=utf-8

from Gaussiana import Gaussiana   # Gaussiana pertenece a la clase Modelo
from Parque_de_turbinas import Parque_de_turbinas
from Turbina_Rawson import Turbina_Rawson
from Coord import Coord
from Estela import Estela
from U_inf import U_inf
from calcular_u_en_coord import calcular_u_en_coord

"""
A continuacion se corre el modelo Gaussiana para el parque Rawson.
Se grafican:
    1) La potencia en funcion de la ubicacion (numero de turbina de label)
    2) El campo de viento en el plano (X,Y) para todo el parque
"""

gaussiana = Gaussiana()
u_inf = U_inf()
u_inf.coord_mast = 8.1
u_inf.perfil = 'log'
N = 10000

z_hub = 80
turbina_0 = Turbina_Rawson(Coord(np.array([0,0,z_hub])))
D = turbina_0.d_0

# z_0 de la superficie
z_0 = 0.01
z_mast = z_hub
parque_de_turbinas = Parque_de_turbinas([turbina_0], z_0, z_mast)

################################################################################

# grafico potencia en funcion de la ubicacion (numero de turbina de label)

x_o = 10
y_o = 0
z_o = z_hub

coord = Coord(np.array([x_o, y_o, z_o]))

potencia_de_cada_turbina = []

data_prueba = calcular_u_en_coord(gaussiana, 'largest', coord, parque_de_turbinas, u_inf, N)

print turbina_0.potencia
