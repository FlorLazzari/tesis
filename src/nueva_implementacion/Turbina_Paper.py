from __future__ import division
# coding=utf-8

import numpy as np
from Turbina_2 import Turbina
from scipy import interpolate
import matplotlib.pyplot as plt


class Turbina_Paper(Turbina):

    def __init__(self, coord):
        d_0 = 0.15
        super(Turbina_Paper, self).__init__(d_0, coord)

    def c_T_tabulado(self, u):
        # Cubic-spline:
        U_tabulado = np.arange(4, 26)
        c_T_tabulado = 0.42

        # Unew = np.arange(4,26,0.1)
        # c_Tnew = interpolate.splev(Unew, tck, der=0)
        # plt.figure()
        # plt.plot(U_tabulado, c_T_tabulado, 'x', Unew, c_Tnew, 'b')
        # plt.legend(['Dato', 'Cubic Spline'])
        # plt.title('Cubic-spline interpolation')
        # plt.show()
        return c_T_tabulado
