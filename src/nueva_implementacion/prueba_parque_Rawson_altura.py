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
A continuacion se corre el modelo Gaussiana para el parque Rawson.
Se grafican:
    1) La potencia en funcion de la ubicacion (numero de turbina de label)
    2) El campo de viento en el plano (X,Y) para todo el parque
"""

gaussiana = Gaussiana()
u_inf = U_inf()
u_inf.coord_mast = 8.1
u_inf.perfil = 'log'
N = 100

z_ground = 154

turbina_0 = Turbina_Rawson(Coord(np.array([0,0,260 - z_ground])))
D = turbina_0.d_0

turbina_1 = Turbina_Rawson(Coord(np.array([-204.9,286.1,269 - z_ground])))
turbina_2 = Turbina_Rawson(Coord(np.array([41.9,565.7,256 - z_ground])))
turbina_3 = Turbina_Rawson(Coord(np.array([8.1,870,247 - z_ground])))
turbina_4 = Turbina_Rawson(Coord(np.array([27.2,1195.9,241 - z_ground])))
turbina_5 = Turbina_Rawson(Coord(np.array([-7,1527,236 - z_ground])))
turbina_6 = Turbina_Rawson(Coord(np.array([190.3,1894.2,234 - z_ground])))
turbina_7 = Turbina_Rawson(Coord(np.array([-78.8,2222.6,234 - z_ground])))
turbina_8 = Turbina_Rawson(Coord(np.array([414.8,2380.9,233 - z_ground])))
turbina_9 = Turbina_Rawson(Coord(np.array([602.4,86.7,253 - z_ground])))
turbina_10 = Turbina_Rawson(Coord(np.array([795.1,386.7,253 - z_ground])))
turbina_11 = Turbina_Rawson(Coord(np.array([965.4,676.2,246 - z_ground])))
turbina_12 = Turbina_Rawson(Coord(np.array([1043.8,988.5,239 - z_ground])))
turbina_13 = Turbina_Rawson(Coord(np.array([1202.3,1269,235 - z_ground])))
turbina_14 = Turbina_Rawson(Coord(np.array([1313.8,1580.7,235 - z_ground])))
turbina_15 = Turbina_Rawson(Coord(np.array([1362.8,1919.5,230 - z_ground])))
turbina_16 = Turbina_Rawson(Coord(np.array([1424.8,2225.1,223 - z_ground])))
turbina_17 = Turbina_Rawson(Coord(np.array([711.8,-766.6,255 - z_ground])))
turbina_18 = Turbina_Rawson(Coord(np.array([1107.7,-503.6,250 - z_ground])))
turbina_19 = Turbina_Rawson(Coord(np.array([1350.9,-206.8,246 - z_ground])))
turbina_20 = Turbina_Rawson(Coord(np.array([1705.8,50.9,239 - z_ground])))
turbina_21 = Turbina_Rawson(Coord(np.array([1949.7,315.4,241 - z_ground])))
turbina_22 = Turbina_Rawson(Coord(np.array([2045.2,603.6,237 - z_ground])))
turbina_23 = Turbina_Rawson(Coord(np.array([2256.4,890.3,234 - z_ground])))
turbina_24 = Turbina_Rawson(Coord(np.array([2331.4,1210.7,229 - z_ground])))
turbina_25 = Turbina_Rawson(Coord(np.array([2451,1517.1,226 - z_ground])))
turbina_26 = Turbina_Rawson(Coord(np.array([2548.5,1800.4,224 - z_ground])))
turbina_27 = Turbina_Rawson(Coord(np.array([2682.7,2068.3,223 - z_ground])))
turbina_28 = Turbina_Rawson(Coord(np.array([2816.2,2348.8,220 - z_ground])))
turbina_29 = Turbina_Rawson(Coord(np.array([1946.5,-1595.2,274 - z_ground])))
turbina_30 = Turbina_Rawson(Coord(np.array([2201.9,-1358.8,269 - z_ground])))
turbina_31 = Turbina_Rawson(Coord(np.array([2357.1,-1060.7,262 - z_ground])))
turbina_32 = Turbina_Rawson(Coord(np.array([2500.9,-787.6,257 - z_ground])))
turbina_33 = Turbina_Rawson(Coord(np.array([2650.9,-516.6,251 - z_ground])))
turbina_34 = Turbina_Rawson(Coord(np.array([2802.7,-212.6,245 - z_ground])))
turbina_35 = Turbina_Rawson(Coord(np.array([2909.2,102.8,241 - z_ground])))
turbina_36 = Turbina_Rawson(Coord(np.array([2982.2,372.5,237 - z_ground])))
turbina_37 = Turbina_Rawson(Coord(np.array([3173.6,690.7,230 - z_ground])))
turbina_38 = Turbina_Rawson(Coord(np.array([3283.3,997.4,224 - z_ground])))
turbina_39 = Turbina_Rawson(Coord(np.array([3432.1,1310.3,220 - z_ground])))
turbina_40 = Turbina_Rawson(Coord(np.array([3562.9,1629.4,219 - z_ground])))
turbina_41 = Turbina_Rawson(Coord(np.array([3785.2,1931.9,214 - z_ground])))
turbina_42 = Turbina_Rawson(Coord(np.array([3947.6,2337.7,214 - z_ground])))

turbinas_list = [turbina_0, turbina_1, turbina_2, turbina_3, turbina_4, turbina_5,
turbina_6, turbina_7, turbina_8, turbina_9, turbina_10, turbina_11,
turbina_12, turbina_13, turbina_14, turbina_15, turbina_16, turbina_17,
turbina_18, turbina_19, turbina_20, turbina_21, turbina_22, turbina_23,
turbina_24, turbina_25, turbina_26, turbina_27, turbina_28, turbina_29,
turbina_30, turbina_31, turbina_32, turbina_33, turbina_34, turbina_35,
turbina_36, turbina_37, turbina_38, turbina_39, turbina_40, turbina_41,
turbina_42]

z_mast = turbina_7.coord.z
# z_0 de la superficie
z_0 = 0.01
parque_de_turbinas = Parque_de_turbinas(turbinas_list, z_0, z_mast)

################################################################################

# grafico potencia en funcion de la ubicacion (numero de turbina de label)

x_o = 4200
y_o = 3000
z_o = 250

coord = Coord(np.array([x_o, y_o, z_o]))

potencia_de_cada_turbina = []

data_prueba = calcular_u_en_coord(gaussiana, 'rss', coord, parque_de_turbinas, u_inf, N)

for turbina in turbinas_list:
    potencia_de_cada_turbina.append(float(turbina.potencia))
    # import pdb; pdb.set_trace()

plt.figure()
plt.plot(np.arange(0, 43), potencia_de_cada_turbina, '-x')
plt.xticks(np.arange(0, 43, 5))
plt.ylim([0, 1200])
plt.grid()
plt.show()

# no me gusta que esten numeradas de 0 a 42, en el mapita estan de 1 a 43...
# pero gonza uso esa numeracion en el grafico
# habria que cambiar el grafico de gonza y el mio con: np.arange(1, 44)

X = []
Y = []

for turbina in turbinas_list:
    X.append(turbina.coord.x)
    Y.append(turbina.coord.y)

plt.figure()
cm = plt.cm.get_cmap('coolwarm')
sc = plt.scatter(X, Y, c=potencia_de_cada_turbina, s=120,marker='v', cmap=cm)
plt.clim(min(potencia_de_cada_turbina),max(potencia_de_cada_turbina))
plt.colorbar(sc)
plt.grid()
plt.show()

# diferencias con respecto al grafico de gonza:
# hay una turbina (la 30 en el mapa, que numera desde 1)
# que genera mucha mas potencia con lo cual "los colores quedan muy distintos"
# pero me parece que la potencia relativa no me esta dando tan mal.
# habria que sacar esa turbina 30 del grafico de gonza para ver si "los colores
# me quedan mas parecidos"










# grafico (X,Y)

# recordar que el range funciona de la siguiente forma [)
# x = np.arange(-300, 4000, 22)
# y = np.arange(-1500, 2500, 22)
# z_o = turbina_0.coord.z
#
# X, Y = np.meshgrid(x, y)
#
# data_prueba = np.zeros([len(y), len(x)])
#
# for i in range(len(x)):
#     for j in range(len(y)):
#         coord = Coord(np.array([x[i], y[j], z_o]))
#         if coord.z != 0:
#             # print "entre en loop"
#             data_prueba[j,i] = calcular_u_en_coord(gaussiana, 'linear', coord, parque_de_turbinas, u_inf, N)
#             # print ('data_prueba[i,j]', i, j, data_prueba[i,j])

# plt.contour(X,Y,data_prueba, linewidths=0.5, colors='k')
# plt.contourf(X,Y,data_prueba, cmap=plt.cm.jet)
# plt.colorbar()
# plt.show()
#
# # faltaria calcular potencia
# print "potencia = ",turbina_0.potencia
# print "potencia = ",turbina_1.potencia
# print "potencia = ",turbina_2.potencia
