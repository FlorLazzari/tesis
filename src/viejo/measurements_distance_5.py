from Figura_Scatter import Figura_Scatter

# measurements:
# TSR = 6
# x/d = 5


# y/r:
# problemas: en el archivo donde estan las mediciones no hay info para "y" y
# hay dos resultados para z. asumi, por analogia con lo anterior, que la primera
# que dice z deberia decir y (a parte dice horizontal diagonal, lo cual indica
# que estan hablando de "y", no de "z")

y = [-2.4444444444,-2.2222222222,-2,-1.7777777778,-1.6888888889,-1.6,-1.5111111111,-1.4222222222,-1.33333333,-1.2444444444,-1.1555555556,-1.0666666667,-0.9777777778,-0.8888888889,-0.8,-0.7111111111,-0.6222222222,-0.5333333333,-0.4444444444,-0.3555555556,-0.2666666667,-0.1777777778,-0.0888888889,0,0.0888888889,0.1777777778,0.2666666667,0.3555555556,-0.3555555556,2.4444444444,2.2222222222,2,1.7777777778,1.6888888889,1.6,
1.5111111111,1.4222222222,1.3333333333,1.2444444444,1.1555555556,1.0666666667,0.9777777778,0.8888888889,0.8,0.7111111111,0.6222222222,0.5333333333,0.4444444444,0.3555555556,0.2666666667,0.1777777778,0.0888888889]

# (1-U/Uref):

U_deficit_dividido_U_inf = [-0.12,-0.109608,-0.100314,-0.097556,-0.093393,-0.087946,-0.077435,-0.058947,-0.03217900,0.005478,0.040037,0.081251,0.132376,0.173214,0.226227,0.263731,0.299944,0.331094,0.353178,0.36502,0.372183,0.373909,0.378681,0.384479,0.396525,0.419994,0.438193,0.448125,0.363603,-0.133648,-0.122078,-0.111003,-0.111549,-0.107405,-0.096905,-0.075745,-0.035703,0.029659,0.08888,
0.156184,0.21735,0.282054,0.332142,0.368158,0.40034,0.420912,0.436859,0.441821,0.444841,0.435482,0.415075,0.394798]

## (1-U/Uref) vs y/r

x_y = {"x_1" : y, "y_1" : U_deficit_dividido_U_inf}
nombre = "y/r vs U_deficit_dividido_U_inf x/d=5"
xLabel = r'$y/r$'
yLabel = r'$U_{deficit}/U_{inf}$'


figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.xLim = [-2,2]
figura_prueba.show()

# a simple vista pareciera que la imagen es el espejo que la del paper (6.a):
# chequear.. (tiene algo que ver con ese (-) que aparece arriba de cada columna?)


# z/r:

z = [1.55556,1.44444,1.33333,1.22222,1.13333,1.04444,0.95556,0.86667,0.77778,0.68889,0.60000,0.51111,0.42222,0.33333,0.24444,0.15556,0.06667,0.00000,-0.06667,-0.15556,-0.24444,-0.33333,-0.42222,-0.51111,-0.60000,-0.68889]

# (1-U/Uref):

U_deficit_dividido_U_inf = [-0.055713,-0.065948,-0.075184,-0.069829,-0.040287,0.005351,0.063245,0.123306,0.181677,0.241557,0.29681,0.332494,0.364417,0.380956,0.387081,0.378931,0.367846,0.360106,0.354915,0.3516,0.352826,0.363364,0.382845,0.401378,0.397624,0.378813]

## (1-U/Uref) vs y/r

x_y = {"x_1" : z, "y_1" : U_deficit_dividido_U_inf}
nombre = "z/r vs U_deficit_dividido_U_inf x/d=5"
xLabel = r'$z/r$'
yLabel = r'$U_{deficit}/U_{inf}$'


figura_prueba = Figura_Scatter(nombre,x_y,xLabel,yLabel,1)
figura_prueba.show()

# no puedo compararla porque no esta graficada en el paper,
# faltaria ver si la forma de la figura tiene sentido
