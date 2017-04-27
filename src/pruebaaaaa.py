import numpy as np

a = np.zeros((2,3,4))

for i in range (0,2):
    for j in range (0,3):
            for k in range (0,4):
                a[i,j,k] = i*j*k

print a

hola = a[1,2,2]
print hola

hola_2 = a[0,1,:]
print hola_2
