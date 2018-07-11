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

import csv

ratio_medido = []

tur_down = 7
tur_up = 8
centro = 315

medido = np.loadtxt('med_{}_{}_{}.csv'.format(tur_down, tur_up, centro), delimiter = ' ')

# angulos_medido = medido[0,290:351]
# ratio_medido = medido[1,290:351]
# std_medido = medido[2,290:351]

angulos_medido = medido[0,285:346]
ratio_medido = medido[1,285:346]
std_medido = medido[2,285:346]
# import pdb; pdb.set_trace()


precision_ang_medido = 1
angulos_medido = angulos = np.arange(-30, 30 + precision_ang_medido, precision_ang_medido)

precision_ang = 1
angulos = np.arange(-30, 30 + precision_ang, precision_ang)

iters_estadistica = 100

metodo_array = ['linear', 'rss', 'largest']
metodo_label = {'linear': 'Lineal', 'rss': 'Cuadratica', 'largest':'Dominante'}

frandsen = Frandsen()
jensen = Jensen()

modelo_array = [jensen, frandsen, gaussiana]
modelo_label = {'Jensen': 'Jensen', 'Frandsen': 'Frandsen', 'Gaussiana':'Gaussiana'}

chi_array = []
p_array = []

for modelo_deficit in modelo_array:
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
                data_prueba = calcular_u_en_coord(modelo_deficit, metodo_superposicion, coord, parque_de_turbinas, u_inf, N)
                array_ratio[i] = turbina_1.potencia/turbina_0.potencia
            ratio = np.append(ratio, np.mean(array_ratio))
            sigma_ratio = np.append(sigma_ratio, np.std(array_ratio))
            parque_de_turbinas.rotar(precision_ang)
            # print theta

        plt.figure(figsize=(10,10))
        # plt.title('Cociente de potencias para dos turbinas separadas por {}D'.format(distancia))
        plt.plot(angulos, ratio, label = u'Modelo analítico', linewidth=3)
        plt.fill_between(angulos, ratio-sigma_ratio, ratio+sigma_ratio, alpha=0.3)
        # plt.errorbar(angulos, ratio, yerr=sigma_ratio, marker='o', markersize=3, label='kdsjghkjng', zorder=0)
        plt.xlabel(u'dirección[º]', fontsize=25)
        plt.ylabel(r'$P_1 / P_0$', fontsize=30)
        plt.plot(angulos_medido, ratio_medido, 'o', label = 'Mediciones', markersize=10)
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
        plt.savefig('potencia_{}_{}_{}'.format(metodo_label[metodo_superposicion], modelo_label[type(modelo_deficit).__name__], str(int(distancia))), dpi=300)

        print ('{}_{} = {}'.format(metodo_label[metodo_superposicion], modelo_label[type(modelo_deficit).__name__], chi))

    # print 'chi_array = ',chi_array
    # print 'p = ',p
