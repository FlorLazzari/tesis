# coding=utf-8

import numpy as np

# me gustaria hacer algo asi para ordenar la implementacion en carpetas:
# import sys
# sys.path.append(/home/florencia/Documentos/tesis_gitHub/tesis/src/nueva_implementacion/casos)
# from Case_2 import Case

from Case_2 import Case
from Coordenadas import Coordenadas
from Coordenadas_Norm import Coordenadas_Norm
from Gaussiana_2 import Gaussiana

################################################################################

d_0 = 0.15
z_h = 0.125
U_hub = 2.2

pto = 1.9

case = Case(d_0,z_h,U_hub)
coord = np.array([pto, pto, pto])

k_estrella = 0.2
epsilon = 0.268855463528

gaussiana = Gaussiana(case,k_estrella,epsilon)

c_T = 0.5

deficit_dividido_U_inf = gaussiana.evalDeficitNorm(coord,c_T)

print "gaussiana nueva = ", deficit_dividido_U_inf

################################################################################

from Gaussiana import Gaussiana
from Case import Case
from indexar import indexar

x = np.arange(0,pto+1,0.1)
y = np.arange(0,pto+1,0.1)
z = np.arange(0,pto+1,0.1)

indice_x_1 = indexar(x, pto)
indice_y_1 = indexar(y, pto)
indice_z_1 = indexar(z, pto)

c_T = 0.5
z_0 = 0.00003
I_0 = 0.07

case = Case(d_0,z_h,U_hub,c_T,z_0,I_0)
coordenadas = Coordenadas(x,y,z)

modelo = Gaussiana(case,k_estrella,epsilon)



modelo.play_cart(coordenadas,c_T)

print "gaussiana vieja = ", modelo.deficit_dividido_U_inf[indice_x_1, indice_y_1, indice_z_1]


# problemas! no obtengo los mismos resultados para las implementaciones
# distintas unicamente para ptos enteros
