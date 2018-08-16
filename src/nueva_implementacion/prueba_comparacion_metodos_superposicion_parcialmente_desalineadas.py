# coding=utf-8

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

from Gaussiana import Gaussiana
from Parque_de_turbinas import Parque_de_turbinas
from Turbina_Paper import Turbina_Paper
from Coord import Coord
from Estela import Estela
from U_inf import U_inf
from calcular_u_en_coord import calcular_u_en_coord

"""
Tenemos dos turbinas parcialmente desalineadas (1D en y) separadas por 8D en z
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
u_inf.coord_mast = 2.2
u_inf.perfil = 'log'

turbina_0 = Turbina_Paper(Coord(np.array([0,0,0.125])))
D = turbina_0.d_0

turbina_1 = Turbina_Paper(Coord(np.array([8*D,1*D,0.125])))
# z_0 de la superficie
z_0 = 0.00003

z_mast = 0.125

# 2)
# calculo el deficit a 16D para la primera turbina independiente

parque_de_turbinas_primera_indep = Parque_de_turbinas([turbina_0], z_0, z_mast)

x_0 = 16*D
y = np.arange(-1.2*D, 2.2*D, 0.01)
z_o = turbina_0.coord.z

data_prueba_primera = np.zeros(len(y))

for i in range(len(y)):
    coord = Coord(np.array([x_0, y[i], z_o]))
    data_prueba_primera[i] = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas_primera_indep, u_inf, 100)

# en este caso el metodo_superposicion = 'linear' pero podria ser cualquier cosa ya que hay unicamente una estela, no hay interaccion

# plt.plot(y, data_prueba_primera)
# plt.show()

# calculo el deficit para la segunda turbina independiente (ubicada en x = 8D) a 16D

parque_de_turbinas_segunda_indep = Parque_de_turbinas([turbina_1], z_0, z_mast)
x_0 = 16*D

y = np.arange(-1.2*D, 2.2*D, 0.01)
z_o = turbina_0.coord.z

data_prueba_segunda = np.zeros(len(y))

for i in range(len(y)):
    coord = Coord(np.array([x_0, y[i], z_o]))
    data_prueba_segunda[i] = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas_segunda_indep, u_inf, 100)

# plt.plot(y, data_prueba_primera/u_inf.coord_hub, label='Single rotor at 16D')
# plt.plot(y, data_prueba_segunda/u_inf.coord_hub, label='Single rotor at 8D')
# plt.legend()
# plt.show()

# 3)
# calculo el deficit generado por ambas (a 16D de la primera turbina) utilizando
# el metodo de superposicion 'linear'

parque_de_turbinas_ambas = Parque_de_turbinas([turbina_0, turbina_1], z_0, z_mast)

x_0 = 16*D
y = np.arange(-1.2*D, 2.2*D, 0.01)
z_o = turbina_0.coord.z

data_prueba_ambas_linear = np.zeros(len(y))

for i in range(len(y)):
    coord = Coord(np.array([x_0, y[i], z_o]))
    data_prueba_ambas_linear[i] = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas_ambas, u_inf, 100)

# calculo el deficit generado por ambas (a 16D de la primera turbina) utilizando
# el metodo de superposicion 'rss'

data_prueba_ambas_rss = np.zeros(len(y))

for i in range(len(y)):
    coord = Coord(np.array([x_0, y[i], z_o]))
    data_prueba_ambas_rss[i] = calcular_u_en_coord(gaussiana, 'rss', coord, parque_de_turbinas_ambas, u_inf, 100)

# calculo el deficit generado por ambas (a 16D de la primera turbina) utilizando
# el metodo de superposicion 'largest'

data_prueba_ambas_largest = np.zeros(len(y))

for i in range(len(y)):
    coord = Coord(np.array([x_0, y[i], z_o]))
    data_prueba_ambas_largest[i] = calcular_u_en_coord(gaussiana, 'largest', coord, parque_de_turbinas_ambas, u_inf, 100)


################################################################################



# plt.title('Perfil de velocidad normalizada detras de dos turbinas parcialmente desalineadas')
# plt.plot(y/D, data_prueba_primera/u_inf.coord_mast, 'bx',label='Single rotor at 16D')
# plt.plot(y/D, data_prueba_segunda/u_inf.coord_mast, 'rx', label='Single rotor at 8D')
# plt.plot(y/D, data_prueba_ambas_linear/u_inf.coord_mast, 'c', label= 'Superposicion lineal')
# plt.plot(y/D, data_prueba_ambas_rss/u_inf.coord_mast, 'g', label= 'Superposicion rss')
# plt.plot(y/D, data_prueba_ambas_largest/u_inf.coord_mast, 'k', label= 'Superposicion largest')
# plt.legend()
# plt.grid()
# plt.xlabel(r'$y/d$')
# plt.ylabel(r'$u/u_{\infty}$')
# plt.show()

plt.figure(figsize=(11,11))
plt.plot(y/D - np.mean(y/D), 1 - data_prueba_primera/u_inf.coord_mast, 'ob',label='Rotor libre (16d)', markersize= 10)
plt.plot(y/D - np.mean(y/D), 1 - data_prueba_segunda/u_inf.coord_mast, 'or', label='Rotor libre (8d)', markersize= 10)
plt.plot(y/D - np.mean(y/D), 1 - data_prueba_ambas_linear/u_inf.coord_mast, 'c', label= 'Lineal (16d)', linewidth= 3)
plt.plot(y/D - np.mean(y/D), 1 - data_prueba_ambas_rss/u_inf.coord_mast, 'g', label= u'Cuadrática (16d)', linewidth= 3)
plt.plot(y/D - np.mean(y/D), 1 - data_prueba_ambas_largest/u_inf.coord_mast, 'k', label= 'Dominante (16d)', linewidth= 3)
plt.legend(fontsize=20, loc= 'upper left')
plt.grid()
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel(r'$y/d$', fontsize=30)
plt.ylabel(r'$\Delta u/u_{\infty}$', fontsize=30)
plt.savefig('superposicion_parcialmente_desalineadas.pdf')
plt.show()

# faltaria comparar con la superposicion de OpenFOAM
