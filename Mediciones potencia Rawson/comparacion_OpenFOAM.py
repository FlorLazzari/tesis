# -*- coding: utf-8 -*-

#--------------------------------------------------------------------
import pylab as pl
import sys
import math
import csv
from scipy import interpolate
import numpy as np
from scipy.interpolate import interp2d
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
#--------------------------------------------------------------------
print('----nueva corrida-------------------------------------------')
#---------------------------------------------------------------------
#------LISTA DE FUNCIONES---------------------------------------------
#---------------------------------------------------------------------

################################################################################
#-------MEDICIONES DE TORRE METEOROLOGICA--------------------------------------

#-----ABRIR txt
def abrir (archivo):
    f = open(archivo, 'r')
    l=(f.readlines())
    tabla=[]
    for i in range (len(l)):
        tabla.append(l[i].rstrip('\n'))
        tabla[i]=tabla[i].split(',')

    return (tabla)

#-----ABRIR .CSV Y GUARDARLO EN UNA TABLA
def abrirCSV (archivo):
    f = open(archivo, 'r')
    tabla=[]
    reader = csv.reader(f)  # creates the reader object

    for row in reader:   # iterates the rows of the file in orders
        tabla.append(row)    # prints each row
    f.close()      # closing

    return (tabla)


#------EXTRAIGO LA POTENCIA DE TABLA PARA LA TURBINA DESEADA (parque es la turbina 44)
def Potencias(U,Dir,turbina,tabla):

    #la P ordenada como le gusta el graficado de superfice
    P_sup=[]
    #la P ordenada como le gusta al interpolador
    P_inter=[]

    #recorro la tabla y voy guardando las potencias para cada caso
    fila=1
    for u in range(len(U)):
        Pi=[]
        for d in range(len(Dir)):
            Pi.append(float(tabla[fila][turbina+1]))
            P_inter.append(float(tabla[fila][turbina+1]))
            fila=fila+1
        P_sup.append(Pi)
    P_sup=np.array(P_sup)

    return(P_sup,P_inter)

#------EXTRAIGO LA POTENCIA DE TABLA PARA UNA DIRECCION Y VELOCIDAD Y TODAS LAS TURBINAS
def PotenciasUD(U,Dir,tabla):

    Plist=False

    for i in range (1,len (tabla)):
        #busco la velocidad
        if (float(tabla[i][0]) == U ):
            #busco la direccion
            if (int(tabla[i][1]) == Dir):
                #guardo la produccion de todas las turbinas
                Plist=[float(i) for i in tabla[i][2:43+2]]

    return(Plist)

#----PLOTEO LAS POTENCIAS PARA UNA VELOCIDAD Y TODO EL RANGO DE DIRECCIONES
def ploteoPot(U,Dir,P_sup,Pcurva):
    plt.figure(1)
    colors=['b','g','r','c','m','y','k']
    for u in range ( len (U)):
        #para turbinas individuales
        plt.plot([0,360],[Pcurva[u*2],Pcurva[u*2]],color=colors[u])
        #para la potencia total del parque
        #plt.plot([0,360],[Pcurva[u*2]*43,Pcurva[u*2]*43],color=colors[u])
        plt.plot(Dir,P_sup[u],color=colors[u])

    #plt.ylim(0, 1800*45)
    plt.xlim(0,360)
    plt.legend(loc='upper right', frameon=False)
    plt.xlabel('Direccion')
    plt.ylabel('Potencia')
    plt.grid()
    plt.savefig("potenciasDir.png", dpi = 300)
    plt.show
    plt.clf
    return()

#---PLOTEO EL DEFICIT CONTRA LA CURVA DE FRABRICA
def ploteoDef(U,Dir,P_sup,Pfabrica):
    plt.figure(2)
    colors=['b','g','r','c','m','y','k']

    ##muevo las mediciones 5º y centro
    for i in range (len (Dir)):
        Dir[i]=(Dir[i]+0)- 320

    for u in range ( len (U)):
        plt.plot(Dir,P_sup[3],color=colors[u])
    plt.plot([0,360],[1,1])
    plt.ylim(0, 1.5)
    plt.xlim(0,360)
    plt.legend(loc='upper right', frameon=False)
    plt.xlabel('Direccion')
    plt.ylabel('Potencia B/Potencia A')
    plt.grid()
    plt.savefig("potenciasDirAd.png", dpi = 300)
    plt.show
    plt.clf
    return()
    return()


#---------------------------------------------------------------------
#------ACCIONES-------------------------------------------------------
#---------------------------------------------------------------------

################################################################################
#-------DATOS DE LA CURVA DE FABRICA
Ufabrica=[]
for i in range (26):
    Ufabrica.append(float(i))
#veloc    0,1,2,3,4 ,5  ,6  ,7  ,8  ,9   ,10
Pfabrica=[0,0,0,0,88,204,371,602,880,1147,1405,1623,1729,1761,1774,1786,1795,1799] #modo 2
for i in range (18,26):
    Pfabrica.append(1800)

#-------INTERPOLADOR
from scipy.interpolate import interp1d
f1 = interp1d(Ufabrica, Pfabrica, kind='cubic')

###############################################################################
#-------TURBINAS A COMPARAR EL DEFICIT
turbA=9 # deficit = turbB / turbA
turbB=8
#centro del deficit
centro=69
U=8
colores='k'
###############################################################################
#------IMPORTO LA TABLA DE CONVERSION DE OPENFOAM
"""
archivo = "./openFOAM/tablaOpenFOAMPotencia.csv"

tabla = abrirCSV (archivo)

#------CARACTERISTICAS DE LA TABLA DE CONVERSION
pasoDir=10
pasoU=2
#------CREO EL RANGO U Y DIR DE LA TABLA OPENFOAM
Uop=np.arange(2, 14+pasoU, pasoU)
Dirop=np.arange(0, 360+pasoDir, pasoDir)
UDir=[]
for i in range (len (Uop)):
    for j in range ( len (Dirop)):
        UDir.append([Uop[i],Dirop[j]])


#-----EXTRAIGO LA POTENCIA DE LAS DOS TURBINAS
P_supA,P_interA = Potencias(Uop,Dirop,turbA,tabla)
P_supB,P_interB = Potencias(Uop,Dirop,turbB,tabla)

#hago el deficit entre las dos turbinas
P_supDEF = P_supB / P_supA

#----PLOTEO POTENCIA MEDIDA PARA todas las U y Dir
#ploteoPot(U,Dir,P_supA,Pfabrica)

#----PLOTEO DEFICIT DE OPENFOAM
ploteoDef(Uop,Dirop,P_supDEF,Pfabrica)
"""
###############################################################################
#------IMPORTO LA TABLA DE MEDICIONES
archivo = "./tablaMediciones/tablaMedicionesPotencia.csv"
tabla = abrirCSV (archivo)


#------CARACTERISTICAS DE LA TABLA DE CONVERSION (no tocar)
pasoDir=1
pasoU=1
#------CREO LA UBICACION DE LOS PUNTOS CON DATOS EN FORMATO QUE LE GUSTA A LA PUTA FUNCION
Um=np.arange(0, 250+pasoU, pasoU)
Dirm=np.arange(0, 359+pasoDir, pasoDir)
UDirm=[]
for i in range (len (Um)):
    for j in range ( len (Dirm)):
        UDirm.append([Um[i],Dirm[j]])

#-----EXTRAIGO LA POTENCIA DE LAS DOS TURBINAS
P_supAm,P_interAm = Potencias(Um,Dirm,turbA,tabla)
P_supBm,P_interBm = Potencias(Um,Dirm,turbB,tabla)

#hago el deficit entre las dos turbinas
P_supDEFm = P_supBm / P_supAm

##centro las mediciones
for i in range (len (Dirm)):
    Dirm[i]=(Dirm[i])- centro

#plt.plot(Dirm,P_supDEFm[80],linewidth=1, label='potencia medida')
plt.scatter(Dirm,P_supDEFm[int(U*10)],color=colores, label='measurements, U='+str(U)+'m/s')

#plt.xlim(280,360)
plt.xlim(-40,40)
plt.ylim(0.2,1.2)
plt.legend(loc='upper right',fontsize = 'x-small')
plt.xlabel('Wind direction')
plt.ylabel('Power deficit turb'+ str(turbB)+"/ turb"+str(turbA))
plt.grid()
plt.savefig("deficit-turb"+str(turbB)+"-turb"+str(turbA)+".png", dpi = 300)
plt.show()
# plt.clf
