import numpy as np
from Gaussiana import Gaussiana # deberia ser Modelo, asi puedo hacer esto con todos los modelos.. no solo con Gaussiana
from math import log
from Case import Case
from Coordenadas import Coordenadas


def crear_U_logaritmico(Case,Coordenadas):
    U_inf = np.zeros((len(Coordenadas.x),len(Coordenadas.y),len(Coordenadas.z)))
    divi = np.zeros((len(Coordenadas.z)))
    num = np.zeros((len(Coordenadas.z)))
    denom = log(Case.z_h / Case.z_0) * np.ones((len(Coordenadas.z)))

    for i in range (0,len(Coordenadas.x)):
        for j in range (0,len(Coordenadas.y)):
            for k in range (1,len(Coordenadas.z)):    # por que aca hay un 1 ??
                divi[k] = Coordenadas.z[k] / Case.z_0
                num[k] = log(divi[k])
                U_inf[i,j,k] = Case.U_hub * ( num[k] / denom[k] )
    return U_inf
