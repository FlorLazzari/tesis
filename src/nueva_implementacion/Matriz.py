from __future__ import division
# coding=utf-8

import numpy as np
from Case_2 import Case


# parametro global de "presicion"


class Matriz(object):

    def __init__(self, q_i, q):
        self.q_i = q_i
        self.q = q

    def crearme(self):
        # return np.zeros((len(np.linspace(0, self.i_total, self.q_i)), len(np.linspace(0, self.j_total, self.q)), len(np.linspace(0, self.k_total, self.q))))
        # medio cabeza hacer esto..
        # TypeError: 'Matriz' object has no attribute '__getitem__'
        # no puede ser con numpy, va a tener que ser una matriz normal
        for i in range(self.q_i):
            for j in range(self.q):
                for k in range(self.q):
                    matriz[i,j,k] = 0
        return matriz

matriz = Matriz(2, 3)
print matriz.crearme()
