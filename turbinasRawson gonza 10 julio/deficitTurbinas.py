# -*- coding: utf-8 -*-
import pylab as plt
import csv  
import numpy as np



#################################################################################  
#---FUNCIONES
    
#-----ABRIR .CSV Y GUARDARLO EN UNA TABLA
def abrirCSV (archivo):
    f = open(archivo, 'r') 
    tabla=[]
    reader = csv.reader(f)  # creates the reader object
    
    for row in reader:   # iterates the rows of the file in orders
        tabla.append(row)    # prints each row
    f.close()      # closing
    
    return (tabla)


def rawsonDatos(archivo):
    #------DATOS DE RAWSON CADA 10MIN  
    tabla=abrirCSV(archivo)
    print('dato cada 10 min: '+tabla[0][2]+'/'+tabla[0][1]+'/'+tabla[0][0]+', hora:'+tabla[0][3]+', min: '+tabla[0][4]+', hasta '+tabla[len(tabla)-1][2]+'/'+tabla[len(tabla)-1][1]+'/'+tabla[len(tabla)-1][0]+', hora:'+tabla[len(tabla)-1][3]+', min: '+tabla[len(tabla)-1][4]+' ')
    
    #---FILTRO LOS DATOS QUE TIENE NAN
    tablaOk=[] 
    for i in range (len(tabla)):
        malo=False
        #---recolecto datos para la rosa de vientos (sin Nans)
        for j in range (len(tabla[i])):
            if (np.isnan(float(tabla[i][j]))):
                malo=True
        if (malo==False):
            tablaOk.append(tabla[i]) 
    return(tablaOk)

def deficitMedido(tablaOk,tur_down,tur_up,centro):
    ##------BUSCO LOS DEFICITS MEIDIDOS ENTRE DOS TURBINAS
    U=8
    rangU=1 
    
    
    deff=[]
    deffOk=[]
    out=[]
    DirDeff=[]
    for i in range(0,360,1):
        out.append([])
        deff.append([])
        deffOk.append([])
        DirDeff.append(i)
    
    for i in range(len(tablaOk)):
        if float(tablaOk[i][5]) > U-rangU and float(tablaOk[i][5]) < U+rangU:
            deff[int(float(tablaOk[i][7]))].append(  float(tablaOk[i][94+tur_down]) / float(tablaOk[i][94+tur_up])   )
    
    deffMean=[]
    deffMax=[]
    deffMin=[]
    deffstdMin=[]
    deffstdMax=[]
    deffstd=[]
    for i in range(len(deff)): 
        if len(deff[i]) == 0:
            print('direccion vacia'+str(i))
            deffMean.append(1)
            deffMin.append(1)
            deffMax.append(1)
            deffstd.append(1)
            deffstdMin.append(1)
            deffstdMax.append(1)
        else:
            deffMean.append(np.mean(deff[i]))
            deffMin.append(min(deff[i]))
            deffMax.append(max(deff[i]))
            deffstd.append(np.std(deff[i]) )
            deffstdMin.append(deffMean[i]-np.std(deff[i]) )
            deffstdMax.append(deffMean[i]+np.std(deff[i]) )
    
    
    #---filtro los datos con dos desvios estandar    
    for i in range(len(deff)):
        for j in range(len(deff[i])):
            if abs(deff[i][j]-deffMean[i]) > 2*deffstd[i]:
                out[i].append(deff[i][j])
            else:
                deffOk[i].append(deff[i][j])
    
    #miro la cantida dde oUtlayers
    """
    outCont=[]
    for i in range(len(out)):
        outCont.append(len(out[i]))
        
    plt.figure(1)
    plt.scatter(DirDeff,outCont)
    """
                
    #calculo todo de nuevo
    deffMean=[]
    deffMax=[]
    deffMin=[]
    deffstd=[]
    for i in range(len(deff)): 
        if len(deffOk[i])<2:
            deffMean.append(np.nan)
            deffMin.append(np.nan)
            deffMax.append(np.nan)
            deffstd.append(np.nan )
        else: 
            deffMean.append(np.mean(deffOk[i]))
            deffMin.append(min(deffOk[i]))
            deffMax.append(max(deffOk[i]))
            deffstd.append(np.std(deffOk[i]) )
    
    #adimensionalizo        
    DirAd=[]
    for i in range(len(DirDeff)):
        DirAd.append(DirDeff[i]-centro)
    
    #ploteo mediciones
    plt.figure(2)     
    plt.errorbar(DirAd,deffMean, yerr=deffstd,color='gray',marker='o',markersize=3,label= "Measurements",zorder=0)
    plt.ylim(0.2,1.3)
    plt.xlim(-25,25)
    
    return()
  
def deficitOpenfoam(tur_down,tur_up,centro,codigo,color,nombre):
    #------IMPORTO LAS POTENCIAS DE LAS DOS TURBINAS OPENFOAM
    tabla = abrirCSV (archivo)
    #saco el encabezado
    tabla=tabla[2:]
      
    P_up=[]
    P_down=[]
    DirDeff_cfd=[]
    Uinf_up=[]
    
    #para P7/P8, centro 320
    if tur_up==8 and tur_down==7: 
        for i in range(0,len(tabla),4):
            textoDir=tabla[i][0].split()
            DirDeff_cfd.append(float(textoDir[1]))
        
        
        for i in range(3,len(tabla),4):
            Uinf_up.append(float(tabla[i][9]))
        
        
        for i in range(3,len(tabla),4):
            P_up.append(float(tabla[i][10]))
        for i in range(2,len(tabla),4):
            P_down.append(float(tabla[i][10]))
        correccion=0
        #plote velocidad
        plt.figure(3) 
        plt.plot(DirDeff_cfd,Uinf_up,color,linewidth=2,markersize=3,label= "U upstream")
        plt.grid()
        plt.show()
        
        
    #para P8/P9, centro 70
    if tur_up==9 and tur_down==8: 
        for i in range(0,len(tabla),4):
            textoDir=tabla[i][0].split()
            DirDeff_cfd.append(float(textoDir[1]))
        
        for i in range(3,len(tabla),4):
            P_up.append(float(tabla[i][10]))
        for i in range(2,len(tabla),4):
            P_down.append(float(tabla[i][10]))
        correccion=0
    
    #para P6/P9, centro 25
    if tur_up==9 and tur_down==6:   
        for i in range(0,len(tabla),6):
            textoDir=tabla[i][0].split()
            DirDeff_cfd.append(float(textoDir[1]))
        for i in range(5,len(tabla),6):
            P_up.append(float(tabla[i][10]))
        for i in range(2,len(tabla),6):
            P_down.append(float(tabla[i][10]))
        correccion=0
        
    #para P7/P9, centro 22
    if tur_up==9 and tur_down==7: 
        for i in range(0,len(tabla),6):
            textoDir=tabla[i][0].split()
            DirDeff_cfd.append(float(textoDir[1]))
        for i in range(5,len(tabla),6):
            P_up.append(float(tabla[i][10]))
        for i in range(3,len(tabla),6):
            P_down.append(float(tabla[i][10]))
        correccion=0
    
    
    
    
    #ploteo la potencia de cada turb
    plt.figure(1) 
    #plt.plot(DirDeff_cfd,P_up,color,linewidth=1,markersize=3,label= "Potencia turb"+str(tur_up)+", "+codigo)    
    plt.plot(DirDeff_cfd,P_down,color,linewidth=2,markersize=3,label= "Potencia turb"+str(tur_down)+", "+codigo+' ('+nombre+')')  
    plt.legend(loc='lower right', frameon=False)
    plt.xlabel('Direction [deg]')  
    plt.ylabel('Power turbine')  
    plt.grid()
    plt.savefig("power_tur"+str(tur_down)+"_"+str(tur_up)+".png", dpi = 300)    
    plt.show() 
    
    #plote el decit  
    deff_cfd=[]
    for i in range(len(P_up)):
        deff_cfd.append(P_down[i]/P_up[i])
    
    DirDeff_cfdAd=[]
    for i in range(len(DirDeff_cfd)):
        DirDeff_cfdAd.append(DirDeff_cfd[i]-centro-correccion)
       
    plt.figure(2)     
    plt.plot(DirDeff_cfdAd,deff_cfd,color,linewidth=1,markersize=5,label= 'Adaptive AD',zorder=1)
    plt.legend(loc='lower right', frameon=False)
    plt.xlabel('Centered wind direction [deg]')  
    plt.ylabel('P'+str(tur_down)+" / P"+str(tur_up))  
    
    
#################################################################################    
#------ACCIONES

#importo los datos de rawson
archivo='/home/gonzalo/GIOL/Rawson/turbinas/rawson10min.csv'
#tablaOk = rawsonDatos(archivo)

#ploteo el deficit medido
tur_down=6
tur_up=9
centro=28 #la direccion donde se produce el maximo deficil
deficitMedido(tablaOk,tur_down,tur_up,centro)

#ploteo el deficit de openfoam
codigos=['v2a','v2b','v2c','v3c']
nombre=['tonto, Uniform T','BSC, uniform T','nuestro, uniform T','nuestro, not uniform T']
color=['bv-','bv--','bv:','rv-']


codigos=['v3c']
nombre=['nuestro, not uniform T']
color=['rv-']


for c in range(len(codigos)):
    archivo='/home/gonzalo/GIOL/Rawson/turbinas/resultados'+str(tur_down)+'_'+str(tur_up)+'_'+codigos[c]+'.csv'
    deficitOpenfoam(tur_down,tur_up,centro,codigos[c],color[c],nombre[c])
    
plt.figure(2)
plt.grid()
#plt.plot([-30,30],[1,1],'k')
plt.savefig("deficit_tur"+str(tur_down)+"_"+str(tur_up)+".png", dpi = 300)    
plt.show() 



#################################################################################    
print('---termino----')