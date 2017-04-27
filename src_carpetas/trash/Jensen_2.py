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




m= raw_input("Do you want to see the Jensen figures? Y/N ")

if m == "Y" :  
	print('se muestra')
	h = 0
else :
	print('no se muestra')	
	h = plt.ion()	


# figure 5:

# Jensen:


k_wake = 0.1						# proposed by Jensen
#k_wake_on_shore = 0.075			#suggested in the literature
#k_wake_off_shore = 0.04 and 0.05	#suggested in the literature



n = (1 - C_T)**0.5
a = 1 - n

# esta es la forma en la que está presentado en el paper:
#denom = (1 + ((2*k_wake*x)/d_0))**2

# lo escribo en fc de x_n:
denom = (1 + 2*k_wake*x_n)**2


deficit_dividido_U_inf = a / denom

h
fig = plt.figure()
plt.xlabel(r'$ x / d_{0} $')
plt.ylabel(r'$\Delta U / U_{\infty} $')
plt.plot(x_n,deficit_dividido_U_inf, 'x')
plt.show()


# modelo de Jensen ya está terminado!






