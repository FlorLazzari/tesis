# coding=utf-8     

# no entiendo por qué si no pongo éste "magic comment" no funciona
# explicación en https://www.python.org/dev/peps/pep-0263/


from __future__ import division  # para evitar el problema de la división entera (must occur at the beginning of the file)


# paper : A new analytical model for wind-turbine wakes

import numpy as np # para trabajar con arrays de forma mas eficiente (tipo matlab)

# import math # para que entienda la funcion exp(), otra opción es:

from numpy import exp, abs, angle, pi

import matplotlib.pyplot as plt # para hacer los gráficos


l = raw_input("Which case do you want to work with? 1/2/3/4?")

if l == "1":
	print("case_1")
	import case_1 as c
elif l == "2":
	print("case_2")
	import case_2


d_0 = c.d_0 
z_h = c.z_h   
U_hub = c.U_hub    
C_T = c.C_T 	
z_0 = c.z_0 		
I_0 = c.I_0 		

x_n = c.x_n 			
y_n = c.y_n 
z_n = c.z_n 



m= raw_input("Do you want to see the gaussian figures? Y/N ")

if m == "Y" :  
	print("You'll see the figures")
	h = 0
else :
	print("You won't see the figures")	
	h =plt.ion()	
	


# defino variables : 

k_estrella = 0.2	#


n = (1 - C_T)**0.5

beta = 0.5 * ((1+n)/n)

epsilon = 0.25 * ((beta)**0.5)



# cambio de coordenadas:

def cart2pol(x, y):
    r = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(r, phi)

def pol2cart(r, phi):
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return(x, y)

[r, phi] = cart2pol(y_n,z_n)		



#######

def modelo(x_var,r_var):
    	sigma_n = k_estrella*x_var + epsilon
	sigma_n_cuadrado = sigma_n**2	
	r_cuadrado = r_var**2
	C = 1 - (1-(C_T/(8*sigma_n_cuadrado)))**(1/2)
	exponente = -r_cuadrado / (2 * sigma_n_cuadrado) 
	gaussiana = exp(exponente)
	deficit_dividido_U_inf = C * gaussiana	
    	return deficit_dividido_U_inf, gaussiana

# figura 3 del paper: gaussiana en funcion de r para distintos x

# quiero graficar deficit_dividido_deficit_max en fc de r_dividido_r_mitad

# deficit_dividido_deficit_max = gaussiana (esto se ve algebraicamente)
# filled contour plot

indice_1 = int(len(x_n)/8)
indice_2 = int(len(x_n)/7)
indice_3 = int(len(x_n)/6)
indice_4 = int(len(x_n)/5)
indice_5 = int(len(x_n)/4)
indice_6 = int(len(x_n)/3)
indice_7 = int(len(x_n)/2)



nada,y_0 = modelo(x_n[0],r)
nada,y_1 = modelo(x_n[indice_1],r)
nada,y_2 = modelo(x_n[indice_2],r)
nada,y_3 = modelo(x_n[indice_3],r)
nada,y_4 = modelo(x_n[indice_4],r)
nada,y_5 = modelo(x_n[indice_5],r)
nada,y_6 = modelo(x_n[indice_6],r)
nada,y_7 = modelo(x_n[indice_7],r)


h
fig = plt.figure(1)
plt.ylim([0,1])	
plt.xlabel('r')
plt.ylabel(r'$\Delta U / \Delta U_{max} $')
plt.plot(r,y_0)
plt.plot(r,y_1)
plt.plot(r,y_2)
plt.plot(r,y_3)
plt.plot(r,y_4)
plt.plot(r,y_5)
plt.plot(r,y_6)
plt.plot(r,y_7)
plt.show()
fig.savefig('figura_3_mejorada_gaussiana.png')


# faltaría ponerle leyenda para que se entienda la variación en x

# figura 5 del paper: deficit_dividido_U_inf en funcion de x para distintos r

r_0 = max(r)
r_1 = max(r) / 2
r_2 = max(r) / 3
r_3 = max(r) * 0.75



w_0,nada = modelo(x_n,r_0)		
w_1,nada = modelo(x_n,r_1)
w_2,nada = modelo(x_n,r_2)
w_3,nada = modelo(x_n,r_3)


# vemos como la relación es casi idéntica para distintos valores de r (esto está bien?)


h
fig = plt.figure(2)
#plt.ylim([0,0.5])	
#plt.xlim([0,6])
plt.xlabel(r'$ x / d_{0} $')
plt.ylabel(r'$\Delta U / U_{\infty} $')
plt.plot(x_n,w_0, 'x')
plt.plot(x_n,w_1, 'x')
plt.plot(x_n,w_2, 'x')
plt.plot(x_n,w_3, 'x')
plt.show()
fig.savefig('figura_5_mejorada_gaussiana.png')

# figura 4 del paper:

# sigma_n en fc de x_n:

sigma_n_ = k_estrella*x_n + epsilon

h
fig = plt.figure(3)	
plt.xlabel(r'$ x / d_{0} $')
plt.ylabel(r'$\sigma / d_{0} $')
plt.plot(x_n,sigma_n_, 'x')
plt.show()
fig.savefig('figura_4_mejorada_gaussiana.png')

# figura 6 del paper:

# filled contour plot

X,R = np.meshgrid(x_n,r)


deficit, nada = modelo(X,R)

fig = plt.figure()  
plt.xlabel(r'$ x / d_{0} $')
plt.ylabel('r')
plt.title('Gaussian Filled Contour Plot')      
cp = plt.contourf(X,R,deficit)
plt.colorbar(cp)
plt.show()
plt.figure()
fig.savefig('figura_6_mejorada_gaussiana.png')


# faltaría hacerlo en función de z_n






