from __future__ import division
# coding=utf-8

from Modelo_2 import Modelo
import numpy as np
from numpy import exp
from Case_2 import Case
# from cart2pol import cart2pol
# from Coordenadas import Coordenadas
# from Coordenadas_Norm import Coordenadas_Norm

# Jensen used:
# k_wake = 0.1
#
# suggested values for k wake in the literature are
# k_wake = 0.075 =====> on-shore
# k_wake = 0.04 / 0.05 =====> off-shore ones

class Jensen(Modelo):

    def __init__(self, case, k_wake):
        super(Jensen, self).__init__(case)        # self.case = case
        self.k_wake = k_wake

    def evalDeficitNorm(self, coord, c_T):
        return (1 - (1 - c_T)**0.5 ) / (1 + (2*(self.k_wake)*coord[0])/self.case.d_0)**2
