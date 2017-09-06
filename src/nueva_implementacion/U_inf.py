class U_inf(object):
    def __init__(self):
        self.coord = None
        self.coord_hub = None

    def calcular_logaritmico(self, z_h, z_0):
        from math import log
        self.coord = self.coord_hub * (log(self.coord.z / z_0) / log(z_h / z_0))



# prueba
# import numpy as np
# u_hub = 7
# z_hub = 80
# z_0 = 0.01
#
# from Coord import Coord
# coord_1 = Coord(np.array([0,0,0.5]))
# coord_2 = Coord(np.array([0,0,80]))
# coord_random_arreglo = [coord_1, coord_2]
# u_inf_arreglo = []
#
# u_inf = U_inf()
# for coord in coord_random_arreglo:
#     u_inf.calcular_logaritmico(coord, u_hub, z_hub, z_0)
#     u_inf_arreglo = np.append(u_inf_arreglo, u_inf.coord)
#
# print "coord_random_arreglo[0].z = ", coord_random_arreglo[0].z
# print "u_inf_arreglo[0] = ", u_inf_arreglo[0]
#
# print "coord_random_arreglo[1].z = ", coord_random_arreglo[1].z
# print "u_inf_arreglo[0] = ", u_inf_arreglo[1]
