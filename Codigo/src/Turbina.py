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

    def calcular_c_T(self, estela, coord_random_adentro_disco, z_0, z_mast, u_inf, N):
        # estela: instancia de clase Estela
            # contiene el arreglo de deficits en un vector de
            # len = cantidad_coords_adentro_disco * cantidad_turbinas_izquierda_de_selec
        # coord_random_adentro_disco: lista de instancias de la clase Coord
            # contiene las coord random que se encuentran adentro del disco
        # z_0: float
            # rugocidad del suelo
        # u_inf: instancia de la clase U_inf
            # usara el metodo calcular_logaritmico
        # N: int
            # numero de coordenadas random que utilizamos para hacer el montecarlo

        if self.c_T is None:

            u_adentro_disco = []
            i = 0
            for coord in coord_random_adentro_disco:
                u_inf.coord = coord
                u_inf.perfil_flujo_base(z_mast, z_0)
                u = u_inf.coord * (1 - estela.mergeada[i])
                i += 1
                u_adentro_disco = np.append(u_adentro_disco, u)
            u_adentro_disco2 = u_adentro_disco**2
            count = sum(u_adentro_disco2)
            u_medio_disco = np.mean(u_adentro_disco)
            c_T_tab = self.c_T_tabulado(u_medio_disco)
            volume = (self.d_0)**2
            integral_u2 = (volume * count)/N
            T_turbina = c_T_tab * integral_u2   # lo dividi por (0.5 * rho) porque luego dividire por eso
            T_disponible = (u_medio_disco)**2 * (np.pi*(self.d_0/2)**2)     # lo dividi por (0.5 * rho) porque luego multiplicare por eso
            self.c_T = T_turbina / T_disponible

    def calcular_c_P(self, estela, coord_random_adentro_disco, z_0, z_mast, u_inf, N):

        # estela: instancia de clase Estela
            # contiene el arreglo de deficits en un vector de
            # len = cantidad_coords_adentro_disco * cantidad_turbinas_izquierda_de_selec
        # coord_random_adentro_disco: lista de instancias de la clase Coord
            # contiene las coord random que se encuentran adentro del disco
        # z_0: float
            # rugocidad del suelo
        # u_inf: instancia de la clase U_inf
            # usara el metodo calcular_logaritmico
        # N: int
            # numero de coordenadas random que utilizamos para hacer el montecarlo

        if self.c_P is None:

            u_adentro_disco = []
            i = 0
            for coord in coord_random_adentro_disco:
                u_inf.coord = coord
                u_inf.perfil_flujo_base(z_mast, z_0)
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

    def calcular_P(self, estela, coord_random_adentro_disco, z_0, z_mast, u_inf, N):

        # estela: instancia de clase Estela
            # contiene el arreglo de deficits en un vector de
            # len = cantidad_coords_adentro_disco * cantidad_turbinas_izquierda_de_selec
        # coord_random_adentro_disco: lista de instancias de la clase Coord
            # contiene las coord random que se encuentran adentro del disco
        # z_0: float
            # rugocidad del suelo
        # u_inf: instancia de la clase U_inf
            # usara el metodo calcular_logaritmico
        # N: int
            # numero de coordenadas random que utilizamos para hacer el montecarlo

        if self.potencia is None:

            u_adentro_disco = []
            i = 0
            for coord in coord_random_adentro_disco:
                u_inf.coord = coord
                u_inf.perfil_flujo_base(z_mast, z_0)
                u = u_inf.coord * (1 - estela.mergeada[i])
                i += 1
                u_adentro_disco = np.append(u_adentro_disco, u)
            u_adentro_disco3 = u_adentro_disco**3
            # try:
            #     u_adentro_disco3 = u_adentro_disco**3
            # except:
            #     import pdb; pdb.set_trace()
            count = sum(u_adentro_disco3)
            u_medio_disco = np.mean(u_adentro_disco)
            c_P_tab = self.c_P_tabulado(u_medio_disco)
            volume = (self.d_0)**2
            integral_u3 = (volume * count)/N
            rho = 1.225  # densidad del aire
            self.potencia = c_P_tab * integral_u3 * 0.5 * rho   # lo dividi por (0.5 * rho) porque luego dividire por eso
            P_disponible = (u_medio_disco)**3 * (np.pi*(self.d_0/2)**2)     # lo dividi por (0.5 * rho) porque luego multiplicare por eso
            self.c_P = self.potencia / (0.5 * rho * P_disponible)
            self.potencia = (10**-3) * self.c_P * 0.5 * rho * (u_medio_disco)**3 * ((self.d_0)*0.5)**2 * np.pi
