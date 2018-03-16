from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
# coding=utf-8


from Turbina import Turbina
from scipy import interpolate

class Turbina_BlindTest(Turbina):

    def __init__(self, coord):
        d_0 = 0.894
        super(Turbina_BlindTest, self).__init__(d_0, coord)

    def c_T_tabulado(self, U):

        # a mi me importa el comportamiento del molino bajo condiciones normales, por
        # lo tanto voy a estudiar unicamente velocity defect para TSR = 6 (10 m/s)

        # c_T correspondiente a U = 10
        c_Tnew = 0.85   ####???? lo chante a ojimetro del grafico del paper BlindTest
        return c_Tnew

    def P_tabulado(self, U):
        Pnew = 0 ###??????
        return Pnew


# at 3 downstream positions, measured from the plane of the rotor:
#
# - x/d = 1
# - x/d = 3
# - x/d = 5
