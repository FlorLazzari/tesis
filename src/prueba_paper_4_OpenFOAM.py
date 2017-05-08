# coding=utf-8

import numpy as np

from Figura_Scatter import Figura_Scatter

import pylab as plb
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp


from Figura_Scatter import Figura_Scatter
from OpenFOAM_Blind_Test_distance_1_gonza import y,y_n,U_x,U_y,U_z,U,deficit_dividido_U_inf_OpenFOAM

################################################################################
# ahora la idea seria fitear una gaussiana para obtener la sigma y asi tener sigma_n
# http://stackoverflow.com/questions/19206332/gaussian-fit-for-python

x_n = np.zeros(3)
sigma = np.zeros(3)

from fitear_gaussiana import fitear_gaussiana

from OpenFOAM_Blind_Test_distance_1_gonza import y_n,deficit_dividido_U_inf_OpenFOAM

x_n[0] = 1
#para fitear voy a recortar a mano los datos de la pared:
y_n = y_n[5:95]
deficit_dividido_U_inf_OpenFOAM = deficit_dividido_U_inf_OpenFOAM[5:95]

x = np.array(y_n)
y = np.array(deficit_dividido_U_inf_OpenFOAM)

sigma = fitear_gaussiana(x,y)
# rotor diameter = 0.894 m
d_0 = 0.894
sigma_0_n = sigma / d_0

from OpenFOAM_Blind_Test_distance_3_gonza import y_n,deficit_dividido_U_inf_OpenFOAM

x_n[1] = 3
#para fitear voy a recortar a mano los datos de la pared:
y_n = y_n[5:95]
deficit_dividido_U_inf_OpenFOAM = deficit_dividido_U_inf_OpenFOAM[5:95]

x = np.array(y_n)
y = np.array(deficit_dividido_U_inf_OpenFOAM)

sigma = fitear_gaussiana(x,y)
# rotor diameter = 0.894 m
d_0 = 0.894
sigma_1_n = sigma / d_0

from OpenFOAM_Blind_Test_distance_5_gonza import y_n,deficit_dividido_U_inf_OpenFOAM

x_n[2] = 5
#para fitear voy a recortar a mano los datos de la pared:
y_n = y_n[5:95]
deficit_dividido_U_inf_OpenFOAM = deficit_dividido_U_inf_OpenFOAM[5:95]

x = np.array(y_n)
y = np.array(deficit_dividido_U_inf_OpenFOAM)

sigma = fitear_gaussiana(x,y)
# rotor diameter = 0.894 m
d_0 = 0.894
sigma_2_n = sigma / d_0


################################################################################
# junto a todos los resultados obtenidos en un vector
sigma_n = [sigma_0_n, sigma_1_n, sigma_2_n]
print sigma_n

################################################################################
# figura 4: sigma_n / x_n

x_y = { 'x_1': x_n, 'y_1': sigma_n }

nombre = "figura_4"
xLabel = r'$x / d_{0}$'
yLabel = r'$\sigma / d_{0} $'
numero = 1

figura = Figura_Scatter(nombre,x_y,xLabel,yLabel,numero)
figura.show()

# figura 4 del paper : checked!
