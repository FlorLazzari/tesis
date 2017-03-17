# coding=utf-8


# comparar POTENCIA de las mediciones del blind test con el modelo Gaussiana

# los archivos que voy a comparar son:
# - measurements_distance_1.py
# - blind_test_Gaussiana_distancia_1.py

################################################################################

import numpy as np

from Figura_Scatter import Figura_Scatter
from measurements_distance_1 import y,deficit_dividido_U_inf_y,sigma_y,z,deficit_dividido_U_inf_z,sigma_z
from blind_test_Gaussiana_distancia_1 import y_Gaussiana, deficit_dividido_U_inf_Gaussiana

from Case import Case
from Coordenadas import Coordenadas
from Coordenadas_Norm import Coordenadas_Norm
from Gaussiana import Gaussiana
from Figura import Figura
from math import log


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


divi = np.zeros((len(modelo.z_n)))
num = np.zeros((len(modelo.z_n)))
U_inf = np.zeros((len(modelo.z_n)))

denom = log(z_h / z_0) * np.ones((len(modelo.z_n)))

from crear_U_logaritmico import crear_U_logaritmico
from restar_U_inf_menos_deficit import restar_U_inf_menos_deficit

U_inf = crear_U_logaritmico(case,coordenadas)
U_gaussiana =  restar_U_inf_menos_deficit(coordenadas, modelo, U_inf)

from potenciar import potenciar

x_0 = 0.2

potencia_disponible = potenciar(modelo.case.d_0,x,y,z,x_0,U)
print "Potencia Disponible:",potencia_disponible

# POTENCIA DISPONIBLE para las MEDICIONES:

U_measurements =  restar_U_inf_menos_deficit(coordenadas, modelo, U_inf)

U[i,j,k] = U_inf[x_0,j,k] * (1 - deficit_dividido_U_inf_x)


U = np.zeros((len(Coordenadas.x),len(Coordenadas.y),len(Coordenadas.z)))
for i in range (0,len(Coordenadas.x)):
    for j in range (0,len(Coordenadas.y)):
        for k in range (1,len(Coordenadas.z)):
            U[i,j,k] = U_inf[i,j,k] * (1 - Gaussiana.deficit_dividido_U_inf[i,j,k])
return U





from potenciar import potenciar

x_0 = 0.2

potencia_disponible = potenciar(modelo.case.d_0,x,y,z,x_0,U)
print "Potencia Disponible:",potencia_disponible




x_y = {"x_1" : y, "y_1" : deficit_dividido_U_inf_y,
       "x_2" : y_Gaussiana, "y_2" : deficit_dividido_U_inf_Gaussiana}
nombre = "y/d vs deficit_dividido_U_inf x/d=3"
xLabel = r'$y/d$'
yLabel = r'$ \Delta U / U_{\infty}$'


figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,2)
figura_prueba.xLim = [-2,2]
figura_prueba.show()
