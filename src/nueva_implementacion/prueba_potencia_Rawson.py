from __future__ import division
import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
# coding=utf-8

from Gaussiana import Gaussiana   # Gaussiana pertenece a la clase Modelo
from Parque_de_turbinas import Parque_de_turbinas
from Turbina_Rawson import Turbina_Rawson
from Coord import Coord
from Estela import Estela
from U_inf import U_inf
from calcular_u_en_coord import calcular_u_en_coord

"""
Para verificar los valores de potencia obtenidos (para el Parque Rawson?? o para
que ejemplo?? Blind Test tiene potencia?? porque el capitulo del parque rawson
viene despues del de potencia) comparamos los resultados de los modelos reducidos
con: las mediciones in situ y las corridas de OpenFOAM.

Blind Test: tiene curva de c_P pero me parece que no tiene sentido calcular la potencia.
Parque Rawson: gonza tiene mediciones y resultados de OpenFOAM para 2 turbinas alineadas
de potencia en funcion del angulo con el que incide el viento.

Entonces los casos que estudiaremos seran:
. una turbina de Rawson (como para validar los resultados de potencia)
. dos turbinas de Rawson alineadas separadas por 5 diametros
    * calcular la relacion entre la potencia de la turbina_1/turbina_0 para
    distintas direcciones de viento, para esto hay que crear la matriz de rotacion
. 5 turbinas alineadas de Barcelona? (gonza tiene datos medidos pero no tiene corrida de openFOAM)

"""

gaussiana = Gaussiana()
u_inf = U_inf()
u_inf.coord_hub = 8
u_inf.perfil = 'log'
N = 600

turbina_0 = Turbina_Rawson(Coord(np.array([0,0,80]))) # chequear altura del hub
D = turbina_0.d_0
turbina_1 = Turbina_Rawson(Coord(np.array([4.7*D,0,80]))) # chequear altura del hub

# z_0 de la superficie
z_0 = 0.1

# 1)
################################################################################
# primero verifico que el resultado de potencia de razonable
# Una turbina de Rawson

parque_de_turbinas_0 = Parque_de_turbinas([turbina_0], z_0)

x_o = 8*D
y_o = 0
z_o = 80

coord = Coord(np.array([x_o, y_o, z_o]))
data_prueba_0 = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas_0, u_inf, N)

print "potencia_0 SOLA = ",turbina_0.potencia

# 2)
################################################################################
# comparo OpenFOAM con modelo reducido
# Dos turbinas de Rawson alineadas separadas por 4.7 diametros
#    * calcular la relacion entre la potencia de la turbina_1/turbina_0 para
#    distintas direcciones de viento, para esto hay que crear la matriz de rotacion


parque_de_turbinas_1 = Parque_de_turbinas([turbina_0, turbina_1], z_0)

data_prueba_1 = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas_1, u_inf, N)

print "potencia_0 DOS ALINEADAS = ",turbina_0.potencia
print "potencia_1 DOS ALINEADAS = ",turbina_1.potencia

ratio = turbina_1.potencia/turbina_0.potencia

angulos = np.arange(-30, +30+5, 5)

for theta in angulos:
    turbina_0
    turbina_1

    parque_de_turbinas = Parque_de_turbinas([turbina_0, turbina_1], z_0)
    data_prueba = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas_1, u_inf, N)
