from __future__ import division
# coding=utf-8

import numpy as np
from Turbina_2 import Turbina
from Turbina_Vestas import Turbina_Vestas
from Gaussiana_2 import Gaussiana

d_0 = 60



turbina_0 = Turbina_Marca(np.array([0,0,100]))
turbina_1 = Turbina_Marca(np.array([20,0,100]))


U_inf = 10
coord_turbina = {0: turbina_0.coord_selec, 1: turbina_1.coord_selec }
n = 2



k_estrella = 0.023
epsilon = 0.219
gaussiana = Gaussiana(k_estrella, epsilon)

turbina_0.calcular_c_T(gaussiana, U_inf, coord_turbina, n)
