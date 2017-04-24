# coding=utf-8

import numpy as np

from Case import Case
from Coordenadas import Coordenadas
from Coordenadas_Norm import Coordenadas_Norm
from Figura import Figura

################################################################################

from Jensen import Jensen

# coordenadas:

x_n = np.arange(0,16,0.05)
y_n = np.arange(0,4.5,0.05)
z_n = np.arange(0,5,0.05)

d_0 = 0.15

x = d_0 * x_n
y = d_0 * y_n
z = d_0 * z_n

# inicializo caso, coordenadas, modelo:

d_0 = 0.15
z_h = 0.125
U_hub = 2.2
C_T = 0.42
z_0 = 0.00003
I_0 = 0.07

case = Case(d_0,z_h,U_hub,C_T,z_0,I_0)
coordenadas = Coordenadas(x,y,z)


jensen = Jensen(case, 0.075)
jensen.play(coordenadas,case.C_T)
