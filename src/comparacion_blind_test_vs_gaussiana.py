# comparar graficos de las mediciones del blind test con el modelo Gaussiana

# los archivos que voy a comparar son:
# - measurements_distance_1.py
# - blind_test_Gaussiana_distancia_1.py

################################################################################

from Figura_Scatter import Figura_Scatter
from measurements_distance_1 import y,deficit_dividido_U_inf_y,sigma_y,z,deficit_dividido_U_inf_z,sigma_z
from blind_test_Gaussiana_distancia_1 import y_Gaussiana, deficit_dividido_U_inf_Gaussiana


x_y = {"x_1" : y, "y_1" : deficit_dividido_U_inf_y,
       "x_2" : y_Gaussiana, "y_2" : deficit_dividido_U_inf_Gaussiana}
nombre = "y/d vs deficit_dividido_U_inf x/d=1"
xLabel = r'$y/d$'
yLabel = r'$ \Delta U / U_{\infty}$'


figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,2)
figura_prueba.xLim = [-2,2]
figura_prueba.show()

from measurements_distance_3 import y,deficit_dividido_U_inf_y,sigma_y,z,deficit_dividido_U_inf_z,sigma_z
from blind_test_Gaussiana_distancia_3 import y_Gaussiana, deficit_dividido_U_inf_Gaussiana

x_y = {"x_1" : y, "y_1" : deficit_dividido_U_inf_y,
       "x_2" : y_Gaussiana, "y_2" : deficit_dividido_U_inf_Gaussiana}
nombre = "y/d vs deficit_dividido_U_inf x/d=3"
xLabel = r'$y/d$'
yLabel = r'$ \Delta U / U_{\infty}$'


figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,2)
figura_prueba.xLim = [-2,2]
figura_prueba.show()

from measurements_distance_5 import y,deficit_dividido_U_inf_y,sigma_y,z,deficit_dividido_U_inf_z,sigma_z
from blind_test_Gaussiana_distancia_5 import y_Gaussiana, deficit_dividido_U_inf_Gaussiana

x_y = {"x_1" : y, "y_1" : deficit_dividido_U_inf_y,
       "x_2" : y_Gaussiana, "y_2" : deficit_dividido_U_inf_Gaussiana}
nombre = "y/d vs deficit_dividido_U_inf x/d=5"
xLabel = r'$y/d$'
yLabel = r'$ \Delta U / U_{\infty}$'


figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,2)
figura_prueba.xLim = [-2,2]
figura_prueba.show()


# el problema que tengo al comparar los graficos es que la gaussiana del modelo se
# achica mucho con la distancia, voy a ver que parametro tengo que tocar para cambiar
# eso
