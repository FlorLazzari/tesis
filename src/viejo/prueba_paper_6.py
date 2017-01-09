# coding=utf-8

import numpy as np

from Case import Case
from Coordenadas import Coordenadas
from Coordenadas_Norm import Coordenadas_Norm
from Gaussiana import Gaussiana
from Figura import Figura
from math import log

# problemas: no me esta guardando las figuras ni los plots!


################################################################################
# coordenadas:

# las coordenadas deben ser un cubo, sino no puedo usar "contour" en todas las
# direcciones
x_n = np.arange(0,2,0.05)
y_n = np.arange(0,2,0.05)
z_n = np.arange(0,2,0.05)

d_0 = 0.15

x = d_0 * x_n
y = d_0 * y_n
z = d_0 * z_n


# inicializo caso, coordenadas, modelo:

d_0 = 0.15
z_h = 0.125
U_hub = 2.2
C_T = 0.42
z_0 = 0.00003
I_0 = 0.07

case = Case(d_0,z_h,U_hub,C_T,z_0,I_0)
coordenadas = Coordenadas(x,y,z)

# para que los resultados sean comparables a los del paper uso los datos que dan en
# la introducción para k_estrella y epsilon (si uso lo del fit lineal de la figura 4
# el gráfico 3 queda cualquier cosa):
# k_estrella = 0.023
# epsilon = 0.219
# estos valores de k_estrella y epsilon los saqué del ajuste de la lineal del gráfico
# de sigmna_n vs x_n (figura 4)

# estos valores salen del calculo en la introduccion
k_estrella = 0.2
epsilon = 0.268855463528

modelo = Gaussiana(case,k_estrella,epsilon)

# corro el modelo:

c_T = 0.5

# no voy a graficar en funcion de "r" (que en realidad lo estoy estudiando como
# r == z), quiero que normalice con z_hub, entonces uso play_cart:
modelo.play_cart(coordenadas,c_T)

################################################################################
# primero voy a hacer x_n vs z_n vs deficit_dividido_U_inf

from Contour import Contour
from colapsar import colapsar

# colapso en la posición y = 0:
b = colapsar(modelo.deficit_dividido_U_inf,0)
a = b.transpose()

x_z_a = {'x_1': modelo.x_n, 'z_1': modelo.z_n, 'a_1': a}

nombre = "figura_6_deficit"
xLabel = r'$x / d_{0}$'
yLabel = r'$z / d_{0}$'

contour = Contour(nombre,x_z_a,xLabel,yLabel)
contour.show()

# figura 6_deficit del paper (sin la condicion de viento externo correcto): checked!


################################################################################
# figura 6: z_n vs U_inf
#
# U_hub = case.U_hub
# z_h = case.z_h
# z_0 = case.z_0
# z_0_vect = case.z_0 * np.ones((len(modelo.z_n)))
#
divi = np.zeros((len(modelo.z_n)))
num = np.zeros((len(modelo.z_n)))
U_inf = np.zeros((len(modelo.z_n)))

denom = log(z_h / z_0) * np.ones((len(modelo.z_n)))
#
# for k in range(1,len(modelo.z_n)):
#     divi[k] = modelo.z[k] / z_0_vect[k]
#     num[k] = log(divi[k])
#     U_inf[k] = U_hub * ( num[k] / denom[k] )
#
# x_y = {'x_1': np.arange(0,len(modelo.z_n)), 'y_1': U_inf}
#
# nombre = "figura_6 z_n vs U_inf"
# xLabel = r'$z / d_{0}$'
# yLabel = r'$U_{inf}$'
#
#
# figura_prueba = Figura(nombre,x_y,xLabel,yLabel,1)
# figura_prueba.show()

################################################################################
# figura 6: z_n vs U_inf para distintos valores de x
#           z_n vs U_inf para distintos valores de y

U_inf_y = np.zeros((len(modelo.x_n),len(modelo.y_n),len(modelo.z_n)))
U_inf = np.zeros((len(modelo.x_n),len(modelo.y_n),len(modelo.z_n)))
U = np.zeros((len(modelo.x_n),len(modelo.y_n),len(modelo.z_n)))


# for i in range (0,len(x_n)):
#     for j in range (0,len(y_n)):
#         U_inf[i,j,0] = 0

for i in range (0,len(x_n)):
    for j in range (0,len(y_n)):
        for k in range (1,len(z_n)):
            divi[k] = modelo.z[k] / z_0
            num[k] = log(divi[k])
            # U_inf_y[i,0,k] = U_hub * ( num[k] / denom[k] )
            # U_inf[i,j,k] = U_inf_y[i,0,k]
            U_inf[i,j,k] = U_hub * ( num[k] / denom[k] )
            U[i,j,k] = U_inf[i,j,k] * (1 - modelo.deficit_dividido_U_inf[i,j,k])


a = U_inf[0,0,:]
b = U_inf[3,0,:]
c = U_inf[10,0,:]
x_y = {'x_1': np.arange(0,len(modelo.z_n)), 'y_1': a,
       'x_2': np.arange(0,len(modelo.z_n)), 'y_2': b,
       'x_3': np.arange(0,len(modelo.z_n)), 'y_3': c }

nombre = "figura_6 z_n vs U_inf para distintos valores de x"
xLabel = r'$z / d_{0}$'
yLabel = r'$U_{inf}$'


figura_prueba = Figura(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show_save("figura_6")
# para distintos x da lo mismo!


a = U_inf[0,0,:]
b = U_inf[0,3,:]
c = U_inf[0,10,:]
x_y = {'x_1': np.arange(0,len(modelo.z_n)), 'y_1': a,
       'x_2': np.arange(0,len(modelo.z_n)), 'y_2': b,
       'x_3': np.arange(0,len(modelo.z_n)), 'y_3': c }

nombre = "figura_6 z_n vs U_inf para distintos valores de y"
xLabel = r'$z / d_{0}$'
yLabel = r'$U_{inf}$'


figura_prueba = Figura(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()
# para distintos y da lo mismo!


# problemas: U_inf deberia tener simetria traslacional en y
#            U_inf tiene simetria esferica  ???


################################################################################
# figura 6: x_n vs z_n vs U para distintos valores de x
#           x_n vs z_n vs U para distintos valores de y

from colapsar import colapsar
from colapsar_x import colapsar_x
from Contour import Contour

# colapso en la posición y = 0:
b = colapsar(U,0)
a = b.transpose()

x_z_a = {'x_1': modelo.x, 'z_1': modelo.z, 'a_1': a}

nombre = "z_n vs U_inf para distintos valores de y (y=0)"
xLabel = r'$x / d_{0}$'
yLabel = r'$z / d_{0}$'

contour = Contour(nombre,x_z_a,xLabel,yLabel)
contour.show_save("figuras_6")

# colapso en la posición x = 0:
b = colapsar_x(U,0)
a = b.transpose()

x_z_a = {'x_1': modelo.y, 'z_1': modelo.z, 'a_1': a}

nombre = "z_n vs U_inf para distintos valores de x (x=0)"
xLabel = r'$y / d_{0}$'
yLabel = r'$z / d_{0}$'

contour = Contour(nombre,x_z_a,xLabel,yLabel)
contour.show_save("figuras_6")

# colapso en la posición y = 10:
b = colapsar(U,10)
a = b.transpose()

x_z_a = {'x_1': modelo.x, 'z_1': modelo.z, 'a_1': a}

nombre = "z_n vs U_inf para distintos valores de y (y=10)"
xLabel = r'$x / d_{0}$'
yLabel = r'$z / d_{0}$'

contour = Contour(nombre,x_z_a,xLabel,yLabel)
contour.show_save("figuras_6")

# colapso en la posición x = 10:
b = colapsar_x(U,10)
a = b.transpose()

x_z_a = {'x_1': modelo.y, 'z_1': modelo.z, 'a_1': a}

nombre = "z_n vs U_inf para distintos valores de x (x=10)"
xLabel = r'$y / d_{0}$'
yLabel = r'$z / d_{0}$'

contour = Contour(nombre,x_z_a,xLabel,yLabel)
contour.show_save("figuras_6")

# colapso en la posición y = 20:
b = colapsar(U,10)
a = b.transpose()

x_z_a = {'x_1': modelo.x, 'z_1': modelo.z, 'a_1': a}

nombre = "z_n vs U_inf para distintos valores de y (y=20)"
xLabel = r'$x / d_{0}$'
yLabel = r'$z / d_{0}$'

contour = Contour(nombre,x_z_a,xLabel,yLabel)
contour.show_save("figuras_6")

# colapso en la posición x = 20:
b = colapsar_x(U,20) # == U[20,:,:]
a = b.transpose()

x_z_a = {'x_1': modelo.y, 'z_1': modelo.z, 'a_1': a}

nombre = "z_n vs U_inf para distintos valores de x (x=20)"
xLabel = r'$y / d_{0}$'
yLabel = r'$z / d_{0}$'

contour = Contour(nombre,x_z_a,xLabel,yLabel)
contour.show_save("figuras_6")

# faltaria analizar estos graficos

# para un mejor analisis quiero hacer este mismo grafico en 3D:

# # ejemplos de graficos 3D que no aportan mucho:
#
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# #from matplotlib.ticker import LinearLocator, FormatStrFormatter
# import matplotlib.pyplot as plt
#
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
#
# fig.colorbar(surf, shrink=0.5, aspect=5)
#
# plt.show()
#
# ########
# b = colapsar(U,0)
# a = b.transpose()
#
# x_z_a = {'x_1': modelo.x, 'z_1': modelo.z, 'a_1': a}
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# X = modelo.x
# Y = modelo.z
# X, Y = np.meshgrid(X, Y)
# Z = a
# surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
#
# fig.colorbar(surf, shrink=0.5, aspect=5)
#
# plt.show()
# #########
# from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt
# from matplotlib import cm
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# X, Y, Z = axes3d.get_test_data(0.05)
# cset = ax.contourf(X, Y, Z, cmap=cm.coolwarm)
# ax.clabel(cset, fontsize=9, inline=1)
#
# plt.show()
# ########
# from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt
# from matplotlib import cm
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# X = modelo.x
# Y = modelo.z
# Z = a
#
# cset = ax.contourf(X, Y, Z, cmap=cm.coolwarm)
# ax.clabel(cset, fontsize=9, inline=1)
#
# plt.show()
