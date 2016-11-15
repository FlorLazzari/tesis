import numpy as np

class Coordenadas(object):

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.x_n = None
        self.y_n = None
        self.z_n = None
        self.r = None
        self.phi = None
        # no se si poner a r y phi como un atributo es lo mejor del mundo

    def normalizar(self,case):
        self.x_n = self.x/case.d_0
        self.y_n = self.y/case.d_0
        self.z_n = (self.z - case.z_h)/case.d_0

    def cart2pol(self):
        self.r = np.sqrt(self.y**2 + self.z**2)
        self.phi = np.arctan2(self.z, self.y)

        #chequear esto! yo hacia car2pol con las coordenadas normalizadas, me parece que eso no tiene sentido

    def pol2cart(self):
        self.y = self.r * np.cos(self.phi)
        self.z = self.r * np.sin(self.phi)
