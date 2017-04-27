# coding=utf-8

# comparar POTENCIA de las mediciones del blind test con el modelo Gaussiana

# los archivos que voy a comparar son:
# - measurements_distance_1.py
# - blind_test_Gaussiana_distancia_1.py

################################################################################

import numpy as np

from Figura_Scatter import Figura_Scatter
from blind_test_Gaussiana_distancia_1 import y_Gaussiana, deficit_dividido_U_inf_Gaussiana

from Case import Case
from Coordenadas import Coordenadas
from Coordenadas_Norm import Coordenadas_Norm
from Gaussiana import Gaussiana
from Figura import Figura
from math import log

################################################################################
# POTENCIA DISPONIBLE para MODELO GAUSSIANA:

from case_blind_test import case, coordenadas


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

# trucheo:
# k_estrella = 0.023
# epsilon = 0.219

modelo = Gaussiana(case,k_estrella,epsilon)

# corro el modelo:

# el c_T lo saco de los datos medidos, yo no lo voy a calcular, no?
# calculo c_T:
TSR_1 = 5.74
c_T_1 = 0.885

TSR_2 = 6.164
c_T_2 = 0.921

c_T = 0.91 # lo calcule haciendo una regresion lineal con los dos puntos
           # se que no es exactamente lineal (se ve del grafico),
           # pero en ese intervalo se aproxima muy bien por una lineal



modelo.play_cart(coordenadas,c_T)

deficit_dividido_U_inf = modelo.deficit_dividido_U_inf

coordenadas.normalizar

x = coordenadas.x
y = coordenadas.y
z = coordenadas.z
x_n = coordenadas.x_n

z_h = case.z_h

from crear_U_logaritmico import crear_U_logaritmico
from restar_U_inf_menos_deficit import restar_U_inf_menos_deficit

U_inf = crear_U_logaritmico(case,coordenadas)
U_gaussiana =  restar_U_inf_menos_deficit(coordenadas, modelo, U_inf)

from potenciar import potenciar

x_n_0 = 1


potencia_disponible = potenciar(modelo.case.d_0,x_n,y,z,x_n_0,U_gaussiana)
print "Potencia Disponible para el modelo gaussiana:",potencia_disponible

################################################################################
# POTENCIA DISPONIBLE para las MEDICIONES:

from measurements_distance_1 import y,deficit_dividido_U_inf_y,sigma_y

# importante: el deficit de las mediciones tiene que tener el mismo espaciado
# que el de U_inf
# creo que la forma facil de hacer esto es calcular el U_inf a partir del
# vector que usan en las mediciones (el vector es el suguiente: y)

# x = vector x que usabamos en el modelo
# z = vector z que usabamos en el modelo
#
# y = vector y que sale de las mediciones

coordenadas_measurements = Coordenadas(x,y,z)

print "coordenadas_measurements.z =",coordenadas_measurements.z
print "case.z_0 =",case.z_0

U_inf = crear_U_logaritmico(case,coordenadas_measurements)

# me gustaria hacer algo de la pinta:
# U_gaussiana =  restar_U_inf_menos_deficit(coordenadas_measurements, modelo, U_inf)
# pero no puedo por un tema de dimensiones... asi que hago lo siguiente:

from indexar import indexar

indice_x_n_1 = indexar(x_n,1)
indice_z_h = indexar(z,z_h)


deficit_dividido_U_inf_y_matrix = np.zeros((len(coordenadas_measurements.x),len(coordenadas_measurements.y),len(coordenadas_measurements.z)))
deficit_dividido_U_inf_y_matrix[indice_x_n_1,:,indice_z_h] = deficit_dividido_U_inf_y

U = np.zeros((len(coordenadas_measurements.x),len(coordenadas_measurements.y),len(coordenadas_measurements.z)))
for i in range (0,len(coordenadas_measurements.x)):
    for j in range (0,len(coordenadas_measurements.y)):
        for k in range (1,len(coordenadas_measurements.z)):
            U[i,j,k] = U_inf[i,j,k] * (1 - deficit_dividido_U_inf_y_matrix[i,j,k])

x_y = {"x_1" : y, "y_1" : U_inf[indice_x_n_1,:,indice_z_h]}
nombre = "y vs U_inf en x/d=1"
xLabel = r'$y$'
yLabel = r'$ U_{\infty}$'

figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()



# esa matriz U[i,j,k] solo tiene sentido para:
# [i,j,k] = [indice_x_n_1,j,indice_z_h]

# grafico a ver que onda

# print "len(y) =",len(y)
# print "U.shape =",U.shape
# print "deficit_dividido_U_inf_y =",deficit_dividido_U_inf_y
# print "U_inf =",U_inf



x_y = {"x_1" : y, "y_1" : U[indice_x_n_1,:,indice_z_h]}
nombre = "y vs U en x/d=1 en z_h"
xLabel = r'$y$'
yLabel = r'$U en x/d=1 en z_h$'

figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()

# ambos graficos tienen sentido:
#
# 1. el grafico de U_inf muestra que para un dado y el U vale lo mismo, perfecto,
# ya que solo deberia depender de z
# 2. el grafico de U muestra que en el eje y el perfil logaritmico no influye en nada
#
# veamos que en z SI deberia cambiar:

################################################################################
from measurements_distance_1 import z,deficit_dividido_U_inf_z,sigma_z
# vamos a tener problemas con esto ya que z no está definido igual que nuestro z,
# acá el 0 está centrado en el hub

for i in range (0,len(z)):
    z[i] = z[i] + z_h

# los valores de z que son negativos deberia volarlos, no tienen sentido físico
# por ahora los dejo, pero habria que borrarlos
# creo que no me queda otra que borrarlos porque sino no puedo calcular el log
# de todas formas no entiendo: por que existen mediciones para esa altura?

indice_z_nulo = indexar(z,0)
z = z[:indice_z_nulo]

deficit_dividido_U_inf_z = deficit_dividido_U_inf_z[:indice_z_nulo]

# print "z truncado =",z

coordenadas_measurements = Coordenadas(x,y,z)

U_inf = crear_U_logaritmico(case,coordenadas_measurements)

from indexar import indexar

indice_x_n_1 = indexar(x_n,1)
indice_z_h = indexar(z,z_h)

deficit_dividido_U_inf_z_matrix = np.zeros((len(coordenadas_measurements.x),len(coordenadas_measurements.y),len(coordenadas_measurements.z)))
deficit_dividido_U_inf_z_matrix[indice_x_n_1,0,:] = deficit_dividido_U_inf_z

U = np.zeros((len(coordenadas_measurements.x),len(coordenadas_measurements.y),len(coordenadas_measurements.z)))
for i in range (0,len(coordenadas_measurements.x)):
    for j in range (0,len(coordenadas_measurements.y)):
        for k in range (1,len(coordenadas_measurements.z)):
            U[i,j,k] = U_inf[i,j,k] * (1 - deficit_dividido_U_inf_z_matrix[i,j,k])

# y = 0 es el medio del hub

# esa matriz U[i,j,k] solo tiene sentido para:
# [i,j,k] = [indice_x_n_1,0,:]

# print "U_inf =", U_inf[indice_x_n_1,0,:]

x_y = {"x_1" : z, "y_1" : U_inf[indice_x_n_1,0,:]}
nombre = "z vs U_inf en x/d=1 en y=0"
xLabel = r'$z$'
yLabel = r'$ U_{\infty} en x/d=1 en y=0$'

figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()


# grafico a ver que onda

# print "len(y) =",len(y)
# print "U.shape =",U.shape
# print "deficit_dividido_U_inf_y =",deficit_dividido_U_inf_y
# print "U_inf =",U_inf

x_y = {"x_1" : z, "y_1" : U[indice_x_n_1,0,:]}
nombre = "z vs U en x/d=1 en y=0"
xLabel = r'$z$'
yLabel = r'$U en x/d=1 en y=0$'

figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()

# conclusiones de esto:
# los graficos no son nada prolijos, habria que frenar y pensar si lo que estoy
# haciendo tiene sentido antes de seguir con el calculo de la potencia

# no se cuan bien esta lo de aplicarle el perfil de viento logaritmico a las
# mediciones, me parece un enchastre

################################################################################
# calculo de POTENCIA

# la idea seria calcular la potencia en un plano
# primero voy a calcular en el plano donde el perfil logaritmico importa,
# es decir en el plano (x,z)

rho = 1.225

# def potenciar(d_0,x,y,z,x_0,U):
#     radio = d_0 / 2
#     area = 3.14 * (radio**2)
#     coeficiente = 0.5 * rho * area
#     indice_radio_y = indexar(y,radio)
#     indice_radio_z = indexar(z,radio)
#     indice_x_0 = indexar(x,x_0)
#     potencia_disponible_parcial = np.zeros((indice_radio_y,indice_radio_z))
#     potencia_disponible = 0
#     for i in range (0,indice_radio_y):
#         for j in range (0,indice_radio_z):
#             potencia_disponible_parcial[i,j] = coeficiente * U[indice_x_0,i,j]
#             potencia_disponible = sum(sum(potencia_disponible_parcial))
#     return potencia_disponible






# potencia_disponible = potenciar(modelo.case.d_0,x,y,z,x_0,U)
# print "Potencia Disponible:",potencia_disponible
