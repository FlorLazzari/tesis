from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
# coding=utf-8


from Turbina import Turbina
from scipy import interpolate

class Turbina_BlindTest_3_TSR6(Turbina):

    def __init__(self, coord):
        d_0 = 0.894
        super(Turbina_BlindTest_3_TSR6, self).__init__(d_0, coord)

    def c_T_tabulado(self, U):

        # el problema esta en U_tabulado
        # U_tabulado = np.arange(18)
        U_tabulado = np.array([5.23941602338, 5.57795662165, 5.96697404436, 6.40512954079, 6.9185009052, 7.53169803911, 8.27074416595, 9.31334397269, 10.5146542732, 10.3242372216, 11.9044041163, 13.480825959, 14.8454486706, 16.8398524373, 18.9394786392, 24.4837666707, 37.3169799328, 76.8302541217])
        c_T_tabulado = np.array([0.849723747241, 0.861351501437, 0.867629193779, 0.864500584885, 0.854468979411, 0.835866760934, 0.808834619317, 0.764095347829, 0.716490293811, 0.719544389506, 0.63973365993, 0.607824759891, 0.569526088252, 0.463827607969, 0.343459877356, 0.269069949519, 0.191626415384, 0.125200685221])
        tck = interpolate.splrep(U_tabulado, c_T_tabulado, s=0)
        c_Tnew = interpolate.splev(U, tck, der=0)
        return c_Tnew

    def P_tabulado(self, U):
        Pnew = 0 ###??????
        return Pnew
#
# coord = 0
# U = 5.23941602338
# turb = Turbina_BlindTest_3_TSR6(coord)
# c_T = turb.c_T_tabulado(U)
#
# print c_T
