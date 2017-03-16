# coding=utf-8

# potencia disponible en el campo de velocidades del fluido

import numpy as np
from Gaussiana import Gaussiana

# rho = densidad del aire
# At sea level and at 15 °C air has a density of approximately 1.225 kg/m3
rho = 1.225

# Gaussiana = es un modelo de estela
# x_0 = es el punto donde quiero calcular la potencia disponible
# U = es el viento a la salida del molino

def potenciar(d_0,x_0,U):
    # area = area sobre la cual quiero estudiar potencia disponible, en general
    # es igual al area que barre el molino
    radio = d_0 / 2
    area = 3.14 * (radio**2)
    potencia_disponible_parcial = np.zeros((radio,radio))
    potencia_disponible = 0
    # voy a hacer la integracion de forma discreta
    coeficiente = 0.5 * rho * area
    # quiero integrar en toda el area
    # deberia encontrar el indice en x(y) para el cual el vector x(y) es igual
    # al radio
    # x [x_indice_radio] = radio 
    for i in range (0,int(radio)):
        for j in range (0,int(radio)):
            potencia_disponible_parcial[i,j] = coeficiente * U[x_0,i,j]
            potencia_disponible = sum(sum(potencia_disponible_parcial))
    return potencia_disponible
