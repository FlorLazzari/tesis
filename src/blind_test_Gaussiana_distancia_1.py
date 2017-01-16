# coding=utf-8

import numpy as np

from Case import Case
from Coordenadas import Coordenadas
from Coordenadas_Norm import Coordenadas_Norm
from Gaussiana import Gaussiana
from Figura import Figura
from math import log

################################################################################

# test section = 12 m x 2 m x 3 m
# rotor diameter = 0.894 m
# centre of the rotor is located at z = 0.817 m
#
# model was designed to operate at 10 m/s with a TSR = 6


# coordenadas:

length = 12
width = 3
height = 2

x = np.arange(0,length,0.05)
y = np.arange(-width,width,0.05)
z = np.arange(0,height,0.05)

# inicializo caso, coordenadas, modelo:

d_0 = 0.894    # diameter of the wind turbine
z_h = 0.817

# no tengo datos de esto:
U_hub = 0      # esto seria una U_ref??
C_T = 0
z_0 = 0
I_0 = 0

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

gaussiana = Gaussiana(case,k_estrella,epsilon)

# corro el modelo:

# el c_T lo saco de los datos medidos, yo no lo voy a calcular, no?
# calculo c_T:
TSR_1 = 5.74
c_T_1 = 0.885

TSR_2 = 6.164
c_T_2 = 0.921

c_T = 0.91 # lo calcule haciendo una regresion lineal con los dos puntos
           # se que no es exactamente lineal (se ve del grafico),
           # pero en ese intervalo se aproxima muy bien por una lineal



gaussiana.play_cart(coordenadas,c_T)

deficit_dividido_U_inf = gaussiana.deficit_dividido_U_inf

################################################################################

# x/d = 1

# voy a tener un problema:
# yo normalice todo como coordenada/d y el nuevo paper normaliza todo con
# coordenada/r por lo tanto voy a tener que usar una de las dos convensiones
# como para que todo sea comparable (voy a tener que cambiar measurements para
# quede como hize todo el resto, lo hago despues, ahora veo si la forma tiene
# algo de sentido)


# corte para z = z_hub, vario en y

# como hago para que indice x/d == 1? primero lo voy a hacer a mano:
coordenadas.normalizar(case)
# print(coordenadas.x_n)

# a mano encuentro:

indice_x_d_1 = 19
indice_z_h = 17

# print(coordenadas.z)
# print(case.z_h)

y_Gaussiana = coordenadas.y_n
deficit_dividido_U_inf_Gaussiana = deficit_dividido_U_inf[indice_x_d_1,:,indice_z_h]
