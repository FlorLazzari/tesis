# coding=utf-8

import numpy as np

from Case import Case
from Coordenadas import Coordenadas
from Coordenadas_Norm import Coordenadas_Norm
from Gaussiana import Gaussiana
from Figura import Figura
from math import log

################################################################################
# coordenadas:

x_n = np.arange(0,2,0.05)
y_n = np.arange(0,2,0.05)
z_n = np.arange(0,2,0.05)

d_0 = 0.15

x = d_0 * x_n
y = d_0 * y_n
z = d_0 * z_n

# inicializo caso, coordenadas, modelo:

d_0 = 0.15
z_h = 0.125
U_hub = 2.2
C_T = 0.42
z_0 = 0.00003
I_0 = 0.07

case = Case(d_0,z_h,U_hub,C_T,z_0,I_0)
coordenadas = Coordenadas(x,y,z)

# para que los resultados sean comparables a los del paper uso los datos que dan en
# la introducción para k_estrella y epsilon (si uso lo del fit lineal de la figura 4
# el gráfico 3 queda cualquier cosa):
# k_estrella = 0.023
# epsilon = 0.219
# estos valores de k_estrella y epsilon los saqué del ajuste de la lineal del gráfico
# de sigmna_n vs x_n (figura 4)

# estos valores salen del calculo en la introduccion
k_estrella = 0.2
epsilon = 0.268855463528

modelo = Gaussiana(case,k_estrella,epsilon)

# corro el modelo:

c_T = 0.5

# no voy a graficar en funcion de "r" (que en realidad lo estoy estudiando como
# r == z), quiero que normalice con z_hub, entonces uso play_cart:
modelo.play_cart(coordenadas,c_T)

################################################################################
# figura 6: x_n vs z_n vs U

# primero voy a hacer x_n vs z_n vs deficit_dividido_U_inf

from Contour import Contour
from colapsar import colapsar

# colapso en la posición y = 0:
b = colapsar(modelo.deficit_dividido_U_inf,0)
a = b.transpose()

x_z_a = {'x_1': modelo.x_n, 'z_1': modelo.z_n, 'a_1': a}

nombre = "figura_6_deficit"
xLabel = r'$x / d_{0}$'
yLabel = r'$z / d_{0}$'

contour = Contour(nombre,x_z_a,xLabel,yLabel)
contour.show()

# figura 6_deficit del paper :
