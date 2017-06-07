from __future__ import division

import numpy as np

# me gustaria hacer algo asi para ordenar la implementacion en carpetas:
# import sys
# sys.path.append(/home/florencia/Documentos/tesis_gitHub/tesis/src/nueva_implementacion/casos)
# from Case_2 import Case

from Case_2 import Case
from Jensen_2 import Jensen
from Figura import Figura

################################################################################

d_0 = 0.15
z_h = 0.125
U_hub = 2.2

y = np.arange(0, 4*d_0, 0.01)
deficit_dividido_U_inf = np.zeros(len(y))

k_wake = 0.075
case = Case(d_0,z_h,U_hub)
jensen = Jensen(case,k_wake)
c_T = 0.5

# barrido en y:
for i in range(0, len(y)):
    coord = np.array([(2*d_0), y[i], z_h])
    deficit_dividido_U_inf[i] = jensen.evalDeficitNorm(coord,c_T)

x_y = {'x_1': y, 'y_1': deficit_dividido_U_inf}

nombre = "deficit en y"
xLabel = r'$y$'
yLabel = r'$deficit$'


figura_prueba = Figura(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()
