from __future__ import division
import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
import itertools
# coding=utf-8

from Gaussiana import Gaussiana
from Jensen import Jensen
from Frandsen import Frandsen
from Larsen import Larsen
from Parque_de_turbinas import Parque_de_turbinas
from Turbina_BlindTest import Turbina_BlindTest
from Coord import Coord
from Estela import Estela
from U_inf import U_inf
from calcular_u_en_coord import calcular_u_en_coord

"""
Tenemos los datos del Turbina_SexbierumWindFarm del parametro U (componente x de la velocidad) para distintas distancias.
Tenemos los modelos reducidos: Gaussiana, Frandsen, Jensen, Larsen.
OpenFOAM??? no tengo nada

A continuacion se grafica comparacion de mediciones de la SexbierumWindFarm y modelos reducidos. (OpenFOAM???)
en graficos de curva
 . a la altura del hub para una turbina en: x = {2.5, 5.5, 8} D
 . en x = 2.5 D a las alturas y = {-0.4, 0, 0.4} D
"""

################################################################################
# las mediciones del SexbierumWindFarm no las tengo como dato, voy a tener que
# usar directamente los graficos

################################################################################
# creo el caso con los modelos reducidos

gaussiana = Gaussiana()
jensen = Jensen()
frandsen = Frandsen()
larsen = Larsen()
modelos = [gaussiana, jensen, frandsen]#, larsen]


u_inf = U_inf()
u_inf.coord_hub = 7.6 # es parametro del BlindTest
u_inf.perfil = 'log'   # por ser un tunel de viento
N = 100

turbina_0 = Turbina_BlindTest(Coord(np.array([0,0,35])))
D = turbina_0.d_0

# z_0 de la superficie
z_0 = 0.1 #?????
parque_de_turbinas = Parque_de_turbinas([turbina_0], z_0)

x_array = [2.5, 5.5, 8]
alpha = np.linspace( (-30 * np.pi) / 180 , (30 * np.pi) / 180 , 500) # ya esta en radianes
z_o = turbina_0.coord.z

for distancia in x_array:
    plt.figure()
    plt.title('x = {}D'.format(distancia))

    for modelo in modelos:

        x_o = distancia * D
        data_prueba = np.zeros(len(alpha))

        for i in range(len(alpha)):

            coord = Coord(np.array([x_o + np.cos(alpha[i]), np.sin(alpha[i]), z_o]))
            data_prueba[i] = calcular_u_en_coord(modelo, 'linear', coord, parque_de_turbinas, u_inf, N)

        plt.plot(alpha * (180/np.pi), data_prueba/u_inf.coord_hub, label= 'Modelo Reducido ({})'.format(type(modelo).__name__))

    # comparo con las mediciocones
    # comparo con OpenFOAM

    # grafico
    plt.xlabel('angulo')
    plt.ylabel('U/U_0')
    plt.legend()
    plt.grid()
    plt.show()
