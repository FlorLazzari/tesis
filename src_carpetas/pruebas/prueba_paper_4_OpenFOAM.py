# coding=utf-8

import numpy as np

import Case
import Coordenadas
import Coordenadas_Norm
import Gaussiana
import Figura
from math import log

import pylab as plb
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp


from Figura_Scatter import Figura_Scatter
from OpenFOAM_Blind_Test_distance_1_gonza import y,y_n,U_x,U_y,U_z,U,deficit_dividido_U_inf_OpenFOAM

################################################################################
# corte horizontal de U:

x_y = {"x_1" : y_n, "y_1" : U}
nombre = "y/d vs U en x/d=1"
xLabel = r'$y/d$'
yLabel = r'$ U$'

figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()

x_y = {"x_1" : y_n, "y_1" : deficit_dividido_U_inf_OpenFOAM}
nombre = "y/d vs deficit_dividido_U_inf_OpenFOAM en x/d=1"
xLabel = r'$y/d$'
yLabel = r'$deficit_dividido_U_inf$'

figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()



# ahora la idea seria fitear una gaussiana para obtener la sigma y asi tener sigma_n
# http://stackoverflow.com/questions/19206332/gaussian-fit-for-python



# para fitear con una gaussiana:

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


# Define model function to be used to fit to the data above:
def gauss(x, *p):
    A, mu, sigma = p
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))

# p0 is the initial guess for the fitting coefficients (A, mu and sigma above)
p0 = [1., 0., 1.]

coeff, var_matrix = curve_fit(gauss, y_n, U, p0=p0)

# Get the fitted curve
fit = gauss(y_n, *coeff)

plt.plot(y_n, U, label='Test data')
plt.plot(y_n, fit, label='Fitted data')

# Finally, lets get the fitting parameters, i.e. the mean and standard deviation:
print 'Fitted mean = ', coeff[1]
print 'Fitted standard deviation = ', coeff[2]

plt.show()





################################################################################
# # coordenadas:
#
# x_n = np.arange(0,16,0.05)
# y_n = np.arange(0,4.5,0.05)
# z_n = np.arange(0,5,0.05)
# # tengo que usar los vectores y_z y z_n del mismo tamaño porque sino no puedo
# # usar cart2pol
#
# d_0 = 0.15
#
# x = d_0 * x_n
# y = d_0 * y_n
# z = d_0 * z_n
#
# # inicializo caso, coordenadas, modelo:
#
# d_0 = 0.15
# z_h = 0.125
# U_hub = 2.2
# C_T = 0.42
# z_0 = 0.00003
# I_0 = 0.07
#
# case = Case(d_0,z_h,U_hub,C_T,z_0,I_0)
# coordenadas = Coordenadas(x,y,z)
#
# k_estrella = 0.023
# epsilon = 0.219
#
# modelo = Gaussiana(case,k_estrella,epsilon)
#
# # corro el modelo:
#
# c_T = 0.42
#
# modelo.play_cart(coordenadas,c_T)
#
# ################################################################################
# # figura 4: sigma_n / x_n
#
# x_y = { 'x_1': modelo.x_n, 'y_1': modelo.sigma_n }
#
# nombre = "figura_4"
# xLabel = r'$x / d_{0}$'
# yLabel = r'$\sigma / d_{0} $'
# numero = 1
#
# figura = Figura(nombre,x_y,xLabel,yLabel,numero)
# figura.yLim = [0,1]
# figura.show_save()
#
# # figura 4 del paper : checked!
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
