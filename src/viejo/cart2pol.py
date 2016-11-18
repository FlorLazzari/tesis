import numpy as np

def cart2pol(y, z):
    r = np.sqrt(y**2 + z**2)
    phi = np.arctan2(z, y)
    return r, phi
    #chequear esto! yo hacia car2pol con las coordenadas normalizadas, me parece que eso no tiene sentido
