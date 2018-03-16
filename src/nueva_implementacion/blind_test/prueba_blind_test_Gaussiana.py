from blind_test_Gaussiana_distancia_1 import y_Gaussiana, deficit_dividido_U_inf_Gaussiana
from Figura_Scatter import Figura_Scatter
from Figura import Figura

x_y = {"x_1" : y_Gaussiana, "y_1" : deficit_dividido_U_inf_Gaussiana}
nombre = "y/d vs deficit_dividido_U_inf x/d=1"
xLabel = r'$y/d$'
yLabel = r'$ \Delta U / U_{\infty}$'

figura_prueba = Figura(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()


figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()


from blind_test_Gaussiana_distancia_3 import y_Gaussiana, deficit_dividido_U_inf_Gaussiana

x_y = {"x_1" : y_Gaussiana, "y_1" : deficit_dividido_U_inf_Gaussiana}
nombre = "y/d vs deficit_dividido_U_inf x/d=3"
xLabel = r'$y/d$'
yLabel = r'$ \Delta U / U_{\infty}$'

figura_prueba = Figura(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()


figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()


from blind_test_Gaussiana_distancia_5 import y_Gaussiana, deficit_dividido_U_inf_Gaussiana

x_y = {"x_1" : y_Gaussiana, "y_1" : deficit_dividido_U_inf_Gaussiana}
nombre = "y/d vs deficit_dividido_U_inf x/d=5"
xLabel = r'$y/d$'
yLabel = r'$ \Delta U / U_{\infty}$'

figura_prueba = Figura(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()


figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()



# ahora me gustaria hacer un fit gaussiano de esto para poder obtener la sigma:
