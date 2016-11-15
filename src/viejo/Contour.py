# coding=utf-8
import matplotlib.pyplot as plt # para hacer los gráficos

class Contour(object):

    def __init__(self,nombre,x_z_a,xLabel,yLabel):
        self.nombre= nombre
        self.x_z_a = x_z_a
        self.xLabel = xLabel
        self.yLabel = yLabel

    def graph(self):
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        cp = plt.contourf(self.x_z_a['x_1'],self.x_z_a['z_1'],self.x_z_a['a_1'])
        plt.colorbar(cp)
        plt.show()
        fig = plt.figure()
        plt.close(fig)

    def graph_save(self):
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        cp = plt.contourf(self.x_z_a['x_1'],self.x_z_a['z_1'],self.x_z_a['a_1'])
        plt.colorbar(cp)
        direc = "figuras/gaussiana_%s.png" % self.nombre
        fig = plt.figure()
        fig.savefig(direc)
        plt.close(fig)

    def graph_show_save(self):
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        cp = plt.contourf(self.x_z_a['x_1'],self.x_z_a['z_1'],self.x_z_a['a_1'])
        plt.colorbar(cp)
        plt.show()
        direc = "figuras/gaussiana_%s.png" % self.nombre
        fig = plt.figure()
        fig.savefig(direc)
        plt.close(fig)
