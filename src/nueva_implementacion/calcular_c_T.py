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


class Gaussiana(Modelo):

    def __init__(self, case, k_estrella, epsilon):
        super(Gaussiana, self).__init__(case)        # self.case = case
        self.k_estrella = k_estrella
        self.epsilon = epsilon

    def evalDeficitNorm(self, coord, c_T):
        # coord deben ser no normalizadas (np.array)
        sigma_n = self.k_estrella * (coord[0]/self.case.d_0) + self.epsilon
        c = 1 - (1-(c_T/(8*(sigma_n**2))))**(0.5)
        return c * exp(-((coord[1]/self.case.d_0)**2 + ((coord[2] - self.case.z_h)/self.case.d_0)**2) / (2 * (sigma_n**2)))



# x_0 = es el punto donde quiero calcular la potencia disponible
# U = es el viento a la salida de la turbina

def potenciar(d_0,x,y,z,U):
    # area = area sobre la cual quiero estudiar potencia disponible, area que barre el molino
    area = 3.14 * ((d_0/2)**2)
    coeficiente = 0.5 * rho * area
    for i in range (0,indice_radio_y):
        for j in range (0,indice_radio_z):
            potencia_disponible_parcial[i,j] = coeficiente * (U[indice_x_n_0,i,j])**3
            potencia_disponible = sum(sum(potencia_disponible_parcial))
    return potencia_disponible
