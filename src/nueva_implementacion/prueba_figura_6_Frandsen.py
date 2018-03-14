from __future__ import division
import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
# coding=utf-8

from Frandsen import Frandsen
from Parque_de_turbinas import Parque_de_turbinas
from Turbina_Paper import Turbina_Paper
from Coord import Coord
from Estela import Estela
from U_inf import U_inf
from calcular_u_en_coord import calcular_u_en_coord

frandsen = Frandsen()
u_inf = U_inf()
u_inf.coord_hub = 2.2
u_inf.perfil = 'log'
N = 1000

turbina_0 = Turbina_Paper(Coord(np.array([0,0,0.125])))
# z_0 de la superficie
z_0 = 0.00003
parque_de_turbinas = Parque_de_turbinas([turbina_0], z_0)

# recordar que el range funciona de la siguiente forma [)
x = np.arange(0, 20*(turbina_0.d_0)+0.1, 0.1)
y_0 = 0
z = np.arange(0, 2*(turbina_0.d_0)+0.005, 0.005)

X, Z = np.meshgrid(x, z)

data_prueba = np.zeros([len(z), len(x)])

for i in range(len(x)):
    for j in range(len(z)):
        coord = Coord(np.array([x[i], y_0, z[j]]))
        if coord.z != 0:
            data_prueba[j,i] = calcular_u_en_coord(frandsen, 'linear', coord, parque_de_turbinas, u_inf, N)
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

# 2) corte X,Y
# recordar que el range funciona de la siguiente forma [)
x = np.arange(0, 27*(turbina_0.d_0)+0.01, 0.01)
y = np.arange(-2*(turbina_0.d_0), 2*(turbina_0.d_0)+0.01, 0.01)
z_0 = turbina_0.coord.z

X, Y = np.meshgrid(x, y)

data_prueba = np.zeros([len(y), len(x)])

for i in range(len(x)):
    for j in range(len(Y)):
        coord = Coord(np.array([x[i], y[j], z_0]))
        if coord.z != 0:
            data_prueba[j,i] = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas, u_inf, N)
            # print ('data_prueba[i,j]', i, j, data_prueba[i,j])

# estoy cambiando la escala, escucho opiniones al respecto de esto
contornos = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2]#, 2.3, 2.4, 2.5]

plt.contour(X,Y,data_prueba, contornos, linewidths=0.5, colors='k')
plt.contourf(X,Y,data_prueba, contornos, cmap=plt.cm.jet)
plt.colorbar(ticks=[1, 1.5, 2, 2.5])
ax = plt.gca()
ax.set_xticks([0, 4*(turbina_0.d_0), 8*(turbina_0.d_0), 12*(turbina_0.d_0), 16*(turbina_0.d_0), 20*(turbina_0.d_0)])
ax.set_yticks([0, 1*(turbina_0.d_0), 2*(turbina_0.d_0)])
ax.set_xlim([0, 27*(turbina_0.d_0)])
ax.set_ylim([-2*(turbina_0.d_0), 2*(turbina_0.d_0)])
plt.show()


print "potencia = ", turbina_0.potencia
# faltaria calcular potencia
