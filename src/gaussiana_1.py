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
	import case_2 as c
elif l == "3":
	print("case_3")
	import case_3 as c
elif l == "4":
	print("case_4")
	import case_4 as c



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



# cómo varía sigma/d_0 (sigma normalizado) con x :

sigma_n = k_estrella*x_n + epsilon


# gaussiana:

sigma_n_cuadrado = (sigma_n)**2

r_cuadrado = r**2

C = 1 - (1-(C_T/(8*sigma_n_cuadrado)))**(1/2)


# introduzco las variables porque sino me dice "sarasa is not defined" (por que??)
exponente = np.zeros((len(x_n),len(r_cuadrado)))
gaussiana = np.zeros((len(x_n),len(r_cuadrado)))
deficit_dividido_U_inf = np.zeros((len(x_n),len(r_cuadrado)))



for i in range (0,len(x_n)):
	for j in range (0,len(r_cuadrado)):
		exponente[i,j] = -r_cuadrado[j] / (2 * sigma_n_cuadrado[i]) 
		gaussiana[i,j] = exp(exponente[i,j])
		deficit_dividido_U_inf[i,j] = C[i] * gaussiana[i,j]

# para chequear:
exponente.shape


# la matriz quedó armada de la siguiente forma:
# (sigma_n_cuadrado , r_cuadrado)

# para obtener la gaussiana para un dado sigma_n_cuadrado (o lo que es lo mismo para una dada x):

#fin = np.arange(0,len(r_cuadrado))

#x = completar con un dado x!

#deficit_dividido_U_inf[x,fin]




# quiero graficar deficit_dividido_deficit_max en fc de r_dividido_r_mitad

# deficit_dividido_deficit_max = gaussiana (esto se ve algebraicamente)

# entonces en principio voy a graficar la gaussiana en funcion de r

fin = np.arange(0,len(r_cuadrado))

y = np.zeros((len(x_n),len(r_cuadrado)))



# figura 3 del paper:

for i in range(0,len(x_n)):
	y[i] = gaussiana[x_n[i],fin]
	
#	plt.ylim([0,1])	
#	plt.xlabel('r')
#	plt.ylabel(r'$\Delta U / \Delta U_{max} $')
#	plt.plot(r,y[i],'x')
	#print("hola %d") % (i) # esto funciona 
#	plt.show()

#plt.savefig("testplot %d .png") % (i) # esto no funciona


# para ver todos los graficos en una misma figure:

h
fig = plt.figure(1)
plt.ylim([0,1])	
plt.xlim([0,1])	
plt.xlabel('r')
plt.ylabel(r'$\Delta U / \Delta U_{max} $')
plt.plot(r,y[0])
plt.plot(r,y[1])
plt.plot(r,y[2])
plt.plot(r,y[3])
plt.plot(r,y[4])
plt.plot(r,y[5])
plt.plot(r,y[6])
plt.plot(r,y[7])
plt.plot(r,y[8])
plt.plot(r,y[9])
plt.show()
fig.savefig('figura_3_gaussiana.png')

# faltaría ponerle leyenda para que se entienda la variación en x

# figura (no está en el paper): deficit_dividido_U_inf en funcion de x para distintos r



fin_2 = np.arange(0,len(x_n))

y_2 = np.zeros((4,len(x_n)))



r_0 = max(r)
r_1 = max(r) / 2
r_2 = max(r) / 3
r_3 = max(r) * 0.75


y_2[0] = deficit_dividido_U_inf[fin_2,r_0]		
y_2[1] = deficit_dividido_U_inf[fin_2,r_1]
y_2[2] = deficit_dividido_U_inf[fin_2,r_2]
y_2[3] = deficit_dividido_U_inf[fin_2,r_3]

# vemos como la relación es casi idéntica para distintos valores de r (esto está bien?)

h
fig = plt.figure(2)
plt.ylim([0,0.5])	
plt.xlim([0,6])
plt.xlabel(r'$ x / d_{0} $')
plt.ylabel(r'$\Delta U / U_{\infty} $')
plt.plot(x_n,y_2[0], 'x')
plt.plot(x_n,y_2[1], 'x')
plt.plot(x_n,y_2[2], 'x')
plt.plot(x_n,y_2[3], 'x')
plt.show()
fig.savefig('figura_5_gaussiana.png')

# quiero calcular los valores r_mitad, se definen como aquellos para los cuales: 

# deficit(r = r_mitad) / U_inf = 0.5 * deficit_dividido_U_inf = 0.5 * C

# busco los valores de r tales que deficit_dividido_U_inf sea igual a 0.5 * C



#esto no funciona pero creo que no vale la pena:


#indices_r_mitad = np.zeros(len(x_n))

#fin = np.arange(0,len(r_cuadrado))

#for i in range (0,len(x_n)):
#	valor_buscado[i] = 0.5 * C[i]
#	indices_r_mitad[i] = np.where(deficit_dividido_U_inf[i,fin] == valor_buscado[i])


# esto no funciona y además no se si es la forma más inteligente de pensarlo:

#valor_buscado_cota_max = valor_buscado*1.05
#valor_buscado_cota_min = valor_buscado*0.95



#indices_r_mitad_rango = np.where(deficit_dividido_U_inf > valor_buscado_cota_min) & (deficit_dividido_U_inf < valor_buscado_cota_max)

# un intento de ayuda en: http://stackoverflow.com/questions/16343752/numpy-where-function-multiple-conditions


# esos son los índices, ahora solo queda ver qué valor de r corresponde a cada índice

# r_mitad = r[indices_r_mitad]
 








#figura 4 del paper:

# sigma_n en fc de x_n:

len(sigma_n)
len(x_n)

h
fig = plt.figure(3)
#plt.ylim([0,1])	
plt.xlabel(r'$ x / d_{0} $')
plt.ylabel(r'$\sigma / d_{0} $')
plt.plot(x_n,sigma_n, 'x')
plt.show()
fig.savefig('figura_4_gaussiana.png')


# voy a hacer gaussiana en forma de función

# esto está mal, ya que en la línea 
# exponente = -r_cuadrado / (2 * sigma_n_cuadrado) 

# r_cuadrado tiene dimensión distinta que sigma_n_cuadrado, asi que no se bien qué está haciendo pero está mal


#def myfunction(x_var,r_var):
#    	sigma_n = k_estrella*x_var + epsilon
#	sigma_n_cuadrado = sigma_n**2
#	r_cuadrado = r_var**2
#	C = 1 - (1-(C_T/(8*sigma_n_cuadrado)))**(1/2)
#	exponente = -r_cuadrado / (2 * sigma_n_cuadrado) 
#	gaussiana = exp(exponente)
#	deficit_dividido_U_inf = C * gaussiana	
#    	return deficit_dividido_U_inf

#X,R = np.meshgrid(x_n,r)

#deficit = myfunction(X,R)



# filled contour plot

X,R = np.meshgrid(x_n,r)

a = deficit_dividido_U_inf.transpose()

fig = plt.figure()  
plt.xlabel(r'$ x / d_{0} $')
plt.ylabel('r')
plt.title('Gaussian Filled Contour Plot')      
cp = plt.contourf(x_n,r,a)
plt.colorbar(cp)
plt.show()
plt.figure()
fig.savefig('figura_6_gaussiana.png')


# faltaría hacerlo en función de z_n. ¿Cómo?

# pero esto no es exactamente lo que aparece en la figura 6, esto es el deficit, yo quiero tener el viento. Veamos cómo se define el deficit y en fc. de eso otenemos el viento












