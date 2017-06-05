# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from Figura_Scatter import Figura_Scatter
from indexar import indexar
from fitear_gaussiana import fitear_gaussiana

# rotor diameter = 0.894 m
d_0 = 0.894

# viento en el infinito para el Blind Test
U_inf = 10

datos = {}
for i in range(1,8):
    datos[i] = np.loadtxt("XD{}.csv".format(i), delimiter = ',', skiprows=1)

# todos los datos tienen el mismo largo y ancho, tomo el de uno como ejemplo
largo = datos[1].shape[0]
ancho =  datos[1].shape[1]

# nut = np.zeros((largo))
# turbulencia = np.zeros((largo))
# presion = np.zeros((largo))
# epsilon = np.zeros((largo))
U_x = np.zeros((largo))
U_y = np.zeros((largo))
U_z = np.zeros((largo))
U = np.zeros((largo))
deficit_dividido_U_inf_OpenFOAM = np.zeros((largo))
coordenada_x = np.zeros((largo))
coordenada_y = np.zeros((largo))
coordenada_z = np.zeros((largo))

distancia = {}
sigma = np.zeros((8))
sigma_n = np.zeros((8))

# corto los datos para tirar el deficit de las paredes
largo_cortado = largo-5
comienzo_cortado = 5

for j in range(1,8):
    for i in range(comienzo_cortado, largo_cortado):
        # nut[i] = datos[j][i, 0]
        # turbulencia[i] = datos[j][i, 1]
        # presion[i] = datos[j][i, 2]
        # epsilon[i] = datos[j][i, 3]
        U_x[i] = datos[j][i, 4]
        U_y[i] = datos[j][i, 5]
        U_z[i] = datos[j][i, 6]
        coordenada_x[i] = datos[j][i, 9]
        coordenada_y[i] = datos[j][i, 10]
        coordenada_z[i] = datos[j][i, 11]
        # # calculo U:
        # U[i] = ((U_x[i])**2 + (U_y[i])**2 + (U_z[i])**2)**0.5
        # # calculo el deficit:
        # deficit_dividido_U_inf_OpenFOAM[i] = 1 - (U[i]/U_inf)
    distancia[j] = {'U_x': datos[j][comienzo_cortado:largo_cortado, 4],
                    'U_y': datos[j][comienzo_cortado:largo_cortado, 5],
                    'U_z': datos[j][comienzo_cortado:largo_cortado, 6],
                    'U': ((datos[j][comienzo_cortado:largo_cortado, 4])**2 + (datos[j][comienzo_cortado:largo_cortado, 5])**2 + (datos[j][comienzo_cortado:largo_cortado, 6])**2)**0.5,
                    'deficit_dividido_U_inf_OpenFOAM': (1 - (((datos[j][comienzo_cortado:largo_cortado, 4])**2 + (datos[j][comienzo_cortado:largo_cortado, 5])**2 + (datos[j][comienzo_cortado:largo_cortado, 6])**2)**0.5/U_inf)),
                    'coordenada_x': datos[j][comienzo_cortado:largo_cortado, 9],
                    'coordenada_y': datos[j][comienzo_cortado:largo_cortado, 10],
                    'coordenada_z': datos[j][comienzo_cortado:largo_cortado, 11]}
    sigma[j] = fitear_gaussiana(distancia[j]['coordenada_y'], distancia[j]['deficit_dividido_U_inf_OpenFOAM'])
    sigma_n[j] = sigma[j] / d_0

# # grafico las figuras para chequear que sean distintas
# x_y = { "x_1" : distancia[1]['coordenada_y'], "y_1" : distancia[1]['deficit_dividido_U_inf_OpenFOAM'],
#         "x_2" : distancia[4]['coordenada_y'], "y_2" : distancia[4]['deficit_dividido_U_inf_OpenFOAM'],
#         "x_3" : distancia[7]['coordenada_y'], "y_3" : distancia[7]['deficit_dividido_U_inf_OpenFOAM']}
# nombre = "y/d vs deficit_dividido_U_inf_OpenFOAM en x/d=1"
# xLabel = r'$y/d$'
# yLabel = r'$ U_y$'
# figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,3)
# figura_prueba.show()

# ################################################################################
# figura 4: sigma_n / x_n

x_y = { 'x_1': np.arange(8), 'y_1': sigma_n }
nombre = "figura_4"
xLabel = r'$x / d_{0}$'
yLabel = r'$\sigma / d_{0} $'
numero = 1

figura = Figura_Scatter(nombre,x_y,xLabel,yLabel,numero)
figura.show()
