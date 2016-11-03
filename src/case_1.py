# coding=utf-8

from __future__ import division  # para evitar el problema de la división entera (must occur at the beginning of the file)

import numpy as np # para trabajar con arrays de forma mas eficiente (tipo matlab)

# CASE 1

d_0 = 0.15			# diametro de blades?
z_h = 0.125			# hub height
U_hub = 2.2			#  (COMO LO INCLUYO EN LA ECUACION??)
C_T = 0.42			#
z_0 = 0.00003		# aerodynamic surface roughness (COMO LO INCLUYO EN LA ECUACION??)
I_0 = 0.070			# (para z = z_h) ambient streamwise turbulence intensity  (COMO LO INCLUYO EN LA ECUACION??)
#
#

# coordenadas:

# x = np.arange()
# y = np.arange()
# z = np.arange()

# normalized coordinates

# x_n = x/d_0
# y_n = y/d_0
# z_n = (z-z_h)/d_0

# escribo a dedo:


x_n = np.arange(0,15,0.01)
y_n = np.arange(0,4.5,0.005)
z_n = np.arange(0,4.5,0.005)
