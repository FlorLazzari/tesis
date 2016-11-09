# coding=utf-8
import matplotlib.pyplot as plt # para hacer los gráficos

class Figura(object):
    def __init__(self):
        self.nombre= None
        self.x = None
        self.y = None
        self.xLim = None
        self.yLim = None
        self.xLablel = None
        self.yLablel = None

    def graph(self,nombre,x,y,xLim,yLim,xLabel,yLabel):
        fig = plt.figure()
        plt.xlim(xLim)
        plt.ylim(yLim)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.plot(x,y)
        plt.show()

    def graph_save(self,nombre,x,y,xLim,yLim,xLabel,yLabel):
        fig = plt.figure()
        plt.xlim(xLim)
        plt.ylim(yLim)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.plot(x,y)
        direc = "figuras/gaussiana_%s.png" % nombre
        fig.savefig(direc)

    def graph_show_save(self,nombre,x,y,xLim,yLim,xLabel,yLabel):
        fig = plt.figure()
        plt.xlim(xLim)
        plt.ylim(yLim)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.plot(x,y)
        plt.show()
        direc = "figuras/gaussiana_%s.png" % nombre
        fig.savefig(direc)
