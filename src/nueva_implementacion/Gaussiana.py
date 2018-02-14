from __future__ import division
# coding=utf-8

from Modelo import Modelo
from numpy import exp

class Gaussiana(Modelo):

    def __init__(self):
        super(Gaussiana, self).__init__()
        # por ahora los datos estan hardcodeados con los parametros del paper, habria que calcularlos correctamente del fit del CFD
        self.k_estrella = 0.023
        self.epsilon = 0.219

        # cambio estos valores con el ajuste del OpenFOAM:
        # self.k_estrella = 1.86
        # self.epsilon = 32.56

    def evaluar_deficit_normalizado(self, turbina, coord_selec):
        sigma_n = self.k_estrella * ((coord_selec.x-turbina.coord.x)/turbina.d_0) + self.epsilon
        c = 1 - (1-(turbina.c_T/(8*(sigma_n**2))))**(0.5)

        # print 'sigma_n = ', sigma_n
        # print 'c = ', c
        #
        # print 'coord_selec.y = ', coord_selec.y
        # print 'turbina.coord.y = ', turbina.coord.y
        #
        # print 'coord_selec.y-turbina.coord.y = ', coord_selec.y-turbina.coord.y
        #
        # print 'gauss = ', c * exp(-(((coord_selec.y-turbina.coord.y)/turbina.d_0)**2 + ((coord_selec.z-turbina.coord.z)/turbina.d_0)**2) / (2 * (sigma_n**2)))
        #
        # def gauss(x, A, mu, sigma):
        #     return A*exp(-((x-mu)/turbina.d_0)**2/(2.*sigma**2))
        #
        # print 'gauss_2 = ', gauss(coord_selec.y, c, 0, sigma_n)
        # print 'coord_selec.z-turbina.coord.z = ', coord_selec.z-turbina.coord.z

        return c * exp(-(((coord_selec.y-turbina.coord.y)/turbina.d_0)**2 + ((coord_selec.z-turbina.coord.z)/turbina.d_0)**2) / (2 * (sigma_n**2)))
