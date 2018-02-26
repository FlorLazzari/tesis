from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
# coding=utf-8

from Gaussiana import Gaussiana   # Gaussiana pertenece a la clase Modelo
from Parque_de_turbinas import Parque_de_turbinas
from Coord import Coord
from Estela import Estela
from U_inf import U_inf
from calcular_u_en_coord import calcular_u_en_coord

"""
A continuacion tengo los siguientes problemas:

    -'AttributeError: max must be larger than min in range parameter.' --> esto me parece que
    esta apareciendo porque en p_turbina hay nans, falta ver: por que aparecen los nans y
    como evitarlos o en caso de no poder evitarlos como borrarlos del array

    -para evaluar correctamente el tiempo de procesamiento hay que comentar las lineas del Histograma,
    por que esta pasando esto?

Cosas a tener en cuenta:

Cada Histograma muestra la distribucion de p_turbina para un dado orden de
montecarlo N (solo se estudio para la turbina 0 por simplicidad, faltaria estudiar el resto de las turbinas)

El SEM relativo esta dando demasiado bajo, faltaria verificar que esto es consistente con la forma del Histograma

"""


# test:
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

z_0 = 0.01

parque_de_turbinas = Parque_de_turbinas([turbina_1, turbina_2, turbina_3], z_0)

iters_i = 50
iters_j = len(parque_de_turbinas.turbinas)
p_turbina = np.zeros([iters_i, iters_j])
p_parque = np.zeros(iters_i)

p_media_por_turbina = np.zeros(iters_j)
# modulo = np.zeros([iters_i, iters_j])
# rms = np.zeros(iters_j)
N_arreglo = []
iters_exp = 5
error_relativo = np.zeros([iters_exp, iters_j])
p_media = np.zeros(iters_j)
numerador = np.zeros(iters_j)

import time
tiempo_procesamiento = np.zeros([iters_i, iters_exp])
tiempo_procesamiento_medio = np.zeros(iters_exp)

for exponente in range(iters_exp):
    N = 2**(exponente + 1)
    N_arreglo.append(N)
    print 'N = ',N
    for i in range(iters_i):
        tic = time.clock()
        calcular_u_en_coord(gaussiana, 'largest', coord, parque_de_turbinas, u_inf, N)
        toc = time.clock()
        tiempo_procesamiento[i, exponente] = toc - tic
        # # ahora quiero calcular la potencia extraida por el parque
        for j in range(iters_j):
            turbina = parque_de_turbinas.turbinas[j]
            parque_de_turbinas.potencia += turbina.potencia
            p_turbina[i,j] = turbina.potencia
            p_media[j] = np.mean(p_turbina[:,j])
            numerador[j] = np.std(p_turbina[:,j])/np.sqrt(iters_i)
            # error_relativo[exponente, j] = numerador[j]/p_media[j]
            error_relativo[exponente, j] = numerador[j]/p_media[j]

    tiempo_procesamiento_medio[exponente] = np.mean(tiempo_procesamiento[:, exponente])

    plt.title('Histograma de distribucion de potencia para turbina {}'.format(0), fontsize=15)
    plt.hist(p_turbina[:, 0], normed=True)
    # plt.xlim([1200, 1600])
    plt.xlim([0, 1600])
    # plt.xlabel('Tiempo[s]', fontsize=15)
    # plt.ylabel('SEM', fontsize=15)
    plt.grid()
    plt.show()


plt.title('SEM para distintos N', fontsize=15)
plt.plot(N_arreglo, error_relativo[:,0], label='turbina 0')
plt.plot(N_arreglo, error_relativo[:,1], label='turbina 1')
plt.plot(N_arreglo, error_relativo[:,2], label='turbina 2')
plt.plot(N_arreglo, np.ones(len(N_arreglo)), '--')
plt.xticks(N_arreglo)
plt.xlabel('N', fontsize=15)
plt.ylabel('SEM', fontsize=15)
plt.legend()
plt.grid()
plt.show()

plt.title('Tiempo de procesamiento para distintos N', fontsize=15)
plt.plot(N_arreglo, tiempo_procesamiento_medio, 'x')
plt.xlabel('N', fontsize=15)
plt.xticks(N_arreglo)
plt.ylabel('Tiempo[s]', fontsize=15)
plt.grid()
plt.show()


plt.title('SEM en funcion del Tiempo de procesamiento', fontsize=15)
plt.plot(tiempo_procesamiento_medio, error_relativo[:,0], 'x')
plt.xlabel('Tiempo[s]', fontsize=15)
plt.ylabel('SEM', fontsize=15)
plt.grid()
plt.show()





# import profile
# profile.run('calcular_u_en_coord(gaussiana, coord, parque_de_turbinas, u_inf)')
