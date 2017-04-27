import numpy as np
from Gaussiana import Gaussiana # deberia ser Modelo, asi puedo hacer esto con todos los modelos.. no solo con Gaussiana
from Coordenadas import Coordenadas

def restar_U_inf_menos_deficit(Coordenadas, Gaussiana, U_inf): # Coordenadas para el largo de
    #los vect, Gaussiana para el deficit, U_inf para saber el viento externo
    U = np.zeros((len(Coordenadas.x),len(Coordenadas.y),len(Coordenadas.z)))
    for i in range (0,len(Coordenadas.x)):
        for j in range (0,len(Coordenadas.y)):
            for k in range (1,len(Coordenadas.z)):    # por que aca hay un 1 ??
                U[i,j,k] = U_inf[i,j,k] * (1 - Gaussiana.deficit_dividido_U_inf[i,j,k])
                # en lugar de Gaussiana deberia decir Modelo!!!!! cambiar eso!
    return U
