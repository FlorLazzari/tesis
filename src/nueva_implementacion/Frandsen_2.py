# coding=utf-8
from __future__ import division

from Modelo_2 import Modelo
import numpy as np
from numpy import exp, abs, angle, pi
from Case_2 import Case
from Turbina import Turbina
# from cart2pol import cart2pol
# from Coordenadas import Coordenadas
# from Coordenadas_Norm import Coordenadas_Norm

#k_wake = 0.1						# proposed by Jensen
#k_wake_on_shore = 0.075			#suggested in the literature
#k_wake_off_shore = 0.04 and 0.05	#suggested in the literature


class Frandsen(Modelo):

    def __init__(self, case, turbina, k_wake):
        super(Frandsen, self).__init__(case, turbina)        # self.case = case + self.turbina = turbina
        self.k_wake = k_wake

    def evalDeficitNorm(self, coord, c_T):
        # coord deben ser no normalizadas (np.array)
		beta = 0.5 * ((1+((1 - c_T)**0.5))/((1 - c_T)**0.5))
		d_w = ((beta + 10 * self.k_wake * (coord[0]/self.turbina.d_0) )**0.5) * self.turbina.d_0
		if (abs(coord[1]) <= (d_w / 2)) & (abs(coord[2] - self.turbina.z_h) <= (d_w / 2)):
			return 0.5 * (1 - (1 - (2*c_T) / beta )**0.5)
		else:
			return 0


# # A_0 = area swept by the wind-turbine blades
# A_0 = pi * (d_0/2)**2
#
# # A_w = cross-sectional area of the wake (el +1 es porque tengo el dato de A_a además de la tira dada por d_w que mide x_n)
# A_w = np.zeros(len(x_n)+1)
#
# n = (1 - C_T)**0.5
# beta = 0.5 * ((1+n)/n)
#
# # A_a = cross-sectional area of the wake just after the initial wake expansion
# A_a = beta * A_0
#
# # expansion factor alpha is of order 10 k_wake
# alpha = 10 * k_wake		# habría que encontrar el valor exacto de alpha
#
# d_w = ((beta + alpha * x_n)**0.5) * d_0
#
# # esto fue una intuición mía, en ningún lugar lo aclara bien:
# A_w = pi * (d_w/2)**2
#
# frac = A_0 / A_w
# deficit_dividido_U_inf = 0.5 * (1 - (1 - 2*C_T*frac )**0.5)
#
