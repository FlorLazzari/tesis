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

# mediciones
dir_medido = np.array([-313, -312, -311, -310, -309, -308, -307, -306, -305, -304, -303,
       -302, -301, -300, -299, -298, -297, -296, -295, -294, -293, -292,
       -291, -290, -289, -288, -287, -286, -285, -284, -283, -282, -281,
       -280, -279, -278, -277, -276, -275, -274, -273, -272, -271, -270,
       -269, -268, -267, -266, -265, -264, -263, -262, -261, -260, -259,
       -258, -257, -256, -255, -254, -253, -252, -251, -250, -249, -248,
       -247, -246, -245, -244, -243, -242, -241, -240, -239, -238, -237,
       -236, -235, -234, -233, -232, -231, -230, -229, -228, -227, -226,
       -225, -224, -223, -222, -221, -220, -219, -218, -217, -216, -215,
       -214, -213, -212, -211, -210, -209, -208, -207, -206, -205, -204,
       -203, -202, -201, -200, -199, -198, -197, -196, -195, -194, -193,
       -192, -191, -190, -189, -188, -187, -186, -185, -184, -183, -182,
       -181, -180, -179, -178, -177, -176, -175, -174, -173, -172, -171,
       -170, -169, -168, -167, -166, -165, -164, -163, -162, -161, -160,
       -159, -158, -157, -156, -155, -154, -153, -152, -151, -150, -149,
       -148, -147, -146, -145, -144, -143, -142, -141, -140, -139, -138,
       -137, -136, -135, -134, -133, -132, -131, -130, -129, -128, -127,
       -126, -125, -124, -123, -122, -121, -120, -119, -118, -117, -116,
       -115, -114, -113, -112, -111, -110, -109, -108, -107, -106, -105,
       -104, -103, -102, -101, -100,  -99,  -98,  -97,  -96,  -95,  -94,
        -93,  -92,  -91,  -90,  -89,  -88,  -87,  -86,  -85,  -84,  -83,
        -82,  -81,  -80,  -79,  -78,  -77,  -76,  -75,  -74,  -73,  -72,
        -71,  -70,  -69,  -68,  -67,  -66,  -65,  -64,  -63,  -62,  -61,
        -60,  -59,  -58,  -57,  -56,  -55,  -54,  -53,  -52,  -51,  -50,
        -49,  -48,  -47,  -46,  -45,  -44,  -43,  -42,  -41,  -40,  -39,
        -38,  -37,  -36,  -35,  -34,  -33,  -32,  -31,  -30,  -29,  -28,
        -27,  -26,  -25,  -24,  -23,  -22,  -21,  -20,  -19,  -18,  -17,
        -16,  -15,  -14,  -13,  -12,  -11,  -10,   -9,   -8,   -7,   -6,
         -5,   -4,   -3,   -2,   -1,    0,    1,    2,    3,    4,    5,
          6,    7,    8,    9,   10,   11,   12,   13,   14,   15,   16,
         17,   18,   19,   20,   21,   22,   23,   24,   25,   26,   27,
         28,   29,   30,   31,   32,   33,   34,   35,   36,   37,   38,
         39,   40,   41,   42,   43,   44,   45,   46])

ratio_medido = np.array([ 1.00957297,  1.00581893,  0.99641991,  0.99784957,  1.01356414,
        1.02127334,  1.00802399,  1.00544668,  1.00368145,  0.96473577,
        0.9118464 ,  0.90278206,  0.90559716,  0.8755781 ,  0.84606756,
        0.82342421,  0.77976616,  0.72820747,  0.69499962,  0.65054955,
        0.57892302,  0.54989425,  0.54895273,  0.55496394,  0.55014834,
        0.56426226,  0.64378896,  0.70061097,  0.71918305,  0.76378602,
        0.83521495,  0.86511228,  0.88389441,  0.94263472,  0.95126591,
        0.90120348,  0.8796288 ,  0.93536131,  0.99622478,  1.04087739,
        1.04584246,  1.00936496,  0.97937376,  0.90676917,  0.87198391,
        0.92679166,  0.98495183,  0.95971602,  0.84902038,  0.73992365,
        0.7975554 ,  0.93161058,  0.98079761,  0.96781824,  0.96874001,
        0.97080577,  0.96121192,  0.96510559,  1.02566022,  1.1406606 ,
        1.20330053,  1.24155389,  1.23346244,  1.12729426,  1.1252285 ,
        1.27106716,  1.4971105 ,  1.6147405 ,  1.60470421,  1.56827737,
        1.47247248,  1.33985774,  1.24236615,  1.2140316 ,  1.18208361,
        1.12846311,  1.11126131,  1.06974527,  1.00809007,  0.95273234,
        0.92443713,  0.93538771,  0.87504145,  0.81388188,  0.83669447,
        0.85598559,  0.8568305 ,  0.86852547,  0.87501069,  0.88813215,
        0.91828068,  0.95498065,  0.97797054,  0.98087959,  0.95879871,
        0.93573721,  0.94736879,  0.9828216 ,  0.99486924,  0.99479965,
        0.98984932,  0.95187882,  0.92596975,  0.94684152,  0.96505906,
        0.92826555,  0.89370443,  0.88277635,  0.899443  ,  0.91383235,
        0.93905753,  0.95549912,  0.96386931,  0.99487468,  0.98608053,
        0.94706424,  0.96350268,  1.00942564,  1.06131593,  1.11343016,
        1.10522258,  1.10464702,  1.10974428,  1.10916268,  1.10906621,
        1.10751312,  1.12141673,  1.18155328,  1.24729787,  1.26727778,
        1.29931241,  1.35936448,  1.35782378,  1.33881747,  1.35131701,
        1.37364009,  1.41131849,  1.4593853 ,  1.49065433,  1.48868848,
        1.41805622,  1.33162825,  1.26673012,  1.19597555,  1.15859326,
        1.18041241,  1.18547619,  1.11968231,  1.04210469,  0.99218658,
        1.00942297,  1.06907051,  1.09240721,  1.0646027 ,  1.02170057,
        1.02639183,  1.08767713,  1.10812268,  1.09407475,  1.04727647,
        0.99530741,  0.98606871,  1.07446038,  1.26852353,  1.46211559,
        1.38547238,  1.27133431,  1.4469229 ,  1.62083027,  1.44758628,
        1.24811331,  1.13314268,  1.12618874,  1.13757599,  1.08294473,
        1.00103191,  0.93361537,  0.95869447,  1.0294599 ,  1.01871309,
        0.92436216,  0.78439582,  0.71385836,  0.73498588,  0.66006578,
        0.56906795,  0.55544394,  0.52619946,  0.47031374,  0.45542972,
        0.51004124,  0.55356726,  0.56595595,  0.5842451 ,  0.57904897,
        0.55091216,  0.56609593,  0.57616005,  0.53241441,  0.48736584,
        0.46214757,  0.43940168,  0.4291079 ,  0.45630479,  0.50971415,
        0.53765359,  0.52430843,  0.53906262,  0.58409331,  0.6234587 ,
        0.64973046,  0.66066879,  0.68759606,  0.75519806,  0.83900834,
        0.93225838,  0.98924527,  0.97958902,  0.94800216,  0.93506327,
        0.93322148,  0.93837355,  0.92680082,  0.89291815,  0.8625091 ,
        0.87683979,  0.92753897,  0.97195425,  0.98701991,  0.98910757,
        0.99394721,  1.00444991,  1.01321585,  1.01338013,  1.03083822,
        1.06054678,  1.06034945,  1.05397251,  1.04992406,  1.00863532,
        0.96879023,  0.98680871,  0.99961227,  0.98638146,  0.98267078,
        0.99794842,  1.02501776,  1.04540417,  1.05705207,  1.05841259,
        1.04269446,  1.02145135,  1.02092579,  1.03309099,  1.04712191,
        1.05659423,  1.05281536,  1.04549218,  1.04489334,  1.04239173,
        1.04401814,  1.05130203,  1.04062259,  1.02134028,  1.01349052,
        1.01280603,  1.02355594,  1.03277442,  1.03272374,  1.03088378,
        1.02721167,  1.02211261,  1.01484224,  1.01769123,  1.03359413,
        1.03907591,  1.04061723,  1.05056102,  1.05407135,  1.05558558,
        1.06095927,  1.06791843,  1.06546685,  1.06219171,  1.07058913,
        1.07448795,  1.06899792,  1.07393039,  1.07319126,  1.05896054,
        1.05593952,  1.04820386,  1.01344593,  0.99996563,  1.00132968,
        1.00803974,  1.01571349,  1.00968384,  0.99638301,  0.98092463,
        0.96060086,  0.93933783,  0.9402352 ,  0.9045184 ,  0.81210061,
        0.74905623,  0.6835521 ,  0.62492257,  0.62884904,  0.65319587,
        0.63303361,  0.57095635,  0.53425566,  0.55455629,  0.58167473,
        0.5786316 ,  0.56829723,  0.60249594,  0.67251558,  0.70437986,
        0.68819865,  0.64452865,  0.65917993,  0.72801739,  0.77669829,
        0.78904856,  0.78748229,  0.73959143,  0.69108669,  0.75112199,
        0.84839215,  0.928382  ,  0.99292241,  0.97395039,  0.92333507,
        0.95293423,  0.99777742,  0.99865363,  1.00339194,  1.02605801,
        1.01621478,  0.99238505,  1.00860384,  1.03304544,  1.04170965,
        1.05074761,  1.07317038,  1.098392  ,  1.09139856,  1.0688286 ,
        1.02841429,  0.9989188 ,  1.0000993 ,  1.00225744,  0.99940107,
        0.99177978,  0.98849933,  0.98282495,  0.97263774,  0.97746164])

precision_ang = 0.625
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

# mediciones
dir_medido = np.array([-69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57,
       -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44,
       -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31,
       -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18,
       -17, -16, -15, -14, -13, -12, -11, -10,  -9,  -8,  -7,  -6,  -5,
        -4,  -3,  -2,  -1,   0,   1,   2,   3,   4,   5,   6,   7,   8,
         9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,
        22,  23,  24,  25,  26,  27,  28,  29,  30,  31,  32,  33,  34,
        35,  36,  37,  38,  39,  40,  41,  42,  43,  44,  45,  46,  47,
        48,  49,  50,  51,  52,  53,  54,  55,  56,  57,  58,  59,  60,
        61,  62,  63,  64,  65,  66,  67,  68,  69,  70,  71,  72,  73,
        74,  75,  76,  77,  78,  79,  80,  81,  82,  83,  84,  85,  86,
        87,  88,  89,  90,  91,  92,  93,  94,  95,  96,  97,  98,  99,
       100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112,
       113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125,
       126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138,
       139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151,
       152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164,
       165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177,
       178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190,
       191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
       204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216,
       217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229,
       230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242,
       243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255,
       256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268,
       269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281,
       282, 283, 284, 285, 286, 287, 288, 289, 290])


ratio_medido = np.array([ 1.04495906,  1.04723209,  1.07741021,  1.09256663,  1.05427293,
        1.0191909 ,  0.98881957,  0.97597236,  0.97985018,  0.99644646,
        1.02097287,  1.01872082,  1.02512043,  1.03698724,  1.01984038,
        0.99138835,  0.9701593 ,  0.967611  ,  0.96997945,  0.97919771,
        1.0049177 ,  1.03757906,  1.04087742,  1.02584805,  1.03306053,
        1.05668643,  1.05790264,  1.05801643,  1.04365867,  1.03731015,
        1.03816653,  1.02499329,  1.0385221 ,  1.06316007,  1.07861189,
        1.07797638,  1.05552464,  1.02552796,  0.99864399,  0.99126019,
        0.99978216,  0.97561013,  0.96540025,  0.98635671,  1.00056743,
        1.02325629,  1.03683874,  1.06877097,  1.18240941,  1.29733647,
        1.18630939,  1.03465156,  0.98988452,  1.03415907,  1.08785321,
        1.09465715,  1.10111132,  1.09194559,  0.99756379,  0.87952202,
        0.82368932,  0.7860844 ,  0.79339295,  0.86602489,  0.86060762,
        0.77864787,  0.67913849,  0.6182711 ,  0.60254093,  0.59886363,
        0.61552625,  0.62898349,  0.63953962,  0.64947816,  0.66659927,
        0.70408107,  0.7290905 ,  0.75710238,  0.77729683,  0.79706765,
        0.83016455,  0.840074  ,  0.85538834,  0.89447898,  0.92221286,
        0.90461667,  0.87380041,  0.91450511,  0.99704113,  1.01166148,
        0.98185436,  0.98957991,  1.00906588,  1.01908759,  1.03435032,
        1.0124844 ,  0.97647185,  0.99681935,  1.06672044,  1.11192966,
        1.10738967,  1.07494611,  1.01368934,  0.96303886,  0.92554256,
        0.92188279,  0.99315388,  1.0793209 ,  1.07090933,  1.03709363,
        1.05506525,  1.08258833,  1.069521  ,  1.02330541,  1.01887861,
        1.03945838,  0.9897647 ,  0.93271275,  0.90258082,  0.89974349,
        0.92727326,  0.94277849,  0.92822241,  0.88562675,  0.85804212,
        0.83672179,  0.8316969 ,  0.82188217,  0.82009636,  0.8350226 ,
        0.78307624,  0.72142476,  0.72268679,  0.74451528,  0.74796038,
        0.72720329,  0.71226919,  0.72186684,  0.72964868,  0.72265383,
        0.74959647,  0.8094727 ,  0.83713884,  0.8763156 ,  0.93015706,
        0.93397283,  0.92437973,  0.96677569,  1.0274956 ,  1.06241292,
        1.00410551,  0.92946589,  0.93830061,  1.00290278,  1.06453382,
        1.06071301,  1.01170104,  1.01223424,  1.03919458,  1.05182929,
        1.03876033,  1.02430137,  0.97733047,  0.86452891,  0.76441376,
        0.79719411,  0.85286302,  0.76953668,  0.70242997,  0.76188109,
        0.83958649,  0.88458697,  0.8838773 ,  0.86582363,  0.86105564,
        0.8651405 ,  0.86332497,  0.84978009,  0.85534929,  0.89728695,
        0.97092838,  1.06798956,  1.0922841 ,  1.10596925,  1.34485868,
        1.66208179,  1.7353702 ,  1.85843864,  2.10717247,  2.20012092,
        2.0151091 ,  1.83172884,  1.76393165,  1.73598757,  1.80060639,
        1.93063753,  1.95431813,  1.97386946,  1.95490957,  1.90377274,
        1.93071878,  1.94279849,  1.94473169,  1.80391137,  1.58868218,
        1.4937039 ,  1.45590282,  1.36145837,  1.2846895 ,  1.27585628,
        1.28511296,  1.30062462,  1.30174874,  1.26049504,  1.17565369,
        1.08357718,  1.03063897,  1.0260493 ,  1.03960163,  1.03994958,
        1.03762035,  1.05861603,  1.08640639,  1.04440464,  1.01255869,
        1.10819585,  1.16782728,  1.13732632,  1.14655297,  1.15725747,
        1.14654847,  1.14004343,  1.12130505,  1.11117987,  1.11575519,
        1.1499905 ,  1.19561091,  1.21973155,  1.2552758 ,  1.27665336,
        1.24867899,  1.27246527,  1.34804013,  1.3940144 ,  1.40067917,
        1.4083193 ,  1.43060345,  1.44390083,  1.46392574,  1.48305753,
        1.48118038,  1.50951374,  1.53175946,  1.50801053,  1.43678061,
        1.32947333,  1.23289108,  1.16474054,  1.11964832,  1.08483865,
        1.06905916,  1.07004793,  1.07484457,  1.07833147,  1.07752486,
        1.0757324 ,  1.07416028,  1.06534156,  1.04779307,  1.0339784 ,
        1.02682442,  1.02746354,  1.0248086 ,  1.01501958,  1.00943187,
        1.01558818,  1.01790308,  1.00790089,  0.99908572,  1.00682664,
        1.01729119,  1.01179903,  1.00645141,  0.99477222,  0.97272529,
        0.96807259,  0.97198725,  0.96889187,  0.97310411,  0.9955446 ,
        1.02502756,  1.03529366,  1.02488443,  1.00436399,  0.98575071,
        0.99026389,  0.97918152,  0.95844192,  0.96972618,  1.00092958,
        1.02916043,  1.03841209,  1.01856701,  1.00859622,  1.03786371,
        1.02973797,  0.97810985,  0.97075703,  0.99997918,  1.01088379,
        1.02587226,  1.05432107,  1.0433273 ,  1.01232589,  1.00660352,
        0.99999231,  0.98187775,  0.97453792,  0.95831067,  0.94553949,
        0.96725481,  1.01364357,  1.03366112,  1.00756596,  0.99813707,
        1.01152626,  1.03488351,  1.05783475,  1.0631855 ,  1.05741331,
        1.04271592,  0.99254903,  0.94284047,  0.90875393,  0.90546497,
        0.95473668,  0.98925862,  0.99923401,  1.00953563,  1.02214185,
        1.0306136 ,  1.02643843,  0.98635497,  0.94024691,  0.9383185 ,
        0.94533618,  0.93242188,  0.93039328,  0.95530687,  0.97292093,
        0.99965556,  1.01514587,  1.00745177,  1.00052376,  0.99005483,
        0.99077933,  1.00279319,  1.00781708,  1.00145123,  0.98746786])

#############################

distancia = 5.7

precision_ang = 0.625
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
