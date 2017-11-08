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

gaussiana = Gaussiana()
u_inf = U_inf()
u_inf.coord_hub = 2.2
u_inf.perfil = 'log'

turbina_0 = Turbina_Paper(Coord(np.array([0,0,0.125])))
# z_0 de la superficie
z_0 = 0.00003
parque_de_turbinas = Parque_de_turbinas([turbina_0], z_0)


coordenadas = []
# recordar que el range funciona de la siguiente forma [)
x = np.arange(0, 20*(turbina_0.d_0), 0.01)
y_0 = 0
z = np.arange(0, 20*(turbina_0.d_0), 0.01)

for i in x:
    for j in z:
        coordenadas.append(Coord(np.array([i, y_0, j])))


# for coord in coordenadas:
#     if coord.z != 0:
#         u_inf.calcular_logaritmico(coord, u_hub, z_h, z_0)
#         u.coord = calcular_u_en_coord(gaussiana, u_inf.coord, coord, parque_de_turbinas)
        # print u_inf.coord
        # print ('u.coord', u.coord)


X, Z = np.meshgrid(x, z)

data_prueba = np.zeros([X.shape[0], X.shape[1]])

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        coord = Coord(np.array([x[i], y_0, z[j]]))
        if coord.z != 0:
            data_prueba[j,i] = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas, u_inf, 50)
            # print ('data_prueba[i,j]', i, j, data_prueba[i,j])

contornos = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5]

plt.contour(X,Z,data_prueba, contornos, linewidths=0.5, colors='k')
plt.contourf(X,Z,data_prueba, contornos, cmap=plt.cm.jet)
plt.colorbar(ticks=[1, 1.5, 2, 2.5])
ax = plt.gca()
ax.set_xticks([0, 2*(turbina_0.d_0), 4*(turbina_0.d_0), 8*(turbina_0.d_0), 12*(turbina_0.d_0), 16*(turbina_0.d_0), 20*(turbina_0.d_0)])
ax.set_yticks([0, 1*(turbina_0.d_0), 2*(turbina_0.d_0)])
ax.set_xlim([0, 20*(turbina_0.d_0)])
ax.set_ylim([0, 2*(turbina_0.d_0)])
plt.show()


# faltaria calcular potencia
