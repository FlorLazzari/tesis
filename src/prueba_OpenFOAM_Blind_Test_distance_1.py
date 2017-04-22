from Figura_Scatter import Figura_Scatter
from OpenFOAM_Blind_Test_distance_1_gonza import y,y_n,U_x,U_y,U_z,U

################################################################################
# U_x

x_y = {"x_1" : y_n, "y_1" : U_x}
nombre = "y/d vs U_x en x/d=1"
xLabel = r'$y/d$'
yLabel = r'$ U_x$'

figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()

################################################################################
# U_y

x_y = {"x_1" : y_n, "y_1" : U_y}
nombre = "y/d vs U_y en x/d=1"
xLabel = r'$y/d$'
yLabel = r'$ U_y$'

figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()

################################################################################
# U_z

x_y = {"x_1" : y_n, "y_1" : U_z}
nombre = "y/d vs U_z en x/d=1"
xLabel = r'$y/d$'
yLabel = r'$ U_z$'

figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()

################################################################################
# U

x_y = {"x_1" : y_n, "y_1" : U}
nombre = "y/d vs U en x/d=1"
xLabel = r'$y/d$'
yLabel = r'$ U$'

figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()

# el grafico del modulo U es (a simple vista) igual al grafico de U_x, chequeo:

diff_U_x_U = []
diff_U_x_U = [U[i] - U_x[i] for i in range(0,len(U_y))]

# print diff_U_x_U

x_y = {"x_1" : y_n, "y_1" : diff_U_x_U}
nombre = "y/d vs diff_U_x_U en x/d=1"
xLabel = r'$y/d$'
yLabel = r'$U_{diff}$'

figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()

# bien! viendolo en detalle los graficos efectivamente son distintos
