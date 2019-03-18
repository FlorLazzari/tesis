from __future__ import division
import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
# coding=utf-8

from Turbina_Rawson import Turbina_Rawson
from Coord import Coord
from U_inf import U_inf

"""
la tabla para la medicion de potencia de Rawson se hace en base a la medicion de
una torre meteorologica a la altura del hub.
Vamos a asociarle a cada u a la altura del hub un u medio sobre el disco para el
caso Rawson
"""

u_inf = U_inf()
u_inf.perfil = 'log'
N = 10000

turbina_0 = Turbina_Rawson(Coord(np.array([0,0,80]))) # chequear altura del hub
d_0 = turbina_0.d_0

# z_0 de la superficie
z_0 = 0.1

U_tabulado = np.arange(4, 26)
u_medio_arreglo = []

for u_nuevo in U_tabulado:
    u_inf.coord_hub = u_nuevo

    coord_random_arreglo = []
    for i in range(N):
        rand_y = np.random.uniform(turbina_0.coord.y-(turbina_0.d_0/2), turbina_0.coord.y+(turbina_0.d_0/2))
        rand_z = np.random.uniform(turbina_0.coord.z-(turbina_0.d_0/2), turbina_0.coord.z+(turbina_0.d_0/2))
        coord_random = Coord(np.array([turbina_0.coord.x, rand_y, rand_z]))
        coord_random_arreglo.append(coord_random)

    coord_random_adentro_disco = []
    for coord_random in coord_random_arreglo:
        if ((coord_random.y-turbina_0.coord.y)**2 + (coord_random.z-turbina_0.coord.z)**2 < (turbina_0.d_0/2)**2):
            coord_random_adentro_disco = np.append(coord_random_adentro_disco, coord_random)

    cantidad_coords_adentro_disco = len(coord_random_adentro_disco)

    u_adentro_disco = []
    for coord in coord_random_adentro_disco:
        u_inf.coord = coord
        u_inf.perfil_flujo_base(turbina_0.coord.z, z_0)
        u_adentro_disco = np.append(u_adentro_disco, u_inf.coord)
    u_medio_disco = np.mean(u_adentro_disco)

    u_medio_arreglo = np.append(u_medio_arreglo, u_medio_disco)

"""
RESULTADO OBTENIDO:
U_tabulado_nuevo = np.array([  3.97553683,   4.9669611 ,   5.95972269,   6.95196727,
         7.95116277,   8.93613964,   9.93634081,  10.92857237,
        11.9171516 ,  12.9245659 ,  13.91116425,  14.90904084,
        15.9053444 ,  16.88414983,  17.88072698,  18.87876044,
        19.87055544,  20.84568607,  21.87016143,  22.8544895 ,
        23.847984  ,  24.83090363])

si grafico se observa que la diferencia es despreciable:

plt.plot(u_medio_arreglo)
plt.plot(np.arange(4, 26))
plt.show()

"""
