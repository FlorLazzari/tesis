from __future__ import division
# coding=utf-8

from Modelo_2 import Modelo
import numpy as np
from numpy import exp
from Case_2 import Case
from integrar_disco_monte_carlo import integrar_disco_monte_carlo

# coord_turbina = {0: np.array([x_0, y_0, z_0])}     ese np array son las coord
# debo numerarlas de izquierda a derecha sino todo el script no tiene sentido
# coord_selec = np.array([x_0, y_0, z_0])     ese np array son las coord

# turbina = {}



def calcular_U_en_pto(modelo, U_inf, coord_turbina, n, coord_selec):

    U_coord_selec = U_inf

    for i in range(n):
        if (coord_selec[0] <= coord_turbina[i][0]):
            U_coord_selec = U_coord_selec + 0
        else:
            pass
    #
    #                                                             # inicializo las turbinas a la izquierda
    #         turbina[i] = Turbina(d_0, coord_turbina)                            # coord deben ser no normalizadas (np.array)
    #         turbina[i].calcular_c_T(c_T_table, modelo, U_disco)         # si es la primer turbina => U_disco = U_inf
    #         estela[i] = Estela(turbina[i], modelo)                      # la turbina le pasa el c_T
    #         deficit_dividido_U_inf[i] = estela[i].calcular_en_coord_selec(coord_selec)   # es el deficit generado por la estela i en la coord_selec
    # suma_deficit = np.sum(deficit_dividido_U_inf)                       # en este caso lo estoy sumando a lo bruto, en el futuro deberia haber algo de la forma:
    #                                                                     # suma_deficit = suma(deficit_dividido_U_inf)

    return U_coord_selec
