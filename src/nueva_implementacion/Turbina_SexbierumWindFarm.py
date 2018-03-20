from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
# coding=utf-8


from Turbina import Turbina
from scipy import interpolate

class Turbina_SexbierumWindFarm(Turbina):

    def __init__(self, coord):
        d_0 = 30.1
        super(Turbina_SexbierumWindFarm, self).__init__(d_0, coord)

    def c_T_tabulado(self, U):

        # a mi me importa el comportamiento del molino bajo condiciones normales, por
        # lo tanto voy a estudiar unicamente velocity defect para TSR = 6 (10 m/s)

        # c_T correspondiente a U = 10
        c_Tnew = 0.75   ####???? lo chante a ojimetro del grafico del paper SexbierumWindFarm
        return c_Tnew

    def P_tabulado(self, U):
        Pnew = 0 ###??????
        return Pnew
