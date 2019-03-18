from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
# coding=utf-8

from Gaussiana import Gaussiana   # Gaussiana pertenece a la clase Modelo
from Parque_de_turbinas import Parque_de_turbinas
from Turbina_Paper import Turbina_Paper
from Coord import Coord
from Estela import Estela
from U_inf import U_inf
from calcular_u_en_coord import calcular_u_en_coord

"""
A continuacion se busco replicar la figura 6 del paper de M. Bastankhah, F. Porte-Agel:

    IMPORTANTE, para que el grafico sea identico al del paper hay que utilizar en
    Gaussiana.py el k y epsilon PARAMETROS DEL PAPER, sino los resultados son ligeramente
    distintos

    Para comparar con el grafico del paper habria que cambiar el xlim y ylim en paint por
    el x/d0 y z/d0

1) corte X,Z
2) corte X,Y

"""

gaussiana = Gaussiana()
u_inf = U_inf()
u_inf.coord_mast = 2.2
u_inf.perfil = 'log'
# N = 1000
N = 50

z_mast = 0.125

turbina_0 = Turbina_Paper(Coord(np.array([0,0,z_mast])))
# z_0 de la superficie
z_0 = 0.00003
parque_de_turbinas = Parque_de_turbinas([turbina_0], z_0, z_mast)

# 2) corte X,Z
# recordar que el range funciona de la siguiente forma [)
#gonza usa una resolucion de 140X35 aprox

x = np.arange(0, 20*(turbina_0.d_0)+0.01, 0.01)
y_0 = 0
z = np.arange(0, 2*(turbina_0.d_0)+0.005, 0.005)

X, Z = np.meshgrid(x, z)

data_prueba = np.zeros([len(z), len(x)])

import time

tiempo_procesamiento = []
tic = time.clock()
for i in range(len(x)):
    for j in range(len(z)):
        coord = Coord(np.array([x[i], y_0, z[j]]))
        if coord.z != 0:
            tic = time.clock()
            data_prueba[j,i] = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas, u_inf, N)
            toc = time.clock()
            # print ('data_prueba[i,j]', i, j, data_prueba[i,j])
            tiempo_procesamiento = np.append(tiempo_procesamiento, toc - tic)
print 'len(tiempo_procesamiento) = ',len(tiempo_procesamiento)
print 'np.mean(tiempo_procesamiento) = ', np.mean(tiempo_procesamiento)
print 'np.std(tiempo_procesamiento) = ', np.std(tiempo_procesamiento)

# contornos = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5]

contornos = np.linspace(1, 2.4, 20)

plt.contour(X,Z,data_prueba, contornos, linewidths=0.5, colors='k')
plt.contourf(X,Z,data_prueba, contornos, cmap=plt.cm.jet)
plt.colorbar(ticks=[1, 1.5, 2, 2.5])
ax = plt.gca()
ax.set_xticks([0, 4*(turbina_0.d_0), 8*(turbina_0.d_0), 12*(turbina_0.d_0), 16*(turbina_0.d_0), 20*(turbina_0.d_0)])
ax.set_yticks([0, 1*(turbina_0.d_0), 2*(turbina_0.d_0)])
ax.set_xlim([0, 20*(turbina_0.d_0)])
ax.set_ylim([0, 2*(turbina_0.d_0)])
plt.show()

# 2) corte X,Y
# recordar que el range funciona de la siguiente forma [)
x = np.arange(0, 32*(turbina_0.d_0)+0.01, 0.01)
y = np.arange(-1*(turbina_0.d_0), 1*(turbina_0.d_0)+0.01, 0.01)
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
# contornos = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2]

contornos = np.linspace(1, 2.2, 20)

plt.contour(X,Y,data_prueba, contornos, linewidths=0.5, colors='k')
plt.contourf(X,Y,data_prueba, contornos, cmap=plt.cm.jet)
plt.colorbar(ticks=[1, 1.5, 2, 2.2])
ax = plt.gca()
ax.set_xticks([0, 2*(turbina_0.d_0), 4*(turbina_0.d_0), 8*(turbina_0.d_0), 12*(turbina_0.d_0), 16*(turbina_0.d_0), 20*(turbina_0.d_0), 24*(turbina_0.d_0), 28*(turbina_0.d_0), 32*(turbina_0.d_0)])
ax.set_yticks([-1*(turbina_0.d_0), 0, 1*(turbina_0.d_0)])
ax.set_xlim([0, 32*(turbina_0.d_0)])
ax.set_ylim([-1*(turbina_0.d_0), 1*(turbina_0.d_0)])
plt.show()


# print "potencia = ",turbina_0.potencia
# faltaria calcular bien potencia
