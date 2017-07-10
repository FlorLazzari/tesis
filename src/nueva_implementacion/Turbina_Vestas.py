from __future__ import division
# coding=utf-8

import numpy as np
from Turbina_2 import Turbina

class Turbina_Vestas(Turbina):

    def __init__(self, coord_selec):
        d_0 = 40
        super(Turbina_Vestas, self).__init__(d_0, coord_selec)

    def c_T_tabulado(self, U):
        print('hola')
