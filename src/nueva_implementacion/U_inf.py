class U_inf(object):
    def __init__(self):
        self.coord = None

    def calcular_logaritmico(self,coordenada, u_hub, z_h, z_0):
        from math import log
        self.coord = u_hub * (log(coordenada.z / z_0) / log(z_h / z_0))
