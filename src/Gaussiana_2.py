from __future__ import division
# coding=utf-8

from Modelo_2 import Modelo
# import numpy as np
from numpy import exp
from Case_2 import Case
# from cart2pol import cart2pol
# from Coordenadas import Coordenadas
# from Coordenadas_Norm import Coordenadas_Norm


class Gaussiana(Modelo):

    def __init__(self, case, k_estrella, epsilon):
        super(Gaussiana, self).__init__(case)        # self.case = case
        self.k_estrella = k_estrella
        self.epsilon = epsilon

    def evalDeficitNorm(self, coord, c_T):
        # coord deben ser no normalizadas (np.array)
        # normalizo:
        coord[0] = coord[0]/self.case.d_0
        coord[1] = coord[1]/self.case.d_0
        coord[2] = (coord[2] - self.case.z_h)/self.case.d_0
        sigma_n = self.k_estrella * coord[0] + self.epsilon
        c = 1 - (1-(c_T/(8*(sigma_n**2))))**(0.5)
        return c * exp(-(coord[1]**2 + coord[2]**2) / (2 * (sigma_n**2)))
