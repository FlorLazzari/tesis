from __future__ import division
import numpy as np
# coding=utf-8

from Turbina import Turbina
from scipy import interpolate

class Turbina_Paper(Turbina):

    def __init__(self, coord):
        d_0 = 0.15
        super(Turbina_Paper, self).__init__(d_0, coord)

    def c_T_tabulado(self, u):
        # Cubic-spline:
        c_T_tabulado = 0.42

        # Unew = np.arange(4,26,0.1)
        # c_Tnew = interpolate.splev(Unew, tck, der=0)
        # plt.figure()
        # plt.plot(U_tabulado, c_T_tabulado, 'x', Unew, c_Tnew, 'b')
        # plt.legend(['Dato', 'Cubic Spline'])
        # plt.title('Cubic-spline interpolation')
        # plt.show()
        return c_T_tabulado

    def P_tabulado(self, U):
        U_tabulado = np.arange(4, 26)

        # este valor es cualquier cosa!! lo invente, habria que ver del paper el c_P
        P_tabulado = 0.42
        return P_tabulado
