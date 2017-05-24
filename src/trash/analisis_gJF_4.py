# coding=utf-8     

from __future__ import division  # para evitar el problema de la división entera (must occur at the beginning of the file)

import numpy as np # para trabajar con arrays de forma mas eficiente (tipo matlab)

from numpy import exp, abs, angle, pi

import matplotlib.pyplot as plt # para hacer los gráficos




# voy a comparar los 3 modelos: gaussiana, Jensen y Frandsen

import gaussiana_1
import Jensen_2
import Frandsen_3



# no trabajo con el mismo intervalo en x_n para los tres modelos, importo el x_n de cada uno


# variables que me interesan de cada archivo:

# gaussiana_1:

x_n_gaussiana = gaussiana_1.x_n
deficit_dividido_U_inf_gaussiana = gaussiana_1.y_2[0]

# como para todos los valores de r encuentro cosas demasiado similares me quedo con un r arbitrario

plt.ioff()
plt.xlabel(r'$ x / d_{0} $')
plt.ylabel(r'$\Delta U / U_{\infty} $')
plt.plot(x_n_gaussiana,deficit_dividido_U_inf_gaussiana, 'x')
plt.show()


# Jensen_2:

x_n_Jensen = Jensen_2.x_n
deficit_dividido_U_inf_Jensen = Jensen_2.deficit_dividido_U_inf

plt.ioff()
plt.xlabel(r'$ x / d_{0} $')
plt.ylabel(r'$\Delta U / U_{\infty} $')
plt.plot(x_n_Jensen,deficit_dividido_U_inf_Jensen, 'x')
plt.show()


# Frandsen_3:

x_n_Frandsen = Frandsen_3.x_n
deficit_dividido_U_inf_Frandsen = Frandsen_3.deficit_dividido_U_inf

plt.ioff()
plt.xlabel(r'$ x / d_{0} $')
plt.ylabel(r'$\Delta U / U_{\infty} $')
plt.plot(x_n_Frandsen,deficit_dividido_U_inf_Frandsen, 'x')
plt.show()

# comparación de los tres modelos:

plt.ioff()
plt.xlim([0,10])
plt.xlabel(r'$ x / d_{0} $')
plt.ylabel(r'$\Delta U / U_{\infty} $')
plt.plot(x_n_gaussiana,deficit_dividido_U_inf_gaussiana, 'x')
plt.legend("Gaussiana")
plt.plot(x_n_Jensen,deficit_dividido_U_inf_Jensen, 'x')
plt.legend("Jensen")
plt.plot(x_n_Frandsen,deficit_dividido_U_inf_Frandsen, 'x')
plt.legend("Frandsen")
plt.show()


# a los gráficos les falta:

# legend
# titulos


# no se cómo se poner ninguno de los dos..

# este último gráfico no está dando como debería (comparar con la fig 6 del paper)



