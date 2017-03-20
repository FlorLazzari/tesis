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

x_n = np.arange(0,2,0.05)
y_n = np.arange(0,2,0.05)
z_n = np.arange(0,2,0.05)

d_0 = 0.15

x = d_0 * x_n
y = d_0 * y_n
z = d_0 * z_n

d_0 = 0.15
z_h = 0.125
U_hub = 2.2
C_T = 0.42
z_0 = 0.00003
I_0 = 0.07

case = Case(d_0,z_h,U_hub,C_T,z_0,I_0)
coordenadas = Coordenadas(x,y,z)

k_estrella = 0.2
epsilon = 0.268855463528

modelo = Gaussiana(case,k_estrella,epsilon)

c_T = 0.5

modelo.play_cart(coordenadas,c_T)

from crear_U_logaritmico import crear_U_logaritmico
from restar_U_inf_menos_deficit import restar_U_inf_menos_deficit

U_inf = crear_U_logaritmico(case,coordenadas)
U_gaussiana =  restar_U_inf_menos_deficit(coordenadas, modelo, U_inf)

from potenciar import potenciar

x_0 = 0.2

potencia_disponible = potenciar(modelo.case.d_0,x,y,z,x_0,U_gaussiana)
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
# U_gaussiana =  restar_U_inf_menos_deficit(coordenadas_measurements, modelo, U_inf)


from indexar import indexar

indice_x_n_1 = indexar(x_n,1)
indice_z_h = indexar(z,z_h)


# U[i,j,k] = U_inf[indice_x_0,j,k] * (1 - deficit_dividido_U_inf_y)

# print type(U_inf)
# print type(deficit_dividido_U_inf_y)
# print U_inf.shape
# print len(deficit_dividido_U_inf_y)
deficit_dividido_U_inf_y_matrix = np.zeros((len(coordenadas_measurements.x),len(coordenadas_measurements.y),len(coordenadas_measurements.z)))
deficit_dividido_U_inf_y_matrix[indice_x_n_1,:,indice_z_h] = deficit_dividido_U_inf_y

U = np.zeros((len(coordenadas_measurements.x),len(coordenadas_measurements.y),len(coordenadas_measurements.z)))
for i in range (0,len(coordenadas_measurements.x)):
    for j in range (0,len(coordenadas_measurements.y)):
        for k in range (1,len(coordenadas_measurements.z)):
            U[i,j,k] = U_inf[i,j,k] * (1 - deficit_dividido_U_inf_y_matrix[i,j,k])

print "U_inf =", U_inf[indice_x_n_1,:,indice_z_h]

x_y = {"x_1" : y, "y_1" : U_inf[indice_x_n_1,:,indice_z_h]}
nombre = "y/d vs deficit_dividido_U_inf x/d=1"
xLabel = r'$y/d$'
yLabel = r'$ \Delta U / U_{\infty}$'

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
nombre = "y/d vs deficit_dividido_U_inf x/d=1"
xLabel = r'$y/d$'
yLabel = r'$ \Delta U / U_{\infty}$'

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


print "z truncado =",z

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

print "U_inf =", U_inf[indice_x_n_1,0,:]

x_y = {"x_1" : z, "y_1" : U_inf[indice_x_n_1,0,:]}
nombre = "y/d vs deficit_dividido_U_inf x/d=1"
xLabel = r'$y/d$'
yLabel = r'$ \Delta U / U_{\infty}$'

figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()

# esa matriz U[i,j,k] solo tiene sentido para:
# [i,j,k] = [indice_x_n_1,0,:]

# grafico a ver que onda

# print "len(y) =",len(y)
# print "U.shape =",U.shape
# print "deficit_dividido_U_inf_y =",deficit_dividido_U_inf_y
# print "U_inf =",U_inf



x_y = {"x_1" : z, "y_1" : U[indice_x_n_1,0,:]}
nombre = "y/d vs deficit_dividido_U_inf x/d=1"
xLabel = r'$y/d$'
yLabel = r'$ \Delta U / U_{\infty}$'

figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()

# conclusiones de esto:
# los graficos no son nada prolijos, habria que frenar y pensar si lo que estoy
# haciendo tiene sentido antes de seguir con el calculo de la potencia

################################################################################
# calculo de POTENCIA

rho = 1.225
#
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
