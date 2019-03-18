from __future__ import division
import numpy as np
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
u_inf.coord_mast = 7
u_inf.perfil = 'log'
N = 300
z_mast = 80

turbina_0 = Turbina_Rawson(Coord(np.array([0,0,80]))) # chequear altura del hub
D = turbina_0.d_0

# z_0 de la superficie
z_0 = 0.075
parque_de_turbinas = Parque_de_turbinas([turbina_0], z_0, z_mast)

# 1)
################################################################################
# grafico (X,Z)

# recordar que el range funciona de la siguiente forma [)
x = np.linspace(0, 10*D, 150)
y_0 = 0
z = np.linspace(0, 2*D, 50)

X, Z = np.meshgrid(x, z)

data_prueba = np.zeros([len(z), len(x)])

import time
array_tiempo_procesamiento = []

for iter_corrida in range(10):
    tiempo_procesamiento = 0
    # tic = time.clock()
    for i in range(len(x)):
        for j in range(len(z)):
            coord = Coord(np.array([x[i], y_0, z[j]]))
            if coord.z != 0:
                tic = time.clock()
                data_prueba[j,i] = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas, u_inf, N)
                toc = time.clock()
                # print ('data_prueba[i,j]', i, j, data_prueba[i,j])
                tiempo_procesamiento = tiempo_procesamiento + (toc - tic)
    array_tiempo_procesamiento = np.append(array_tiempo_procesamiento, tiempo_procesamiento)
print 'len(array_tiempo_procesamiento) = ',len(array_tiempo_procesamiento)
print 'np.mean(array_tiempo_procesamiento) = ', np.mean(array_tiempo_procesamiento)
print 'np.std(array_tiempo_procesamiento) = ', np.std(array_tiempo_procesamiento)


# contornos = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5]

contornos = np.linspace(0, 8, 15)

plt.contour(X,Z,data_prueba, contornos, linewidths=0, colors='k')
plt.contourf(X,Z,data_prueba, contornos, cmap=plt.cm.jet)
plt.colorbar(ticks=[0, 2, 4, 6, 8])
ax = plt.gca()
ax.set_xticks([0])
ax.set_yticks([0])
ax.set_xlim([0, 10*(turbina_0.d_0)])
ax.set_ylim([0, 2*(turbina_0.d_0)])
plt.show()
print 'tiempo procesamiento =',tiempo_procesamiento
