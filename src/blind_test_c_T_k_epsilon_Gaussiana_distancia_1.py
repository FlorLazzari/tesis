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


# el c_T lo saco de los datos medidos, yo no lo voy a calcular, no?
# calculo c_T:
TSR_1 = 5.74
c_T_1 = 0.885

TSR_2 = 6.164
c_T_2 = 0.921

c_T = 0.91 # lo calcule haciendo una regresion lineal con los dos puntos
           # se que no es exactamente lineal (se ve del grafico),
           # pero en ese intervalo se aproxima muy bien por una lineal

betha = 0.5 * ((1 + (1 - c_T)**0.5 ) / ((1 - c_T)**0.5 ))

epsilon = 0.2 * (betha)**0.5  # esta correccion sale de la pagina 5 del paper

print "epsilon:",epsilon

print "epsilon calculado con case 1 =  0.268855463528"

print "espilon de la regrecion lineal = 0.219"



# de la galera, lo saque a mano del fit:
k_estrella = 0.03

gaussiana = Gaussiana(case,k_estrella,epsilon)

# corro el modelo:


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

# busco indice x/d == 1:
coordenadas.normalizar(case)


from indexar import indexar

indice_x_d_1 = indexar(coordenadas.x_n, 1)
indice_z_h = indexar(coordenadas.z,case.z_h)


print "indice_x_d_1",indice_x_d_1
print "coordenadas.x_n",coordenadas.x_n
print "case.z_h",case.z_h
print "indice_z_h",indice_z_h
print "coordenadas.z",coordenadas.z


y_Gaussiana = coordenadas.y_n
deficit_dividido_U_inf_Gaussiana = deficit_dividido_U_inf[indice_x_d_1,:,indice_z_h]


print "deficit_dividido_U_inf",deficit_dividido_U_inf
print "deficit_dividido_U_inf_Gaussiana",deficit_dividido_U_inf_Gaussiana


# problema: no se por que deficit_dividido_U_inf_Gaussiana es una lista de puros nan's
