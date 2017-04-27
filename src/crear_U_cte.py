import numpy as np
from Gaussiana import Gaussiana # deberia ser Modelo, asi puedo hacer esto con todos los modelos.. no solo con Gaussiana
from math import log
from Case import Case
from Coordenadas import Coordenadas


def crear_U_cte(Case,Coordenadas):
    U_inf = np.zeros((len(Coordenadas.x),len(Coordenadas.y),len(Coordenadas.z)))
    for i in range (0,len(Coordenadas.x)):
        for j in range (0,len(Coordenadas.y)):
            for k in range (0,len(Coordenadas.z)):
                U_inf[i,j,k] = Case.U_hub 
    return U_inf
