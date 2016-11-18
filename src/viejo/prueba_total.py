# coding=utf-8

import numpy as np

from Case import Case
from Coordenadas import Coordenadas
from Gaussiana import Gaussiana
from Figura import Figura

x_n = np.arange(0,15,0.01)
y_n = np.arange(0,4.5,0.005)
z_n = np.arange(0,4.5,0.005)

d_0 = 0.15

x = d_0 * x_n
y = d_0 * y_n
z = d_0 * z_n


case_1 = Case(0.15,0.125,2.2,0.42,0.00003,0.07)
coordenadas_1 = Coordenadas(x,y,z)

modelo_1 = Gaussiana(coordenadas_1,0.5,case_1,0.2,0.25)

modelo_1.play()


from fraccionar import fraccionar
from barrer import barrer

barrido_r = barrer(modelo_1.r)
v_0, v_1, v_2, v_3 = fraccionar(modelo_1.x_n)

nombre = "testDrive"
xLabel = 'r'
yLabel = r'$\Delta U / \Delta U_{max} $'
numero = 4

x_y = { 'x_1': modelo_1.r, 'y_1': modelo_1.gauss[v_0,barrido_r],
        'x_2': modelo_1.r, 'y_2': modelo_1.gauss[v_1,barrido_r],
        'x_3': modelo_1.r, 'y_3': modelo_1.gauss[v_2,barrido_r],
        'x_4': modelo_1.r, 'y_4': modelo_1.gauss[v_3,barrido_r]}

figura_1 = Figura(nombre,x_y,xLabel,yLabel,numero)
figura_1.show_save()

# el save de la figura no esta funcionando
################################################################################

from Contour import Contour
#
# a = modelo_1.deficit_dividido_U_inf.transpose()
#
# x_z_a = {'x_1': modelo_1.x_n, 'z_1': modelo_1.r, 'a_1': a}
#
# contour_1 = Contour("contour_1",x_z_a,"xLabel","yLabel")
#
# contour_1.show()

#########


import matplotlib.pyplot as plt # para hacer los gráficos


fig = plt.figure()
plt.xlabel(r'$ x / d_{0} $')
plt.ylabel('r')
plt.title('Gaussian Filled Contour Plot')
cp = plt.contourf(modelo_1.x_n,modelo_1.r,modelo_1.deficit_dividido_U_inf.transpose())
plt.colorbar(cp)
plt.show()
plt.figure()


##########
# print(modelo_1.gauss)
# print(modelo_1.exponente)
print(modelo_1.c)
#print(modelo_1.deficit_dividido_U_inf)
