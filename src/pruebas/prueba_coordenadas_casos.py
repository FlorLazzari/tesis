# prueba de cordenadas y casos:

import numpy as np
from Case import Case
from Coordenadas import Coordenadas

case_1 = Case(0.15,0.125,2.2,0.42,0.00003,0.7)
coordenada_1 = Coordenadas(np.arange(0,15,1),np.arange(0,4.5,5),np.arange(0,4.5,0.005))


print coordenada_1.x_n

coordenada_1.normalizar(case_1)

print coordenada_1.x_n
