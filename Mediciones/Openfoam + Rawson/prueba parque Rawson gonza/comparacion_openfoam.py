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

#-------INTERPOLADOR DE LA CURVA DE POTENCIA
from scipy.interpolate import interp1d
f1 = interp1d(Ufabrica, Pfabrica, kind='cubic')


################################################################################
#------POTENCIAS OPENFOAM
codigo="v3.c"
Uop=7
Dir=270

archivo = "./potenciaTurbinas_terreno/outTurbines.Dir"+str(Dir)+".U"+str(Uop)+"_"+codigo+".csv"
tabla = abrirCSV (archivo)

#me guardo el ultimo paso de tiempo
tabla=tabla[-44:]

#guardo lo que mide en la torre met, como Ucenter
UmetOp=round((float(tabla[-1][8])),1)
Pmet=float(f1(UmetOp))

#separo las turbinas
tabla=tabla[:-1]

#guardo las potencias
Pop=[]
for i in range(len(tabla)):
    Pop.append(float(tabla[i][10]))

print('eficiencia de las potencias de openfoam: '+str(sum (Pop)/float(Pmet*43)   ))
#adimensionalizo
PopAd=[]
for i in range(len(Pop)):
    PopAd.append(Pop[i]/Pmet)

#-----PLOTEO OPENFOAM
plt.figure(4)
plt.plot(PopAd,'rs',linewidth=1,markersize=5 ,label=codigo)

################################################################################
#------POTENCIAS MEDIDAS PARA UNA DIRECCION
Um=UmetOp
archivo = "./tablaMediciones/tablaMedicionesPotencia.csv"
tabla = abrirCSV (archivo)
Pmlist=PotenciasUD(Um,Dir,tabla)

#adimensionalizo
PmlistAd=[]
for i in range(len(Pmlist)):
    PmlistAd.append(Pmlist[i]/Pmet)

print('eficiencia de las potencias de las mediciones: '+str(sum (Pmlist)/float(Pmet*43)   ))
#-----PLOTEO MEDICIONES
plt.figure(4)
plt.plot(PmlistAd,'ko',linewidth=1,markersize=5 ,label='measurements')
plt.plot(7,Pmlist[7],'ro',linewidth=1,markersize=7)
plt.plot([0,42],[1,1],'k-',linewidth=1)
plt.xlim(-1,43)
plt.ylim(0.2,1.4)
plt.xlabel('Turbine')
plt.ylabel('P_i / P_(Umet)')
plt.title('Dir: '+str(Dir)+',Umet: '+str(Um))
plt.legend(loc='lower right',fontsize = 'small')
plt.grid()
plt.savefig('rawsonPotenciaComparacion'+str(Dir), dpi = 300)
plt.show
plt.clf

################################################################################
#------    error
err=[]
for i in range(len(Pop)):
    err.append((abs(Pop[i]-Pmlist[i])/Pmlist[i])*100)

print('error absoluto promedio: '+str(round(np.mean(err),3))+'%')

################################################################################
#----VALORES EN MAPA

#---uBICACION DE LAS TURBINAS
turb=[[834.89999999999998, 2225.1999999999998], [630.0, 2511.3000000000002], [876.79999999999995, 2790.9000000000001], [843.0, 3095.1999999999998], [862.10000000000002, 3421.1000000000004], [827.89999999999998, 3752.1999999999998], [1025.2, 4119.3999999999996], [756.10000000000002, 4447.8000000000002], [1249.7, 4606.1000000000004], [1437.3, 2311.9000000000001], [1630.0, 2611.9000000000001], [1800.3, 2901.4000000000001], [1878.7, 3213.6999999999998], [2037.2, 3494.1999999999998], [2148.6999999999998, 3805.9000000000001], [2197.6999999999998, 4144.6999999999998], [2259.6999999999998, 4450.3000000000002], [1546.6999999999998, 1458.5999999999999], [1942.6000000000001, 1721.5999999999999], [2185.8000000000002, 2018.4000000000001], [2540.6999999999998, 2276.1000000000004], [2784.5999999999999, 2540.5999999999999], [2880.0999999999999, 2828.8000000000002], [3091.3000000000002, 3115.5], [3166.3000000000002, 3435.9000000000001], [3285.9000000000001, 3742.3000000000002], [3383.4000000000001, 4025.6000000000004], [3517.5999999999999, 4293.5], [3651.0999999999999, 4574.0], [2781.4000000000001, 630.0], [3036.8000000000002, 866.40000000000009], [3192.0, 1164.5], [3335.8000000000002, 1437.5999999999999], [3485.8000000000002, 1708.5999999999999], [3637.5999999999999, 2012.6000000000001], [3744.0999999999999, 2328.0], [3817.0999999999999, 2597.6999999999998], [4008.5, 2915.9000000000001], [4118.2000000000007, 3222.5999999999999], [4267.0, 3535.5], [4397.8000000000002, 3854.6000000000004], [4620.1000000000004, 4157.1000000000004], [4782.5, 4562.8999999999996]]

turbX=[]
turbY=[]

for i in range(len(turb)):
    turbX.append(turb[i][0]/90.0)
    turbY.append(turb[i][1]/90.0)

#ploteo openfoam
plt.figure()
cm = plt.cm.get_cmap('bwr')
sc = plt.scatter(turbX,turbY,c=PopAd,s=120,marker='v' ,edgecolor='black', linewidth='0.5', cmap=cm)
plt.xlim(0,60)
plt.ylim(0,60)
# plt.clim(min(PopAd), max(PopAd))
plt.clim(0.5,1.5)
plt.xlabel(r'$x/d$', fontsize=20)
plt.ylabel(r'$y/d$', fontsize=20)
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.colorbar(sc, ticks=[0.5, 1, 1.5]).set_label(label=r'$P_{TURBINA} / P_{REF}$', size=22, weight='bold')
# plt.colorbar(sc, ticks=[min(PopAd), 1, max(PopAd)]).set_label(label=r'$P_{TURBINA} / P_{REF}$', size=22, weight='bold')
# plt.axes().set_aspect('equal', 'datalim')
plt.grid()
# plt.title('Openfoam, Dir: '+str(Dir)+',Umet: '+str(Um))
plt.savefig('Rawson_Potencia_Openfoam_'+str(Dir), dpi = 300)
plt.show
plt.clf

potencia_mast = 949.027296358
potenciaTotalNormalizadaOF = sum(PopAd) / (43)
print 'OF = ',potenciaTotalNormalizadaOF

#ploteo mediciones
# plt.figure(figsize=(9,9))
# cm = plt.cm.get_cmap('bwr')
# sc = plt.scatter(turbX,turbY,c=PmlistAd,s=120,marker='v' ,edgecolor='black', linewidth='0.5', cmap=cm)
# plt.xlim(0,60)
# plt.ylim(0,60)
# # plt.clim(0.5,1.5)
# plt.clim(min(PmlistAd), max(PmlistAd))
# plt.xlabel(r'$x/d$', fontsize=20)
# plt.ylabel(r'$y/d$', fontsize=20)
# plt.xticks(fontsize=20)
#
# plt.yticks(fontsize=20)
# # plt.colorbar(sc, ticks=[0.5, 1, 1.5]).set_label(label=r'$P_{TURBINA} / P_{REF}}$', size=22, weight='bold')
# plt.colorbar(sc, ticks=[min(PmlistAd), 1, max(PmlistAd)]).set_label(label=r'$P_{TURBINA} / P_{REF}$', size=22, weight='bold')
# # plt.axes().set_aspect('equal', 'datalim')
# plt.grid()
# # plt.xlim(0,60)
# # plt.ylim(0,60)
# # plt.title(r'$P_i / P_{u_{mast}}$')
# # 'Measurements, Dir: '+str(Dir)+',Umet: '+str(Um))
# plt.savefig('ESCALARawson_Potencia_Medido_'+str(Dir), dpi = 300)
# plt.show
# plt.clf

# potenciaTotalNormalizadaMed = sum(plt.figure())


plt.figure()
cm = plt.cm.get_cmap('bwr')
sc = plt.scatter(turbX,turbY,c=PopAd,s=120,marker='v' ,edgecolor='black', linewidth='0.5', cmap=cm)
plt.xlim(0,60)
plt.ylim(0,60)
# plt.clim(min(PopAd), max(PopAd))
plt.clim(0.5,1.5)
plt.xlabel(r'$x/d$', fontsize=20)
plt.ylabel(r'$y/d$', fontsize=20)
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.colorbar(sc, ticks=[0.5, 1, 1.5]).set_label(label=r'$P_{TURBINA} / P_{REF}$', size=22, weight='bold')
# plt.colorbar(sc, ticks=[min(PopAd), 1, max(PopAd)]).set_label(label=r'$P_{TURBINA} / P_{REF}$', size=22, weight='bold')
# plt.axes().set_aspect('equal', 'datalim')
plt.grid()
# plt.title('Openfoam, Dir: '+str(Dir)+',Umet: '+str(Um))
plt.savefig('Rawson_Potencia_Openfoam_'+str(Dir), dpi = 300)
plt.show
plt.clf

#  / 43
# print 'Med = ',potenciaTotalNormalizadaMed


plt.figure()
cm = plt.cm.get_cmap('bwr')
sc = plt.scatter(turbX,turbY,c=PmlistAd,s=120,marker='v' ,edgecolor='black', linewidth='0.5', cmap=cm)
plt.xlim(0,60)
plt.ylim(0,60)
# plt.clim(min(PopAd), max(PopAd))
plt.clim(0.5,1.5)
plt.xlabel(r'$x/d$', fontsize=20)
plt.ylabel(r'$y/d$', fontsize=20)
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.colorbar(sc, ticks=[0.5, 1, 1.5]).set_label(label=r'$P_{TURBINA} / P_{REF}$', size=22, weight='bold')
# plt.colorbar(sc, ticks=[min(PopAd), 1, max(PopAd)]).set_label(label=r'$P_{TURBINA} / P_{REF}$', size=22, weight='bold')
# plt.axes().set_aspect('equal', 'datalim')
plt.grid()
# plt.title('Openfoam, Dir: '+str(Dir)+',Umet: '+str(Um))
plt.savefig('Rawson_Potencia_Medido_'+str(Dir), dpi = 300)
plt.show
plt.clf


fig, ax = plt.subplots()
ax.hist(PmlistAd)#, alpha=0.9)
plt.ylabel('Frecuencia', fontsize=16)
plt.xlabel(r'$P_{TURBINA} / P_{REF}$', fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.xlim([0.5, 1.5])
plt.ylim([0, 11])
plt.grid()
plt.savefig('histograma_Rawson_medido.pdf')
plt.show()

fig, ax = plt.subplots()
ax.hist(PopAd)#, alpha=0.9)
plt.ylabel('Frecuencia', fontsize=16)
plt.xlabel(r'$P_{TURBINA} / P_{REF}$', fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.xlim([0.5, 1.5])
plt.ylim([0, 11])
plt.grid()
plt.savefig('histograma_Rawson_OF.pdf')
plt.show()
