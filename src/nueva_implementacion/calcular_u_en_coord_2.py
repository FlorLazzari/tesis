from __future__ import division
# coding=utf-8

from Modelo_2 import Modelo
from Gaussiana_2 import Gaussiana
from Parque_de_turbinas import Parque_de_turbinas
from Turbina_Marca import Turbina_Marca
from U import U
from Coord import Coord
import numpy as np
from numpy import exp


def calcular_u_en_coord(modelo, u_inf, coord, parque_de_turbinas):

    turbinas_a_la_izquierda_de_coord = parque_de_turbinas.turbinas_a_la_izquierda_de_una_coord(coord)
    deficit_normalizado_en_coord = []
    parque_de_turbinas.inicializar_parque(u_inf)

    # el parque ya esta inicializado, el c_T de la primera turbina esta calculado

    print "c_T primera turbina", parque_de_turbinas.turbinas[0].c_T

    # calculo c_T teniendo en cuenta la interaccion de las otras turbinas
    
    for turbina_selec in turbinas_a_la_izquierda_de_coord[1:]:

        # print "turbina selec:", turbina_selec
        coord_random_arreglo = turbina_selec.generar_coord_random()
        turbinas_a_la_izquierda_de_turbina_selec = parque_de_turbinas.turbinas_a_la_izquierda_de_una_coord(turbina_selec.coord)
        cantidad_turbinas_izquierda_de_selec = len(turbinas_a_la_izquierda_de_turbina_selec)
        print "cantidad_turbinas_izquierda_de_selec:", cantidad_turbinas_izquierda_de_selec
        estela = []
        for turbina in turbinas_a_la_izquierda_de_turbina_selec:
            print "turbina c_T:", turbina.c_T
            if turbina.c_T == None:
                print "calculo el c_T"
                # ahora procedo a calcular el c_T de la turbina_selec
                cantidad_adentro_disco = 0
                count = 0
                N = len(coord_random_arreglo)
                print N
                U_adentro_disco = 0
                coord_random_adentro_disco = []
                for coord_random in coord_random_arreglo:
                    # print coord_random.x
                    # print coord_random.y
                    # print coord_random.z
                    if ((coord_random.y-turbina_selec.coord.y)**2 + (coord_random.z-turbina_selec.coord.z)**2 < (turbina_selec.d_0/2)**2):
                        deficit_normalizado_en_coord_random = modelo.evaluar_deficit_normalizado(turbina, coord_random)
                        estela = np.append(estela, deficit_normalizado_en_coord_random)
                        coord_random_adentro_disco = np.append(coord_random_adentro_disco, coord_random)

                print "estela", estela
                print "coord_random_adentro_disco", coord_random_adentro_disco

                # la siguiente linea es en la que hay que seguir trabajando: (en la clase turbina)
                turbina_selec.calcular_c_T(estela, coord_random_adentro_disco, u_inf)
            else:
                print "no calculo c_T"

        deficit_normalizado_en_coord_contribucion_turbina_selec = modelo.evaluar_deficit_normalizado(parque_de_turbinas.turbina_selec, coord)
        deficit_normalizado_en_coord = np.append(deficit_normalizado_en_coord_contribucion_turbina_selec)
        # estas dos cosas estan hechas muy a lo bestia en la clase U, falta terminar eso y probarlo
        merge_estela()
        restar_deficit()
        # u_coord = ??

        print u_coord





            # cantidad_adentro_disco = len(estela)/cantidad_turbinas_izquierda_de_selec
            # turbina.merge_estela(estela, cantidad_adentro_disco, cantidad_turbinas_izquierda_de_selec)
            #
            # U_medio_disco = np.mean(U_adentro_disco)
            # c_T_tab = turbina_selec.c_T_tabulado(U_medio_disco)
            # volume = (turbina_selec.d_0)**2
            # integral_U_cuadrado = (volume * count)/N
            # T_turbina_selec = c_T_tab * integral_U_cuadrado   # lo dividi por (0.5 * rho) porque luego dividire por eso
            # T_disponible = (U_medio_disco)**2 * (np.pi*(turbina_selec.d_0/2)**2)     # lo dividi por (0.5 * rho) porque luego multiplicare por eso
            # turbina_selec.c_T = T_turbina_selec / T_disponible





# prueba:
from Turbina_Paper import Turbina_Paper
gaussiana = Gaussiana()
u_inf = 10
coord = Coord(np.array([60*7*6, 0, 100]))
turbina_1 = Turbina_Paper(Coord(np.array([60,0,100])))
turbina_2 = Turbina_Paper(Coord(np.array([60*7,0,100])))
turbina_3 = Turbina_Paper(Coord(np.array([60*7*2,0,100])))

parque_de_turbinas = Parque_de_turbinas([turbina_1, turbina_2, turbina_3])
calcular_u_en_coord(gaussiana, u_inf, coord, parque_de_turbinas)


        # turbina_selec.calcular_c_T(cantidad_adentro_disco, cantidad_turbinas_izquierda_de_selec)
        #
        # q = 10              # division dentro de la grilla (queda hardcodeado aca adentro, habria que ver que valor de q es el ideal)
        # U = []
        # U_adentro_disco = np.array([])
        # count = 0
        # for coord_random in coord_random_arreglo:
        #     if ((coord_random[1]-self.coord[1])**2 + (coord_random[2]-self.coord[2])**2 < (self.d_0/2)**2):
        #         deficit_normalizado_en_coord_random = modelo.evaluar_deficit_normalizado(turbina, coord_random)
        #         u_coord = u_coord * (1 - deficit_normalizado_en_coord_random)
        #         U = u_coord
        #
        #         U = calcular_U_en_pto(Modelo, U_inf, coord_turbina, n, coord_random)
        #         U_adentro_disco = np.append(U_adentro_disco, U)
        #         count = count + U**2
        #     U_medio_disco = np.mean(U_adentro_disco)
        #     print(U_medio_disco)
        #     c_T_tab = self.c_T_tabulado(U_medio_disco)
        #     volume = (self.d_0)**2
        #     integral_U_cuadrado = (volume * count)/N
        #     T_turbina = c_T_tab * integral_U_cuadrado   # lo dividi por (0.5 * rho) porque luego dividire por eso
        #     T_disponible = (U_medio_disco)**2 * (np.pi*(self.d_0/2)**2)     # lo dividi por (0.5 * rho) porque luego multiplicare por eso
        #     c_T = T_turbina / T_disponible
        #     print ('c_T calculado:', c_T)
        #     print ('c_T_tab:', c_T_tab)
        #
        # turbina.calcular_c_T(gaussiana, u_inf, coord_turbina, n)
        # # u_coord = u_coord * (1 - deficit_normalizado_en_coord)
        # print "index =", index
        # print 'deficit_normalizado_en_coord_por_[index] =', deficit_normalizado_en_coord[index]
        # index = index + 1

    # return u_coord

# problema: se me va el indice
# habria que hacer algo como un u_disco = [u.coord1, u.coord2, ...] donde coord1, coord2, etc sean random

# # test
# gaussiana = Gaussiana()
# turbina_1 = Turbina_Paper(Coord(np.array([0,0,100])))
# turbina_2 = Turbina_Paper(Coord(np.array([4,0,100])))
# turbina_3 = Turbina_Paper(Coord(np.array([5,0,100])))
# parque_de_turbinas = Parque_de_turbinas([turbina_1, turbina_2, turbina_3])
# u_inf = 10
# parque_de_turbinas.inicializar_parque(u_inf)
# u = U()
# coord = Coord(np.array([6,0,100]))
# u.coord = calcular_u_en_coord(gaussiana, u_inf, coord, parque_de_turbinas)
# print u.coord
