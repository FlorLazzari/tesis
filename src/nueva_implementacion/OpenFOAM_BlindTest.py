from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
# -*- coding: utf-8 -*-

"""
Tenemos los datos de OpenFOAM del parametro U para distintas distancias
A continuacion se grafica:
    1) El deficit a la altura del hub para una turbina en x = {1, 3, 5} D
    (Para cada grafico se recortaron los datos de modo de poder ajustar una gaussiana correctamente)
    Y el ajuste de los graficos anteriores con su fiteo gaussiano asociado
    2) El ajuste lineal de las sigmas de las gaussianas obtenidas con el fit
    de modo de obtener k y epsilon para el metodo Gaussiana
    3) El ajuste de A (amplitud) vs sigma con la funcion: 1 - (1-(c_T/(8*(sigma_n**2))))**(0.5)
    del cual se obtiene el c_T adecuado segun el modelo de Porte -Agel
    Se compara con el grafico para c_T = 0.8 (valor correspondiente a las turbinas de Rawson)
    4) Como el c_T es algo fijo, el 3) no tiene mucho sentido.
    Se obtiene el k y epsilon a partir del ajuste de las dos funciones: 1 - (1-(c_T/(8*(sigma_n**2))))**(0.5) y la relacion lineal para sigma_n
    Al comparar el ajuste con los valores medidos se ve que los resultados son mejores que los anteriores.
    5) Sin embargo, cuando comparo la relacion lineal del sigma obtenida a traves de 3) y 4) veo que la de 3) es mucho mejor.
    Posible solucion: cambiar el ajuste lineal por algo mas cuadratico (?), porque se ve de 3) que la relacion que siguen los datos claramente no es lineal
"""

U_inf = 10

# Define model function to be used to fit to the data above:
def gauss(x, A, mu, sigma):
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))

x_array = [1, 2, 3, 4, 5, 6, 7]
sigma_array = []
sigmaAltura_array = []
A_array = []

# diametro de la turbina
D = 0.894

for distancia in x_array:


    datos = np.loadtxt("BT1_{}.csv".format(distancia), delimiter = ',', skiprows=1)

    largo = datos.shape[0]
    ancho =  datos.shape[1]

    u_OpenFOAM = np.zeros((largo))
    y_norm_OpenFOAM = np.zeros((largo))


    for i in range(largo):
        y_norm_OpenFOAM[i] = datos[i, 0]/D
        u_OpenFOAM[i] = datos[i, 1]

    y_norm_OpenFOAM = y_norm_OpenFOAM - np.mean(y_norm_OpenFOAM)
    deficit_normalizado_OpenFOAM = 1 - u_OpenFOAM/U_inf


    # calculo sigma de una forma nueva, teniendo en cuenta la atura de los datos de OpenFOAM

    maximo = deficit_normalizado_OpenFOAM[50]
    altura_dosSigma = maximo*0.5753   # altura a la cual tenemos una campana con ancho igual a dos sigmas

    print maximo
    print altura_dosSigma

    idx = np.where(deficit_normalizado_OpenFOAM[7:-7] > altura_dosSigma)

    print deficit_normalizado_OpenFOAM[7:-7]

    print idx[0]

    idx_iSigma = idx[0][0]+7
    idx_fSigma = idx[0][-1]+7

    print idx_iSigma
    print idx_fSigma

    yiSigma = y_norm_OpenFOAM[idx_iSigma]
    yfSigma = y_norm_OpenFOAM[idx_fSigma]

    deficit_iSigma = deficit_normalizado_OpenFOAM[idx_iSigma]
    deficit_fSigma = deficit_normalizado_OpenFOAM[idx_fSigma]

    dosSigma_altura = abs(yiSigma) + abs(yfSigma)
    sigma_altura = dosSigma_altura/2

    sigmaAltura_array.append(sigma_altura)

    # recorto donde tiene sentido que la modele como una gaussiana
    # idx = np.where(deficit_normalizado_OpenFOAM > 0)
    # idx2 = np.diff(idx[0])
    # idx3 = np.where(abs(idx2)>10)
    #
    # idx_i = idx[0][idx3[0][0]+1]
    # idx_f = idx[0][idx3[0][1]]
    #
    # deficit_viejo = deficit_normalizado_OpenFOAM
    # coordenada_vieja = y_norm_OpenFOAM

    # deficit_normalizado_OpenFOAM = deficit_normalizado_OpenFOAM[idx_i:idx_f]
    # y_norm_OpenFOAM = y_norm_OpenFOAM[idx_i:idx_f]


    n = len(y_norm_OpenFOAM)                          #the number of data
    mean = sum(y_norm_OpenFOAM*deficit_normalizado_OpenFOAM)/n                   #note this correction
    sigma = np.sqrt(sum(deficit_normalizado_OpenFOAM*(y_norm_OpenFOAM-mean)**2)/n)        #note this correction

    # p0 is the initial guess for the fitting coefficients (A, mu and sigma above)
    p0 = [0, mean, sigma]

    coeff, var_matrix = curve_fit(gauss, y_norm_OpenFOAM, deficit_normalizado_OpenFOAM, p0=p0)

    A = coeff[0]
    mu = coeff[1]
    sigma = coeff[2]

    # Get the fitted curve
    fit = gauss(y_norm_OpenFOAM, A, mu, sigma)

    plt.figure()
    plt.title('x = {}D'.format(distancia))
    plt.plot(deficit_normalizado_OpenFOAM, 'x', label='Test data')
    plt.plot(fit, 'x', label='Fitted data')
    plt.plot(idx_iSigma, deficit_iSigma, 'o')
    plt.plot(idx_fSigma, deficit_fSigma, 'o')
    # plt.ylim([-0.05, 0.4])
    plt.legend()
    plt.show()


    # plt.figure()
    # plt.title('x = {}D'.format(distancia))
    # plt.plot(y_norm_OpenFOAM, deficit_normalizado_OpenFOAM, label='Test data')
    # plt.plot(y_norm_OpenFOAM, fit, label='Fitted data')
    # plt.ylim([-0.05, 0.4])
    # plt.legend()
    # plt.show()

    # Finally, lets get the fitting parameters, i.e. the standard deviation:



    sigma_array.append(coeff[2])
    A_array.append(coeff[0])

plt.plot(sigma_array, label='vieja')
plt.plot(sigmaAltura_array, label='nueva')
plt.legend()
plt.show()

# quiero ver como quedan los coeficientes con la nueva forma de calcular el sigma:
sigma_array = sigmaAltura_array

# 2)
def linear(x, a, b):
    return (a*x) + b
    # d_0 = 90     # esto es unicamente para las turbinas de Rawson
    # return ((a*x)/d_0) + b

p0= [1, 30]

sigma_array = np.abs(sigma_array)

coeff, var_matrix = curve_fit(linear, x_array, sigma_array, p0)

k_linear = coeff[0]
epsilon_linear = coeff[1]

fit_linear = linear(np.array(x_array), k_linear, epsilon_linear)

plt.figure()
plt.title(r'Ajuste lineal ')
plt.plot(x_array, sigma_array, 'x', label='datos')
plt.plot(x_array, fit_linear, label= r'$\sigma = k \cdot (x/d_0) + \epsilon$ con $k = {:.4f}$ y $\epsilon = {:.4f}$'.format(coeff[0], coeff[1]))
plt.ylabel(r'$\sigma$')
plt.xlabel(r'$x/D$')
plt.legend()
plt.show()


# 3)

def funcion(sigma_n, c_T):
    return 1 - (1-(c_T/(8*(sigma_n**2))))**(0.5)

p0= [1]

coeff, var_matrix = curve_fit(funcion, sigma_array, A_array, p0)

sigmas_continuo = np.linspace(min(sigma_array), max(sigma_array), 100)
fit = funcion(sigmas_continuo, coeff[0])
curva_c_T_a_mano = funcion(sigmas_continuo, 0.8)

# sigma_n =  32.0
# c = 0.504414014776


plt.figure()
plt.title('Ajuste')
plt.plot(sigma_array, A_array, 'x', label='datos')
plt.plot(sigmas_continuo, fit, label= r'$1 - (1-(c_T/(8(sigma_n ^2)))) ^ 0.5$ con $c_T = {:.2f}$'.format(coeff[0]))
plt.plot(sigmas_continuo, curva_c_T_a_mano, label=r'$1 - (1-(c_T/(8*(sigma_n^2))))^0.5$ con $c_T = 0.8$')
# plt.plot(sigma_n, c, 'x')
plt.ylabel(r'$A$')
plt.xlabel(r'$\sigma$')
plt.legend()
plt.show()

# 4)

def funcion_completa(x_norm, k, epsilon):
    c_T = 0.8
    sigma_n = k * x_norm + epsilon
    return 1 - (1-(c_T/(8*(sigma_n**2))))**(0.5)

p0= [0.02, 0.37]

coeff, var_matrix = curve_fit(funcion_completa, x_array, A_array, p0)

x_array_continuo = np.linspace(min(x_array), max(x_array), 100)
fit = funcion_completa(x_array_continuo, coeff[0], coeff[1])

k_completo = coeff[0]
epsilon_completo = coeff[1]

# sigma_n =  32.0
# c = 0.504414014776

plt.figure()
plt.title('Ajuste')
plt.plot(x_array, A_array, 'x', label='datos')
plt.plot(x_array_continuo, fit, label= r'ajuste con $k = {:.4f}$ y $\epsilon = {:.4f}$'.format(coeff[0], coeff[1]))
# plt.plot(sigma_n, c, 'x')
plt.ylabel(r'$A$')
plt.xlabel(r'$x/d$')
plt.legend()
plt.show()


# 5)

fit_completo = linear(np.array(x_array), k_completo, epsilon_completo)

plt.figure()
plt.title(r'Ajuste lineal ')
plt.plot(x_array, sigma_array, 'x', label='datos')
plt.plot(x_array, fit_linear, label= r'$\sigma = k \cdot (x/d_0) + \epsilon$ con $k = {:.4f}$ y $\epsilon = {:.4f}$'.format(k_linear, epsilon_linear))
plt.plot(x_array, fit_completo, label= r'$\sigma = k \cdot (x/d_0) + \epsilon$ con $k = {:.4f}$ y $\epsilon = {:.4f}$'.format(k_completo, epsilon_completo))
plt.ylabel(r'$\sigma$')
plt.xlabel(r'$x/D$')
plt.legend()
plt.show()
