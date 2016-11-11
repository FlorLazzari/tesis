# coding=utf-8
import matplotlib.pyplot as plt # para hacer los gráficos

class Figura(object):
    def __init__(self,nombre,x,y,xLim,yLim,xLabel,yLabel):
        self.nombre= nombre
        self.x = x
        self.y = y
        self.xLim = xLim
        self.yLim = yLim
        self.xLabel = xLabel
        self.yLabel = yLabel

    def graph(self):
        fig = plt.figure()
        plt.xlim(self.xLim)
        plt.ylim(self.yLim)
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        plt.plot(self.x,self.y)
        plt.show()

    def graph_save(self):
        fig = plt.figure()
        plt.xlim(self.xLim)
        plt.ylim(self.yLim)
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        plt.plot(self.x,self.y)
        direc = "figuras/gaussiana_%s.png" % self.nombre
        fig.savefig(direc)

    def graph_show_save(self):
        fig = plt.figure()
        plt.xlim(self.xLim)
        plt.ylim(self.yLim)
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        plt.plot(self.x,self.y)
        plt.show()
        direc = "figuras/gaussiana_%s.png" % self.nombre
        fig.savefig(direc)
