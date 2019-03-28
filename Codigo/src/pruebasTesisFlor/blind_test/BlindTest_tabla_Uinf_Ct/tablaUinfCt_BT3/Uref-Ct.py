# -*- coding: utf-8 -*-
#Writing turbine array 
#Gonzalo Navarro - CSC,CONICET - Buenos Aires, Argentina
import pylab as pl 
import sys
import math
import csv  


R=0.45
D=R*2
Uref=10

turbinas=[1,1] #obtengo las dos curvas usando la turbina 1 con distintos landas
landa=[6,4.75] #los landas para las dos turbinas

#para las dos turbinas
for t in range ( len (turbinas)):
    
    #importo tabla de Landa-Ct para la turbina 1
    landaTabla=[]
    ctTabla=[]
    
    grafico='grafico-turbina'+str(turbinas[t])+'.csv'
    f=open(grafico,'r')
    tabla=[]
    reader = csv.reader(f)  # creates the reader object
    for row in reader:   # iterates the rows of the file in orders
        tabla.append(row)    # prints each row
    
    for i in range (len (tabla)):
        landaTabla.append(float(tabla[i][0]))
        ctTabla.append(float(tabla[i][2]))
         
    #obtengo el w a partir de Uref y Landa
    w=(landa[t]*Uref)/R
    
    print ('turbina: '+str(turbinas[t])+', con TSR:'+str(landa[t]))
    
    UrefTabla=[]
    #a partir de la tabla de landa obtengo el Uinf
    for i in range (len (landaTabla)):
        UrefTabla.append( (R*w)/landaTabla[i]  )
        
    #doy vuelta las tablas
    UrefTabla=UrefTabla[::-1]    
    landaTabla=landaTabla[::-1] 
    ctTabla=ctTabla[::-1] 
    
    #guardo en .CSV la tabla Uref - Ct
    salida=open('Uref-Ct-turbina'+str(turbinas[t])+'-TSR'+str(landa[t])+'.csv','w')
    
    for i in range ( len(landaTabla)):
        salida.write(str(UrefTabla[i])+' '+str(ctTabla[i])+'\n')
    salida.close()




    plt.figure(0)
    plt.plot(UrefTabla, ctTabla, linewidth=1,label='turbina '+str(turbinas[t])+', w ctte='+str(round(w,1)))
    #--ploteo------------------------------  
    plt.legend(loc='upper right', frameon=False)   
    plt.xlabel(r"$U_{ref}$",fontsize=18)  
    plt.ylabel(r"$C_{t}$",fontsize=18)  
    plt.grid()
     
    plt.axvline(x=10,linewidth=2, color='k',linestyle="--")
    
    #text(10, 0.88, 'TSR=6', color='red', bbox=dict(facecolor='none', edgecolor='red'))

    #plt.xlim([-5,1])
    #pylab.ylim([0.6,1.05])  
    figure = plt.gcf() # get current figure
    figure.set_size_inches(8, 6)
    # when saving, specify the DPI
    plt.savefig("Uref-Ct-turbina"+str(turbinas[t])+".png", dpi = 300) 
    
    
    plt.figure(1)
    plt.plot(UrefTabla, landaTabla, linewidth=1,label='turbina '+str(turbinas[t])+', w ctte='+str(round(w,1)))
    #--ploteo------------------------------  
    plt.legend(loc='upper right', frameon=False)   
    plt.xlabel(r"$U_{ref}$",fontsize=18)  
    plt.ylabel(r"$TSR$",fontsize=18)  
    plt.grid()
     
    plt.axvline(x=10,linewidth=2, color='k',linestyle="--")
    
    text(10, landa[t], 'TSR='+str(landa[t]), color='red', bbox=dict(facecolor='none', edgecolor='red'))

    #plt.xlim([-5,1])
    #pylab.ylim([0.6,1.05])  
    figure = plt.gcf() # get current figure
    figure.set_size_inches(8, 6)
    # when saving, specify the DPI
    plt.savefig("Uref-landa-turbina"+str(turbinas[t])+".png", dpi = 300) 
    
    plt.figure(2)
    plt.plot(landaTabla, ctTabla, linewidth=1,label='turbina '+str(turbinas[t])+', Uref ctte='+str(Uref))
    #--ploteo------------------------------  
    plt.legend(loc='lower right', frameon=False)   
    plt.xlabel(r"$TSR$",fontsize=18)  
    plt.ylabel(r"$C_{t}$",fontsize=18)  
    plt.grid()
     
    plt.axvline(x=landa[t],linewidth=2, color='k',linestyle="--")
    
    #text(6, 0.88, 'TSR=6, w='+str(w), color='red', bbox=dict(facecolor='none', edgecolor='red'))

    #plt.xlim([-5,1])
    #pylab.ylim([0.6,1.05])  
    figure = plt.gcf() # get current figure
    figure.set_size_inches(8, 6)
    # when saving, specify the DPI
    plt.savefig("landa-ct-turbina"+str(turbinas[t])+".png", dpi = 300) 