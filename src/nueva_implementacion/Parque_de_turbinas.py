
from __future__ import division
import numpy as np
# coding=utf-8

class Parque_de_turbinas(object):

    def __init__(self, turbinas, z_0, z_mast):
        self.turbinas = turbinas
        self.z_0 = z_0
        self.potencia = 0
        self.z_mast = z_mast

    def ordenar_turbinas_de_izquierda_a_derecha(self):
        turbinas_ordenadas = []
        for turbina in self.turbinas:
            self.turbinas.sort(key=lambda turbina:turbina.coord.x)

    def turbinas_a_la_izquierda_de_una_coord(self, una_coord):
        turbinas_a_la_izquierda = []
        for turbina in self.turbinas:
            if (turbina.coord.x < una_coord.x):
                turbinas_a_la_izquierda.append(turbina)
        return turbinas_a_la_izquierda

    # def calcular_c_T_tabulado(self):

    def calcular_c_T_primer_turbina(self, u_inf):
        self.turbinas[0].c_T = self.turbinas[0].c_T_tabulado(u_inf)

    def inicializar_parque(self, u_inf):
        self.ordenar_turbinas_de_izquierda_a_derecha()
        # self.turbinas[0].c_T = self.calcular_c_T_primer_turbina(u_inf)

    def rotar(self, theta):
        theta_rad = (np.pi/180) * theta
        R = np.matrix([[np.cos(theta_rad), -np.sin(theta_rad)], [np.sin(theta_rad), np.cos(theta_rad)]])
        for turbina in self.turbinas:
            vector_coord = np.array([turbina.coord.x, turbina.coord.y])
            vector_coord_rotado = np.dot(R, vector_coord)
            turbina.coord.x = vector_coord_rotado.getA1()[0]
            turbina.coord.y = vector_coord_rotado.getA1()[1]





# # test rotar
#
# from Turbina_Marca import Turbina_Marca
# import numpy as np
# from Coord import Coord
#
# turbina_0 = Turbina_Marca(Coord(np.array([0,0,10])))
# turbina_1 = Turbina_Marca(Coord(np.array([20,0,10])))
# turbina_2 = Turbina_Marca(Coord(np.array([40,0,10])))
# parque_de_turbinas = Parque_de_turbinas([turbina_0, turbina_1, turbina_2], 0.1)
#
# print turbina_0.coord.x, turbina_0.coord.y, turbina_0.coord.z
# print turbina_1.coord.x, turbina_1.coord.y, turbina_1.coord.z
# print turbina_2.coord.x, turbina_2.coord.y, turbina_2.coord.z
#
# print 'ROTO'
# parque_de_turbinas.rotar(90)
#
# print turbina_0.coord.x, turbina_0.coord.y, turbina_0.coord.z
# print turbina_1.coord.x, turbina_1.coord.y, turbina_1.coord.z
# print turbina_2.coord.x, turbina_2.coord.y, turbina_2.coord.z


## test:
# from Turbina_Marca import Turbina_Marca
# import numpy as np
#
# turbina_0 = Turbina_Marca(np.array([0,20,10]))
# turbina_1 = Turbina_Marca(np.array([20,20,10]))
# turbina_2 = Turbina_Marca(np.array([40,20,10]))
# parque_de_turbinas = Parque_de_turbinas([turbina_0, turbina_1, turbina_2])
# turbinas_a_la_izquierda = parque_de_turbinas.turbinas_a_la_izquierda_de_una_coord(np.array([20,20,10]))
# print 'ok' if turbinas_a_la_izquierda[0] == turbina_0 else 'error'
#
# parque_de_turbinas = Parque_de_turbinas([turbina_1, turbina_2, turbina_0])
# parque_de_turbinas.ordenar_turbinas_de_izquierda_a_derecha()
# print 'ok' if (parque_de_turbinas.turbinas[0] == turbina_0 and parque_de_turbinas.turbinas[1] == turbina_1 and parque_de_turbinas.turbinas[2] == turbina_2) else 'error'
#
# c_T_tab = parque_de_turbinas.calcular_c_T_primer_turbina(10)
# print c_T_tab
