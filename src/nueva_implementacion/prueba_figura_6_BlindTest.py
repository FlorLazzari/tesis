# coding=utf-8
from __future__ import division
import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
import itertools

from Gaussiana import Gaussiana
from Jensen import Jensen
from Frandsen import Frandsen
from Larsen import Larsen
from Parque_de_turbinas import Parque_de_turbinas
from Turbina_BlindTest import Turbina_BlindTest
from Coord import Coord
from Estela import Estela
from U_inf import U_inf
from calcular_u_en_coord import calcular_u_en_coord

"""
Tenemos los datos del BlindTest del parametro U para distintas distancias.
Tenemos corridas de OpenFOAM para ese mismo caso (las corrio Gonza hace bastante)
Tenemos los modelos reducidos: Gaussiana, Frandsen, Jensen, Larsen.

A continuacion se grafica comparacion de BlindTest, OpenFOAM y modelos reducidos
en un grafico de curva a la altura del hub para una turbina en: x = {1, 3, 5} D
"""

################################################################################
# aca tengo las mediciones del BlindTest

gaussiana = Gaussiana()

z_mast = 0.817

u_inf = U_inf()
u_inf.coord_mast = 10 # es parametro del BlindTest
u_inf.perfil = 'cte'   # por ser un tunel de viento
N = 300

turbina_0 = Turbina_BlindTest(Coord(np.array([0,0,0.817])))
D = turbina_0.d_0

# z_0 de la superficie
z_0 = 0 #?????
parque_de_turbinas = Parque_de_turbinas([turbina_0], z_0, z_mast)

# The turbine is located in a wind tunnel with dimensions 2.70 m wide, 1.80 m high and 11.15 m long.
#desde el inicio del tunel hasta la turbina 4.05m

x = np.linspace(0, 11.15-4.05, 200)
y_0 = 0
z = np.linspace(0, 1.8, 20)

X, Z = np.meshgrid(x, z)

data_prueba = np.zeros([len(z), len(x)])

import time

tiempo_procesamiento = []
tic = time.clock()
for i in range(len(x)):
    for j in range(len(z)):
        coord = Coord(np.array([x[i], y_0, z[j]]))
        # if coord.z != 0:
        tic = time.clock()
        data_prueba[j,i] = (calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas, u_inf, N))/u_inf.coord_mast
        toc = time.clock()
        # print ('data_prueba[i,j]', i, j, data_prueba[i,j])
        tiempo_procesamiento = np.append(tiempo_procesamiento, toc - tic)
print 'len(tiempo_procesamiento) = ',len(tiempo_procesamiento)
print 'np.mean(tiempo_procesamiento) = ', np.mean(tiempo_procesamiento)
print 'np.std(tiempo_procesamiento) = ', np.std(tiempo_procesamiento)

# contornos = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5]

contornos = np.linspace(0.5, 1.1, 15)

plt.contour(X,Z,data_prueba, contornos, linewidths=0.5, colors='k')
plt.contourf(X,Z,data_prueba, contornos, cmap=plt.cm.jet)
# plt.colorbar(ticks=[1, 1.5, 2, 2.5])
plt.colorbar()
ax = plt.gca()
ax.set_xticks([0, 4*(turbina_0.d_0), 8*(turbina_0.d_0), 12*(turbina_0.d_0), 16*(turbina_0.d_0), 20*(turbina_0.d_0)])
ax.set_yticks([0, 1*(turbina_0.d_0), 2*(turbina_0.d_0)])
ax.set_xlim([0, 11.15-4.05])
ax.set_ylim([0, 1.8])
plt.show()
