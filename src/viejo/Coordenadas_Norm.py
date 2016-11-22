# coding=utf-8# coding=utf-8

from Case import Case
from Coordenadas import Coordenadas
import numpy as np

class Coordenadas_Norm(object):

    def __init__(self,x_n,y_n,z_n):
        self.x_n = x_n
        self.y_n = y_n
        self.z_n = z_n
        self.x = None
        self.y = None
        self.z = None
        self.r = None
        self.phi = None
        # no se si poner a r y phi como un atributo es lo mejor del mundo

    def des_normalizar(self,case):
        self.x = self.x_n*case.d_0
        self.y = self.y_n*case.d_0
        self.z = (self.z_n*case.d_0) + case.z_h

# esto es medio un enchastre, habría que usar super o pensar algo mas inteligente
