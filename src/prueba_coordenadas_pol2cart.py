# prueba de pol2cart:

import numpy as np
from Case import Case
from Coordenadas import Coordenadas

coordenada_1 = Coordenadas(np.arange(0,15),np.arange(0,10),np.arange(0,10))

coordenada_1.cart2pol()

print coordenada_1.r
print coordenada_1.phi

print len(coordenada_1.y)
print len(coordenada_1.z)
print len(coordenada_1.r)
print len(coordenada_1.phi)
