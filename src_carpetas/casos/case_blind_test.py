# coding=utf-8

import numpy as np

from Case import Case
from Coordenadas import Coordenadas
from Coordenadas_Norm import Coordenadas_Norm

# test section = 12 m x 2 m x 3 m
# rotor diameter = 0.894 m
# centre of the rotor is located at z = 0.817 m
#
# model was designed to operate at 10 m/s with a TSR = 6


# coordenadas:

length = 12
width = 3
height = 2

x = np.arange(0,length,0.05)
y = np.arange(-width,width,0.05)
z = np.arange(0,height,0.05)

# inicializo caso, coordenadas, modelo:

d_0 = 0.894    # diameter of the wind turbine
z_h = 0.817

# no tengo datos de esto:
U_hub = 10     # esto seria una U_ref?? Gaussiana no lo usa asi que no me preocupa
C_T = 0
z_0 = 0.00001
I_0 = 0

case = Case(d_0,z_h,U_hub,C_T,z_0,I_0)
coordenadas = Coordenadas(x,y,z)
