class Flujo_base(Punto):
    def __init__(self):
        super(Flujo_base, self).__init__()
        self.u_hub = None

def calcular_logaritmico(self, pto, z_h, z_0):
    from math import log
    pto.u = self.u_hub * (log(pto.coord.z / z_0) / log(z_h / z_0))
