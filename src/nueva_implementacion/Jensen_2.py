from __future__ import division
# coding=utf-8

from Modelo_2 import Modelo
import numpy as np

# Jensen used:
# k_wake = 0.1
#
# suggested values for k wake in the literature are
# k_wake = 0.075 =====> on-shore
# k_wake = 0.04 / 0.05 =====> off-shore ones

class Jensen(Modelo):

    def __init__(self):
        super(Jensen, self).__init__()        # self.case = case + self.turbina = turbina
        self.k_wake = 0.1

    def evaluar_deficit_normalizado(self, turbina, coord_selec):
        beta = 0.5 * ((1+((1 - turbina.c_T)**0.5))/((1 - turbina.c_T)**0.5))
        d_w = ((beta + 10 * self.k_wake * (coord_selec.x/turbina.d_0) )**0.5) * turbina.d_0
        if (abs(coord_selec.y) <= (d_w / 2)) & (abs(coord_selec.z - turbina.coord.z) <= (d_w / 2)):
            return (1 - (1 - turbina.c_T)**0.5 ) / (1 + (2*(self.k_wake)*coord_selec.x)/turbina.d_0)**2
        else:
            return 0


# problema con Jensen: donde termina la estela? cual es el d_w equivalente al de Frandsen?
