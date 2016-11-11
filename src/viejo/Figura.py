# coding=utf-8
import matplotlib.pyplot as plt # para hacer los gráficos

class Figura(object):
    def __init__(self,nombre,x_y,xLabel,yLabel,numero):
        self.nombre= nombre
        self.x_y = x_y
        self.xLim = None
        self.yLim = None
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.numero = numero

    def graph(self):
        if self.xLim != None:
            plt.xlim(self.xLim)
        if self.yLim != None:
            plt.ylim(self.yLim)
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        if self.numero == 1:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'])
        elif self.numero == 2:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],self.x_y['x_2'],self.x_y['y_2'])
        elif self.numero == 3:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],self.x_y['x_2'],self.x_y['y_2'],self.x_y['x_3'],self.x_y['y_3'])
        elif self.numero == 4:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],self.x_y['x_2'],self.x_y['y_2'],self.x_y['x_3'],self.x_y['y_3'],self.x_y['x_4'],self.x_y['y_4'])
        plt.show()
        fig = plt.figure()
        plt.close(fig)

    def graph_save(self):
        if self.xLim != None:
            plt.xlim(self.xLim)
        if self.yLim != None:
            plt.ylim(self.yLim)
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        if self.numero == 1:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'])
        elif self.numero == 2:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],self.x_y['x_2'],self.x_y['y_2'])
        elif self.numero == 3:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],self.x_y['x_2'],self.x_y['y_2'],self.x_y['x_3'],self.x_y['y_3'])
        elif self.numero == 4:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],self.x_y['x_2'],self.x_y['y_2'],self.x_y['x_3'],self.x_y['y_3'],self.x_y['x_4'],self.x_y['y_4'])
        direc = "figuras/gaussiana_%s.png" % self.nombre
        fig = plt.figure()
        fig.savefig(direc)
        plt.close(fig)

    def graph_show_save(self):
        if self.xLim != None:
            plt.xlim(self.xLim)
        if self.yLim != None:
            plt.ylim(self.yLim)
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        if self.numero == 1:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'])
        elif self.numero == 2:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],self.x_y['x_2'],self.x_y['y_2'])
        elif self.numero == 3:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],self.x_y['x_2'],self.x_y['y_2'],self.x_y['x_3'],self.x_y['y_3'])
        elif self.numero == 4:
            plt.plot(self.x_y['x_1'],self.x_y['y_1'],self.x_y['x_2'],self.x_y['y_2'],self.x_y['x_3'],self.x_y['y_3'],self.x_y['x_4'],self.x_y['y_4'])
        plt.show()
        direc = "figuras/gaussiana_%s.png" % self.nombre
        fig = plt.figure()
        fig.savefig(direc)
        plt.close(fig)



# el error que me tira es el siguiente:

# can't invoke "event" command: application has been destroyed
#     while executing
# "event generate $w <<ThemeChanged>>"
#     (procedure "ttk::ThemeChanged" line 6)
#     invoked from within
# "ttk::ThemeChanged"
