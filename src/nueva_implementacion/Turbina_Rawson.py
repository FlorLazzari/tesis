from __future__ import division
import numpy as np
# coding=utf-8


from Turbina import Turbina
from scipy import interpolate

class Turbina_Rawson(Turbina):

    def __init__(self, coord):
        d_0 = 90
        super(Turbina_Rawson, self).__init__(d_0, coord)

    def c_T_tabulado(self, U):
        # Cubic-spline:
        U_tabulado = np.arange(4, 26)
        # tabla para "regimen de trabajo" = Modo 2
        c_T_tabulado = np.array([0.824, 0.791, 0.791, 0.791, 0.732, 0.606, 0.510, 0.433, 0.319, 0.247, 0.196, 0.159, 0.134, 0.115, 0.100, 0.086, 0.074, 0.064, 0.057, 0.050, 0.045, 0.040])
        tck = interpolate.splrep(U_tabulado, c_T_tabulado, s=0)
        c_Tnew = interpolate.splev(U, tck, der=0)

        # Unew = np.arange(4,26,0.1)
        # c_Tnew = interpolate.splev(Unew, tck, der=0)
        # plt.figure()
        # plt.plot(U_tabulado, c_T_tabulado, 'x', Unew, c_Tnew, 'b')
        # plt.legend(['Dato', 'Cubic Spline'])
        # plt.title('Cubic-spline interpolation')
        # plt.show()
        return c_Tnew

    def P_tabulado(self, U):
        # Cubic-spline:
        U_tabulado = np.arange(4, 26)
        # tabla para "regimen de trabajo" = Modo 2
        P_tabulado = np.array([88, 204, 371, 602, 880, 1147, 1405, 1623, 1729, 1761, 1774, 1786, 1795, 1799, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800])
        tck = interpolate.splrep(U_tabulado, P_tabulado, s=0)
        Pnew = interpolate.splev(U, tck, der=0)
        return Pnew
