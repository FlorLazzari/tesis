from __future__ import division
import numpy as np
# coding=utf-8

from Modelo import Modelo
from Parque_de_turbinas import Parque_de_turbinas
from Turbina import Turbina
from Coord import Coord
from Estela import Estela

def calcular_u_en_coord(modelo_deficit, metodo_superposicion, coord, parque_de_turbinas, u_inf, N):

    parque_de_turbinas.inicializar_parque(u_inf.coord_hub)
    turbinas_a_la_izquierda_de_coord = parque_de_turbinas.turbinas_a_la_izquierda_de_una_coord(coord)
    deficit_normalizado_en_coord = []

    # calculo c_T teniendo en cuenta la interaccion de las otras turbinas


    for turbina_selec in turbinas_a_la_izquierda_de_coord:
        # print '-----------------------------------------------------------------'
        # print 'coordenadas de TURBINA SELECCIONADA:'
        # print 'x =', turbina_selec.coord.x, ', y =', turbina_selec.coord.y, ', z =', turbina_selec.coord.y
        coord_random_arreglo = turbina_selec.generar_coord_random(N)
        turbinas_a_la_izquierda_de_turbina_selec = parque_de_turbinas.turbinas_a_la_izquierda_de_una_coord(turbina_selec.coord)
        cantidad_turbinas_izquierda_de_selec = len(turbinas_a_la_izquierda_de_turbina_selec)

        # print "cantidad de turbinas a la IZQUIERDA de TURBINA SELEC:", cantidad_turbinas_izquierda_de_selec
        if cantidad_turbinas_izquierda_de_selec==0:
            turbina_virtual = Turbina(turbina_selec.d_0, Coord(np.array([turbina_selec.coord.x,turbina_selec.coord.y,turbina_selec.coord.z])))
            turbina_virtual.c_T = 0
            turbinas_a_la_izquierda_de_turbina_selec = [turbina_virtual]
        arreglo_deficit = []


        for turbina in turbinas_a_la_izquierda_de_turbina_selec:

            # print 'coordenadas de TURBINA:'
            # print 'x =', turbina.coord.x, ', y = ', turbina.coord.y, ', z =', turbina.coord.y
            # ahora calculo la estela de turbina sobre turbina_selec
            coord_random_adentro_disco = []
            # print 'c_T de TURBINA = ',turbina.c_T
            for coord_random in coord_random_arreglo:
                if ((coord_random.y-turbina_selec.coord.y)**2 + (coord_random.z-turbina_selec.coord.z)**2 < (turbina_selec.d_0/2)**2):
                    deficit_normalizado_en_coord_random = modelo_deficit.evaluar_deficit_normalizado(turbina, coord_random)
                    arreglo_deficit = np.append(arreglo_deficit, deficit_normalizado_en_coord_random)
                    coord_random_adentro_disco = np.append(coord_random_adentro_disco, coord_random)
        cantidad_coords_adentro_disco = len(coord_random_adentro_disco)
        estela_sobre_turbina_selec = Estela(arreglo_deficit, cantidad_coords_adentro_disco, cantidad_turbinas_izquierda_de_selec)



        estela_sobre_turbina_selec.merge(metodo_superposicion)
        turbina_selec.calcular_c_T(estela_sobre_turbina_selec, coord_random_adentro_disco, parque_de_turbinas.z_0, u_inf, N)
        # turbina_selec.calcular_c_P(estela_sobre_turbina_selec, coord_random_adentro_disco, parque_de_turbinas.z_0, u_inf, N)
        turbina_selec.calcular_P(estela_sobre_turbina_selec, coord_random_adentro_disco, parque_de_turbinas.z_0, u_inf, N)

        # print turbina_selec.c_T
        # print 'turbina seleccionada = ', turbina_selec
        # print 'c_T de TURBINA SELECCIONADA = ',turbina_selec.c_T
        # from decimal import Decimal
        # print 'potencia generada por TURBINA SELECCIONADA = %.2e' % Decimal(turbina_selec.potencia)

        # calculo en la coord
        deficit_normalizado_en_coord_contribucion_turbina_selec = modelo_deficit.evaluar_deficit_normalizado(turbina_selec, coord)
        deficit_normalizado_en_coord.append(deficit_normalizado_en_coord_contribucion_turbina_selec)
    estela_sobre_coord = Estela(deficit_normalizado_en_coord, 1, len(turbinas_a_la_izquierda_de_coord))
    estela_sobre_coord.merge(metodo_superposicion)
    u_inf.coord = coord
    # tome a la primer turbina como la altura donde se mide la u_inf (en principio
    # no tiene mucha relevancia ya que las turbinas tienen todas la misma altura,
    # en caso de hacer un parque con otra topologia entonces habria que pensar bien esto)
    u_inf.perfil_flujo_base(parque_de_turbinas.turbinas[0].coord.z, parque_de_turbinas.z_0)
    u = u_inf.coord * (1 - estela_sobre_coord.mergeada[0])

    # print '************************************************************************'
    # print 'coordenada en la que quiero calcular el viento: x =',coord.x, ', y =',coord.y, ', z =',coord.z
    # print 'modulo del viento en la coordenada buscada:  u =', u
    # print 'modulo del viento en la coordenada buscada SIN TURBINAS:  u_inf =',u_inf.coord
    return u
