class U_inf_arreglo(object):
    def __init__(self, u_inf_arreglo):
        self.u_inf_arreglo = u_inf_arreglo


    def calcular_logaritmico_arreglo(self,coordenada, u_hub, z_h, z_0):
        from math import log
        for u_inf in u_inf_arreglo:
            self.u_inf.coord = u_hub * (log(coordenada.z / z_0) / log(z_h / z_0))
