from __future__ import division
# coding=utf-8

import numpy as np
from Coord import Coord
from U_inf import U_inf

class Turbina(object):

    def __init__(self, d_0, coord):
        self.d_0 = d_0
        self.coord = coord
        self.c_T = None
        self.c_P = None
        self.estela_de_otras_turbinas = []
        self.potencia = None

    def c_T_tabulado(self, u):
        pass

    def c_P_tabulado(self, u):
        pass

    def P_tabulado(self, u):
        pass

    def generar_coord_random(self, N):
        coord_random_arreglo = []
        for i in range(N):
            rand_y = np.random.uniform(self.coord.y-(self.d_0/2), self.coord.y+(self.d_0/2))
            rand_z = np.random.uniform(self.coord.z-(self.d_0/2), self.coord.z+(self.d_0/2))
            coord_random = Coord(np.array([self.coord.x, rand_y, rand_z]))
            coord_random_arreglo.append(coord_random)
        return coord_random_arreglo

    def calcular_c_T(self, estela, coord_random_adentro_disco, z_0, u_inf, N):
        # estela: [element of class Estela]
            # contiene el arreglo de deficits en un vector de
            # len = cantidad_coords_adentro_disco * cantidad_turbinas_izquierda_de_selec
        # coord_random_adentro_disco: [list of elements of class Coord]
            # contiene las coord random que se encuentran adentro del disco
        # z_0: [float]
            # rugocidad del suelo
        # u_inf: [element of class U_inf]
            # usaremos el metodo calcular_logaritmico
        # N: [int]
            # numero de coordenadas random que utilizamos para hacer el montecarlo

# problemas! el c_T esta dando mayor a 1

        if self.c_T is None:
            u_adentro_disco = []
            i = 0
            for coord in coord_random_adentro_disco:
                u_inf.coord = coord
                # print 'u_inf.coord.x = ',u_inf.coord.x
                # print 'u_inf.coord.y = ',u_inf.coord.y
                # print 'u_inf.coord.z = ',u_inf.coord.z
                u_inf.perfil_flujo_base(self.coord.z, z_0)
                # print 'u_inf = ', u_inf.coord
                # print 'i = ',i
                # print 'estela.mergeada[i] = ', estela.mergeada[i]
                u = u_inf.coord * (1 - estela.mergeada[i])
                # print 'u = ', u
                i += 1
                u_adentro_disco = np.append(u_adentro_disco, u)
                # print 'u_adentro_disco = ',u_adentro_disco
            u_adentro_disco2 = u_adentro_disco**2
            # print 'u_adentro_disco2 = ',u_adentro_disco2
            count = sum(u_adentro_disco2)
            u_medio_disco = np.mean(u_adentro_disco)
            c_T_tab = self.c_T_tabulado(u_medio_disco)
            volume = (self.d_0)**2
            integral_u2 = (volume * count)/N
            T_turbina = c_T_tab * integral_u2   # lo dividi por (0.5 * rho) porque luego dividire por eso
            T_disponible = (u_medio_disco)**2 * (np.pi*(self.d_0/2)**2)     # lo dividi por (0.5 * rho) porque luego multiplicare por eso
            self.c_T = T_turbina / T_disponible

            # print ('c_T calculado:', self.c_T)
            # print ('c_T_tab:', c_T_tab)


# #prueba calcular_c_T:
#
# from U_inf import U_inf
# from Coord import Coord
# import numpy as np
# from Estela import Estela
#
# coord_random_1 = Coord(np.array([0,80,1]))
# coord_random_2 = Coord(np.array([0,80,80]))
# coord_random_3 = Coord(np.array([0,80,120]))
# coord_random_adentro_disco = [coord_random_1, coord_random_2, coord_random_3]
# cantidad_coords_adentro_disco = len(coord_random_adentro_disco)
#
# arreglo_estela = [0.1, 0.2, 0.3, 1, 2, 3]
# cantidad_turbinas_izquierda_de_selec = 2
#
# u_hub = 7
# z_0 = 0.01
#
# estela = Estela(arreglo_estela, cantidad_coords_adentro_disco, cantidad_turbinas_izquierda_de_selec)
#
# estela.calcular_c_T(estela, coord_random_adentro_disco, z_0, u_inf, N):
#
#
# u_inf = U_inf()
#
# from U import U
# u = U()
# d_0 = 60
# coord = Coord(np.array([0, 0, 80]))
#
# turbina = Turbina(d_0, coord)
#
# turbina.calcular_c_T(estela, coord_random_adentro_disco, u_hub, z_0, u_inf, 4)

    def calcular_c_P(self, estela, coord_random_adentro_disco, z_0, u_inf, N):

        # estela: [element of class Estela]
            # contiene el arreglo de deficits en un vector de
            # len = cantidad_coords_adentro_disco * cantidad_turbinas_izquierda_de_selec
        # coord_random_adentro_disco: [list of elements of class Coord]
            # contiene las coord random que se encuentran adentro del disco
        # z_0: [float]
            # rugocidad del suelo
        # u_inf: [element of class U_inf]
            # usaremos el metodo calcular_logaritmico
        # N: [int]
            # numero de coordenadas random que utilizamos para hacer el montecarlo

        u_adentro_disco = []
        i = 0
        for coord in coord_random_adentro_disco:
            u_inf.coord = coord
            u_inf.perfil_flujo_base(self.coord.z, z_0)
            u = u_inf.coord * (1 - estela.mergeada[i])
            i += 1
            u_adentro_disco = np.append(u_adentro_disco, u)
        u_adentro_disco3 = u_adentro_disco**3
        count = sum(u_adentro_disco3)
        u_medio_disco = np.mean(u_adentro_disco)
        c_P_tab = self.c_P_tabulado(u_medio_disco)
        volume = (self.d_0)**2
        integral_u3 = (volume * count)/N
        rho = 1.225  # densidad del aire
        self.potencia = c_P_tab * integral_u3 * 0.5 * rho   # lo dividi por (0.5 * rho) porque luego dividire por eso
        P_disponible = (u_medio_disco)**3 * (np.pi*(self.d_0/2)**2)     # lo dividi por (0.5 * rho) porque luego multiplicare por eso
        self.c_P = self.potencia / (0.5 * rho * P_disponible)
        # print ('c_P calculado:', self.c_P)
        # print ('c_P_tab:', c_P_tab)


    def calcular_P(self, estela, coord_random_adentro_disco, z_0, u_inf, N):

        u_adentro_disco = []
        i = 0
        for coord in coord_random_adentro_disco:
            u_inf.coord = coord
            u_inf.perfil_flujo_base(self.coord.z, z_0)
            u = u_inf.coord * (1 - estela.mergeada[i])
            i += 1
            u_adentro_disco = np.append(u_adentro_disco, u)
        u_medio_disco = np.mean(u_adentro_disco)
        self.potencia = self.P_tabulado(u_medio_disco)
