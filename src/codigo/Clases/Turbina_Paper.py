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
        c_T_tabulado = 0.42
        return c_T_tabulado

    def c_P_tabulado(self, U):
        # este valor es inventado, habria que ver del paper el c_P
        c_P_tabulado = 0
        return c_P_tabulado
