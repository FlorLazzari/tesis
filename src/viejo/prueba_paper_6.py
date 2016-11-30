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
# # primero voy a hacer x_n vs z_n vs deficit_dividido_U_inf
#
# from Contour import Contour
# from colapsar import colapsar
#
# # colapso en la posición y = 0:
# b = colapsar(modelo.deficit_dividido_U_inf,0)
# a = b.transpose()
#
# x_z_a = {'x_1': modelo.x_n, 'z_1': modelo.z_n, 'a_1': a}
#
# nombre = "figura_6_deficit"
# xLabel = r'$x / d_{0}$'
# yLabel = r'$z / d_{0}$'
#
# contour = Contour(nombre,x_z_a,xLabel,yLabel)
# contour.show()
#
# # figura 6_deficit del paper : checked!

################################################################################
# figura 6: x_n vs z_n vs U


# U = U_inf * (1 - modelo.deficit_dividido_U_inf)


# no puedo hacer log(vector)

U_hub = case.U_hub
z_h = case.z_h
z_0 = case.z_0
z_0_vect = case.z_0 * np.ones((len(modelo.z_n)))

# for i in range (0,len(self.x_n)):
#     for j in range (0,len(self.y_n)):
#         for k in range (0,len(self.z_n)):
#             U_inf[i,j,k] = U_hub * ((log(modelo.z_n[k] / z_0)) / log(z_h / z_0)

U_inf = np.zeros((len(modelo.z_n)))
divi = np.zeros((len(modelo.z_n)))
num = np.zeros((len(modelo.z_n)))

denom = log(z_h / z_0) * np.ones((len(modelo.z_n)))
print(modelo.z)
print(z_0_vect)

U_inf[0] = 0

for k in range(1,len(modelo.z_n)):
    divi[k] = modelo.z[k] / z_0_vect[k]
    num[k] = log(divi[k])
    U_inf[k] = U_hub * ( num[k] / denom[k])

print(divi)
print(U_inf)
x_y = {'x_1': np.arange(0,len(modelo.z_n)), 'y_1': U_inf}

figura_prueba = Figura("hola",x_y,"hola","chau",1)
figura_prueba.show()
