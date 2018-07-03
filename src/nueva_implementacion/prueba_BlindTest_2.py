# coding=utf-8

from __future__ import division
import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
import itertools

from Gaussiana import Gaussiana
from Jensen import Jensen
from Frandsen import Frandsen
from Larsen import Larsen
from Parque_de_turbinas import Parque_de_turbinas
from Turbina_BlindTest_2_TSR4 import Turbina_BlindTest_2_TSR4
from Turbina_BlindTest_2_TSR6 import Turbina_BlindTest_2_TSR6
from Coord import Coord
from Estela import Estela
from U_inf import U_inf
from calcular_u_en_coord import calcular_u_en_coord

"""
Tenemos dos turbinas alineadas separadas por 3D en x
A continuacion se grafica:
    1) El deficit a la altura del hub para dos turbinas alineadas a 7D por
    atras de la primera (4D del segundo) usando CFD (OpenFOAM).
    2) El deficit de las dos turbinas trabajando independientemente (a 7D de
    la primera turbina y a 4D de la segunda turbina)
    3) El deficit generado por ambas (a 7D de la primera turbina) utilizando
    distintos metodos de superposicion de estelas

Tenemos los datos del BlindTest2 del parametro U para distintas distancias:
x = {4, 5.5, 7} D (downstream distances from T1)


Tenemos corridas de OpenFOAM para ese mismo caso (las corrio Gonza hace bastante)
Trabajamos unicamente con el modelo reducido: Gaussiana.

A continuacion se grafica comparacion de BlindTest, OpenFOAM y modelos reducidos
en un grafico de curva a la altura del hub para una turbina en las tres distancias
mencionadas

"""

################################################################################
# aca tengo las mediciones del BlindTest

y_norm_med = {'4': np.array([2.46666666666667, 2.4, 2.33333333333333, 2.26666666666667, 2.2, 2.13333333333333, 2.06666666666667, 2, 1.93333333333333, 1.86666666666667, 1.8, 1.73333333333333, 1.66666666666667, 1.6, 1.53333333333333, 1.46666666666667, 1.4, 1.33333333333333, 1.26666666666667, 1.2, 1.13333333333333, 1.06666666666667, 1, 0.933333333333333, 0.866666666666667, 0.8, 0.733333333333333, 0.666666666666667, 0.6, 0.533333333333333,0.466666666666667, 0.4, 0.4, 0.4, 0.266666666666667, 0.2, 0.333333333333333, 0.133333333333333,0, 0, 0.0666666666666667, -0.0666666666666667, -0.133333333333333, -0.2, -0.266666666666667,-0.333333333333333, -0.4, -2.26667333333333, -2.20000666666667, -2.13334, -2.06667333333333,-2.06667333333333, -2.00000666666667, -1.93334, -1.86667333333333, -1.80000666666667,-1.80000666666667, -1.73334, -1.66667333333333, -1.60000666666667, -1.60000666666667,-1.53334, -1.53334, -1.46667333333333, -1.40000666666667, -1.33334, -1.20000666666667,-1.13334, -1.06667333333333, -1.00000666666667, -0.93334, -0.866673333333333, -0.800006666666667,-0.73334, -0.73334, -0.73334, -0.666673333333333, -0.600006666666667, -0.53334, -0.466673333333333,-0.400006666666667, -0.33334, -0.266673333333333, -0.200006666666667, -0.133344444444444, -0.0666733333333333,0, 0, 0, 0, 0]),
'5.5': np.array([2.46666666666667,2.36666666666667,2.26666666666667,2.2,2.13333333333333,2.06666666666667,2,1.93333333333333,1.86666666666667,1.8,1.73333333333333,1.66666666666667,1.6,1.53333333333333,1.46666666666667,1.4,1.33333333333333,1.26666666666667,1.2,1.13333333333333,1.06666666666667,1,0.933333333333333,0.866666666666667,0.8,0.733333333333333,0.666666666666667,0.6,0.533333333333333,0.466666666666667,0.4,0.333333333333333,0.266666666666667,0.2,0.133333333333333,0.0666666666666667,0,-0.0666666666666667,-0.133333333333333,-0.2,-0.266666666666667,-0.333333333333333,-2.46666666666667,-2.4,-2.33333333333333,-2.26666666666667,-2.2,-2.13333333333333,-2.06666666666667,-1.93333333333333,-1.86666666666667,-1.86666666666667,-1.8,-1.73333333333333,-1.66666666666667,-1.66666666666667,-1.6,-1.6,-1.53333333333333,-1.46666666666667,-1.4,-1.33333333333333,-1.26666666666667,-1.26666666666667,-1.2,-1.13333333333333,-1.06666666666667,-1,-1,-0.933333333333333,-0.933333333333333,-0.866666666666667,-0.8,-0.733333333333333,-0.666666666666667,-0.6,-0.533333333333333,-0.466666666666667,-0.4,-0.333337777777778,-0.266666666666667,-0.2,-0.133333333333333,-0.133333333333333,-0.0666666666666667,-0.0666666666666667,0,0.0666666666666667,0.133333333333333,0.2,0.266666666666667]),
'7': np.array([2.46666666666667,2.36666888888889, 2.26666666666667, 2.16666666666667, 2.06666666666667, 2.0, 1.93333333333333, 1.86666666666667, 1.8, 1.73333333333333, 1.66666666666667, 1.6, 1.53333333333333, 1.46666666666667, 1.4, 1.33333333333333, 1.26666666666667, 1.2, 1.13333333333333, 1.06666666666667, 0.933357777777778, 1.00002666666667, 0.866693333333333, 0.800024444444445, 0.73336, 0.666691111111111, 0.600024444444445, 0.53336, 0.466693333333333, 0.400026666666667, 0.33336, 0.266691111111111, 0.198944444444444, 0.13336, 0.0666933333333333, 0.0000266666666666667, -0.06664, -0.133306666666667, -0.199973333333333, -0.26664, -0.333306666666667, -2.39999555555556, -2.19999555555556, -1.99999555555556, -1.89999555555556, -1.79999555555556, -1.69999555555556, -1.59999555555556, -1.49999555555556, -1.39999555555556, -1.29999555555556, -1.19999555555556, -1.09999555555556, -0.999991111111111, -0.899995555555556, -0.799995555555556, -0.699995555555556, -0.599995555555556, -0.499995555555556, -0.399991111111111, -0.299995555555556, -0.2, -0.0999955555555556, 0.00000444444444444444, 0.100004444444444])
}

deficit_x_med = {'4': np.array([-0.2148791955518, -0.2176650604824, -0.2122684870194, -0.2098962753560, -0.2050555388998, -0.2012390551553, -0.2000346867146, -0.1980725325194, -0.1969396923508, -0.1978108293960, -0.1949979591291, -0.1919292977287, -0.1874159493211, -0.1754649311606, -0.1542033378594, -0.1175908955123, -0.0627722366421, 0.0126219920745, 0.0897240630473, 0.1798007171845, 0.2671204434830, 0.3467597756012, 0.4169865456921, 0.4712709578275, 0.4894885514462, 0.4907059182999, 0.4777169462601, 0.4723306713379, 0.4770625019323, 0.4834008193939, 0.4956929717675, 0.5012629031140, 0.5031192934706, 0.5022606224697, 0.4790673397605, 0.4550167928872, 0.4977204419964, 0.4334968821404, 0.4294411770844, 0.4300066739201, 0.4244553144641, 0.4491922236786, 0.4715113403944, 0.4918974924956, 0.5042497706785, 0.5067077272322, 0.5006178260355, -0.1946763575922, -0.1894590988508, -0.1855195077971, -0.1831770234107, -0.1825144866167, -0.1807652178071, -0.1792408819886, -0.1817050139156, -0.1818755076487, -0.1794365079676, -0.1649035507694, -0.1635476874508, -0.1558304966090, -0.1560102725664, -0.1334123308567, -0.1330526809728, -0.0774174608571, 0.0009670957316, 0.0866354803250, 0.2552440554366, 0.3437351881970, 0.4365520774698, 0.5230145556772, 0.5736409972009, 0.5866068196443, 0.5796651323995, 0.5588226355319, 0.5595182791947, 0.5601496399811, 0.5398441311875, 0.5237885340772, 0.5125568013935, 0.5096488692068, 0.5124778016329, 0.5157647785948, 0.5119200598344, 0.4999982652839, 0.4799559476538, 0.4593286709854, 0.4410650722809, 0.4463555914859, 0.4465761754278, 0.4474884059778, 0.4476410136844, ]),
'5.5': np.array([-0.16758318415927, -0.17007777353708, -0.16590294830233, -0.15874018751730, -0.15706062940244, -0.15280867087581, -0.15041257162031, -0.14952022919318, -0.14667110487621, -0.13877612279896, -0.12860088477534, -0.11371619867680, -0.08161034229038, -0.05061962127679, -0.01047621554154, 0.03052695899441, 0.07826971460254, 0.12702697269490, 0.17721204629212, 0.21693327298350, 0.26132946424311, 0.30451795472821, 0.33837632559081, 0.36530505608581, 0.38569990210993, 0.40199206453097, 0.42407843532729, 0.43192415070686, 0.45756972187329, 0.46884211423577, 0.47769845716303, 0.48645740526894, 0.49832898024791, 0.50632357843964, 0.51182102646942, 0.52206589847274, 0.53180372763411, 0.53788402190110, 0.54427890718201, 0.55095571407776, 0.54817593827874, 0.54517048834985, -0.19507075375805, -0.19002104956104, -0.18663026044443, -0.18348868669394, -0.17826962806736, -0.17288057136268, -0.17102759695708, -0.16810296604285, -0.16925914594422, -0.16931456090874, -0.16535239689078, -0.15796955981703, -0.13703851622265, -0.13429163441944, -0.10564277100467, -0.10176941892382, -0.05668800910103, -0.00689643943036, 0.05500533734100, 0.10762564289380, 0.16822730295989, 0.16990947812809, 0.22683676314366, 0.27950148721011, 0.34205753947366, 0.39609489446911, 0.39677640291347, 0.44626975541438, 0.44932350196124, 0.48626089547606, 0.51142771674139, 0.52579068305552, 0.52328090128505, 0.52328077501770, 0.52289229514619, 0.51976659190373, 0.52780958270103, 0.52892854965629, 0.52957857222116, 0.53146672165830, 0.52796194807810, 0.52902496444116, 0.52332976429297, 0.52306977125751, 0.51989977441068, 0.51433178246505, 0.50571372967718, 0.49802297887068, 0.49551656176167, ]),
'7': np.array([-0.16975, -0.17279, -0.16595, -0.15784, -0.15254, -0.14883, -0.14096, -0.13065, -0.11324, -0.09313, -0.06308, -0.04447, -0.01340, 0.01511, 0.04595, 0.07810, 0.11121, 0.13102, 0.17592, 0.20412, 0.25667, 0.23313, 0.28752, 0.31091, 0.34723, 0.37335, 0.39848, 0.42848, 0.44966, 0.47473, 0.49146, 0.51056, 0.51985, 0.51988, 0.51888, 0.51378, 0.50843, 0.49244, 0.47601, 0.46357, 0.45353, -0.15796, -0.14751, -0.14009, -0.13290, -0.11145, -0.07370, -0.01614, 0.03900, 0.09943, 0.15442, 0.21110, 0.26870, 0.31374, 0.35054, 0.38049, 0.40301, 0.41553, 0.42876, 0.43904, 0.45954, 0.48258, 0.50234, 0.51305, 0.51596, ])
}

gaussiana = Gaussiana()

u_inf = U_inf()
u_inf.coord_mast = 10 # es parametro del BlindTest
u_inf.perfil = 'cte'   # por ser un tunel de viento
N = 100

turbina_0 = Turbina_BlindTest_2_TSR6(Coord(np.array([0,0,0.817])))
D = 0.894
turbina_1 = Turbina_BlindTest_2_TSR4(Coord(np.array([3*D,0,0.817])))

z_mast = 0.817

# z_0 de la superficie
z_0 = 0
parque_de_turbinas = Parque_de_turbinas([turbina_0, turbina_1], z_0, z_mast)

x_array = [4, 5.5, 7]
y = np.linspace(-1.5*D, 1.5*D, 500)
y_norm = y/D
z_o = turbina_0.coord.z

metodo_array = ['linear', 'rss', 'largest']
metodo_label = {'linear': 'Lineal', 'rss': u'Cuadrática', 'largest':'Dominante'}

for distancia in x_array:
    plt.figure(figsize=(10,10))
    # plt.title('x = {}D'.format(distancia))

    for metodo_superposicion in metodo_array:
        x_o = distancia * D
        data_prueba = np.zeros(len(y))

        for i in range(len(y)):
            coord = Coord(np.array([x_o, y[i], z_o]))
            data_prueba[i] = calcular_u_en_coord(gaussiana, metodo_superposicion, coord, parque_de_turbinas, u_inf, N)

        plt.plot(y_norm, 1 - data_prueba/u_inf.coord_mast, label= u'{}'.format(metodo_label[metodo_superposicion]), linewidth=3)

        # print data_prueba
    # comparo con las mediciocones

    plt.plot(y_norm_med["{}".format(distancia)]*0.5, deficit_x_med["{}".format(distancia)],'o',label='Mediciones', markersize=10)

    # comparo con OpenFOAM

    # todavia no las tengo
    datos = np.loadtxt("BT2_{}.csv".format(distancia), delimiter = ',', skiprows=1)

    largo = datos.shape[0]
    ancho =  datos.shape[1]

    u_OpenFOAM = np.zeros((largo))
    y_norm_OpenFOAM = np.zeros((largo))


    for i in range(largo):
        y_norm_OpenFOAM[i] = datos[i, 0]/D
        u_OpenFOAM[i] = datos[i, 1]

    plt.plot(y_norm_OpenFOAM - np.mean(y_norm_OpenFOAM), 1 - u_OpenFOAM/u_inf.coord_mast, '--', label='OpenFOAM (CFD)', linewidth= 3)
    plt.xlabel(r'$y/d$', fontsize=30)
    plt.ylabel(r'$1 - u/u_{\infty}$', fontsize=30)
    plt.legend(fontsize=16, loc= 'upper right')
    plt.xlim([-1.3,1.3])
    plt.ylim([-0.3, 1])
    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    plt.grid()
    plt.savefig('BlindTest2_{}'.format(int(distancia)), dpi=300)
