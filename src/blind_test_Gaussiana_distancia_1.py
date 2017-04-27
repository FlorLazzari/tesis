# coding=utf-8

import numpy as np

from Case import Case
from Coordenadas import Coordenadas
from Coordenadas_Norm import Coordenadas_Norm
from Gaussiana import Gaussiana
from Figura import Figura
from math import log

################################################################################

from case_blind_test import case, coordenadas


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

# trucheo:
# k_estrella = 0.023
# epsilon = 0.219

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
# como para que todo sea comparable (voy a tener que cambiar measurements para que
# quede como hize todo el resto, lo hago despues, ahora veo si la forma tiene
# algo de sentido)


# corte para z = z_hub, vario en y

# como hago para que indice x/d == 1? primero lo voy a hacer a mano:
coordenadas.normalizar(case)
# print(coordenadas.x_n)

# a mano encuentro:

# indice_x_d_1 = 19
# indice_z_h = 17

# como python indexa desde 0 voy a restar uno a estos indices encontrados

indice_x_d_1 = 18
indice_z_h = 16

# print(coordenadas.z)
# print(case.z_h)

y_Gaussiana = coordenadas.y_n
deficit_dividido_U_inf_Gaussiana = deficit_dividido_U_inf[indice_x_d_1,:,indice_z_h]


# print deficit_dividido_U_inf_Gaussiana
# print deficit_dividido_U_inf


# problema: no se por que deficit_dividido_U_inf_Gaussiana es una lista de puros nan's
