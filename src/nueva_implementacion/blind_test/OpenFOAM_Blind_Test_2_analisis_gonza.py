# coding=utf-8

# descarto este metodo porque tengo pocos puntos con el mismo valor de x


import numpy as np
import matplotlib.pyplot as plt
from Figura_Scatter import Figura_Scatter
from indexar import indexar

datos = np.loadtxt("OpenFOAM_Blind_Test_2_gonza.csv", delimiter = ',', skiprows=1)

largo = datos.shape[0]
ancho =  datos.shape[1]

nut = np.zeros((largo))
turbulencia = np.zeros((largo))
presion = np.zeros((largo))
epsilon = np.zeros((largo))
U_x = np.zeros((largo))
U_y = np.zeros((largo))
U_z = np.zeros((largo))
coordenada_x = np.zeros((largo))
coordenada_y = np.zeros((largo))
coordenada_z = np.zeros((largo))

for i in range(largo):
    nut[i] = datos[i, 0]
    turbulencia[i] = datos[i, 1]
    presion[i] = datos[i, 2]
    epsilon[i] = datos[i, 3]
    U_x[i] = datos[i, 4]
    U_y[i] = datos[i, 5]
    U_z[i] = datos[i, 6]
    coordenada_x[i] = datos[i, 7]
    coordenada_y[i] = datos[i, 8]
    coordenada_z[i] = datos[i, 9]

U = np.zeros((largo))
deficit_dividido_U_inf_OpenFOAM = np.zeros((largo))
# calculo U:
U[:] = [((U_x[i])**2 + (U_y[i])**2 + (U_z[i])**2)**0.5 for i in range(largo)]

# calculo el deficit:
U_inf = 10
deficit_dividido_U_inf_OpenFOAM[:] = [1 - (U[i]/U_inf) for i in range(largo)]

# busco el indice de coordenada_x donde "x=1" por primera vez en el vector
indices_x_1 = indexar(coordenada_x, 1)
print

# grafico la coordenada x para tener una idea de la forma que tiene
x_y = {"x_1" : np.arange(largo), "y_1" : coordenada_x}
nombre = "y/d vs deficit_dividido_U_inf x/d=1"
xLabel = r'$numero$'
yLabel = r'$ coordenada x$'

figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()
