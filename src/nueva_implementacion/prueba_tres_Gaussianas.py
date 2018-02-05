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

gaussiana = Gaussiana()
u_inf = U_inf()
u_inf.coord_hub = 7
u_inf.perfil = 'log'
N = 50

turbina_0 = Turbina_Rawson(Coord(np.array([0,0,120]))) # chequear altura del hub
D = turbina_0.d_0

turbina_1 = Turbina_Rawson(Coord(np.array([7*D,0,120])))
turbina_2 = Turbina_Rawson(Coord(np.array([14*D,0,120])))
# z_0 de la superficie
z_0 = 0.1
parque_de_turbinas = Parque_de_turbinas([turbina_0, turbina_1, turbina_2], z_0)


################################################################################
# grafico (X,Z)

coordenadas = []
# recordar que el range funciona de la siguiente forma [)
x = np.arange(0, 22*D, 22)
y_0 = 0
z = np.arange(0, 22*D, 22)

for i in x:
    for j in z:
        coordenadas.append(Coord(np.array([i, y_0, j])))

X, Z = np.meshgrid(x, z)

data_prueba = np.zeros([X.shape[0], X.shape[1]])

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        coord = Coord(np.array([x[i], y_0, z[j]]))
        if coord.z != 0:
            data_prueba[j,i] = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas, u_inf, N)
            # print ('data_prueba[i,j]', i, j, data_prueba[i,j])

# contornos = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5]

plt.contour(X,Z,data_prueba, linewidths=0.5, colors='k')
plt.contourf(X,Z,data_prueba, cmap=plt.cm.jet)
ax = plt.gca()
ax.set_xticks([0, 3.5*D, 7*D, 10.5*D, 14*D, 18.5*D, 22*D])
ax.set_yticks([0, 1*(turbina_0.d_0), 2*(turbina_0.d_0)])
ax.set_xlim([0, 22*D])
ax.set_ylim([0, 2*(turbina_0.d_0)])
plt.colorbar()
plt.show()

################################################################################
# grafico (X,Y)

coordenadas = []
# recordar que el range funciona de la siguiente forma [)
x = np.arange(0, 22*D, 22)
y = np.arange(-11*D, 11*D, 22)
z_0 = turbina_0.coord.z

for i in x:
    for j in y:
        coordenadas.append(Coord(np.array([i, j, z_0])))

X, Z = np.meshgrid(x, z)

data_prueba = np.zeros([X.shape[0], X.shape[1]])

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        coord = Coord(np.array([x[i], y[i], z_0]))
        if coord.z != 0:
            data_prueba[j,i] = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas, u_inf, N)
            # print ('data_prueba[i,j]', i, j, data_prueba[i,j])

plt.contour(X,Z,data_prueba, linewidths=0.5, colors='k')
plt.contourf(X,Z,data_prueba, cmap=plt.cm.jet)
ax = plt.gca()
ax.set_xticks([0, 3.5*D, 7*D, 10.5*D, 14*D, 18.5*D, 22*D])
ax.set_yticks([0, 1*(turbina_0.d_0), 2*(turbina_0.d_0)])
ax.set_xlim([0, 22*D])
ax.set_ylim([-7*D, 7*D])
plt.colorbar()
plt.show()

# faltaria calcular potencia
print "potencia = ",turbina_0.potencia
print "potencia = ",turbina_1.potencia
print "potencia = ",turbina_2.potencia
