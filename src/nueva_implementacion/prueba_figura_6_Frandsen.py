from __future__ import division
# coding=utf-8

from Frandsen_2 import Frandsen
from Parque_de_turbinas import Parque_de_turbinas
from Turbina_Paper import Turbina_Paper
from U import U
from U_inf import U_inf
from Coord import Coord
from calcular_u_en_coord import calcular_u_en_coord

import numpy as np
import matplotlib.pyplot as plt

frandsen = Frandsen()
turbina_0 = Turbina_Paper(Coord(np.array([0,0,0.125])))
parque_de_turbinas = Parque_de_turbinas([turbina_0])

u_inf = U_inf()
# velocidad a la altura de la turbina
u_hub = 2.2

parque_de_turbinas.inicializar_parque(u_hub)

u = U()

coordenadas = []
# recordar que el range funciona de la siguiente forma [)
x = np.arange(0, 20.01*(turbina_0.d_0), 0.01)
y_0 = 0
z = np.arange(0, 20.01*(turbina_0.d_0), 0.01)

for i in x:
    for j in z:
        coordenadas.append(Coord(np.array([i, y_0, j])))

# calculo el u con perfil logaritmico
# altura del hub:
z_h = turbina_0.coord.z
# z_0 de la superficie
z_0 = 0.00003

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
            u_inf.calcular_logaritmico(coord, u_hub, z_h, z_0)
            data_prueba[j,i] = calcular_u_en_coord(frandsen, u_inf.coord, coord, parque_de_turbinas)
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
