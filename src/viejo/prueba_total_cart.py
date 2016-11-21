# coding=utf-8

import numpy as np

from Case import Case
from Coordenadas import Coordenadas
from Gaussiana import Gaussiana
from Figura import Figura

################################################################################

x_n = np.arange(0,4.5,0.05)
y_n = np.arange(0,4,0.05)
z_n = np.arange(0,5,0.05)

d_0 = 0.15

x = d_0 * x_n
y = d_0 * y_n
z = d_0 * z_n

################################################################################

case_1 = Case(0.15,0.125,2.2,0.42,0.00003,0.07)
coordenadas_2 = Coordenadas(x,y,z)

modelo_2 = Gaussiana(case_1,0.2,0.25)

modelo_2.play_cart(coordenadas_2,0.5)

from fraccionar import fraccionar
from barrer import barrer

barrido_z_n = barrer(modelo_2.z_n)
v_0, v_1, v_2, v_3 = fraccionar(modelo_2.x_n)

nombre = "testDrive"
xLabel = r'$z/d_{0}$'
yLabel = r'$\Delta U / \Delta U_{max} $'
numero = 1

print(modelo_2.gauss)
print(modelo_2.z_n)

x_y = { 'x_1': modelo_2.z_n, 'y_1': modelo_2.gauss[v_0,0,barrido_z_n]}

figura_1 = Figura(nombre,x_y,xLabel,yLabel,numero)
figura_1.show_save()

################################################################################

from Contour import Contour
from colapsar import colapsar

# colapso en la posición y = 0:
b = colapsar(modelo_2.deficit_dividido_U_inf,0)
a = b.transpose()

x_z_a = {'x_1': modelo_2.x_n, 'z_1': modelo_2.z_n, 'a_1': a}

contour_1 = Contour("contour_1",x_z_a,"xLabel","yLabel")
contour_1.show()
