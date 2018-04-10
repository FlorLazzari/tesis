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

#-----ABRIR .CSV Y GUARDARLO EN UNA TABLA
def abrirCSV (archivo):
    f = open(archivo, 'rb') 
    tabla=[]
    reader = csv.reader(f)  # creates the reader object
    for row in reader:   # iterates the rows of the file in orders
        tabla.append(row)    # prints each row
    f.close()      # closing
    
    return (tabla)

#----EXTRAIGO U, DIR Y POTENCIA DE LAS MEDICIONES
def medicionesExtraccion (mediciones,turbina):
    Umed=[]
    Dirmed=[]
    Pmed=[]
    dias=[]
    horas=[]
    dia=0
    hora=0
    for i in range(1,len(mediciones)): #para cada caso
        hora=hora+(1)/6.00
        horas.append(hora)
        dia=dia+(1/24.00)/6.00
        dias.append(dia)
        Umed.append(float(mediciones[i][5]))
        if (math.isnan(float(mediciones[i][6]))):
            Dirmed.append(float(mediciones[i][6]))
        else:
            Dirmed.append(int(mediciones[i][6]))
        Pmed.append(float(mediciones[i][6+turbina]))
    
    return(Umed, Dirmed, Pmed,horas,dias)
    

#-----GRAFICO LA SUPERFICIE DE POTENCIA 
def superficiePotencia(U,Dir,P,nombre):
    Direje, Ueje = meshgrid(Dir, U)
    fig = figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(Ueje, Direje, P, cmap=cm.coolwarm, linewidth=0)
    #ax.set_zlim(0, 1800*43)
    ax.set_xlim3d(0,25)
    ax.set_ylim3d(0,360)
    ax.view_init(20, -120)
    
    plt.xlabel('Velocidad entrante')  
    plt.ylabel('Direccion')  
    ax.set_zlabel('Potencia del parque')
    ax.grid()
    fig.tight_layout()
    #fig.set_size_inches(12,9) 
    plt.savefig(nombre+'.png', dpi = 300) 
    plt.show() 
    plt.clf()
    
    return()

#----LIMPIO LA BASE DE DATOS DE MEDICIONES DE VIENTO Y POTENCIA
def limpiarBaseDatos(U,Dir,P):
    cantidadNan=0
    cantidadCeros=0
    Ulimpio=[]
    Dirlimpio=[]
    Plimpio=[]
    
    for i in range ( len(U) ):
        if ( math.isnan(U[i]) or math.isnan(Dir[i]) or math.isnan(P[i])): #elimino Nans
            cantidadNan=cantidadNan+1
            
        elif ( ( U[i] < 0.5 ) or ( P[i] < 10 ) ): #elimino ceros
              cantidadCeros=cantidadCeros +1
                
        else: #guardo los datos limpios
            Ulimpio.append (U[i])
            Dirlimpio.append (Dir[i])
            Plimpio.append (P[i])
    
    print('cantidad de Nans: '+str(cantidadNan))
    print('cantidad de ceros: '+str(cantidadCeros))
    return (Ulimpio, Dirlimpio, Plimpio)

#-----GRAFICO LOS PUNTOS MEDIDOS EN 3D
def puntos3D(U,Dir,P,nombre):
    fig = figure()
    puntos3D = fig.gca(projection='3d')
    puntos3D.scatter(U, Dir, P, c=P, marker='D',s=0.1, cmap=cm.coolwarm)
    plt.xlabel('Velocidad entrante')  
    plt.ylabel('Direccion')
    puntos3D.set_zlabel('Potencia del parque')
    puntos3D.set_ylim3d(0,360)
    puntos3D.set_xlim3d(0,25)
    pl.grid()
    fig.tight_layout()
    puntos3D.view_init(20, -120)
    plt.savefig(nombre+'.png', dpi = 300)  
    plt.show() 
    plt.clf()
    return()

#----CREO LA SUPERFICIE DE POTENCIA A PARTIR DE MEDICIONES
def promedioMediciones(U,Dir,P):
    Umc=[]
    for i in range(0, 251, 1):
        Umc.append(i/10.0)
    pasoDir=1
    Dirmc=np.arange(0, 360, pasoDir) 
    
    #creo la matriz vacia de datos
    datos = np.empty((len(Umc),len(Dirmc),))
    datos[:] = np.NAN
    #creo la matriz vacia de las repeticiones
    conteo = np.empty((len(Umc),len(Dirmc),))
    conteo[:] = np.NAN

    for i in range (len(U)): #recorro todos los datos
        #busca en que posición del vector U está
        buscar=[item for item in range(len(Umc)) if Umc[item] == U[i]]
        if (buscar == []):
            Upos=0
        else:
            Upos=buscar[0] 
                  
        #busca en que posición del vector Dir está
        buscar=[item for item in range(len(Dirmc)) if Dirmc[item] == Dir[i]]
        Dirpos=buscar[0]
        
        if ( math.isnan(datos[ Upos ][ Dirpos]) ): # si nunca fue llenado
            datos[ Upos ][ Dirpos]= P[i]
        else: # si ya tenia dato
            datos[ Upos ][ Dirpos]= datos[ Upos ][ Dirpos] + P[i]
            
        if ( math.isnan(conteo[ Upos ][ Dirpos] ) ): # si nunca fue llenado
            conteo[ Upos ][ Dirpos]= 1
        else: # si ya tenia dato
            conteo[ Upos ][ Dirpos]= conteo[ Upos ][ Dirpos] + 1
   

    #promedio los datos con los conteos
    for i in range (len(datos)): #para cada velocidad
        for j in range (len(datos[i])): #para cada direccion
            datos[i][j]=datos[i][j]/conteo[i][j]

    return(Umc,Dirmc,datos)
   
    
#-----INTERPOLACION VIENTO EN POTENCIA
def interpolacionTiempo(U,Dir, P_inter, Um,Dirm):
    from scipy.interpolate import griddata
    
    #acomodo las U y D con P incognita
    Um_grid=[]
    Dirm_grid=[]
    for i in range (len (Dirm)):
        Um_grid.append(Um)
    for i in range (len (Um)):
        Dirm_grid.append(Dirm)
    
    grid_z0 = griddata(UDir, P_inter, (Um_grid, Dirm_grid), method='linear')

    Pinter=[]
    diago=(grid_z0.diagonal())
    for i in range (len (diago)):
        Pinter.append(diago[i])
    
    return(Pinter)  
    return()


#....DATOS PARA MACHINE LEARNING
def datosMachineLearning(Ulimpio,Dirlimpio,Plimpio):
    salida=open('salidasXYZ.csv','w')
    #encabezado
    salida.write('intensidad, direccion, potencia\n')
    for i in range ( len (Ulimpio)):
        salida.write( str(Ulimpio[i]) + ' ,'  + str(Dirlimpio[i]) +' ,' +str (Plimpio[i])+ '\n')
    return ()

#---CREO LA SUPERFICIE DE POTENCIA SUAVIZADA A PARTIR DE LAS MEDICIONES 
def superficieSuavizada (Umc,Dirmc,Pmc ):
    from scipy.interpolate import griddata
        
    #creo UDirm (son los pares de [U,Dir] medidos, de los que tengo una potencia en Pmc)
    UDirm=[]
    for i in range (len (Umc)):
        for j in range ( len (Dirmc)):
            UDirm.append([Umc[i],Dirmc[j]])   
    UDirm=np.array(UDirm)
         
    #creo una lista única de Pmc
    Pm_inter=[]
    for i in range(len (Pmc)):
        for j in range (len (Pmc[i])):
            Pm_inter.append(Pmc[i][j])
    Pm_inter=np.array(Pm_inter)
     
    #limpio los nans
    UDirl=[]
    Pl_inter=[]
    for i in range (len(Pm_inter)):
        if (math.isnan(float(Pm_inter[i]))):
            """
            """
        else:
            UDirl.append(UDirm[i])
            Pl_inter.append(Pm_inter[i])
    Pl_inter=np.array(Pl_inter)
    UDirl=np.array(UDirl)
    
    #grafico densidad de puntos
    fig = figure(12)
    plt.plot(UDirl[:,0], UDirl[:,1], 'k.', ms=1)       
    plt.show() 
    plt.clf() 
     

    #creo la grilla donde quiero averiguar los valores
    grid_U, grid_D = np.mgrid[0:25:251j, 0:359:360j]
    
    #interpolo sobre la grilla     
    grid_z0 = griddata(UDirl, Pl_inter, (grid_U, grid_D), method='nearest')  
    plt.imshow(grid_z0.T, cmap=cm.coolwarm, extent=[3,24,360,0], aspect='auto')
    
    #suavizo la grilla con filtro gaussiano   
    from scipy import ndimage
    blurred_face = ndimage.gaussian_filter(grid_z0, sigma=3)
    #giro la iamgen
    blurred_face180 = ndimage.rotate(blurred_face.T, 90)
    print(len(blurred_face))
    print(len(blurred_face[0]))
    
    #ploteo la imagen
    fig = figure(5)
    plt.imshow(blurred_face180, cm.coolwarm, extent=[0,360,0,25], aspect='auto')
    plt.xlabel('Direccion')  
    plt.ylabel('Velocidad entrante')  
    plt.savefig('ImgCurvaMedidaSuavizada.png', dpi = 300) 
    plt.show() 
    plt.clf()
    
    #ploteo la superfice cruda en 3D
    fig = figure(10)
    ax = fig.gca(projection='3d')
    ax.plot_surface(grid_U, grid_D, grid_z0, cmap=cm.coolwarm, linewidth=0)
    #ax.set_zlim(0, 1800*43)
    ax.set_xlim3d(0,25)
    ax.set_ylim3d(0,360)
    ax.view_init(20, -120)  
    plt.xlabel('Velocidad entrante')  
    plt.ylabel('Direccion')  
    ax.set_zlabel('Potencia del parque')
    ax.grid()
    fig.tight_layout()
    #fig.set_size_inches(12,9) 
    plt.savefig('curvaMedida.png', dpi = 300) 
    plt.show() 
    plt.clf()
        
    #ploteo la superfice suavizada en 3D
    fig = figure(11)
    ax = fig.gca(projection='3d')
    ax.plot_surface(grid_U, grid_D, blurred_face, cmap=cm.coolwarm, linewidth=0)
    #ax.set_zlim(0, 1800*43)
    ax.set_xlim3d(0,25)
    ax.set_ylim3d(0,360)
    ax.view_init(20, -120)  
    plt.xlabel('Velocidad entrante')  
    plt.ylabel('Direccion')  
    ax.set_zlabel('Potencia del parque')
    ax.grid()
    fig.tight_layout()
    #fig.set_size_inches(12,9) 
    plt.savefig('curvaMedidaSuavizada.png', dpi = 300) 
    plt.show() 
    plt.clf()
    
    return (blurred_face)

#----IMPRIMO SALIDA
def salidas (nombre,U,Dir,Pt, Tt, Ptotal):
    salida=open(nombre,'a')
    salida.write(str(U)+' ,')
    salida.write(str(Dir)+' ,')
    #escribo para cada turbina
    for i in range (len (Pt)):
        salida.write(str(Pt[i])+' ,')
    salida.write(str(Ptotal))
    for i in range (len (Tt)):
        salida.write(' ,'+str(Tt[i]))
    salida.write('\n')
    salida.close()
    
    return ()
  
#
#
#-------FIN DE LAS FUNCIONES------------------------------------------
#
#

#---------------------------------------------------------------------
#------ACCIONES-------------------------------------------------------
#---------------------------------------------------------------------

################################################################################
#-------MEDICIONES DE TORRE METEOROLOGICA--------------------------------------
#------IMPORTO DATOS DE MEDICIONES


archivo = "../../viento/medicionesTorre/salidaVientoRawson10min.csv"
mediciones = abrirCSV (archivo)

#-----EXTRAIGO LA U, DIR Y POTENCIA MEDIDAS EN EL TIEMPO
turbina=7 #para el parque entero es 44
Umed,Dirmed,Pmed,horas,dias1 = medicionesExtraccion(mediciones,turbina)


#-----GRAFICO LOS DATOS MEDIDOS COMO NUBE DE PUNTOS
#nombre='medicionesCrudas'
#puntos3D(Umed,Dirmed,Pmed,nombre)

#----LIMPIO LA BASE DE DATOS  
Ulimpio,Dirlimpio, Plimpio = limpiarBaseDatos(Umed,Dirmed,Pmed)

#---veo que las mediciones esten medio bien
P7=[]
Dir7=[]
for i in range ( len(Ulimpio)):
    if (Ulimpio[i]>6.7 and Ulimpio[i]<7.2):
        P7.append(Plimpio[i])
        Dir7.append(Dirlimpio[i])
        
plt.plot(Dir7,P7,'ko',ms=1)
plt.plot([0,360],[602,602])
plt.show() 



#----GUARDO LOS DATOS PARA HACER Machine Learning
#datosMachineLearning(Ulimpio,Dirlimpio,Plimpio)

#-----GRAFICO LOS DATOS LIMPIOS COMO NUBE DE PUNTOS
#nombre='medicionesLimpio'
#puntos3D(Ulimpio,Dirlimpio,Plimpio,nombre)

#----PROMEDIO LAS MEDICIONES LIMPIAS
Umc,Dirmc,Pmc = promedioMediciones(Ulimpio,Dirlimpio,Plimpio)

#---INTERPOLO Y GRAFICO LOS PUNTOS INTERPOLADOS
#interpolacionGrilla(Umc,Dirmc,Pmc)

#---CREO LA SUPERFICIE DE POTENCIA SUAVIZADA A PARTIR DE LAS MEDICIONES
Psup = superficieSuavizada (Umc,Dirmc,Pmc )

################################################################################
#------GUARDO LA TABLA PARA TODOS LOS CASOS

cantidadTurbinas=43
nombre='tablaMedicionesPotencia.csv'
salida=open(nombre,'w')
#escribo encabezado
salida.write('intensidad, direccion, ')
for i in range(cantidadTurbinas):
    salida.write('P'+str(i+1)+' ,')
salida.write('Ptotal ')
for i in range(cantidadTurbinas):
    salida.write(',T'+str(i+1)+' ')
salida.write('\n')
salida.close()

Dirmc=Dirmc.tolist()

#------escribo las potencias modeladas   
for u in range (len(Umc)):
    for d in range (len (Dirmc)):
        #para cada turbina
        
        #no tengo datos de empuje para cada turbina
        Tt=[]
        for i in range (43):
            Tt.append(0)
        #aca poner un for que recorra todas las turbinas
        Pt=[]
        for i in range (43):
            Pt.append(0)
        #potencia del parque entero
        Ptotal=Psup[u][d]
        salidas (nombre,Umc[u],Dirmc[d],Pt, Tt, Ptotal)
   


print('###termino la corrida####################################################')