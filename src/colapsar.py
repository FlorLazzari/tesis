import numpy as np

def colapsar(matriz,posicion):
    dim_x = matriz.shape[0]
    dim_z = matriz.shape[2]
    b = np.zeros((dim_x,dim_z))
    for i in range (0,dim_x):
        for k in range (0, dim_z):
            b[i,k] = matriz[i,posicion,k]
    return b
