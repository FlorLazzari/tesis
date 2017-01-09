# coding=utf-8
import matplotlib.pyplot as plt # para hacer los gráficos
import os

class Contour(object):

    def __init__(self,nombre,x_z_a,xLabel,yLabel):
        self.nombre= nombre
        self.x_z_a = x_z_a
        self.xLabel = xLabel
        self.yLabel = yLabel

    def show(self):
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        cp = plt.contourf(self.x_z_a['x_1'],self.x_z_a['z_1'],self.x_z_a['a_1'])
        plt.colorbar(cp)
        plt.show()
        fig = plt.figure()
        plt.close(fig)

    def save(self,direc):
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        cp = plt.contourf(self.x_z_a['x_1'],self.x_z_a['z_1'],self.x_z_a['a_1'])
        plt.colorbar(cp)
        try:
            os.makedirs(direc)
        except OSError:
            if not os.path.isdir(direc):
                raise
        path = "%s/%s.png" % (direc,self.nombre)
        fig = plt.figure()
        fig.savefig(path)
        plt.close(fig)

    def show_save(self,direc):
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        cp = plt.contourf(self.x_z_a['x_1'],self.x_z_a['z_1'],self.x_z_a['a_1'])
        plt.colorbar(cp)
        plt.show()
        try:
            os.makedirs(direc)
        except OSError:
            if not os.path.isdir(direc):
                raise
        path = "%s/%s.png" % (direc,self.nombre)
        fig = plt.figure()
        fig.savefig(path)
        plt.close(fig)
