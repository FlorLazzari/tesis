from Figura_Scatter import Figura_Scatter
from Figura import Figura
from measurements_distance_1 import sigma_y,sigma_z
import numpy as np
from blind_test_Gaussiana import case

# replico la figura de prueba_paper_4.py

sigma_y_vector = np.zeros(3)
sigma_z_vector = np.zeros(3)

sigma_y_vector[0] = sigma_y
sigma_z_vector[0] = sigma_z

from measurements_distance_3 import sigma_y,sigma_z

sigma_y_vector[1] = sigma_y
sigma_z_vector[1] = sigma_z

from measurements_distance_5 import sigma_y,sigma_z

sigma_y_vector[2] = sigma_y
sigma_z_vector[2] = sigma_z

################################################################################
# problema!! habria que ver el tema del error de medicion


################################################################################
# hago un figura para "y" y otra para "z":
# figura "y":

x_d = [1,3,5]
sigma_y_vector_n = sigma_y_vector / case.d_0

x_y = {"x_1" : x_d, "y_1" : sigma_y_vector_n}
nombre = "x/d vs sigma_y"
xLabel = r'$x/d$'
yLabel = r'$ \sigma_{y} / d_{0}$'

figura_prueba = Figura(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()

# figura "z":

x_d = [1,3,5]
sigma_z_vector_n = sigma_z_vector / case.d_0

x_y = {"x_1" : x_d, "y_1" : sigma_z_vector_n}
nombre = "x/d vs sigma_z"
xLabel = r'$x/d$'
yLabel = r'$ \sigma_{z} / d_{0}$'

figura_prueba = Figura(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()


# hago un promedio entre ambas:
# esto tiene sentido?
# habria que sumar el error de hacer esto.. esto deberia reducir el error, no?

sigma = np.zeros(3)
sigma_n = np.zeros(3)
for i in range(0,3):
    sigma[i] = np.mean([sigma_y_vector[i],sigma_z_vector[i]])
    sigma_n[i] = sigma[i] / case.d_0


print x_d, sigma, sigma_n

x_y = {"x_1" : x_d, "y_1" : sigma_n}
nombre = "x/d vs sigma"
xLabel = r'$x/d$'
yLabel = r'$ \sigma / d_{0}$'


figura_prueba = Figura(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()
