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
    f = open(archivo, 'rb') 
    l=(f.readlines())
    tabla=[]
    for i in range (len(l)):
        tabla.append(l[i].rstrip('\n'))
        tabla[i]=tabla[i].split()
    
    return (tabla)
    
#-----ABRIR .CSV Y GUARDARLO EN UNA TABLA
def abrirCSV (archivo):
    f = open(archivo, 'rb') 
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
  
    
################################################################################
#------POTENCIAS MEDIDAS PARA UNA DIRECCION
Um=8.1
Dir=30

archivo = "./tablaMediciones/tablaMedicionesPotencia.csv"
tabla = abrirCSV (archivo)

Pmlist=PotenciasUD(Um,Dir,tabla)
################################################################################
#------COMPARO MODELO CONTRA MEDICIONES
casoAlya=Dir

###################################################################################    
##------ SIN CORIOLIS k-e-std SIN TERRENO
#archivo = "./potenciaTurbinas/resultadosPotencia."+str(casoAlya)+".kestd.txt"
#
#alya = abrir(archivo)
#
#PalyaD=[]
#UalyaD=[]
#for i in range ( len (alya)):
#    PalyaD.append(float(alya [i][7]))
#    UalyaD.append(float(alya [i][4]) )
#
#UT8=UalyaD[8-1]
##---modifico la U para  que coincida con las mediciones
#for i in range(len(UalyaD)):
#    UalyaD[i]=UalyaD[i]*(8/UT8)
#    
#for i in range(len(PalyaD)):
#    PalyaD[i]=f1(UalyaD[i])
#
##---ERROR
#err=[]
#for i in range(len(Pmlist)):
#    err.append (abs( (PalyaD[i]-Pmlist[i]) / float(Pmlist[i]) )*100)
#   
##-----VALORES EN UNA LINEA
#plt.figure(4)
#plt.plot(PalyaD,'g--',linewidth=1,markersize=5 ,label='k-e-std - NO coriolis - NO terreno, error promedio: '+str ( round(np.mean (err),2) ) +'%') 
#
###################################################################################    
##------ SIN CORIOLIS realW SIN TERRENO
#archivo = "./potenciaTurbinas/resultadosPotencia."+str(casoAlya)+".realW.txt"
#
#alya = abrir(archivo)
#
#PalyaD=[]
#UalyaD=[]
#for i in range ( len (alya)):
#    PalyaD.append(float(alya [i][7]))
#    UalyaD.append(float(alya [i][4]) )
#
#UT8=UalyaD[8-1]
##---modifico la U para  que coincida con las mediciones
#for i in range(len(UalyaD)):
#    UalyaD[i]=UalyaD[i]*(Um/UT8)
#    
#for i in range(len(PalyaD)):
#    PalyaD[i]=f1(UalyaD[i])
#
##---ERROR
#err=[]
#for i in range(len(Pmlist)):
#    err.append (abs( (PalyaD[i]-Pmlist[i]) / float(Pmlist[i]) )*100)
#   
##-----VALORES EN UNA LINEA
#plt.figure(4)
#plt.plot(PalyaD,'k--',linewidth=1,markersize=5 ,label='realW - NO coriolis - NO terreno, error promedio: '+str ( round(np.mean (err),2) ) +'%') 


#################################################################################    
#------ SIN CORIOLIS k-e-std CON TERRENO
archivo = "./potenciaTurbinas_terreno/resultadosPotencia."+str(casoAlya)+".kestd.txt"

alya = abrir(archivo)

PalyaD=[]
UalyaD=[]
for i in range ( len (alya)):
    PalyaD.append(float(alya [i][7]))
    UalyaD.append(float(alya [i][4]) )

UT8=UalyaD[8-1]
#---modifico la U para  que coincida con las mediciones
for i in range(len(UalyaD)):
    UalyaD[i]=UalyaD[i]*(Um/UT8)
    
for i in range(len(PalyaD)):
    PalyaD[i]=f1(UalyaD[i])

#---ERROR
err=[]
for i in range(len(Pmlist)):
    err.append (abs( (PalyaD[i]-Pmlist[i]) / float(Pmlist[i]) )*100)
   
#-----VALORES EN UNA LINEA
plt.figure(4)
plt.plot(PalyaD,'g-',linewidth=1,markersize=5 ,label='k-e-std - NO coriolis - CON terreno, error promedio: '+str ( round(np.mean (err),2) ) +'%') 

##################################################################################    
##------ SIN CORIOLIS realW CON TERRENO
#archivo = "./potenciaTurbinas_terreno/resultadosPotencia."+str(casoAlya)+".realW.txt"
#
#alya = abrir(archivo)
#
#PalyaD=[]
#UalyaD=[]
#for i in range ( len (alya)):
#    PalyaD.append(float(alya [i][7]))
#    UalyaD.append(float(alya [i][4]) )
#
#UT8=UalyaD[8-1]
##---modifico la U para  que coincida con las mediciones
#for i in range(len(UalyaD)):
#    UalyaD[i]=UalyaD[i]*(Um/UT8)
#    
#for i in range(len(PalyaD)):
#    PalyaD[i]=f1(UalyaD[i])
#
##---ERROR
#err=[]
#for i in range(len(Pmlist)):
#    err.append (abs( (PalyaD[i]-Pmlist[i]) / float(Pmlist[i]) )*100)
#   
##-----VALORES EN UNA LINEA
#plt.figure(4)
#plt.plot(PalyaD,'b-',linewidth=1,markersize=5 ,label='realW - NO coriolis - CON terreno, error promedio: '+str ( round(np.mean (err),2) ) +'%') 
#
##################################################################################    
##------ SIN CORIOLIS k-e-fp CON TERRENO
#archivo = "./potenciaTurbinas_terreno/resultadosPotencia."+str(casoAlya)+".kefp.txt"
#
#alya = abrir(archivo)
#
#PalyaD=[]
#UalyaD=[]
#for i in range ( len (alya)):
#    PalyaD.append(float(alya [i][7]))
#    UalyaD.append(float(alya [i][4]) )
#
#UT8=UalyaD[8-1]
##---modifico la U para  que coincida con las mediciones
#for i in range(len(UalyaD)):
#    UalyaD[i]=UalyaD[i]*(Um/UT8)
#    
#for i in range(len(PalyaD)):
#    PalyaD[i]=f1(UalyaD[i])
#
##---ERROR
#err=[]
#for i in range(len(Pmlist)):
#    err.append (abs( (PalyaD[i]-Pmlist[i]) / float(Pmlist[i]) )*100)
#   
##-----VALORES EN UNA LINEA
#plt.figure(4)
#plt.plot(PalyaD,'m-',linewidth=1,markersize=5 ,label='k-e-fp - NO coriolis - CON terreno, error promedio: '+str ( round(np.mean (err),2) ) +'%') 



################################################################################ 
#-----MEDICIONES
plt.figure(4)
plt.plot(Pmlist,'ko',linewidth=1,markersize=5 ,label='measurements') 
plt.plot(7,Pmlist[7],'ro',linewidth=1,markersize=7) 
Pu=f1(Um)
plt.plot([0,42],[Pu,Pu],'k-',linewidth=1) 
plt.xlim(-1,43)
plt.ylim(0,Pu*1.5)
plt.title('Dir: '+str(Dir)+',Umet: '+str(Um))
plt.legend(loc='lower right',fontsize = 'small') 
plt.grid()
plt.savefig('rawsonPotenciaComparacion'+str(casoAlya), dpi = 300)     
plt.show
plt.clf
################################################################################ 
#----VALORES EN MAPA

#---uBICACION DE LAS TURBINAS
turb=[[834.89999999999998, 2225.1999999999998], [630.0, 2511.3000000000002], [876.79999999999995, 2790.9000000000001], [843.0, 3095.1999999999998], [862.10000000000002, 3421.1000000000004], [827.89999999999998, 3752.1999999999998], [1025.2, 4119.3999999999996], [756.10000000000002, 4447.8000000000002], [1249.7, 4606.1000000000004], [1437.3, 2311.9000000000001], [1630.0, 2611.9000000000001], [1800.3, 2901.4000000000001], [1878.7, 3213.6999999999998], [2037.2, 3494.1999999999998], [2148.6999999999998, 3805.9000000000001], [2197.6999999999998, 4144.6999999999998], [2259.6999999999998, 4450.3000000000002], [1546.6999999999998, 1458.5999999999999], [1942.6000000000001, 1721.5999999999999], [2185.8000000000002, 2018.4000000000001], [2540.6999999999998, 2276.1000000000004], [2784.5999999999999, 2540.5999999999999], [2880.0999999999999, 2828.8000000000002], [3091.3000000000002, 3115.5], [3166.3000000000002, 3435.9000000000001], [3285.9000000000001, 3742.3000000000002], [3383.4000000000001, 4025.6000000000004], [3517.5999999999999, 4293.5], [3651.0999999999999, 4574.0], [2781.4000000000001, 630.0], [3036.8000000000002, 866.40000000000009], [3192.0, 1164.5], [3335.8000000000002, 1437.5999999999999], [3485.8000000000002, 1708.5999999999999], [3637.5999999999999, 2012.6000000000001], [3744.0999999999999, 2328.0], [3817.0999999999999, 2597.6999999999998], [4008.5, 2915.9000000000001], [4118.2000000000007, 3222.5999999999999], [4267.0, 3535.5], [4397.8000000000002, 3854.6000000000004], [4620.1000000000004, 4157.1000000000004], [4782.5, 4562.8999999999996]]
turbX=[]
turbY=[]

for i in range(len(turb)):
    turbX.append(turb[i][0])
    turbY.append(turb[i][1])  
    
plt.figure(5) 
cm = plt.cm.get_cmap('coolwarm')
sc = plt.scatter(turbX,turbY,c=PalyaD,s=120,marker='v' , cmap=cm)
plt.xlim(0,5412)
plt.ylim(0,5236)
plt.clim(min(Pmlist),max(Pmlist))
plt.title('Alya, Dir: '+str(Dir)+',Umet: '+str(Um))
plt.colorbar(sc)

plt.xlabel('x (m)')  
plt.ylabel('y (m)')  
plt.grid()
plt.savefig('rawsonPotenciaAlya'+str(casoAlya), dpi = 300)     
plt.show
plt.clf

plt.figure(6) 
cm = plt.cm.get_cmap('coolwarm')
sc = plt.scatter(turbX,turbY,c=Pmlist,s=120,marker='v' , cmap=cm)
plt.xlim(0,5412)
plt.ylim(0,5236)
plt.clim(min(Pmlist),max(Pmlist))
plt.title('Measurements, Dir: '+str(Dir)+',Umet: '+str(Um)) 
plt.colorbar(sc)

plt.xlabel('x (m)')  
plt.ylabel('y (m)')  
plt.grid()
plt.savefig('rawsonPotenciaMedidas'+str(casoAlya), dpi = 300)     
plt.show
plt.clf