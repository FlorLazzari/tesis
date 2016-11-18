import numpy as np

def pol2cart(r, phi):
    y = r * np.cos(phi)
    z = r * np.sin(phi)
    return y, z
