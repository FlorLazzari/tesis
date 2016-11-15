# coding=utf-8

# from Modelo import Modelo
import numpy as np
from numpy import exp

# super() lets you avoid referring to the base class explicitly, which can be nice.
# But the main advantage comes with multiple inheritance, where all sorts of fun
# stuff can happen.


# tengo de estos por todos lados: IndentationError: unexpected indent
# tiene que ver con usar la barra espaciadora y y el tab en el mismo script??


class Gaussiana(object):

    def __init__(self,coordenadas,c_T,case,k_estrella,epsilon):
        super(Gaussiana, self).__init__()
        # aca no sirve de nada porque le puse (object)
        self.coordenadas = coordenadas
        self.c_T = c_T
        self.case = case
        self.k_estrella = k_estrella
        self.epsilon = epsilon
        # aca las coordenadas nuevas estan pisando las "coordenadas de Metodo"
        # no entiendo si me sirve para algo la inheritance en este caso
        self.exponente = None
        self.gauss = None
        self.deficit_dividido_U_inf = None
        self.r = np.arange(1)
        self.x_n = np.arange(1)

    def play(self):
        self.coordenadas.normalizar(self.case)
        self.x_n = self.coordenadas.x_n
        y_n = self.coordenadas.y_n
        z_n = self.coordenadas.z_n
        self.coordenadas.cart2pol()
        self.r = self.coordenadas.r
        phi = self.coordenadas.phi
        sigma_n = self.k_estrella * self.x_n + self.epsilon
        sigma_n_cuadrado = (sigma_n)**2
        r_cuadrado = self.r**2
        c = 1 - (1-(self.c_T/(8*sigma_n_cuadrado)))**(1/2)
        self.exponente = np.zeros((len(self.x_n),len(self.r)))
        self.gauss = np.zeros((len(self.x_n),len(self.r)))
        self.deficit_dividido_U_inf = np.zeros((len(self.x_n),len(self.r)))
        for i in range (0,len(self.x_n)):
            for j in range (0,len(self.r)):
                self.exponente[i,j] = -r_cuadrado[j] / (2 * sigma_n_cuadrado[i])
                self.gauss[i,j] = exp(self.exponente[i,j])
                self.deficit_dividido_U_inf[i,j] = c[i] * self.gauss[i,j]



# hay que chequear bien cuales de todos estos son los que necesitan el self.
# (osea, los que hará falta usar en el futuro para hacer Figuras)
