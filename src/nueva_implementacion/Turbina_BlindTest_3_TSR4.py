from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
# coding=utf-8


from Turbina import Turbina
from scipy import interpolate

class Turbina_BlindTest_3_TSR4(Turbina):

    def __init__(self, coord):
        d_0 = 0.894
        super(Turbina_BlindTest_3_TSR4, self).__init__(d_0, coord)

    def c_T_tabulado(self, U):

        U_tabulado = np.array([4.14787101851, 4.41588232547, 4.72385445179, 5.07072755312, 5.47714654995, 5.96259428096, 6.54767246471, 7.37306397838, 8.32410129961, 8.17335446707, 9.42431992541, 10.6723205508, 11.7526468642, 13.3315498462, 14.9937539227, 19.3829819477, 29.5426091135, 60.8239511797])
        c_T_tabulado = np.array([0.849723747241, 0.861351501437, 0.867629193779, 0.864500584885, 0.854468979411, 0.835866760934, 0.808834619317, 0.764095347829, 0.716490293811, 0.719544389506, 0.63973365993, 0.607824759891, 0.569526088252, 0.463827607969, 0.343459877356, 0.269069949519, 0.191626415384, 0.125200685221])
        tck = interpolate.splrep(U_tabulado, c_T_tabulado, s=0)
        c_Tnew = interpolate.splev(U, tck, der=0)
        return c_Tnew

    def P_tabulado(self, U):
        Pnew = 0 ###??????
        return Pnew
