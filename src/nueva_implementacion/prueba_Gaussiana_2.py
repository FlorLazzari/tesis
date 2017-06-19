from __future__ import division

import numpy as np

# me gustaria hacer algo asi para ordenar la implementacion en carpetas:
# import sys
# sys.path.append(/home/florencia/Documentos/tesis_gitHub/tesis/src/nueva_implementacion/casos)
# from Case_2 import Case

from Case_2 import Case
from Gaussiana_2 import Gaussiana
from Figura import Figura
from Turbina import Turbina

################################################################################

d_0 = 0.15
x_h = 0
y_h = 0
z_h = 0.125
U_inf = 2.2

y = np.arange(0, 4*d_0, 0.01)
deficit_dividido_U_inf = np.zeros(len(y))

k_estrella = 0.2
epsilon = 0.268855463528
case = Case(U_inf)
turbina = Turbina(d_0, x_h, y_h, z_h)
gaussiana = Gaussiana(case,turbina,k_estrella,epsilon)
c_T = 0.5

# barrido en y:
for i in range(0, len(y)):
    coord = np.array([(2*d_0), y[i], z_h])
    deficit_dividido_U_inf[i] = gaussiana.evalDeficitNorm(coord,c_T)

x_y = {'x_1': y, 'y_1': deficit_dividido_U_inf}

nombre = "deficit en y"
xLabel = r'$y$'
yLabel = r'$deficit$'


figura_prueba = Figura(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()
