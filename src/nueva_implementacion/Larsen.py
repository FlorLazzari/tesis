from __future__ import division
# coding=utf-8

from Modelo import Modelo
from numpy import pi

class Larsen(Modelo):

    def __init__(self):
        super(Larsen, self).__init__()
        # ambient streamwise turbulence intensity:
        self.Ia = 0.07
        self.D_eff = turbina.d_0 * ( (1 + (1 - turbina.c_T)**0.5 ) / (2 * (1 - turbina.c_T)*0.5 ) )**0.5
        self.R_nb = max(1.08 * turbina.d_0, 1.08 * turbina.d_0 + 21.7 * turbina.d_0 * (self.Ia - 0.05))
        self.R_95 = 0.5 * (self.R_nb + min(turbina.coord.z, self.R_nb))
        self.x_0 = (9.5 * turbina.d_0) / (((2 * self.R_92) / self.D_eff)**3 - 1)
        self.c_T_A = turbina.c_T * pi * (turbina.d_0/2)**2
        self.C1 = (self.D_eff / 2)**(5/2) * (105 / (2*pi))**(-1/2) * (self.c_T_A * self.x_0)**(-5/6)


    def evaluar_deficit_normalizado(self, turbina, coord_selec):

        dist = coord_selec.x-self.x_0
        radio_W = (35 / (2*pi))**(1/5) * (3 * self.C1**2)**(1/5) * (self.c_T_A * dist)**(1/3)
        r = ((turbina.coord.y - coord_selec.y)**2 + (turbina.coord.z - coord_selec.z)**2)**0.5

        U_inf = 2.2 #### ???????

        return (-U_inf / 9) * (self.c_T_A * dist**(-2))**(1/3) * (r**(3/2) * (3 * self.C1**2 * self.c_T_A * dist)**(-1/2) - (35 / (2*pi))**(3/10) * (3 * self.C1**2)**(-1/5))**2
