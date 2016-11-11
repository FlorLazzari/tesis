from Figura import Figura

class Figura_Mixta(Figura):

    def __init__(self,nombre,x,y,xLabel,yLabel,x_1,y_1,x_2,y_2,x_3,y_3,x_4,y_4):
        super(Figura_Mixta, self).__init__(nombre,x,y,xLabel,yLabel)
        self.nombre = nombre
        self.x = x
        self.y = y
        self.xLim = None
        self.yLim = None
        self.xLabel = xLabel
        self.yLabel = yLabel

    def imprimir(self):
        print self.nombre

#
# class Person(object):
#
#     def __init__(self, name):
#         self.name = name
#         self.pet = None
#
# class Employee(Person):
#
#     def __init__(self, name, salary):
#         super(Employee, self).__init__(name)
#         self.salary = salary
#
# x_1 = range(0,50)
# y_1 = range(0,50)
# x_2 = range(0,50)
# y_2 = range(0,100,2)
# x_3 = range(0,50)
# y_3 = range(0,200,4)
#
#
# fig = plt.figure()
# plt.xlabel("hola")
# plt.ylabel("chau")
# plt.plot(x_1, y_1, x_2, y_2, x_3, y_3)
# plt.show()
