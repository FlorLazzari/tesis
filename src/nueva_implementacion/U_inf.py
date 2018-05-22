class U_inf(object):
    def __init__(self):
        self.coord = None
        self.coord_mast = None
        self.perfil = None

    def perfil_flujo_base(self, z_mast, z_0):
        if self.perfil == 'log':
            from math import log
            self.coord = self.coord_mast * (log(self.coord.z / z_0) / log(z_mast / z_0))

        elif self.perfil == 'cte':
            self.coord = self.coord_mast

# prueba
# import numpy as np
# u_inf = U_inf()
# u_inf.coord_mast = 8.1
# u_inf.perfil = 'log'
# z_mast = 234-154
# z_0 = 0.01
# from Coord import Coord
# u_inf.coord = Coord(np.array([0, 0, 274-154]))
#
# u_inf.perfil_flujo_base(z_mast, z_0)
#
# print u_inf.coord
