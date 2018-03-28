from __future__ import division
import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
import itertools
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
Tenemos dos turbinas alineadas separadas por 3D en x
A continuacion se grafica:
    1) El deficit a la altura del hub para dos turbinas alineadas a 7D por
    atras de la primera (4D del segundo) usando CFD (OpenFOAM).
    2) El deficit de las dos turbinas trabajando independientemente (a 7D de
    la primera turbina y a 4D de la segunda turbina)
    3) El deficit generado por ambas (a 7D de la primera turbina) utilizando
    distintos metodos de superposicion de estelas

Tenemos los datos del BlindTest2 del parametro U para distintas distancias:
x = {4, 5.5, 7} D (downstream distances from T1)


Tenemos corridas de OpenFOAM para ese mismo caso (las corrio Gonza hace bastante)
Trabajamos unicamente con el modelo reducido: Gaussiana.

A continuacion se grafica comparacion de BlindTest, OpenFOAM y modelos reducidos
en un grafico de curva a la altura del hub para una turbina en las tres distancias
mencionadas

"""

################################################################################
# aca tengo las mediciones del BlindTest

y_norm_med = {'1': np.array([]),
'3': np.array([]),
'5': np.array([])}

deficit_x_med = {'1': np.array([]),
'3': np.array([]),
'5': np.array([])}

gaussiana = Gaussiana()

u_inf = U_inf()
u_inf.coord_hub = 10 # es parametro del BlindTest
u_inf.perfil = 'cte'   # por ser un tunel de viento
N = 100

turbina_0 = Turbina_BlindTest(Coord(np.array([0,-0.2, 0.817])))
D = turbina_0.d_0
turbina_1 = Turbina_BlindTest(Coord(np.array([3*D,0.2,0.817])))

# z_0 de la superficie
z_0 = 0.1 #?????
parque_de_turbinas = Parque_de_turbinas([turbina_0, turbina_1], z_0)

x_array = [4, 5.5, 7]
y = np.linspace(-1.5*D, 1.5*D, 500)
y_norm = y/D
z_o = turbina_0.coord.z

parque_de_turbinas_primera_indep = Parque_de_turbinas([turbina_0], z_0)
parque_de_turbinas_segunda_indep = Parque_de_turbinas([turbina_1], z_0)

metodo_array = ['linear', 'rss', 'largest']

data_prueba = np.zeros(len(y))

for distancia in x_array:
    plt.figure()
    plt.title('x = {}D'.format(distancia))
    x_o = distancia * D


    for i in range(len(y)):
        coord = Coord(np.array([x_o, y[i], z_o]))
        data_prueba[i] = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas_primera_indep, u_inf, N)
    plt.plot(y_norm, data_prueba/u_inf.coord_hub, 'x',label='Single rotor T1')

    for i in range(len(y)):
        coord = Coord(np.array([x_o, y[i], z_o]))
        data_prueba[i] = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas_segunda_indep, u_inf, N)
    plt.plot(y_norm, data_prueba/u_inf.coord_hub, 'x',label='Single rotor T2')


    for metodo_superposicion in metodo_array:

        for i in range(len(y)):
            coord = Coord(np.array([x_o, y[i], z_o]))
            data_prueba[i] = calcular_u_en_coord(gaussiana, metodo_superposicion, coord, parque_de_turbinas, u_inf, N)
        plt.plot(y_norm, data_prueba/u_inf.coord_hub, label= 'Metodo Superposicion ({})'.format(metodo_superposicion))

    # comparo con las mediciocones

    # todavia no las tengo
    # plt.plot(y_norm_med["{}".format(distancia)], deficit_x_med["{}".format(distancia)],'x',label='Mediciones')

    # comparo con OpenFOAM

    # todavia no las tengo
    # datos = np.loadtxt("XD{}.csv".format(distancia), delimiter = ',', skiprows=1)
    #
    # largo = datos.shape[0]
    # ancho =  datos.shape[1]
    #
    # u_OpenFOAM = np.zeros((largo))
    # y_norm_OpenFOAM = np.zeros((largo))
    #
    #
    # for i in range(largo):
    #     y_norm_OpenFOAM[i] = datos[i, 8]/D
    #     u_OpenFOAM[i] = datos[i, 4]
    #
    # plt.plot(y_norm_OpenFOAM - np.mean(y_norm_OpenFOAM), 1 - u_OpenFOAM/u_inf.coord_hub, label='OpenFOAM')

    plt.xlabel('y/D')
    plt.ylabel('U/U_{ref}')
    plt.legend()
    plt.grid()
    plt.show()
