import numpy as np

from Case import Case
from Coordenadas import Coordenadas
from Gaussiana import Gaussiana

case_1 = Case(0.15,0.125,2.2,0.42,0.00003,0.7)
coordenadas_1 = Coordenadas(np.arange(0,15,1),np.arange(0,4.5,5),np.arange(0,4.5,0.5))

modelo_1 = Gaussiana(coordenadas_1,0.5,case_1,0.2,0.25)

modelo_1.play()
