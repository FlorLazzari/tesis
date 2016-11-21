# coding=utf-8

import numpy as np

from Case import Case
from Coordenadas import Coordenadas
from Gaussiana import Gaussiana
from Figura import Figura
from math import log

################################################################################
# coordenadas:

x_n = np.arange(0,4.5,0.05)
y_n = np.arange(0,5,0.05)
z_n = np.arange(0,5,0.05)
# tengo que usar los vectores y_z y z_n del mismo tamaño porque sino no puedo
# usar cart2pol

d_0 = 0.15

x = d_0 * x_n
y = d_0 * y_n
z = d_0 * z_n

# inicializo caso, coordenadas, modelo:
case = Case(0.15,0.125,2.2,0.42,0.00003,0.07)
coordenadas = Coordenadas(x,y,z)
modelo = Gaussiana(case,0.2,0.25)

# corro el modelo:
modelo.play_cart(coordenadas,0.5)

################################################################################
# figura 3: delta_U / delta_U_inf vs r / r_{1/2}

from cart2pol import cart2pol

r_n, phi = cart2pol(y_n, z_n)

# calculo r_medio (alaliticamente) : (para cada x voy a tener un r_medio)

cociente_r_r_medio = np.zeros((len(modelo.x_n),len(modelo.z_n)))
r_medio = log(2) * 2 * (modelo.sigma_n**2)

# esto sale de hacer la cuenta
# por definición log es en base e

for i in range (0,len(x_n)):
    for j in range (0,len(r_n)):
        cociente_r_r_medio[i,j] = r_n[j]/r_medio[i]

from fraccionar import fraccionar
from barrer import barrer

v_0, v_1, v_2, v_3 = fraccionar(modelo.x_n)
barrido_r_n = barrer(r_n)

print(len(cociente_r_r_medio[v_0,barrido_r_n]))
print(len(modelo.gauss[v_0,barrido_r_n]))

print(len(cociente_r_r_medio[v_1,barrido_r_n]))
print(len(modelo.gauss[v_1,barrido_r_n]))

print(len(cociente_r_r_medio[v_2,barrido_r_n]))
print(len(modelo.gauss[v_2,barrido_r_n]))

print(len(cociente_r_r_medio[v_3,barrido_r_n]))
print(len(modelo.gauss[v_3,barrido_r_n]))

print(v_0, v_1, v_2, v_3)
print(barrido_r_n)
print(cociente_r_r_medio[v_3,barrido_r_n])
print(modelo.gauss[v_3,barrido_r_n,0])

x_y = { 'x_1': cociente_r_r_medio[v_0,barrido_r_n], 'y_1': modelo.gauss[v_0,barrido_r_n,0],
        'x_2': cociente_r_r_medio[v_1,barrido_r_n], 'y_2': modelo.gauss[v_1,barrido_r_n,0],
        'x_3': cociente_r_r_medio[v_2,barrido_r_n], 'y_3': modelo.gauss[v_2,barrido_r_n,0],
        'x_4': cociente_r_r_medio[v_3,barrido_r_n], 'y_4': modelo.gauss[v_3,barrido_r_n,0]}

nombre = "figura_3"
xLabel = r'$r/r_{1/2}$'
yLabel = r'$\Delta U / \Delta U_{max} $'
numero = 4


figura_1 = Figura(nombre,x_y,xLabel,yLabel,numero)
figura_1.show_save()

# problemas: las gaussianas no deberian depender del valor de x
