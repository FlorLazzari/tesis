from __future__ import division
# coding=utf-8

from Modelo_2 import Modelo
import numpy as np
from numpy import exp
from Case_2 import Case
from Turbina import Turbina
# from cart2pol import cart2pol
# from Coordenadas import Coordenadas
# from Coordenadas_Norm import Coordenadas_Norm



class Gaussiana(Modelo):

    def __init__(self, case, turbina, k_estrella, epsilon):
        super(Gaussiana, self).__init__(case, turbina)        # self.case = case + self.turbina = turbina
        self.k_estrella = k_estrella
        self.epsilon = epsilon

    def evalDeficitNorm(self, coord, c_T):
        # coord deben ser no normalizadas (np.array)
        sigma_n = self.k_estrella * (coord[0]/self.turbina.d_0) + self.epsilon
        c = 1 - (1-(c_T/(8*(sigma_n**2))))**(0.5)
        return c * exp(-((coord[1]/self.turbina.d_0)**2 + ((coord[2] - self.turbina.z_h)/self.turbina.d_0)**2) / (2 * (sigma_n**2)))
