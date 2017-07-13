from __future__ import division
# coding=utf-8

from Gaussiana_2 import Gaussiana
from Parque_de_turbinas import Parque_de_turbinas
from Turbina_Marca import Turbina_Marca
from U import U
from Coord import Coord
from calcular_u_en_coord import calcular_u_en_coord

import numpy as np
import matplotlib.pyplot as plt

gaussiana = Gaussiana()
turbina_0 = Turbina_Marca(Coord(np.array([0,0,100])))
parque_de_turbinas = Parque_de_turbinas([turbina_0])

u_inf = 10

parque_de_turbinas.inicializar_parque(u_inf)

u = U()

coordenadas = []
# recordar que el range funciona de la siguiente forma [)
x = np.arange(0,300,0.5)
y_0 = 0
z = np.arange(0,300,0.5)

for i in x:
    for j in z:
        coordenadas.append(Coord(np.array([i, y_0, j])))

for coord in coordenadas:
    u.coord = calcular_u_en_coord(gaussiana, u_inf, coord, parque_de_turbinas)
    # print ('u.coord', u.coord)

import numpy as np
import matplotlib.pyplot as plt

X, Z = np.meshgrid(x, z)

data_prueba = np.zeros([X.shape[0], X.shape[1]])

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        coord = Coord(np.array([x[i], y_0, z[j]]))
        data_prueba[j,i] = calcular_u_en_coord(gaussiana, u_inf, coord, parque_de_turbinas)
        # print ('data_prueba[i,j]', i, j, data_prueba[i,j])

cp = plt.contourf(X,Z,data_prueba)
plt.colorbar(cp)
plt.show()

# # test
# print 'ok' if print coordenadas[0].x == 0 else 'error'
# print coordenadas[0].y
# print coordenadas[0].z
# print coordenadas[1].x
# print coordenadas[1].y
# print coordenadas[1].z

# faltaria calcular perfil logaritmico + potencia 
