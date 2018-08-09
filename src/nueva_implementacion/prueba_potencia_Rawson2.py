# coding=utf-8

from __future__ import division
import numpy as np
from numpy import exp
import matplotlib.pyplot as plt

from Gaussiana import Gaussiana   # Gaussiana pertenece a la clase Modelo
from Frandsen import Frandsen
from Jensen import Jensen
from Parque_de_turbinas import Parque_de_turbinas
from Turbina_Rawson import Turbina_Rawson
from Coord import Coord
from Estela import Estela
from U_inf import U_inf
from calcular_u_en_coord import calcular_u_en_coord

"""
Para verificar los valores de potencia obtenidos (para el Parque Rawson?? o para
que ejemplo?? Blind Test tiene potencia?? porque el capitulo del parque rawson
viene despues del de potencia) comparamos los resultados de los modelos reducidos
con: las mediciones in situ y las corridas de OpenFOAM.

Blind Test: tiene curva de c_P pero me parece que no tiene sentido calcular la potencia.
Parque Rawson: gonza tiene mediciones y resultados de OpenFOAM para 2 turbinas alineadas
de potencia en funcion del angulo con el que incide el viento.

Entonces los casos que estudiaremos seran:
. una turbina de Rawson (como para validar los resultados de potencia)
. dos turbinas de Rawson alineadas separadas por 5 diametros
    * calcular la relacion entre la potencia de la turbina_1/turbina_0 para
    distintas direcciones de viento, para esto hay que crear la matriz de rotacion

"""

# comparo Mediciones con modelo reducido
# casos:
# * caso 1 : turbina 7 (BARLOVENTO) - turbina 8 (SOTAVENTO)
#            DISTANCIA = 4.7d ----------------                                  ANGULO = 320
# * caso 2 : turbina 9 (BARLOVENTO) - turbina 7 (medio) - turbina 6 (SOTAVENTO)
#            DISTANCIA = 5.7d ----------------                                  ANGULO = 25
#            DISTANCIA = 10.5d ----------------------------------               ANGULO = 25

from scipy.stats import chisquare

gaussiana = Gaussiana()
u_inf = U_inf()
u_inf.coord_mast = 8
u_inf.perfil = 'log'
N = 300
z_mast = 80

x_o = 20*90
y_o = 0
z_o = 80

coord = Coord(np.array([x_o, y_o, z_o]))

z_0 = 0.1

turbina_0 = Turbina_Rawson(Coord(np.array([0,0,80]))) # chequear altura del hub
D = turbina_0.d_0

import csv

ratio_medido = []

# 1)
################################################################################
# ratio_medido_47 = np.array([1.06219171,  1.07058913,  1.07448795,  1.06899792,  1.07393039,
#         1.07319126,  1.05896054,  1.05593952,  1.04820386,  1.01344593,
#         0.99996563,  1.00132968,  1.00803974,  1.01571349,  1.00968384,
#         0.99638301,  0.98092463,  0.96060086,  0.93933783,  0.9402352 ,
#         0.9045184 ,  0.81210061,  0.74905623,  0.6835521 ,  0.62492257,
#         0.62884904,  0.65319587,  0.63303361,  0.57095635,  0.53425566,
#         0.55455629,  0.58167473,  0.5786316 ,  0.56829723,  0.60249594,
#         0.67251558,  0.70437986,  0.68819865,  0.64452865,  0.65917993,
#         0.72801739,  0.77669829,  0.78904856,  0.78748229,  0.73959143,
#         0.69108669,  0.75112199,  0.84839215,  0.928382  ,  0.99292241,
#         0.97395039,  0.92333507,  0.95293423,  0.99777742,  0.99865363,
#         1.00339194,  1.02605801,  1.01621478,  0.99238505,  1.00860384,
#         1.03304544])
#
# ratio_medido_57 = np.array([0.99126019,  0.99978216,  0.97561013,  0.96540025,  0.98635671,
#         1.00056743,  1.02325629,  1.03683874,  1.06877097,  1.18240941,
#         1.29733647,  1.18630939,  1.03465156,  0.98988452,  1.03415907,
#         1.08785321,  1.09465715,  1.10111132,  1.09194559,  0.99756379,
#         0.87952202,  0.82368932,  0.7860844 ,  0.79339295,  0.86602489,
#         0.86060762,  0.77864787,  0.67913849,  0.6182711 ,  0.60254093,
#         0.59886363,  0.61552625,  0.62898349,  0.63953962,  0.64947816,
#         0.66659927,  0.70408107,  0.7290905 ,  0.75710238,  0.77729683,
#         0.79706765,  0.83016455,  0.840074  ,  0.85538834,  0.89447898,
#         0.92221286,  0.90461667,  0.87380041,  0.91450511,  0.99704113,
#         1.01166148,  0.98185436,  0.98957991,  1.00906588,  1.01908759,
#         1.03435032,  1.0124844 ,  0.97647185,  0.99681935,  1.06672044,
#         1.11192966])

# distancia = 4.7
# print distancia
#
# tur_down = 7
# tur_up = 8
# centro = 320
#
# medido = np.loadtxt('med_{}_{}_{}.csv'.format(tur_down, tur_up, centro), delimiter = ' ')
# ratio_medido = medido[1,320-30:320+31]
#
# CFD = np.loadtxt('cfd_{}_{}_{}.csv'.format(tur_down, tur_up, centro), delimiter = ' ')
# angulos_CFD = CFD[0,:]
# ratio_CFD = CFD[1,:]
#
#
# precision_ang = 1
# angulos = np.arange(-30, 30 + precision_ang, precision_ang)
#
# iters_estadistica = 100
#
# metodo_array = ['linear', 'rss', 'largest']
# metodo_label = {'linear': 'Lineal', 'rss': 'Cuadratica', 'largest':'Dominante'}
#
# chi_array = []
# p_array = []
#
# for metodo_superposicion in metodo_array:
#     turbina_0 = Turbina_Rawson(Coord(np.array([0,0,80]))) # chequear altura del hub
#     turbina_1 = Turbina_Rawson(Coord(np.array([distancia*D,0,80]))) # chequear altura del hub
#     parque_de_turbinas = Parque_de_turbinas([turbina_0, turbina_1], z_0, z_mast)
#     parque_de_turbinas.rotar(-30)
#     array_ratio = np.zeros(iters_estadistica)
#     sigma_ratio = []
#     ratio = []
#     for theta in angulos:
#         for i in range(iters_estadistica):
#             data_prueba = calcular_u_en_coord(gaussiana, metodo_superposicion, coord, parque_de_turbinas, u_inf, N)
#             array_ratio[i] = turbina_1.potencia/turbina_0.potencia
#         ratio = np.append(ratio, np.mean(array_ratio))
#         sigma_ratio = np.append(sigma_ratio, np.std(array_ratio))
#         parque_de_turbinas.rotar(precision_ang)
#         # print theta
#
#     plt.figure(figsize=(10,10))
#     plt.plot(angulos, ratio, label = u'Modelo analítico', linewidth=3)
#     plt.fill_between(angulos, ratio-sigma_ratio, ratio+sigma_ratio, alpha=0.3)
#     plt.xlabel(u'dirección[º]', fontsize=25)
#     plt.ylabel(r'$P_{BARLOVENTO} / P_{SOTAVENTO}$', fontsize=30)
#     plt.plot(angulos, ratio_medido, 'o', label = 'Mediciones', markersize=10)
#     plt.plot(angulos_CFD, ratio_CFD, '--', label='OpenFOAM (CFD)', linewidth = 3)
#     plt.xlim(-30,30)
#     plt.ylim(0.2,1.2)
#     plt.xticks(fontsize=22)
#     plt.yticks(fontsize=22)
#     plt.grid()
#     plt.legend(fontsize=18, loc= 'lower right')
#     chi, p = chisquare(ratio, f_exp=ratio_medido)
#     chi_array = np.append(chi_array, chi)
#     p_array = np.append(p_array, p)
#     plt.savefig('potencia_{}_{}_CFD.pdf'.format(metodo_label[metodo_superposicion], str(int(distancia))))
#     # plt.show()
#
# print 'chi_array = ',chi_array
# print 'p_array = ',p_array
#
# # 2)
# ################################################################################
# # +39
#
# distancia = 5.7
# print distancia
#
# tur_down = 7
# tur_up = 9
# centro = 25
#
# medido = np.loadtxt('med_{}_{}_{}.csv'.format(tur_down, tur_up, centro), delimiter = ' ')
# ratio_medido = np.concatenate((medido[1, -5:], medido[1, 0:25+31]), axis=0)
#
# CFD = np.loadtxt('cfd_{}_{}_{}.csv'.format(tur_down, tur_up, centro), delimiter = ' ')
# angulos_CFD = CFD[0,:]
# ratio_CFD = CFD[1,:]
#
#
# precision_ang = 1
# angulos = np.arange(-30, 30 + precision_ang, precision_ang)
#
# iters_estadistica = 100
#
# metodo_array = ['linear', 'rss', 'largest']
# metodo_label = {'linear': 'Lineal', 'rss': 'Cuadratica', 'largest':'Dominante'}
#
# chi_array = []
# p_array = []
#
# for metodo_superposicion in metodo_array:
#     turbina_0 = Turbina_Rawson(Coord(np.array([0,0,80]))) # chequear altura del hub
#     turbina_1 = Turbina_Rawson(Coord(np.array([distancia*D,0,80]))) # chequear altura del hub
#     parque_de_turbinas = Parque_de_turbinas([turbina_0, turbina_1], z_0, z_mast)
#     parque_de_turbinas.rotar(-30)
#     array_ratio = np.zeros(iters_estadistica)
#     sigma_ratio = []
#     ratio = []
#     for theta in angulos:
#         for i in range(iters_estadistica):
#             data_prueba = calcular_u_en_coord(gaussiana, metodo_superposicion, coord, parque_de_turbinas, u_inf, N)
#             array_ratio[i] = turbina_1.potencia/turbina_0.potencia
#         ratio = np.append(ratio, np.mean(array_ratio))
#         sigma_ratio = np.append(sigma_ratio, np.std(array_ratio))
#         parque_de_turbinas.rotar(precision_ang)
#         # print theta
#
#     plt.figure(figsize=(10,10))
#     plt.plot(angulos, ratio, label = u'Modelo analítico', linewidth=3)
#     plt.fill_between(angulos, ratio-sigma_ratio, ratio+sigma_ratio, alpha=0.3)
#     plt.xlabel(u'dirección[º]', fontsize=25)
#     plt.ylabel(r'$P_{BARLOVENTO} / P_{SOTAVENTO}$', fontsize=30)
#     plt.plot(angulos, ratio_medido, 'o', label = 'Mediciones', markersize=10)
#     plt.plot(angulos_CFD, ratio_CFD, '--', label='OpenFOAM (CFD)', linewidth = 3)
#     plt.xlim(-30,30)
#     plt.ylim(0.2,1.2)
#     plt.xticks(fontsize=22)
#     plt.yticks(fontsize=22)
#     plt.grid()
#     plt.legend(fontsize=18, loc= 'lower right')
#     chi, p = chisquare(ratio, f_exp=ratio_medido)
#     chi_array = np.append(chi_array, chi)
#     p_array = np.append(p_array, p)
#     plt.savefig('potencia_{}_{}_CFD.pdf'.format(metodo_label[metodo_superposicion], str(int(distancia))))
#     # plt.show()
#
# print 'chi_array = ',chi_array
# print 'p_array = ',p_array

# 3)
################################################################################

distancia_1 = 5.7
distancia_2 = 10.5
print distancia_2

tur_down = 6
tur_up = 9
centro = 25

medido = np.loadtxt('med_{}_{}_{}.csv'.format(tur_down, tur_up, centro), delimiter = ' ')
ratio_medido = np.concatenate((medido[1, -5:], medido[1, 0:25+31]), axis=0)

CFD = np.loadtxt('cfd_{}_{}_{}.csv'.format(tur_down, tur_up, centro), delimiter = ' ')
angulos_CFD = CFD[0,:]
ratio_CFD = CFD[1,:]


precision_ang = 1
angulos = np.arange(-30, 30 + precision_ang, precision_ang)

iters_estadistica = 100

metodo_array = ['linear', 'rss', 'largest']
metodo_label = {'linear': 'Lineal', 'rss': 'Cuadratica', 'largest':'Dominante'}

chi_array = []
p_array = []

for metodo_superposicion in metodo_array:
    turbina_0 = Turbina_Rawson(Coord(np.array([0,0,80]))) # chequear altura del hub
    turbina_1 = Turbina_Rawson(Coord(np.array([distancia_1*D,0,80]))) # chequear altura del hub
    turbina_2 = Turbina_Rawson(Coord(np.array([distancia_2*D,0,80]))) # chequear altura del hub
    parque_de_turbinas = Parque_de_turbinas([turbina_0, turbina_1, turbina_2], z_0, z_mast)
    parque_de_turbinas.rotar(-30)
    array_ratio = np.zeros(iters_estadistica)
    sigma_ratio = []
    ratio = []
    for theta in angulos:
        for i in range(iters_estadistica):
            data_prueba = calcular_u_en_coord(gaussiana, metodo_superposicion, coord, parque_de_turbinas, u_inf, N)
            array_ratio[i] = turbina_2.potencia/turbina_0.potencia
        ratio = np.append(ratio, np.mean(array_ratio))
        sigma_ratio = np.append(sigma_ratio, np.std(array_ratio))
        parque_de_turbinas.rotar(precision_ang)
        # print theta

    plt.figure(figsize=(10,10))
    plt.plot(angulos, ratio, label = u'Modelo analítico', linewidth=3)
    plt.fill_between(angulos, ratio-sigma_ratio, ratio+sigma_ratio, alpha=0.3)
    plt.xlabel(u'dirección[º]', fontsize=25)
    plt.ylabel(r'$P_{BARLOVENTO} / P_{SOTAVENTO}$', fontsize=30)
    plt.plot(angulos, ratio_medido, 'o', label = 'Mediciones', markersize=10)
    plt.plot(angulos_CFD, ratio_CFD, '--', label='OpenFOAM (CFD)', linewidth = 3)
    plt.xlim(-30,30)
    plt.ylim(0.2,1.2)
    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    plt.grid()
    plt.legend(fontsize=18, loc= 'lower right')
    chi, p = chisquare(ratio, f_exp=ratio_medido)
    chi_array = np.append(chi_array, chi)
    p_array = np.append(p_array, p)
    plt.savefig('potencia_{}_{}_CFD.pdf'.format(metodo_label[metodo_superposicion], str(int(distancia_2))))
    # plt.show()

print 'chi_array = ',chi_array
print 'p_array = ',p_array
