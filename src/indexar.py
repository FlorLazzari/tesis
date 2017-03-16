# indexar
import numpy as np

def indexar(vector, n):
    diferencia = np.zeros(len(vector))
    for l in range(len(vector)):
        diferencia[l] = n -vector[l]
        print diferencia
    for i, j in enumerate(vector):
        if j == min(diferencia):
            return i


# for i, j in enumerate(vector):
#     if j == n:
#         return i

#
# for i, j in enumerate(['foo', 'bar', 'baz']):
#     if j == 'bar':
#         print i
