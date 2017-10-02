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
from Estela import Estela

def calcular_u_en_coord(modelo, coord, parque_de_turbinas, u_inf):

    turbinas_a_la_izquierda_de_coord = parque_de_turbinas.turbinas_a_la_izquierda_de_una_coord(coord)
    deficit_normalizado_en_coord = []
    parque_de_turbinas.inicializar_parque(u_inf.coord_hub)

    # el parque ya esta inicializado, el c_T de la primera turbina esta calculado

    print "c_T primera turbina", parque_de_turbinas.turbinas[0].c_T

    # calculo c_T teniendo en cuenta la interaccion de las otras turbinas

    for turbina_selec in turbinas_a_la_izquierda_de_coord[1:]:
        print turbina_selec
        # orden del montecarlo
        N = 500
        coord_random_arreglo = turbina_selec.generar_coord_random(N)
        turbinas_a_la_izquierda_de_turbina_selec = parque_de_turbinas.turbinas_a_la_izquierda_de_una_coord(turbina_selec.coord)
        cantidad_turbinas_izquierda_de_selec = len(turbinas_a_la_izquierda_de_turbina_selec)
        print "cantidad_turbinas_izquierda_de_selec:", cantidad_turbinas_izquierda_de_selec
        arreglo_deficit = []
        for turbina in turbinas_a_la_izquierda_de_turbina_selec:
            # ahora calculo la estela de turbina sobre turbina_selec
            coord_random_adentro_disco = []
            for coord_random in coord_random_arreglo:
                if ((coord_random.y-turbina_selec.coord.y)**2 + (coord_random.z-turbina_selec.coord.z)**2 < (turbina_selec.d_0/2)**2):
                    deficit_normalizado_en_coord_random = modelo.evaluar_deficit_normalizado(turbina, coord_random)
                    arreglo_deficit = np.append(arreglo_deficit, deficit_normalizado_en_coord_random)
                    coord_random_adentro_disco = np.append(coord_random_adentro_disco, coord_random)
        cantidad_coords_adentro_disco = len(coord_random_adentro_disco)
        estela = Estela(arreglo_deficit, cantidad_coords_adentro_disco, cantidad_turbinas_izquierda_de_selec)
        estela.merge()

        turbina_selec.calcular_c_T(estela, coord_random_adentro_disco, u_inf.coord_hub, parque_de_turbinas.z_0, u_inf, N)
#
#         deficit_normalizado_en_coord_contribucion_turbina_selec = modelo.evaluar_deficit_normalizado(parque_de_turbinas.turbina_selec, coord)
#         deficit_normalizado_en_coord = np.append(deficit_normalizado_en_coord_contribucion_turbina_selec)
#         # estas dos cosas estan hechas muy a lo bestia en la clase U, falta terminar eso y probarlo
#         merge_estela()
#         restar_deficit()
#         # u_coord = ??



# prueba:
from Turbina_Rawson import Turbina_Rawson
from U_inf import U_inf
gaussiana = Gaussiana()
u_inf = U_inf()
u_inf.coord_hub = 10
coord = Coord(np.array([60*7*6, 0, 100]))

z_h = 80
turbina_1 = Turbina_Rawson(Coord(np.array([0,0,z_h])))
d_0 = turbina_1.d_0

turbina_2 = Turbina_Rawson(Coord(np.array([d_0*7,0,z_h])))
turbina_3 = Turbina_Rawson(Coord(np.array([d_0*14,0,z_h])))

# turbina_1.c_T = 0.5
# turbina_2.c_T = 0.5
z_0 = 0.01

parque_de_turbinas = Parque_de_turbinas([turbina_1, turbina_2, turbina_3], z_0)
calcular_u_en_coord(gaussiana, coord, parque_de_turbinas, u_inf)


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
