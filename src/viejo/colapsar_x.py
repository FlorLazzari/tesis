import numpy as np

def colapsar_x(matriz,posicion):
    dim_y = matriz.shape[1]
    dim_z = matriz.shape[2]
    b = np.zeros((dim_y,dim_z))
    for j in range (0,dim_y):
        for k in range (0, dim_z):
            b[j,k] = matriz[posicion,j,k]
    return b
