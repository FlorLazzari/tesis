from __future__ import division
# coding=utf-8

from Modelo_2 import Modelo
from Gaussiana_2 import Gaussiana
from Parque_de_turbinas import Parque_de_turbinas
from Turbina_Paper import Turbina_Paper
from Turbina_2 import Turbina
from U import U
from Coord import Coord
import numpy as np
from numpy import exp
from Estela import Estela
from decimal import Decimal
from U_inf import U_inf
from calcular_u_en_coord_2 import calcular_u_en_coord

import numpy as np
import matplotlib.pyplot as plt

"""
Tenemos dos turbinas alineadas separadas por 8D
A continuacion se grafica:
    1) El deficit a la altura del hub para dos turbinas alineadas a 16D por
    atras de la primera (8D del segundo) usando CFD (OpenFOAM).
    2) El deficit de las dos turbinas trabajando independientemente (a 16D de
    la primera turbina y a 8D de la segunda turbina)
    3) El deficit generado por ambas (a 16D de la primera turbina) utilizando
    distintos metodos de superposicion de estelas
"""

gaussiana = Gaussiana()
u_inf = U_inf()
u_inf.coord_hub = 2.2
u_inf.perfil = 'log'

turbina_0 = Turbina_Paper(Coord(np.array([0,0,0.125])))
D = turbina_0.d_0

turbina_1 = Turbina_Paper(Coord(np.array([8*D,0,0.125])))
# z_0 de la superficie
z_0 = 0.00003


# 2)
# calculo el deficit para la primera turbina independiente a 16D

parque_de_turbinas_primera_indep = Parque_de_turbinas([turbina_0], z_0)

x_0 = 16*D
y = np.arange(-1.2*D, 1.2*D, 0.01)
z_o = turbina_0.coord.z

data_prueba_primera = np.zeros(len(y))

for i in range(len(y)):
    coord = Coord(np.array([x_0, y[i], z_o]))
    data_prueba_primera[i] = calcular_u_en_coord(gaussiana, 'linear',coord, parque_de_turbinas_primera_indep, u_inf, 50)

# plt.plot(y, data_prueba_primera)
# plt.show()

# calculo el deficit para la segunda turbina independiente a 8D


# problemas! esto deberia ser lo mismo que cambiar la turbina_0 por turbina_1 y
# tomar el x_0 como 16D, por que dan resultados distintos?

# parque_de_turbinas_segunda_indep = Parque_de_turbinas([turbina_1], z_0)
# x_0 = 16*D


parque_de_turbinas_segunda_indep = Parque_de_turbinas([turbina_0], z_0)

x_0 = 8*D
y = np.arange(-1.2*D, 1.2*D, 0.01)
z_o = turbina_0.coord.z

data_prueba_segunda = np.zeros(len(y))

for i in range(len(y)):
    coord = Coord(np.array([x_0, y[i], z_o]))
    data_prueba_segunda[i] = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas_segunda_indep, u_inf, 50)

# plt.plot(y, data_prueba_primera/u_inf.coord_hub, label='Single rotor at 16D')
# plt.plot(y, data_prueba_segunda/u_inf.coord_hub, label='Single rotor at 8D')
# plt.legend()
# plt.show()

# 3)
# calculo el deficit generado por ambas (a 16D de la primera turbina) utilizando
# el metodo de superposicion 'linear'

parque_de_turbinas_ambas = Parque_de_turbinas([turbina_0, turbina_1], z_0)

x_0 = 16*D
y = np.arange(-1.2*D, 1.2*D, 0.01)
z_o = turbina_0.coord.z

data_prueba_ambas_linear = np.zeros(len(y))

for i in range(len(y)):
    coord = Coord(np.array([x_0, y[i], z_o]))
    data_prueba_ambas_linear[i] = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas_ambas, u_inf, 50)

# calculo el deficit generado por ambas (a 16D de la primera turbina) utilizando
# el metodo de superposicion 'rss'

data_prueba_ambas_rss = np.zeros(len(y))

for i in range(len(y)):
    coord = Coord(np.array([x_0, y[i], z_o]))
    data_prueba_ambas_rss[i] = calcular_u_en_coord(gaussiana, 'rss', coord, parque_de_turbinas_ambas, u_inf, 50)

# calculo el deficit generado por ambas (a 16D de la primera turbina) utilizando
# el metodo de superposicion 'largest'

data_prueba_ambas_largest = np.zeros(len(y))

for i in range(len(y)):
    coord = Coord(np.array([x_0, y[i], z_o]))
    data_prueba_ambas_largest[i] = calcular_u_en_coord(gaussiana, 'largest', coord, parque_de_turbinas_ambas, u_inf, 50)

plt.title('Perfil de velocidad normalizada detras de dos turbinas alineadas')
plt.plot(y, data_prueba_primera/u_inf.coord_hub, 'bx',label='Single rotor at 16D')
plt.plot(y, data_prueba_segunda/u_inf.coord_hub, 'rx', label='Single rotor at 8D')
plt.plot(y, data_prueba_ambas_linear/u_inf.coord_hub, 'c', label= 'Superposicion lineal')
plt.plot(y, data_prueba_ambas_rss/u_inf.coord_hub, 'g', label= 'Superposicion rss')
plt.plot(y, data_prueba_ambas_largest/u_inf.coord_hub, 'k', label= 'Superposicion largest')
plt.legend()
plt.show()
