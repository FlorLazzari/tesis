# coding=utf-8
import matplotlib.pyplot as plt # para hacer los gráficos
import os

class Figura_Scatter(object):

    def __init__(self,nombre,x_y,xLabel,yLabel,numero):
        self.nombre= nombre
        self.x_y = x_y
        self.xLim = None
        self.yLim = None
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.numero = numero

    def show(self):
        if self.xLim != None:
            plt.xlim(self.xLim)
        if self.yLim != None:
            plt.ylim(self.yLim)
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        if self.numero == 1:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],'x')
        elif self.numero == 2:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],'x',self.x_y['x_2'],self.x_y['y_2'])
        elif self.numero == 3:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],'x',self.x_y['x_2'],self.x_y['y_2'],'x',self.x_y['x_3'],self.x_y['y_3'],'x')
        elif self.numero == 4:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],'x',self.x_y['x_2'],self.x_y['y_2'],'x',self.x_y['x_3'],self.x_y['y_3'],'x',self.x_y['x_4'],self.x_y['y_4'],'x')
        plt.show()
        fig = plt.figure()
        plt.close(fig)

    def save(self,direc):
        if self.xLim != None:
            plt.xlim(self.xLim)
        if self.yLim != None:
            plt.ylim(self.yLim)
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        if self.numero == 1:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],'x')
        elif self.numero == 2:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],'x',self.x_y['x_2'],self.x_y['y_2'],'x')
        elif self.numero == 3:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],'x',self.x_y['x_2'],self.x_y['y_2'],'x',self.x_y['x_3'],self.x_y['y_3'],'x')
        elif self.numero == 4:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],'x',self.x_y['x_2'],self.x_y['y_2'],'x',self.x_y['x_3'],self.x_y['y_3'],'x',self.x_y['x_4'],self.x_y['y_4'],'x')

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
        if self.xLim != None:
            plt.xlim(self.xLim)
        if self.yLim != None:
            plt.ylim(self.yLim)
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        if self.numero == 1:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],'x')
        elif self.numero == 2:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],'x',self.x_y['x_2'],self.x_y['y_2'],'x')
        elif self.numero == 3:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],'x',self.x_y['x_2'],self.x_y['y_2'],'x',self.x_y['x_3'],self.x_y['y_3'],'x')
        elif self.numero == 4:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],'x',self.x_y['x_2'],self.x_y['y_2'],'x',self.x_y['x_3'],self.x_y['y_3'],'x',self.x_y['x_4'],self.x_y['y_4'],'x')
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
