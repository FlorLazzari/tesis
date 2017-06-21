# coding=utf-8

import numpy as np

from Case import Case
from Coordenadas import Coordenadas
from Coordenadas_Norm import Coordenadas_Norm
from Jensen import Jensen
from Figura import Figura
from math import log
from indexar import indexar

################################################################################

from case_blind_test import case, coordenadas

# constantes que utiliza el modelo:

jensen = Jensen(case)

c_T = 0.91 # lo calcule haciendo una regresion lineal con los dos puntos
           # se que no es exactamente lineal (se ve del grafico),
           # pero en ese intervalo se aproxima muy bien por una lineal

jensen.play(coordenadas,c_T)
deficit_dividido_U_inf = jensen.deficit_dividido_U_inf

print deficit_dividido_U_inf

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
coordenadas_norm = coordenadas.normalizar_hub(case)     # por que esto no funciona?!
print type(coordenadas)                                 # esto esta bien
print coordenadas_norm                                  # aca se ve que no funciona
print type(case)                                        # esto esta bien

indice_x_d_1 = indexar(coordenadas_norm.x_n, 1)
indice_z_h = indexar(coordenadas_norm.z_n, case.z_h)

y_Jensen = coordenadas.y_n
deficit_dividido_U_inf_Jensen = deficit_dividido_U_inf[indice_x_d_1,:,indice_z_h]


print deficit_dividido_U_inf_Jensen
print deficit_dividido_U_inf


# problema: no se por que deficit_dividido_U_inf_Gaussiana es una lista de puros nan's
