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

        U_tabulado = 10
        c_Tnew = 0.8
        return c_Tnew

    def P_tabulado(self, U):
        Pnew = 0 ###??????
        return Pnew
