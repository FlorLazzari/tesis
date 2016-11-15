# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt # para hacer los gráficos

# prueba de figuras:

from Contour import Contour

hola = np.matrix([[1,1,1,1,1,1,1],[2,2,2,2,2,2,2]])
b = hola.transpose()

print np.shape(hola)
print np.shape(b)

x_z_a = {'x_1': range(1,3), 'y_1': range(1,8), 'a_1': b}

# contour_1 = Contour("contour_1",x_z_a,"xLabel","yLabel")
# contour_2 = Contour("contour_2",x_z_a,"xLabel","yLabel")
# contour_3 = Contour("contour_3",x_z_a,"xLabel","yLabel")
#
# contour_1.graph()
# contour_2.graph_save()
# contour_3.graph_show_save()

print len(x_z_a['x_1'])
print len(x_z_a['y_1'])


cp = plt.contourf(x_z_a['x_1'],x_z_a['y_1'],x_z_a['a_1'])
plt.colorbar(cp)
plt.show()
fig = plt.figure()


# lo dejo por un rato y lo retomo cuando tenga el modelo gaussiana terminado
