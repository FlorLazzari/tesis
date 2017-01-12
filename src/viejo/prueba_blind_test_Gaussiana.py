from blind_test_Gaussiana import x,y
from Figura_Scatter import Figura_Scatter
from Figura import Figura

x_y = {"x_1" : x, "y_1" : y}
nombre = "y/d vs deficit_dividido_U_inf x/d=1"
xLabel = r'$y/d$'
yLabel = r'$ \Delta U / U_{\infty}$'

figura_prueba = Figura(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()


figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()
