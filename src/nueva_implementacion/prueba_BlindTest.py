from __future__ import division
import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
# coding=utf-8

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

gaussiana = Gaussiana()
jensen = Jensen()
frandsen = Frandsen()
larsen = Larsen()
modelos = [gaussiana, jensen, frandsen]#, larsen]


u_inf = U_inf()
u_inf.coord_hub = 10 # es parametro del BlindTest
u_inf.perfil = 'cte'   # por ser un tunel de viento
N = 100

turbina_0 = Turbina_BlindTest(Coord(np.array([0,0,80]))) # chequear altura del hub
D = turbina_0.d_0

# z_0 de la superficie
z_0 = 0.1 #?????
parque_de_turbinas = Parque_de_turbinas([turbina_0], z_0)

x_array = [1, 3, 5]
y = np.linspace(-1.5*D, 1.5*D, 500)
y_norm = y/D
z_o = turbina_0.coord.z

for distancia in x_array:
    plt.figure()
    plt.title('x = {}D'.format(distancia))


    for modelo in modelos:

        x_o = distancia * D
        data_prueba = np.zeros(len(y))

        for i in range(len(y)):
            coord = Coord(np.array([x_o, y[i], z_o]))
            data_prueba[i] = calcular_u_en_coord(modelo, 'linear', coord, parque_de_turbinas, u_inf, N)

        plt.plot(y_norm, 1-data_prueba/u_inf.coord_hub, label= 'Modelo Reducido ({})'.format(modelo))

    # comparo con las mediciocones


    # comparo con OpenFOAM

    datos = np.loadtxt("XD{}.csv".format(distancia), delimiter = ',', skiprows=1)

    largo = datos.shape[0]
    ancho =  datos.shape[1]

    u_OpenFOAM = np.zeros((largo))
    y_norm_OpenFOAM = np.zeros((largo))


    for i in range(largo):
        y_norm_OpenFOAM[i] = datos[i, 8]/D
        u_OpenFOAM[i] = datos[i, 4]

    plt.plot(y_norm_OpenFOAM - np.mean(y_norm_OpenFOAM), 1 - u_OpenFOAM/u_inf.coord_hub, label='OpenFOAM')
    plt.xlabel('y/D')
    plt.ylabel('U')
    plt.legend()
    plt.show()
