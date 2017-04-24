# indexar
import numpy as np

def indexar(vector, n):
    a = len(vector)
    diferencia = np.zeros(a)
    for l in range(len(vector)):
        diferencia[l] = (n -vector[l])**2
    for i, j in enumerate(diferencia):
        if j == min(diferencia):
            return i
