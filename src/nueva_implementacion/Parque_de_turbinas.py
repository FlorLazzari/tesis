from __future__ import division
# coding=utf-8

class Parque_de_turbinas(object):

    def __init__(self, turbinas):
        self.turbinas = turbinas

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
        c_T_tab = self.turbinas[0].c_T_tabulado(u_inf)
        return c_T_tab

    def inicializar_parque(self, u_inf):
        self.ordenar_turbinas_de_izquierda_a_derecha()
        self.turbinas[0].c_T = self.calcular_c_T_primer_turbina(u_inf)


# test:
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
