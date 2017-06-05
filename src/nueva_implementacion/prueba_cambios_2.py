import numpy as np

# me gustaria hacer algo asi para ordenar la implementacion en carpetas:
# import sys
# sys.path.append(/home/florencia/Documentos/tesis_gitHub/tesis/src/nueva_implementacion/casos)
# from Case_2 import Case

from Case_2 import Case
from Gaussiana_2 import Gaussiana
from Figura import Figura

################################################################################

d_0 = 0.15
z_h = 0.125
U_hub = 2.2

y = np.arange(0, 2*d_0, 0.01)
deficit_dividido_U_inf = np.zeros(len(y))

k_estrella = 0.2
epsilon = 0.268855463528
case = Case(d_0,z_h,U_hub)
gaussiana = Gaussiana(case,k_estrella,epsilon)
c_T = 0.5
coord = np.array([0, 0, 0])

a = 2*d_0

coord = np.array([0.3, 0.5, 0.125])
deficit_dividido_U_inf = gaussiana.evalDeficitNorm(coord,c_T)
print "coord =",coord
print "np.array =",np.array([0.3, 0.5, 0.125])
print "deficit_dividido_U_inf[i] =",deficit_dividido_U_inf




# barrido en y:
# for i in y:
#     coord = np.array([0.3, 0.5, 0.125])
#     deficit_dividido_U_inf[i] = gaussiana.evalDeficitNorm(coord,c_T)
#     print "coord =",coord
#     print "deficit_dividido_U_inf[i] =",deficit_dividido_U_inf[i]

x_y = {'x_1': y, 'y_1': deficit_dividido_U_inf}

nombre = "deficit en y"
xLabel = r'$y$'
yLabel = r'$deficit$'


figura_prueba = Figura(nombre,x_y,xLabel,yLabel,1)
# figura_prueba.show()
