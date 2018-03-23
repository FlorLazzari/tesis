from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# coding=utf-8

from Gaussiana import Gaussiana   # Gaussiana pertenece a la clase Modelo
from Parque_de_turbinas import Parque_de_turbinas
from Coord import Coord
from Estela import Estela
from U_inf import U_inf
from calcular_u_en_coord import calcular_u_en_coord

"""
. Calculo potencia para las turbinas Rawson 1, 2 y 3 ALINEADAS con una separacion de 7 diametros
. Para cada N de MC hago 100 corridas
. Para cada corrida calculo la norma de la potencia = (p1**2 + p2**2 + p3**2)**0.5
. Calculo la dispersion sigma de la norma de la potencia para cada N
. Calculo la derivada numerica = diff(sigma) / diff(N)

Finalmente, el criterio para cortar el MC sera cuando la derivada numerica se plancha


A continuacion tengo los siguientes PROBLEMAS:

    -'AttributeError: max must be larger than min in range parameter.' --> esto me parece que
    esta apareciendo porque en p_turbina hay nans, falta ver: por que aparecen los nans y
    como evitarlos o en caso de no poder evitarlos como borrarlos del array

        * Como solucion provisoria lo que estoy haciendo es borrando los nans del array
        con dropna() de pandas

    -para evaluar correctamente el tiempo de procesamiento hay que comentar las lineas del Histograma,
    por que esta pasando esto?


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

iters_corrida = 100
iters_turbina = len(parque_de_turbinas.turbinas)
p_turbina = np.zeros([iters_corrida, iters_turbina])
p_parque = np.zeros(iters_corrida)

p_media_por_turbina = np.zeros(iters_turbina)
# modulo = np.zeros([iters_corrida, iters_turbina])
# rms = np.zeros(iters_turbina)
N_arreglo = []
iters_exp = 9
SEM_relativo = np.zeros([iters_exp, iters_turbina])
p_media = np.zeros(iters_turbina)
SEM = np.zeros([iters_exp, iters_turbina])
norma_p = np.zeros([iters_exp, iters_corrida])
sigma_norma_p = np.zeros(iters_exp)
norma_p_media = np.zeros(iters_exp)

import time
tiempo_procesamiento = np.zeros([iters_corrida, iters_exp])
tiempo_procesamiento_medio = np.zeros(iters_exp)

for exponente in range(iters_exp):
    N = 2**(exponente + 1)
    N_arreglo.append(N)
    print 'N = ',N
    for corrida in range(iters_corrida):
        tic = time.clock()
        calcular_u_en_coord(gaussiana, 'largest', coord, parque_de_turbinas, u_inf, N)
        toc = time.clock()
        tiempo_procesamiento[corrida, exponente] = toc - tic
        # # ahora quiero calcular la potencia extraida por el parque
        for numero_turbina in range(iters_turbina):
            turbina = parque_de_turbinas.turbinas[numero_turbina]
            p_turbina[corrida, numero_turbina] = turbina.potencia

        norma_p[exponente, corrida] = (p_turbina[corrida, 0]**2 + p_turbina[corrida, 1]**2 + p_turbina[corrida, 2]**2)**0.5

        # norma_p_media[exponente] = np.mean(norma_p[exponente, :])
        norma_p[exponente, corrida] = ((norma_p[exponente, corrida])**0.5) #/ norma_p_media[exponente]

    sigma_norma_p[exponente] = np.std(norma_p[exponente, :])

    tiempo_procesamiento_medio[exponente] = np.mean(tiempo_procesamiento[:, exponente])

    # NaN's are not handled well by the hist function of matplotlib
    serie = pd.Series(norma_p[exponente, :])
    fig, ax = plt.subplots()
    ax.hist(serie.dropna(), bins = np.linspace(40, 52, 30))#, alpha=0.9)
    plt.title('Histograma de distribucion de la norma de la potencia para N = {}'.format(exponente), fontsize=15)
    plt.xlim([40, 52])
    plt.ylim([0, 100])
    plt.grid()
    plt.show()

abs_dsigma_dN = np.abs(np.diff(sigma_norma_p) / np.diff(N_arreglo))

plt.title(r'$\sigma$ de la norma de p para distintos N', fontsize=15)
plt.plot(N_arreglo, sigma_norma_p, 'o')
plt.xticks(N_arreglo)
plt.xlabel('N', fontsize=15)
plt.ylabel(r'$\sigma$', fontsize=15)
plt.legend()
plt.grid()
plt.show()

plt.title(r'Modulo de la derivada numerica de $\sigma$', fontsize=15)
plt.plot(N_arreglo[+1:], abs_dsigma_dN, 'o')
plt.xticks(N_arreglo[+1:])
plt.xlabel('N', fontsize=15)
plt.ylabel(r'$|\frac{d\sigma}{dN}|$', fontsize=15)
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


plt.title(r'Modulo de la derivada numerica de $\sigma$ en funcion del tiempo de procesamiento', fontsize=15)
plt.plot(abs_dsigma_dN, tiempo_procesamiento_medio[+1:], 'x')
plt.xlabel(r'$|\frac{d\sigma}{dN}|$', fontsize=15)
plt.ylabel('Tiempo[s]', fontsize=15)
plt.grid()
plt.show()
