import numpy as np
from Turbina import Turbina

class Coordenadas(object):

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.x_n = None
        self.y_n = None
        self.z_n = None

    def normalizar(self,Turbina):
        self.x_n = self.x/Turbina.d_0
        self.y_n = self.y/Turbina.d_0
        self.z_n = self.z/Turbina.d_0

    def normalizar_hub(self,Turbina):
        self.x_n = self.x/Turbina.d_0
        self.y_n = self.y/Turbina.d_0
        self.z_n = (self.z - Turbina.z_h)/Turbina.d_0
