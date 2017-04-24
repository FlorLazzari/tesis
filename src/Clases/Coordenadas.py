import numpy as np
from Case import Case

class Coordenadas(object):

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.x_n = None
        self.y_n = None
        self.z_n = None

    def normalizar(self,Case):
        self.x_n = self.x/Case.d_0
        self.y_n = self.y/Case.d_0
        self.z_n = self.z/Case.d_0

    def normalizar_hub(self,Case):
        self.x_n = self.x/Case.d_0
        self.y_n = self.y/Case.d_0
        self.z_n = (self.z - Case.z_h)/Case.d_0
