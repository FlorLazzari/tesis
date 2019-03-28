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
from Turbina_BlindTest_3_TSR4_75 import Turbina_BlindTest_3_TSR4_75
from Turbina_BlindTest_3_TSR6 import Turbina_BlindTest_3_TSR6
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

Tenemos los datos del BlindTest3 del parametro U para distintas distancias:
x = {4, 5.5, 7} D (downstream distances from T1)


Tenemos corridas de OpenFOAM para ese mismo caso (las corrio Gonza hace bastante)
Trabajamos unicamente con el modelo reducido: Gaussiana.

A continuacion se grafica comparacion de BlindTest, OpenFOAM y modelos reducidos
en un grafico de curva a la altura del hub para una turbina en las tres distancias
mencionadas

"""

################################################################################
# aca tengo las mediciones del BlindTest

# veo problemas en el OpenFOAM, saco el 0.5 * ?

y_norm_med = {'4': 0.5 * np.array([0, 0.0444444444444444, 0.0888888888888889, 0.133333333333333, 0.177777777777778, 0.222222222222222, 0.333333333333333, 0.444444444444444, 0.555555555555556, 0.666666666666667, 0.711111111111111, 0.755555555555556, 0.8, 0.844444444444444, 0.888888888888889, 0.933333333333333, 0.977777777777778, 1.02222222222222, 1.06666666666667, 1.11111111111111, 1.15555555555556, 1.2, 1.24444444444444, 1.28888888888889, 1.33333333333333, 1.37777777777778, 1.42222222222222, 1.46666666666667, 1.51111111111111, 1.55555555555556, 1.66666666666667, 1.77777777777778, 1.88888888888889, 2, 2.11111111111111, 2.22222222222222, 0, -0.0444444444444444, -0.0888888888888889, -0.133333333333333, -0.177777777777778, -0.222222222222222, -0.333333333333333, -0.444444444444444, -0.555555555555556, -0.666666666666667, -0.711111111111111, -0.755555555555556, -0.8, -0.844444444444444, -0.888888888888889, -0.933333333333333, -0.977777777777778, -1.02222222222222, -1.06666666666667, -1.11111111111111, -1.15555555555556, -1.2, -1.24444444444444, -1.28888888888889, -1.33333333333333, -1.37777777777778, -1.42222222222222, -1.46666666666667, -1.51111111111111, -1.55555555555556, -1.6, -1.64444444444444, -1.68888888888889, -1.73333333333333, -1.77777777777778, -1.82222222222222, -1.86666666666667, -1.91111111111111, -1.95555555555556, -2, -2.11111111111111, -2.22222222222222, -2.33333333333333, -2.44444444444444, -2.55555555555556, -2.66666666666667, -2.77777777777778, -2.88888888888889, -3, -3.11111111111111]),
'6': 0.5 * np.array([0, -0.0444444444444444, -0.0888888888888889, -0.133333333333333, -0.177777777777778, -0.222222222222222, -0.333333333333333, -0.444444444444444, -0.555555555555556, -0.666666666666667, -0.711111111111111, -0.755555555555556, -0.8, -0.844444444444444, -0.888888888888889, -0.933333333333333, -0.977777777777778, -1.02222222222222, -1.06666666666667, -1.11111111111111, -1.15555555555556, -1.2, -1.24444444444444, -1.28888888888889, -1.33333333333333, -1.37777777777778, -1.42222222222222, -1.46666666666667, -1.51111111111111, -1.55555555555556, -1.6, -1.64444444444444, -1.68888888888889, -1.73333333333333, -1.77777777777778, -1.82222222222222, -1.86666666666667, -1.91111111111111, -1.95555555555556, -2, -2.11111111111111, -2.22222222222222, -2.33333333333333, -2.44444444444444, -2.55555555555556, -2.66666666666667, -2.77777777777778, -2.88888888888889, -3, -3.11111111111111, 0, 0.0444444444444444, 0.0888888888888889, 0.133333333333333, 0.177777777777778, 0.222222222222222, 0.333333333333333, 0.444444444444444, 0.555555555555556, 0.666666666666667, 0.711111111111111, 0.755555555555556, 0.8, 0.844444444444444, 0.888888888888889, 0.933333333333333, 0.977777777777778, 1.02222222222222, 1.06666666666667, 1.11111111111111, 1.15555555555556, 1.2, 1.24444444444444, 1.28888888888889, 1.33333333333333, 1.37777777777778, 1.42222222222222, 1.46666666666667, 1.51111111111111, 1.55555555555556, 1.66666666666667, 1.77777777777778, 1.88888888888889, 2, 2.11111111111111, 2.22222222222222]),
}

deficit_x_med = {'4': 1 + (-1) * np.array([0.580333, 0.571525, 0.563397, 0.564181, 0.568632, 0.570379, 0.578995, 0.662972, 0.791936, 0.853034, 0.85987, 0.860993, 0.856781, 0.857568, 0.860608, 0.870789, 0.878695, 0.913695, 1.145415, 1.236998, 1.242551, 1.242745, 1.242501, 1.24141, 1.242153, 1.242239, 1.242056, 1.240867, 1.239801, 1.239327, 1.242038, 1.246448, 1.253377, 1.258026, 1.263434, 1.27374, 0.566378, 0.570963, 0.567699, 0.558572, 0.543311, 0.527209, 0.500394, 0.481458, 0.482736, 0.492241, 0.492794, 0.499473, 0.510256, 0.541101, 0.594869, 0.667946, 0.730228, 0.779877, 0.801183, 0.807486, 0.80872, 0.806513, 0.803982, 0.804564, 0.804393, 0.803256, 0.803394, 0.807065, 0.815011, 0.81488, 0.814033, 0.813412, 0.812182, 0.812231, 0.813798, 0.818637, 0.825386, 0.831526, 0.851388, 0.873005, 0.969155, 1.081713, 1.16383, 1.203899, 1.215812, 1.221226, 1.223443, 1.220631, 1.224996, 1.24656]),
'6': 1 + (-1) * np.array([0.574055, 0.593999, 0.612613, 0.630159, 0.648347, 0.656815, 0.674499, 0.678441, 0.687727, 0.699904, 0.701475, 0.706979, 0.710516, 0.713499, 0.719744, 0.723383, 0.7227, 0.727147, 0.726965, 0.73138, 0.73574, 0.730879, 0.730833, 0.733508, 0.734596, 0.734433, 0.735453, 0.740267, 0.743502, 0.758544, 0.7689, 0.776372, 0.796467, 0.808811, 0.838467, 0.854406, 0.872164, 0.894335, 0.905048, 0.931568, 0.975708, 1.027915, 1.075306, 1.126054, 1.164076, 1.193792, 1.211562, 1.217105, 1.223955, 1.234717, 0.595733, 0.578779, 0.563515, 0.546276, 0.537628, 0.539686, 0.576056, 0.643524, 0.713429, 0.785415, 0.807212, 0.828479, 0.857151, 0.887704, 0.925191, 0.954624, 0.976683, 0.999201, 1.034058, 1.078576, 1.149531, 1.208574, 1.233542, 1.238625, 1.23913, 1.240003, 1.23995, 1.24025, 1.239879, 1.238967, 1.239442, 1.246355, 1.252632, 1.257339, 1.261648, 1.270515])
}

gaussiana = Gaussiana()

u_inf = U_inf()
u_inf.coord_mast = 10 # es parametro del BlindTest
u_inf.perfil = 'cte'   # por ser un tunel de viento
N = 300

turbina_0 = Turbina_BlindTest_3_TSR6(Coord(np.array([0,-0.2, 0.817])))
D = 0.894
turbina_1 = Turbina_BlindTest_3_TSR4_75(Coord(np.array([3*D,0.2,0.817])))

# z_0 de la superficie
z_0 = 0.1 #?????
z_mast = 0.817
parque_de_turbinas = Parque_de_turbinas([turbina_0, turbina_1], z_0, z_mast)

x_array = [4, 6]
y = np.linspace(-1.5*D, 1.5*D, 500)
y_norm = y/D
z_o = turbina_0.coord.z

parque_de_turbinas_primera_indep = Parque_de_turbinas([turbina_0], z_0, z_mast)
parque_de_turbinas_segunda_indep = Parque_de_turbinas([turbina_1], z_0, z_mast)

metodo_array = ['linear', 'rss', 'largest']
metodo_label = {'linear': 'Lineal', 'rss': u'Cuadrática', 'largest':'Dominante'}

data_prueba = np.zeros(len(y))

for distancia in x_array:
    plt.figure(figsize=(11,11))
    # plt.title('x = {}D'.format(distancia))
    x_o = distancia * D


    for i in range(len(y)):
        coord = Coord(np.array([x_o, y[i], z_o]))
        data_prueba[i] = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas_primera_indep, u_inf, N)
    # plt.plot(y_norm, 1-data_prueba/u_inf.coord_mast, '.',label='Single rotor T1', linewidth=3)

    for i in range(len(y)):
        coord = Coord(np.array([x_o, y[i], z_o]))
        data_prueba[i] = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas_segunda_indep, u_inf, N)
    # plt.plot(y_norm, 1-data_prueba/u_inf.coord_mast, '.',label='Single rotor T2', linewidth=3)


    for metodo_superposicion in metodo_array:

        for i in range(len(y)):
            coord = Coord(np.array([x_o, y[i], z_o]))
            data_prueba[i] = calcular_u_en_coord(gaussiana, metodo_superposicion, coord, parque_de_turbinas, u_inf, N)
        plt.plot(y_norm, 1-data_prueba/u_inf.coord_mast, label= u'{}'.format(metodo_label[metodo_superposicion]), linewidth=3)

    # comparo con las mediciocones

    # todavia no las tengo
    plt.plot(y_norm_med["{}".format(distancia)]-np.mean(y_norm_med["{}".format(distancia)]), deficit_x_med["{}".format(distancia)],'o',label='Mediciones', markersize=10)

    # comparo con OpenFOAM

    datos = np.loadtxt("BT3_{}.csv".format(distancia), delimiter = ',', skiprows=1)

    largo = datos.shape[0]
    ancho =  datos.shape[1]

    u_OpenFOAM = np.zeros((largo))
    y_norm_OpenFOAM = np.zeros((largo))


    for i in range(largo):
        y_norm_OpenFOAM[i] = datos[i, 0]/D
        u_OpenFOAM[i] = datos[i, 1]

    plt.plot(y_norm_OpenFOAM - np.mean(y_norm_OpenFOAM), 1 - u_OpenFOAM/u_inf.coord_mast, '--', label='OpenFOAM (CFD)', linewidth= 3)
    plt.xlabel(r'$y/d$', fontsize=30)
    plt.ylabel(r'$\Delta u/u_{\infty}$', fontsize=30)
    plt.legend(fontsize=20, loc= 'upper right')
    plt.xlim([-1.3,1.3])
    plt.ylim([-0.3, 1.4])
    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    plt.grid()
    plt.savefig('BlindTest3_{}.pdf'.format(int(distancia)))
