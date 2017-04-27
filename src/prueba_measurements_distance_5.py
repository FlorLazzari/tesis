from Figura_Scatter import Figura_Scatter
from measurements_distance_5 import y,deficit_dividido_U_inf_y,sigma_y,z,deficit_dividido_U_inf_z,sigma_z

## (1-U/Uref) vs y/d

x_y = {"x_1" : y, "y_1" : deficit_dividido_U_inf_y}
nombre = "y/d vs deficit_dividido_U_inf x/d=5"
xLabel = r'$y/d$'
yLabel = r'$ \Delta U / U_{\infty}$'


figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()

# a simple vista pareciera que la imagen es el espejo que la del paper (6.a):
# chequear.. (tiene algo que ver con ese (-) que aparece arriba de cada columna?)

## (1-U/Uref) vs z/d

x_y = {"x_1" : z, "y_1" : deficit_dividido_U_inf_z}
nombre = "z/d vs deficit_dividido_U_inf x/d=5"
xLabel = r'$z/d$'



figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()

# no puedo compararla porque no esta graficada en el paper,
# faltaria ver si la forma de la figura tiene sentido
