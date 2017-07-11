from __future__ import division
# coding=utf-8

import numpy as np
from Turbina_2 import Turbina
from scipy import interpolate
import matplotlib.pyplot as plt


class Turbina_Marca(Turbina):

    def __init__(self, coord_selec):
        d_0 = 40
        super(Turbina_Marca, self).__init__(d_0, coord_selec)

    def c_T_tabulado(self, U):
        # Cubic-spline:
        U_tabulado = np.arange(4, 26)
        c_T_tabulado = np.array([0.824, 0.791, 0.791, 0.791, 0.732, 0.606, 0.510, 0.433, 0.319, 0.247, 0.196, 0.159, 0.134, 0.115, 0.100, 0.086, 0.074, 0.064, 0.057, 0.050, 0.045, 0.040])
        tck = interpolate.splrep(U_tabulado, c_T_tabulado, s=0)
        c_Tnew = interpolate.splev(self.U, tck, der=0)

        # Unew = np.arange(4,26,0.1)
        # c_Tnew = interpolate.splev(Unew, tck, der=0)
        # plt.figure()
        # plt.plot(U_tabulado, c_T_tabulado, 'x', Unew, c_Tnew, 'b')
        # plt.legend(['Dato', 'Cubic Spline'])
        # plt.title('Cubic-spline interpolation')
        # plt.show()
        return c_Tnew
