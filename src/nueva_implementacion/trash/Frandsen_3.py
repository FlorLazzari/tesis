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



m= raw_input("Do you want to see the Frandsen figures? Y/N ")

if m == "Y" :  
	print('se muestra')
	h = 0
else :
	print('no se muestra')	
	h = plt.ion()	




# figure 5:

k_wake = 0.1						# proposed by Jensen
#k_wake_on_shore = 0.075			#suggested in the literature
#k_wake_off_shore = 0.04 and 0.05	#suggested in the literature




# Frandsen:

# este modelo en lugar de ser en fc de x es en fc de A que es en fc de x

C_T = 0.42			

# A_0 = area swept by the wind-turbine blades
A_0 = pi * (d_0/2)**2


# A_w = cross-sectional area of the wake (el +1 es porque tengo el dato de A_a además de ela tira dada por d_w que mide x_n)

A_w = np.zeros(len(x_n)+1)


n = (1 - C_T)**0.5

beta = 0.5 * ((1+n)/n)

# A_a = cross-sectional area of the wake just after the initial wake expansion

# according to the actuator disk concept:  

A_a = beta * A_0




# expansion factor alpha is of order 10 k_wake


alpha = 10 * k_wake		# habría que encontrar el valor exacto de 					alpha, esto es un aproximado


d_w = ((beta + alpha * x_n)**0.5) * d_0



# A_w(x=0) = A_a :  

# A_w_0 = np.arange(1)

# A_w_0 = A_a

# no hace falta plantear esto porque es una condición que por el álgebra de como se define A_w se satisface siempre


# esto fue una intuición mía, en ningún lugar lo aclara bien:

A_w = pi * (d_w/2)**2

frac = A_0 / A_w

deficit_dividido_U_inf = 0.5 * (1 - (1 - 2*C_T*frac )**0.5)

h
plt.xlabel(r'$ x / d_{0} $')
plt.ylabel(r'$\Delta U / U_{\infty} $')
plt.plot(x_n,deficit_dividido_U_inf, 'x')
plt.show()



