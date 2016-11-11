# prueba de figuras:

from Figura import Figura

x_y = {'x_1': range(1,50), 'y_1': range(1,50), 'x_2': range(0,50), 'y_2': range(0,100,2), 'x_3': range(0,50), 'y_3': range(0,200,4)}

figura_1 = Figura("figura_1",x_y,"xLabel","yLabel",1)
figura_2 = Figura("figura_2",x_y,"xLabel","yLabel",2)
figura_3 = Figura("figura_3",x_y,"xLabel","yLabel",3)

figura_1.graph()
figura_2.graph_save()
figura_3.graph_show_save()
