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
Tenemos los datos del BlindTest del parametro U para distintas distancias.
Tenemos corridas de OpenFOAM para ese mismo caso (las corrio Gonza hace bastante)
Tenemos los modelos reducidos: Gaussiana, Frandsen, Jensen, Larsen.

A continuacion se grafica comparacion de BlindTest, OpenFOAM y modelos reducidos
en un grafico de curva a la altura del hub para una turbina en: x = {1, 3, 5} D
"""

################################################################################
# aca tengo las mediciones del BlindTest

y_norm_med = {'1': np.array([-1.22    , -1.11111 , -1.      , -0.88889 , -0.77778 , -0.666665,
       -0.62222 , -0.6     , -0.58889 , -0.57778 , -0.57222 , -0.566665,
       -0.56111 , -0.555555, -0.55    , -0.544445, -0.53889 , -0.533335,
       -0.52222 , -0.51111 , -0.5     , -0.466665, -0.433335, -0.4     ,
       -0.366665, -0.333335, -0.3     , -0.266665, -0.233335, -0.2     ,
       -0.166665, -0.133335, -0.11111 , -0.08889 , -0.066665, -0.044445,
       -0.02222 ,  0.      ,  0.02222 ,  0.044445,  0.066665,  0.08889 ,
        0.11111 ,  0.11111 ,  0.133335,  0.133335,  0.166665,  0.166665,
        0.2     ,  0.233335,  0.266665,  0.3     ,  0.333335,  0.366665,
        0.4     ,  0.433335,  0.466665,  0.5     ,  0.51111 ,  0.52222 ,
        0.533335,  0.53889 ,  0.544445,  0.55    ,  0.555555,  0.56111 ,
        0.566665,  0.57222 ,  0.57778 ,  0.58889 ,  0.6     ,  0.62222 ,
        0.666665,  0.77778 ,  0.88889 ,  1.      ,  1.11111 ]),
'3': np.array([-1.22222222, -1.11111111, -1.        , -0.88888889, -0.77777778,
       -0.72222222, -0.66666667, -0.64444444, -0.62222222, -0.6       ,
       -0.57777778, -0.55555556, -0.53333333, -0.51111111, -0.48888889,
       -0.46666667, -0.44444444, -0.41111111, -0.37777778, -0.34444444,
       -0.31111111, -0.27777778, -0.24444444, -0.21111111, -0.17777778,
       -0.14444444, -0.11111111, -0.07777778, -0.04444444, -0.02222222,
        0.        ,  0.02222222,  0.04444444,  0.07777778,  0.11111111,
        0.14444444,  0.17777778,  1.22222222,  1.11111111,  1.        ,
        0.88888889,  0.77777778,  0.72222222,  0.66666667,  0.64444444,
        0.62222222,  0.6       ,  0.57777778,  0.55555556,  0.53333333,
        0.51111111,  0.48888889,  0.46666667,  0.44444444,  0.41111111,
        0.37777778,  0.34444444,  0.31111111,  0.27777778,  0.24444444,
        0.21111111,  0.17777778,  0.14444444,  0.11111111]),
'5': np.array([-1.22222222, -1.11111111, -1.        , -0.88888889, -0.84444444,
       -0.8       , -0.75555556, -0.71111111, -0.66666667, -0.62222222,
       -0.57777778, -0.53333333, -0.48888889, -0.44444444, -0.4       ,
       -0.35555556, -0.31111111, -0.26666667, -0.22222222, -0.17777778,
       -0.13333333, -0.08888889, -0.04444444,  0.        ,  0.04444444,
        0.08888889,  0.13333333,  0.17777778, -0.17777778,  1.22222222,
        1.11111111,  1.        ,  0.88888889,  0.84444444,  0.8       ,
        0.75555556,  0.71111111,  0.66666667,  0.62222222,  0.57777778,
        0.53333333,  0.48888889,  0.44444444,  0.4       ,  0.35555556,
        0.31111111,  0.26666667,  0.22222222,  0.17777778,  0.13333333,
        0.08888889,  0.04444444])
}


deficit_x_med = {'1': np.array([-0.12,-0.1167,-0.111362,-0.112161,-0.110806,-0.11834,-0.127145,-0.1325,-0.140023,-0.140612,-0.108756,-0.045743,0.058173,0.162247,0.260128,0.321452,0.358434,0.378412,0.39601,0.406613,0.414042,0.425711,0.425953,0.414195,0.408059,0.395966,0.376666,0.373122,0.392333,0.431709,0.465621,0.466639,0.445204,0.409643,0.361389,0.312706,0.271825,0.256527,0.250834,0.220575,0.196648,0.217383,0.246492,0.266215,0.269438,0.324422,0.327677,0.352927,0.367211,0.389466,0.405311,0.418325,0.426744,0.424173,0.430718,0.433471,0.426555,0.418596,0.408934,0.392704,0.378186,0.352408,0.310289,0.246683,0.171726,0.091271,0.003167,-0.084245,-0.154532,-0.151967,-0.13927,-0.13387,-0.129913,-0.125842,-0.123664,-0.130612,-0.140644]),
'3': np.array([-0.13,-0.120832,-0.1121,-0.11097,-0.105897,-0.105364,-0.108564,-0.104881,-0.09281900,-0.062463,-0.012375,0.040826,0.095571,0.152607,0.206715,0.268767,0.314955,0.373356,0.406477,0.423108,0.424607,0.417272,0.403287,0.376692,0.347769,0.325932,0.306947,0.304024,0.308578,0.318688,0.333908,0.356701,0.380317,0.40338,0.430249,0.42784,0.350081,-0.163245,-0.152989,-0.154996,-0.150537,-0.146355,-0.145065,-0.122388,-0.086403,-0.026253,0.057092,0.141113,0.219945,0.288574,0.34605,0.383469,0.410948,0.426934,0.437725,0.428667,0.414188,0.400707,0.387266,0.380222,0.385473,0.403194,0.414382,0.411642]),
'5': np.array([-0.12,-0.109608,-0.100314,-0.097556,-0.093393,-0.087946,-0.077435,-0.058947,-0.03217900,0.005478,0.040037,0.081251,0.132376,0.173214,0.226227,0.263731,0.299944,0.331094,0.353178,0.36502,0.372183,0.373909,0.378681,0.384479,0.396525,0.419994,0.438193,0.448125,0.363603,-0.133648,-0.122078,-0.111003,-0.111549,-0.107405,-0.096905,-0.075745,-0.035703,0.029659,0.08888,0.156184,0.21735,0.282054,0.332142,0.368158,0.40034,0.420912,0.436859,0.441821,0.444841,0.435482,0.415075,0.394798])}

gaussiana = Gaussiana()
jensen = Jensen()
frandsen = Frandsen()
larsen = Larsen()
modelos = [gaussiana, jensen, frandsen, larsen]


u_inf = U_inf()
u_inf.coord_hub = 10 # es parametro del BlindTest
u_inf.perfil = 'cte'   # por ser un tunel de viento
N = 100

turbina_0 = Turbina_BlindTest(Coord(np.array([0,0,0.817])))
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

        plt.plot(y_norm, 1-data_prueba/u_inf.coord_hub, label= 'Modelo Reducido ({})'.format(type(modelo).__name__))

    # comparo con las mediciocones

    plt.plot(y_norm_med["{}".format(distancia)], deficit_x_med["{}".format(distancia)],'x',label='Mediciones')

    # comparo con OpenFOAM

    datos = np.loadtxt("BT1_{}.csv".format(distancia), delimiter = ',', skiprows=1)

    largo = datos.shape[0]
    ancho =  datos.shape[1]

    u_OpenFOAM = np.zeros((largo))
    y_norm_OpenFOAM = np.zeros((largo))


    for i in range(largo):
        y_norm_OpenFOAM[i] = datos[i, 0]/D
        u_OpenFOAM[i] = datos[i, 1]

    plt.plot(y_norm_OpenFOAM - np.mean(y_norm_OpenFOAM), 1 - u_OpenFOAM/u_inf.coord_hub, label='OpenFOAM')
    plt.xlabel('y/D')
    plt.ylabel('1 - U/U_{ref}')
    plt.legend()
    plt.grid()
    plt.show()
