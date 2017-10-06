from __future__ import division
# coding=utf-8

from Modelo_2 import Modelo
from Gaussiana_2 import Gaussiana
from Parque_de_turbinas import Parque_de_turbinas
from Turbina_Marca import Turbina_Marca
from Turbina_2 import Turbina
from U import U
from Coord import Coord
import numpy as np
from numpy import exp
from Estela import Estela
from decimal import Decimal


def calcular_u_en_coord(modelo, coord, parque_de_turbinas, u_inf):

    turbinas_a_la_izquierda_de_coord = parque_de_turbinas.turbinas_a_la_izquierda_de_una_coord(coord)
    deficit_normalizado_en_coord = []
    parque_de_turbinas.inicializar_parque(u_inf.coord_hub)

    # calculo c_T teniendo en cuenta la interaccion de las otras turbinas
    for turbina_selec in turbinas_a_la_izquierda_de_coord:
        print '-----------------------------------------------------------------'
        print 'coordenadas de TURBINA SELECCIONADA:'
        print 'x =', turbina_selec.coord.x, ', y =', turbina_selec.coord.y, ', z =', turbina_selec.coord.y
        # orden del montecarlo
        N = 500
        coord_random_arreglo = turbina_selec.generar_coord_random(N)
        turbinas_a_la_izquierda_de_turbina_selec = parque_de_turbinas.turbinas_a_la_izquierda_de_una_coord(turbina_selec.coord)
        cantidad_turbinas_izquierda_de_selec = len(turbinas_a_la_izquierda_de_turbina_selec)
        print "cantidad de turbinas a la IZQUIERDA de TURBINA SELEC:", cantidad_turbinas_izquierda_de_selec
        if cantidad_turbinas_izquierda_de_selec==0:
            turbina_virtual = Turbina(turbina_selec.d_0, Coord(np.array([turbina_selec.coord.x,turbina_selec.coord.y,turbina_selec.coord.z])))
            turbina_virtual.c_T = 0
            turbinas_a_la_izquierda_de_turbina_selec = [turbina_virtual]
        arreglo_deficit = []
        for turbina in turbinas_a_la_izquierda_de_turbina_selec:
            print 'coordenadas de TURBINA:'
            print 'x =', turbina.coord.x, ', y = ', turbina.coord.y, ', z =', turbina.coord.y
            # ahora calculo la estela de turbina sobre turbina_selec
            coord_random_adentro_disco = []
            print 'c_T de TURBINA = ',turbina.c_T
            for coord_random in coord_random_arreglo:
                if ((coord_random.y-turbina_selec.coord.y)**2 + (coord_random.z-turbina_selec.coord.z)**2 < (turbina_selec.d_0/2)**2):
                    deficit_normalizado_en_coord_random = modelo.evaluar_deficit_normalizado(turbina, coord_random)
                    arreglo_deficit = np.append(arreglo_deficit, deficit_normalizado_en_coord_random)
                    coord_random_adentro_disco = np.append(coord_random_adentro_disco, coord_random)
        cantidad_coords_adentro_disco = len(coord_random_adentro_disco)
        estela_sobre_turbina_selec = Estela(arreglo_deficit, cantidad_coords_adentro_disco, cantidad_turbinas_izquierda_de_selec)
        estela_sobre_turbina_selec.merge()

        turbina_selec.calcular_c_T(estela_sobre_turbina_selec, coord_random_adentro_disco, parque_de_turbinas.z_0, u_inf, N)
        turbina_selec.calcular_c_P(estela_sobre_turbina_selec, coord_random_adentro_disco, parque_de_turbinas.z_0, u_inf, N)

        print 'c_T de TURBINA SELECCIONADA = ',turbina_selec.c_T
        print 'potencia generada por TURBINA SELECCIONADA = %.2e' % Decimal(turbina_selec.potencia)

        # calculo en la coord
        deficit_normalizado_en_coord_contribucion_turbina_selec = modelo.evaluar_deficit_normalizado(turbina_selec, coord)
        deficit_normalizado_en_coord.append(deficit_normalizado_en_coord_contribucion_turbina_selec)
    estela_sobre_coord = Estela(deficit_normalizado_en_coord, 1, len(turbinas_a_la_izquierda_de_coord))
    estela_sobre_coord.merge()

    u_inf.coord = coord
    # tome a la primer turbina como la altura donde se mide la u_inf (en principio
    # no tiene mucha relevancia ya que las turbinas tienen todas la misma altura,
    # en caso de hacer un parque con otra topologia entonces habria que pensar bien esto)
    u_inf.perfil_flujo_base(parque_de_turbinas.turbinas[0].coord.z, z_0)
    u = u_inf.coord * (1 - estela_sobre_coord.mergeada)
    print '************************************************************************'
    print 'coordenada en la que quiero calcular el viento: x =',coord.x, ', y =',coord.y, ', z =',coord.z
    print 'modulo del viento en la coordenada buscada:  u =', u[0]
    print 'modulo del viento en la coordenada buscada SIN TURBINAS:  u_inf =',u_inf.coord

# prueba:
from Turbina_Rawson import Turbina_Rawson
from U_inf import U_inf
gaussiana = Gaussiana()
u_inf = U_inf()
u_inf.coord_hub = 10
u_inf.perfil = 'log'
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


# ahora quiero calcular la potencia extraida por el parque
for turbina in parque_de_turbinas.turbinas:
    parque_de_turbinas.potencia += turbina.potencia
    # print turbina.potencia

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
