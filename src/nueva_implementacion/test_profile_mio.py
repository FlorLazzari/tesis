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
import matplotlib.pyplot as plt
from numpy import exp
from Estela import Estela
from decimal import Decimal
from U_inf import U_inf
from calcular_u_en_coord_2 import calcular_u_en_coord

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

# turbina_1.c_T = 0.5
# turbina_2.c_T = 0.5
z_0 = 0.01

parque_de_turbinas = Parque_de_turbinas([turbina_1, turbina_2, turbina_3], z_0)

iters_i = 100
iters_j = len(parque_de_turbinas.turbinas)
p_turbina = np.zeros([iters_i, iters_j])
p_parque = np.zeros(iters_i)

from math import sqrt

p_media_por_turbina = np.zeros(iters_j)
modulo = np.zeros([iters_i, iters_j])
rms = np.zeros(iters_j)
N_arreglo = []
iters_exp = 13
error_relativo = np.zeros([iters_exp, iters_j])
p_media = np.zeros(iters_j)
numerador = np.zeros([iters_i,iters_j])

for exponente in range(iters_exp):
    N = 2**(exponente + 1)
    N_arreglo.append(N)
    print 'N = ',N
    for i in range(iters_i):
        calcular_u_en_coord(gaussiana, 'largest', coord, parque_de_turbinas, u_inf, N)
        # # ahora quiero calcular la potencia extraida por el parque
        for j in range(iters_j):
            turbina = parque_de_turbinas.turbinas[j]
            parque_de_turbinas.potencia += turbina.potencia
            # print '-'*40
            # print 'Potencia de {}'.format(turbina)
            # print turbina.potencia
            p_turbina[i,j] = turbina.potencia
            print 'iteracion =', i
            print "turbina =", j
            print 'potencia =', turbina.potencia
            # print '*'*40
            # print 'Potencia de todo el Parque'
            # print parque_de_turbinas.potencia
            # p_parque[i] = parque_de_turbinas.potencia
            # parque_de_turbinas.potencia = 0
            # print '\n'
            p_media[j] = np.mean(p_turbina[:,j])
            # rms[j] = np.sqrt(np.mean(np.square(p_turbina[:, j])))
            # error_relativo[exponente, j] = rms[j] / p_media[j]
            numerador[i, j] = np.abs(p_turbina[i, j] - p_media[j])
            print 'p_media =', p_media[j]
            print 'np.abs(p_turbina[i, j] - p_media[j]) =', np.abs(p_turbina[i, j] - p_media[j])
            print 'numerador[i,j] =', numerador[i, j]
            error_relativo[exponente, j] = np.sum(numerador[:,j])/iters_i

plt.plot(N_arreglo, error_relativo[:,0], label='turbina 0')
plt.plot(N_arreglo, error_relativo[:,1], label='turbina 1')
plt.plot(N_arreglo, error_relativo[:,2], label='turbina 2')
plt.legend()
plt.grid()
plt.show()


# import profile
# profile.run('calcular_u_en_coord(gaussiana, coord, parque_de_turbinas, u_inf)')
