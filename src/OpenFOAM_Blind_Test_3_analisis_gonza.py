# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from Figura_Scatter import Figura_Scatter
from indexar import indexar

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
coordenada_x = np.zeros((largo))
coordenada_y = np.zeros((largo))
coordenada_z = np.zeros((largo))

distancia = {}

for j in range(1,8):
    for i in range(largo):
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
    distancia[j] = {'U_x': U_x,
                    'U_y': U_y,
                    'U_z': U_z,
                    'coordenada_x': coordenada_x,
                    'coordenada_y': coordenada_y,
                    'coordenada_z': coordenada_z}


U = np.zeros((largo))
deficit_dividido_U_inf_OpenFOAM = np.zeros((largo))
# calculo U:
U[:] = [((U_x[i])**2 + (U_y[i])**2 + (U_z[i])**2)**0.5 for i in range(largo)]

# calculo el deficit:
U_inf = 10
deficit_dividido_U_inf_OpenFOAM[:] = [1 - (U[i]/U_inf) for i in range(largo)]

# busco el indice de coordenada_x donde "x=1" por primera vez en el vector
indices_x_1 = indexar(coordenada_x, 1)

# grafico la coordenada x para tener una idea de la forma que tiene
x_y = {"x_1" : np.arange(largo), "y_1" : coordenada_x}
nombre = "y/d vs deficit_dividido_U_inf x/d=1"
xLabel = r'$numero$'
yLabel = r'$ coordenada x$'

figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()
