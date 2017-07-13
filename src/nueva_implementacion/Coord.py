from __future__ import division
# coding=utf-8

class Coord(object):

    def __init__(self, arreglo):
        self.x = arreglo[0]
        self.y = arreglo[1]
        self.z = arreglo[2]

# # test
# import numpy as np
# coord = Coord(np.array([0,1,2]))
# print 'ok' if coord.x == 0 else 'error'
