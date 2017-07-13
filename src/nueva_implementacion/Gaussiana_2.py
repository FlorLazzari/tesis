from __future__ import division
# coding=utf-8

from Modelo_2 import Modelo
import numpy as np
from numpy import exp
# from cart2pol import cart2pol
# from Coordenadas import Coordenadas
# from Coordenadas_Norm import Coordenadas_Norm



class Gaussiana(Modelo):

    def __init__(self):
        super(Gaussiana, self).__init__()
        # por ahora los datos estan hardcodeados, habria que calcularlos correctamente del fit del CFD
        self.k_estrella = 0.2
        self.epsilon = 0.268855463528

    def evaluar_deficit_normalizado(self, turbina, coord_selec):
        sigma_n = self.k_estrella * ((coord_selec.x-turbina.coord.x)/turbina.d_0) + self.epsilon
        c = 1 - (1-(turbina.c_T/(8*(sigma_n**2))))**(0.5)
        return c * exp(-(((coord_selec.y-turbina.coord.y)/turbina.d_0)**2 + ((coord_selec.z-turbina.coord.z)/turbina.d_0)**2) / (2 * (sigma_n**2)))
