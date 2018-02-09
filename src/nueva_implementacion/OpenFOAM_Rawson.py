from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
# coding=utf-8

"""
Tenemos los datos de OpenFOAM del parametro U para distintas distancias
(la coordenada_y en este estudio es la que yo llame x en mi modelo)
A continuacion se grafica:
    1) El deficit a la altura del hub para una turbina en x = {2.5, 5, 10, 20} D
    Para cada grafico se recortaron los datos de modo de poder ajustar una gaussiana correctamente
    2) El ajuste de los graficos anteriores con su fiteo gaussiano asociado
    3) El ajuste lineal de las sigmas de las gaussianas obtenidas con el fit
    de modo de obtener k y epsilon para el metodo Gaussiana
"""

## esto esta funcionando muy bien! solo faltaria ver el de 20d



# que valor de U_inf uso gonza?? estoy usando U_inf = 8

# 1)
# x = 2.5D

datos = np.loadtxt("lineY-2.5d_U.csv", delimiter = ',', skiprows=1)

largo = datos.shape[0]
ancho =  datos.shape[1]

coordenada_y = np.zeros((largo))
U_x = np.zeros((largo))
U_y = np.zeros((largo))
U_z = np.zeros((largo))

for i in range(largo):
    coordenada_y[i] = datos[i, 0]
    U_x[i] = datos[i, 1]
    U_y[i] = datos[i, 2]
    U_z[i] = datos[i, 3]

U = np.zeros((largo))
deficit_normalizado_25 = np.zeros((largo))
# calculo U:
U[:] = [((U_x[i])**2 + (U_y[i])**2 + (U_z[i])**2)**0.5 for i in range(largo)]

# calculo el deficit:
U_inf = 8
deficit_normalizado_25[:] = [1 - (U[i]/U_inf) for i in range(largo)]

plt.figure()
plt.plot(deficit_normalizado_25)
plt.show()

# recorto donde tiene sentido que la modele como una gaussiana
idx = np.where(deficit_normalizado_25 > 0.03)[0]
idx_i = idx[0]
idx_f = idx[-1]


deficit_normalizado_25 = deficit_normalizado_25[idx_i:idx_f]
coordenada_y = coordenada_y[idx_i:idx_f]

# Define model function to be used to fit to the data above:
def gauss(x, A, mu, sigma):
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))

n = len(coordenada_y)                          #the number of data
mean = sum(coordenada_y*deficit_normalizado_25)/n                   #note this correction
sigma = np.sqrt(sum(deficit_normalizado_25*(coordenada_y-mean)**2)/n)        #note this correction


# p0 is the initial guess for the fitting coefficients (A, mu and sigma above)
p0 = [1., mean, sigma]

coeff, var_matrix = curve_fit(gauss, coordenada_y, deficit_normalizado_25, p0=p0)

A = coeff[0]
mu = coeff[1]
sigma = coeff[2]


# Get the fitted curve
fit = gauss(coordenada_y, A, mu, sigma)

# 2)
plt.plot(coordenada_y, deficit_normalizado_25, label='Test data')
plt.plot(coordenada_y, fit, label='Fitted data')
plt.show()

# Finally, lets get the fitting parameters, i.e. the standard deviation:
print 'Fitted standard deviation = ', coeff[2]
sigma_25 = coeff[2]

# 1)
# x = 5D

datos = np.loadtxt("lineY-5d_U.csv", delimiter = ',', skiprows=1)

largo = datos.shape[0]
ancho =  datos.shape[1]

coordenada_y = np.zeros((largo))
U_x = np.zeros((largo))
U_y = np.zeros((largo))
U_z = np.zeros((largo))

for i in range(largo):
    coordenada_y[i] = datos[i, 0]
    U_x[i] = datos[i, 1]
    U_y[i] = datos[i, 2]
    U_z[i] = datos[i, 3]

U = np.zeros((largo))
deficit_normalizado_5 = np.zeros((largo))
# calculo U:
U[:] = [((U_x[i])**2 + (U_y[i])**2 + (U_z[i])**2)**0.5 for i in range(largo)]

# calculo el deficit:
U_inf = 8
deficit_normalizado_5[:] = [1 - (U[i]/U_inf) for i in range(largo)]

plt.figure()
plt.plot(deficit_normalizado_5)
plt.show()

# recorto donde tiene sentido que la modele como una gaussiana
idx = np.where(deficit_normalizado_5 > 0.03)[0]
idx_i = idx[0]
idx_f = idx[-1]


deficit_normalizado_5 = deficit_normalizado_5[idx_i:idx_f]
coordenada_y = coordenada_y[idx_i:idx_f]

# Define model function to be used to fit to the data above:
def gauss(x, A, mu, sigma):
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))

n = len(coordenada_y)                          #the number of data
mean = sum(coordenada_y*deficit_normalizado_5)/n                   #note this correction
sigma = np.sqrt(sum(deficit_normalizado_5*(coordenada_y-mean)**2)/n)        #note this correction


# p0 is the initial guess for the fitting coefficients (A, mu and sigma above)
p0 = [1., mean, sigma]

coeff, var_matrix = curve_fit(gauss, coordenada_y, deficit_normalizado_5, p0=p0)

A = coeff[0]
mu = coeff[1]
sigma = coeff[2]

# Get the fitted curve
fit = gauss(coordenada_y, A, mu, sigma)

# 2)
plt.plot(coordenada_y, deficit_normalizado_5, label='Test data')
plt.plot(coordenada_y, fit, label='Fitted data')
plt.show()

# Finally, lets get the fitting parameters, i.e. the standard deviation:
print 'Fitted standard deviation = ', coeff[2]
sigma_5 = coeff[2]

# 1)
# x = 10D

datos = np.loadtxt("lineY-10d_U.csv", delimiter = ',', skiprows=1)

largo = datos.shape[0]
ancho =  datos.shape[1]

coordenada_y = np.zeros((largo))
U_x = np.zeros((largo))
U_y = np.zeros((largo))
U_z = np.zeros((largo))

for i in range(largo):
    coordenada_y[i] = datos[i, 0]
    U_x[i] = datos[i, 1]
    U_y[i] = datos[i, 2]
    U_z[i] = datos[i, 3]

U = np.zeros((largo))
deficit_normalizado_10 = np.zeros((largo))
# calculo U:
U[:] = [((U_x[i])**2 + (U_y[i])**2 + (U_z[i])**2)**0.5 for i in range(largo)]

# calculo el deficit:
U_inf = 8
deficit_normalizado_10[:] = [1 - (U[i]/U_inf) for i in range(largo)]

plt.figure()
plt.plot(deficit_normalizado_10)
plt.show()

# recorto donde tiene sentido que la modele como una gaussiana
idx = np.where(deficit_normalizado_10 > 0.03)[0]
idx_i = idx[0]
idx_f = idx[-1]


deficit_normalizado_10 = deficit_normalizado_10[idx_i:idx_f]
coordenada_y = coordenada_y[idx_i:idx_f]

# Define model function to be used to fit to the data above:
def gauss(x, A, mu, sigma):
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))

n = len(coordenada_y)                          #the number of data
mean = sum(coordenada_y*deficit_normalizado_10)/n                   #note this correction
sigma = np.sqrt(sum(deficit_normalizado_10*(coordenada_y-mean)**2)/n)        #note this correction


# p0 is the initial guess for the fitting coefficients (A, mu and sigma above)
p0 = [0.12, mean, sigma]

coeff, var_matrix = curve_fit(gauss, coordenada_y, deficit_normalizado_10, p0=p0)

A = coeff[0]
mu = coeff[1]
sigma = coeff[2]

# Get the fitted curve
fit = gauss(coordenada_y, A, mu, sigma)

# 2)
plt.plot(coordenada_y, deficit_normalizado_10, label='Test data')
plt.plot(coordenada_y, fit, label='Fitted data')
plt.show()

# Finally, lets get the fitting parameters, i.e. the standard deviation:
print 'Fitted standard deviation = ', coeff[2]
sigma_10 = coeff[2]


# 1)
# x = 20D

datos = np.loadtxt("lineY-20d_U.csv", delimiter = ',', skiprows=1)

largo = datos.shape[0]
ancho =  datos.shape[1]

coordenada_y = np.zeros((largo))
U_x = np.zeros((largo))
U_y = np.zeros((largo))
U_z = np.zeros((largo))

for i in range(largo):
    coordenada_y[i] = datos[i, 0]
    U_x[i] = datos[i, 1]
    U_y[i] = datos[i, 2]
    U_z[i] = datos[i, 3]

U = np.zeros((largo))
deficit_normalizado_20 = np.zeros((largo))
# calculo U:
U[:] = [((U_x[i])**2 + (U_y[i])**2 + (U_z[i])**2)**0.5 for i in range(largo)]

# calculo el deficit:
U_inf = 8
deficit_normalizado_20[:] = [1 - (U[i]/U_inf) for i in range(largo)]

plt.figure()
plt.plot(deficit_normalizado_20)
plt.show()

# recorto donde tiene sentido que la modele como una gaussiana
idx = np.where(deficit_normalizado_20 > 0.03)[0]
idx_i = idx[0]
idx_f = idx[-1]


deficit_normalizado_20 = deficit_normalizado_20[idx_i:idx_f]
coordenada_y = coordenada_y[idx_i:idx_f]

# Define model function to be used to fit to the data above:
def gauss(x, A, mu, sigma):
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))

n = len(coordenada_y)                          #the number of data
mean = sum(coordenada_y*deficit_normalizado_20)/n                   #note this correction
sigma = np.sqrt(sum(deficit_normalizado_20*(coordenada_y-mean)**2)/n)        #note this correction


# p0 is the initial guess for the fitting coefficients (A, mu and sigma above)
p0 = [0.12, mean, sigma]

coeff, var_matrix = curve_fit(gauss, coordenada_y, deficit_normalizado_20, p0=p0)

A = coeff[0]
mu = coeff[1]
sigma = coeff[2]

# Get the fitted curve
fit = gauss(coordenada_y, A, mu, sigma)

# 2)
plt.plot(coordenada_y, deficit_normalizado_20, label='Test data')
plt.plot(coordenada_y, fit, label='Fitted data')
plt.show()

# Finally, lets get the fitting parameters, i.e. the standard deviation:
print 'Fitted standard deviation = ', coeff[2]
sigma_20 = coeff[2]

# 3)

coordenadas = np.array([2.5, 5, 10, 20])
sigmas = np.array([abs(sigma_25), abs(sigma_5), abs(sigma_10), abs(sigma_20)])

def linear(x, a, b):
    d_0 = 90     # esto es unicamente para las turbinas de Rawson
    return (a*x)/d_0 + b

p0= [1, 30]

coeff, var_matrix = curve_fit(linear, coordenadas, sigmas, p0)

fit = linear(coordenadas, coeff[0], coeff[1])

plt.figure()
plt.title(r'Ajuste lineal ')
plt.plot(coordenadas, sigmas, 'x', label='datos')
plt.plot(coordenadas, fit, label= r'$\sigma = k \cdot (x/d_0) + \epsilon$ con $k = {:.2f}$ y $\epsilon = {:.2f}$'.format(coeff[0], coeff[1]))
plt.ylabel(r'$\sigma$')
plt.xlabel(r'$x$')
plt.legend()
plt.show()
