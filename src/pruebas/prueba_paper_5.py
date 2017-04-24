# coding=utf-8

import numpy as np

from Case import Case
from Coordenadas import Coordenadas
from Coordenadas_Norm import Coordenadas_Norm
from Gaussiana import Gaussiana
from Figura import Figura
from math import log

################################################################################
# coordenadas:

x_n = np.arange(0,20,0.05)
y_n = np.arange(0,3,0.05)
z_n = np.arange(0,3,0.05)

d_0 = 0.15

x = d_0 * x_n
y = d_0 * y_n
z = d_0 * z_n

# inicializo caso, coordenadas, modelo:

# case = 1 :
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
k_estrella = 0.023
epsilon = 0.219
# estos valores de k_estrella y epsilon los saqué del ajuste de la lineal del gráfico
# de sigmna_n vs x_n (figura 4)

# estos valores salen del calculo en la introduccion
# k_estrella = 0.2
# epsilon = 0.268855463528

modelo = Gaussiana(case,k_estrella,epsilon)

# corro el modelo:

c_T = 0.42

# como voy a graficar en funcion de "r" (que en realidad lo estoy estudiando como
# r == z) no quiero que normalice con z_hub, entonces uso play_pol:
modelo.play_pol(coordenadas,c_T)

################################################################################
# figura 5: ( deficit_dividido_U_inf )_{max} vs x_n

from barrer import barrer

barrido_x_n = barrer(x_n)
# el máximo lo consigo para el valor mas pequeño de y_n y z_n por eso los tomo nulos

x_y = { 'x_1': modelo.x_n, 'y_1': modelo.deficit_dividido_U_inf[barrido_x_n,0,0] }

nombre = "figura_5"
xLabel = r'$x / d_{0}$'
yLabel = r'$ (\Delta U / U_{\infty})_{max} $'
numero = 1

from Figura_Scatter import Figura_Scatter

figura = Figura_Scatter(nombre,x_y,xLabel,yLabel,numero)
figura.yLim = [0,0.6]
figura.xLim = [2,20]
figura.show()

# figura 5 del paper : checked! (no queda exactamente igual que el del paper pero
# cambia mucho dependiendo del epsilon y el k_estrella asi que tengo que entender
# bien cuales usaron)
