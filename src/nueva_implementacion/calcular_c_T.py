from __future__ import division
# coding=utf-8

from Modelo_2 import Modelo
import numpy as np
from numpy import exp
from Case_2 import Case
from integrar_disco_monte_carlo import integrar_disco_monte_carlo
# rho = densidad del aire
# At sea level and at 15 °C air has a density of approximately 1.225 kg/m3
rho = 1.225

def calcular_c_T(modelo,d_0,x,y,z,U):
    U_mean = np.mean()  # saldra de calcular el U dependiendo del modelo y la distribucion de turbinas
    # U_mean debe ser un valor entero, por lo tanto lo redondeo
    c_T_tab = tabla[round(U_mean,0)]
    n = # como estimo el orden de n?
    f = # saldra del modelo
    T = integrar_disco_monte_carlo(n,f,d_0)
    c_T_mean = T / (0.5 * rho * (U_mean)**2 * (pi*(d_0/2)**2) )
