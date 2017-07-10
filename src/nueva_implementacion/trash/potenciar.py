# coding=utf-8

# potencia disponible en el campo de velocidades del fluido

import numpy as np
from indexar import indexar

# rho = densidad del aire
# At sea level and at 15 °C air has a density of approximately 1.225 kg/m3
rho = 1.225

# x_0 = es el punto donde quiero calcular la potencia disponible
# U = es el viento a la salida del molino

def potenciar(d_0,x,y,z,U):
    # area = area sobre la cual quiero estudiar potencia disponible, area que barre el molino
    area = 3.14 * ((d_0/2)**2)
    coeficiente = 0.5 * rho * area
    for i in range (0,indice_radio_y):
        for j in range (0,indice_radio_z):
            potencia_disponible_parcial[i,j] = coeficiente * (U[indice_x_n_0,i,j])**3
            potencia_disponible = sum(sum(potencia_disponible_parcial))
    return potencia_disponible
