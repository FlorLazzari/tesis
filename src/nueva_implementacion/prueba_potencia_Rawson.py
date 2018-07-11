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
. 5 turbinas alineadas de Barcelona? (gonza tiene datos medidos pero no tiene corrida de openFOAM)

"""

from scipy.stats import chisquare

from scipy import interpolate
def interpolar(x, y, nuevo_x):
    tck = interpolate.splrep(x, y, s=0)
    nuevo_y = interpolate.splev(nuevo_x, tck, der=0)
    return nuevo_y

gaussiana = Gaussiana()
u_inf = U_inf()
u_inf.coord_mast = 8
u_inf.perfil = 'log'
N = 300

z_mast = 80

# casos medidos (elegi unicamente estas mediciones ya que son las que se ven
# menos interferidas por las otras turbinas):
# 4.7D : entre turbina 7 y 8
# 5.7D : entre turbina 8 y 9
# arreglo_distancia = [4.7, 5.7]

turbina_0 = Turbina_Rawson(Coord(np.array([0,0,80]))) # chequear altura del hub
distancia = 4.7
D = turbina_0.d_0
turbina_1 = Turbina_Rawson(Coord(np.array([distancia*D,0,80]))) # chequear altura del hub
# z_0 de la superficie
z_0 = 0.1

x_o = 8*D
y_o = 0
z_o = 80

coord = Coord(np.array([x_o, y_o, z_o]))

# 1)
################################################################################
# comparo OpenFOAM con modelo reducido
# Dos turbinas de Rawson alineadas separadas por 4.7 diametros
#    * calcular la relacion entre la potencia de la turbina_1/turbina_0 para
#    distintas direcciones de viento, para esto hay que crear la matriz de rotacion

ratio_medido_47 = np.array([1.06219171,  1.07058913,  1.07448795,  1.06899792,  1.07393039,
        1.07319126,  1.05896054,  1.05593952,  1.04820386,  1.01344593,
        0.99996563,  1.00132968,  1.00803974,  1.01571349,  1.00968384,
        0.99638301,  0.98092463,  0.96060086,  0.93933783,  0.9402352 ,
        0.9045184 ,  0.81210061,  0.74905623,  0.6835521 ,  0.62492257,
        0.62884904,  0.65319587,  0.63303361,  0.57095635,  0.53425566,
        0.55455629,  0.58167473,  0.5786316 ,  0.56829723,  0.60249594,
        0.67251558,  0.70437986,  0.68819865,  0.64452865,  0.65917993,
        0.72801739,  0.77669829,  0.78904856,  0.78748229,  0.73959143,
        0.69108669,  0.75112199,  0.84839215,  0.928382  ,  0.99292241,
        0.97395039,  0.92333507,  0.95293423,  0.99777742,  0.99865363,
        1.00339194,  1.02605801,  1.01621478,  0.99238505,  1.00860384,
        1.03304544])

ratio_medido_57 = np.array([0.99126019,  0.99978216,  0.97561013,  0.96540025,  0.98635671,
        1.00056743,  1.02325629,  1.03683874,  1.06877097,  1.18240941,
        1.29733647,  1.18630939,  1.03465156,  0.98988452,  1.03415907,
        1.08785321,  1.09465715,  1.10111132,  1.09194559,  0.99756379,
        0.87952202,  0.82368932,  0.7860844 ,  0.79339295,  0.86602489,
        0.86060762,  0.77864787,  0.67913849,  0.6182711 ,  0.60254093,
        0.59886363,  0.61552625,  0.62898349,  0.63953962,  0.64947816,
        0.66659927,  0.70408107,  0.7290905 ,  0.75710238,  0.77729683,
        0.79706765,  0.83016455,  0.840074  ,  0.85538834,  0.89447898,
        0.92221286,  0.90461667,  0.87380041,  0.91450511,  0.99704113,
        1.01166148,  0.98185436,  0.98957991,  1.00906588,  1.01908759,
        1.03435032,  1.0124844 ,  0.97647185,  0.99681935,  1.06672044,
        1.11192966])

precision_ang_medido = 1
angulos_medido = angulos = np.arange(-30, 30 + precision_ang_medido, precision_ang_medido)

precision_ang = 1
angulos = np.arange(-30, 30 + precision_ang, precision_ang)

iters_estadistica = 100

metodo_array = ['linear', 'rss', 'largest']
metodo_label = {'linear': 'Lineal', 'rss': 'Cuadratica', 'largest':'Dominante'}

chi_array = []
p_array = []

for metodo_superposicion in metodo_array:
    turbina_0 = Turbina_Rawson(Coord(np.array([0,0,80]))) # chequear altura del hub
    turbina_1 = Turbina_Rawson(Coord(np.array([distancia*D,0,80]))) # chequear altura del hub
    parque_de_turbinas = Parque_de_turbinas([turbina_0, turbina_1], z_0, z_mast)
    parque_de_turbinas.rotar(-30)
    array_ratio = np.zeros(iters_estadistica)
    sigma_ratio = []
    ratio = []
    for theta in angulos:
        for i in range(iters_estadistica):
            data_prueba = calcular_u_en_coord(gaussiana, metodo_superposicion, coord, parque_de_turbinas, u_inf, N)
            array_ratio[i] = turbina_1.potencia/turbina_0.potencia
        ratio = np.append(ratio, np.mean(array_ratio))
        sigma_ratio = np.append(sigma_ratio, np.std(array_ratio))
        parque_de_turbinas.rotar(precision_ang)
        print theta

    plt.figure(figsize=(10,10))
    # plt.title('Cociente de potencias para dos turbinas separadas por {}D'.format(distancia))
    plt.plot(angulos, ratio, label = u'Modelo analítico', linewidth=3)
    plt.fill_between(angulos, ratio-sigma_ratio, ratio+sigma_ratio, alpha=0.3)
    # plt.errorbar(angulos, ratio, yerr=sigma_ratio, marker='o', markersize=3, label='kdsjghkjng', zorder=0)
    plt.xlabel(u'dirección[º]', fontsize=25)
    plt.ylabel(r'$P_1 / P_0$', fontsize=30)
    plt.plot(dir_medido, ratio_medido, 'o', label = 'Mediciones', markersize=10)
    plt.xlim(-30,30)
    plt.ylim(0.2,1.2)
    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    plt.grid()
    plt.legend(fontsize=16, loc= 'upper right')
    # ratio_interpolado_modelado = interpolar(angulos, ratio, dir_medido)
    # chi, p = chisquare(ratio_interpolado_modelado, f_exp=ratio_medido)
    chi, p = chisquare(ratio, f_exp=ratio_medido)
    chi_array = np.append(chi_array, chi)
    p_array = np.append(p_array, p)
    plt.savefig('potencia_{}_{}'.format(metodo_label[metodo_superposicion], str(int(distancia))), dpi=300)

print 'chi_array = ',chi_array
print 'p_array = ',p_array


frandsen = Frandsen()
jensen = Jensen()

modelo_array = [jensen, frandsen, gaussiana]
modelo_label = {'Jensen': 'Jensen', 'Frandsen': 'Frandsen', 'Gaussiana':'Gaussiana'}


for modelo_deficit in modelo_array:
    turbina_0 = Turbina_Rawson(Coord(np.array([0,0,80]))) # chequear altura del hub
    turbina_1 = Turbina_Rawson(Coord(np.array([distancia*D,0,80]))) # chequear altura del hub
    parque_de_turbinas = Parque_de_turbinas([turbina_0, turbina_1], z_0, z_mast)
    parque_de_turbinas.rotar(-30)
    array_ratio = np.zeros(iters_estadistica)
    sigma_ratio = []
    ratio = []
    for theta in angulos:
        for i in range(iters_estadistica):
            data_prueba = calcular_u_en_coord(modelo_deficit, 'linear', coord, parque_de_turbinas, u_inf, N)
            array_ratio[i] = turbina_1.potencia/turbina_0.potencia
        ratio = np.append(ratio, np.mean(array_ratio))
        sigma_ratio = np.append(sigma_ratio, np.std(array_ratio))
        parque_de_turbinas.rotar(precision_ang)

    plt.figure(figsize=(10,10))
    # plt.title('Cociente de potencias para dos turbinas separadas por {}D'.format(distancia))
    plt.plot(angulos, ratio, label = u'Modelo analítico', linewidth=3)
    plt.fill_between(angulos, ratio-sigma_ratio, ratio+sigma_ratio, alpha=0.3)
    # plt.errorbar(angulos, ratio, yerr=sigma_ratio, marker='o', markersize=3, label='kdsjghkjng', zorder=0)
    plt.xlabel(u'dirección[º]', fontsize=25)
    plt.ylabel(r'$P_1 / P_0$', fontsize=30)
    plt.plot(dir_medido, ratio_medido, 'o', label = 'Mediciones', markersize=10)
    plt.xlim(-30,30)
    plt.ylim(0.2,1.2)
    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    plt.grid()
    plt.legend(fontsize=16, loc= 'upper right')
    ratio_interpolado_modelado = interpolar(angulos, ratio, dir_medido)
    chi, p = chisquare(ratio_interpolado_modelado, f_exp=ratio_medido)
    chi_array = np.append(chi_array, chi)
    p_array = np.append(p_array, p)
    plt.savefig('potencia_{}_{}'.format(modelo_label[type(modelo_deficit).__name__], str(int(distancia))), dpi=300)

print 'chi_array = ',chi_array
print 'p_array = ',p_array


#############################
+39

dir_medido_57 = dir_medido
ratio_medido_57 = ratio_medido

distancia = 5.7

precision_ang = 1
angulos = np.arange(-30, 30 + precision_ang, precision_ang)

iters_estadistica = 100

metodo_array = ['linear', 'rss', 'largest']
metodo_label = {'linear': 'Lineal', 'rss': 'Cuadratica', 'largest':'Dominante'}

for metodo_superposicion in metodo_array:
    turbina_0 = Turbina_Rawson(Coord(np.array([0,0,80]))) # chequear altura del hub
    turbina_1 = Turbina_Rawson(Coord(np.array([distancia*D,0,80]))) # chequear altura del hub
    parque_de_turbinas = Parque_de_turbinas([turbina_0, turbina_1], z_0, z_mast)
    parque_de_turbinas.rotar(-30)
    array_ratio = np.zeros(iters_estadistica)
    sigma_ratio = []
    ratio = []
    for theta in angulos:
        for i in range(iters_estadistica):
            data_prueba = calcular_u_en_coord(gaussiana, metodo_superposicion, coord, parque_de_turbinas, u_inf, N)
            array_ratio[i] = turbina_1.potencia/turbina_0.potencia
        ratio = np.append(ratio, np.mean(array_ratio))
        sigma_ratio = np.append(sigma_ratio, np.std(array_ratio))
        parque_de_turbinas.rotar(precision_ang)

    plt.figure(figsize=(10,10))
    # plt.title('Cociente de potencias para dos turbinas separadas por {}D'.format(distancia))
    plt.plot(angulos, ratio, label = u'Modelo analítico', linewidth=3)
    plt.fill_between(angulos, ratio-sigma_ratio, ratio+sigma_ratio, alpha=0.3)
    # plt.errorbar(angulos, ratio, yerr=sigma_ratio, marker='o', markersize=3, label='kdsjghkjng', zorder=0)
    plt.xlabel(u'dirección[º]', fontsize=25)
    plt.ylabel(r'$P_1 / P_0$', fontsize=30)
    plt.plot(dir_medido, ratio_medido, 'o', label = 'Mediciones', markersize=10)
    plt.xlim(-30,30)
    plt.ylim(0.2,1.2)
    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    plt.grid()
    plt.legend(fontsize=16, loc= 'upper right')
    ratio_interpolado_modelado = interpolar(angulos, ratio, dir_medido[283:344])
    chi, p = chisquare(ratio_interpolado_modelado, f_exp=ratio_medido[283:344])
    chi_array = np.append(chi_array, chi)
    p_array = np.append(p_array, p)
    plt.savefig('potencia_{}_{}'.format(metodo_label[metodo_superposicion], str(int(distancia))), dpi=300)

print 'chi_array = ',chi_array
print 'p_array = ',p_array



frandsen = Frandsen()
jensen = Jensen()

modelo_array = [jensen, frandsen, gaussiana]
modelo_label = {'Jensen': 'Jensen', 'Frandsen': 'Frandsen', 'Gaussiana':'Gaussiana'}


for modelo_deficit in modelo_array:
    turbina_0 = Turbina_Rawson(Coord(np.array([0,0,80]))) # chequear altura del hub
    turbina_1 = Turbina_Rawson(Coord(np.array([distancia*D,0,80]))) # chequear altura del hub
    parque_de_turbinas = Parque_de_turbinas([turbina_0, turbina_1], z_0, z_mast)
    parque_de_turbinas.rotar(-30)
    array_ratio = np.zeros(iters_estadistica)
    sigma_ratio = []
    ratio = []
    for theta in angulos:
        for i in range(iters_estadistica):
            data_prueba = calcular_u_en_coord(modelo_deficit, 'linear', coord, parque_de_turbinas, u_inf, N)
            array_ratio[i] = turbina_1.potencia/turbina_0.potencia
        ratio = np.append(ratio, np.mean(array_ratio))
        sigma_ratio = np.append(sigma_ratio, np.std(array_ratio))
        parque_de_turbinas.rotar(precision_ang)

    plt.figure(figsize=(10,10))
    # plt.title('Cociente de potencias para dos turbinas separadas por {}D'.format(distancia))
    plt.plot(angulos, ratio, label = u'Modelo analítico', linewidth=3)
    plt.fill_between(angulos, ratio-sigma_ratio, ratio+sigma_ratio, alpha=0.3)
    # plt.errorbar(angulos, ratio, yerr=sigma_ratio, marker='o', markersize=3, label='kdsjghkjng', zorder=0)
    plt.xlabel(u'dirección[º]', fontsize=25)
    plt.ylabel(r'$P_1 / P_0$', fontsize=30)
    plt.plot(dir_medido, ratio_medido, 'o', label = 'Mediciones', markersize=10)
    plt.xlim(-30,30)
    plt.ylim(0.2,1.2)
    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    plt.grid()
    plt.legend(fontsize=16, loc= 'upper right')
    ratio_interpolado_modelado = interpolar(angulos, ratio, dir_medido[283:344])
    chi, p = chisquare(ratio_interpolado_modelado, f_exp=ratio_medido[283:344])
    chi_array = np.append(chi_array, chi)
    p_array = np.append(p_array, p)
    plt.savefig('potencia_{}_{}'.format(modelo_label[type(modelo_deficit).__name__], str(int(distancia))), dpi=300)

print 'chi_array = ',chi_array
print 'p_array = ',p_array




#############


#
# turbina_0 = Turbina_Rawson(Coord(np.array([0,0,80]))) # chequear altura del hub
# D = turbina_0.d_0
# turbina_1 = Turbina_Rawson(Coord(np.array([distancia*D,0,80]))) # chequear altura del hub
#
# x_o = 8*D
# y_o = 0
# z_o = 80
#
# coord = Coord(np.array([x_o, y_o, z_o]))
#
# precision_ang = 0.625
# angulos = np.arange(-30, 30 + precision_ang, precision_ang)
# ratio = []
#
# parque_de_turbinas = Parque_de_turbinas([turbina_0, turbina_1], z_0, z_mast)
# parque_de_turbinas.rotar(-30)
#
# for theta in angulos:
#     data_prueba = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas, u_inf, N)
#     # potencia_0 = turbina_0.potencia
#     # potencia_1 = turbina_1.potencia
#     ratio = np.append(ratio, turbina_1.potencia/turbina_0.potencia)
#     parque_de_turbinas.rotar(precision_ang)
#
# plt.figure(figsize=(10,10))
# # plt.title('Cociente de potencias para dos turbinas separadas por {}D'.format(distancia))
# plt.plot(angulos, ratio, 'o', label = u'Modelo analítico', markersize=10)
# plt.xticks(fontsize=22)
# plt.yticks(fontsize=22)
# plt.xlabel(u'dirección[º]')
# plt.ylabel(r'$P_1 / P_0$')
# plt.grid()
# plt.legend()
#
#
#
# plt.plot(dir_medido, ratio_medido, 'o', label = 'Mediciones', markersize=10)
# plt.xlim(-30,30)
# plt.ylim(0.2,1.2)
# plt.savefig('potencia_2', dpi=300)




# # intente ajustar una gaussiana pero no pude
# from scipy.optimize import curve_fit
#
# def gauss(x, A, mu, sigma):
#     return A*np.exp(-(x-mu)**2/(2.*sigma**2))
#
# n = len(angulos)                          #the number of data
# mean = np.abs(sum(angulos*ratio)/n)                   #note this correction
# sigma = np.abs(np.sqrt(sum(ratio*(angulos-mean)**2)/n))        #note this correction
#
# # p0 is the initial guess for the fitting coefficients (A, mu and sigma above)
# p0 = [-0.5, 0, 20]
#
# coeff, var_matrix = curve_fit(gauss, angulos, ratio, p0=p0)
#
# A = coeff[0]
# mu = coeff[1]
# sigma = coeff[2]
#
# # Get the fitted curve
# fit = gauss(angulos, A, mu, sigma)
#
# plt.plot(angulos, fit)
# plt.show()
