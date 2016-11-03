# coding=utf-8     
from __future__ import division
import numpy as np 
import matplotlib.pyplot as plt


exponente = np.zeros((len(x_n),len(r_cuadrado)))
gaussiana = np.zeros((len(x_n),len(r_cuadrado)))
deficit_dividido_U_inf = np.zeros((len(x_n),len(r_cuadrado)))



def modelo_gaussiana(x_n,r,C_T)
	k_estrella = 0.2	
	n = (1 - C_T)**0.5
	beta = 0.5 * ((1+n)/n)
	epsilon = 0.25 * ((beta)**0.5)

	sigma_n = k_estrella*x_n + epsilon
	sigma_n_cuadrado = (sigma_n)**2
	r_cuadrado = r**2
	C = 1 - (1-(C_T/(8*sigma_n_cuadrado)))**(1/2)

	for i in range (0,len(x_n)):
		for j in range (0,len(r_cuadrado)):
			exponente[i,j] = -r_cuadrado[j] / (2 * sigma_n_cuadrado[i]) 
			g[i,j] = exp(exponente[i,j])
			d[i,j] = C[i] * gauss[i,j]
	return g, d	


def gaussiana(x_n,r,C_T)
	g,d = modelo_gaussiana(x_n,r,C_T)
	return g

def deficit_dividido_U_inf(x_n,r,C_T)
	g,d = modelo_gaussiana(x_n,r,C_T)
	return d

