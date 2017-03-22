# coding=utf-8

# potencia disponible en el campo de velocidades del fluido

import numpy as np
from indexar import indexar

# rho = densidad del aire
# At sea level and at 15 °C air has a density of approximately 1.225 kg/m3
rho = 1.225

# x_0 = es el punto donde quiero calcular la potencia disponible
# U = es el viento a la salida del molino

def potenciar(d_0,x_n,y,z,x_n_0,U):
    # area = area sobre la cual quiero estudiar potencia disponible, en general
    # es igual al area que barre el molino
    radio = d_0 / 2
    area = 3.14 * (radio**2)
    # voy a hacer la integracion de forma discreta
    coeficiente = 0.5 * rho * area
    # quiero integrar en toda el area
    # deberia encontrar el indice en x(y) para el cual el vector x(y) es igual
    # al radio
    # x [x_indice_radio] = radio
    indice_radio_y = indexar(y,radio)
    indice_radio_z = indexar(z,radio)
    indice_x_n_0 = indexar(x_n,x_n_0)
    potencia_disponible_parcial = np.zeros((indice_radio_y,indice_radio_z))
    potencia_disponible = 0
    for i in range (0,indice_radio_y):
        for j in range (0,indice_radio_z):
            potencia_disponible_parcial[i,j] = coeficiente * U[indice_x_n_0,i,j]
            potencia_disponible = sum(sum(potencia_disponible_parcial))
    return potencia_disponible
