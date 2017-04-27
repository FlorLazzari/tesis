# coding=utf-8

import numpy as np

def abre_archivo (fn):
    # Se abre el archivo de entrada
    # Se crea una variable array, cuyos elementos serán las lineas del archivo de
    #entrada
    array = []
    # Se extrae el enter entre líneas y se separan los campos que están separados por espacios
    for line in fn.readlines():
        array.append(line.rstrip('\n').split(','))
        # Hasta ahora el archivo contiene solo strings, se convierten todos los
        # elementos a números
        for i in range (len(array)):
            for j in range (len(array[i])):
                array[i][j] = float (array[i][j])
    return array

g = open('OpenFOAM_Blind_Test_2_gonza.csv', 'r')
array = abre_archivo(g)


print (len(array))

nut = []
turbulencia = []
presion = []
epsilon = []
U_x = []
U_y = []
U_z = []
coordenada_x = []
coordenada_y = []
coordenada_z = []


for i in range (0,len(array)):
    nut.append(array[i][0])
    turbulencia.append(array[i][1])
    presion.append(array[i][2])
    epsilon.append(array[i][3])
    U_x.append(array[i][4])
    U_y.append(array[i][5])
    U_z.append(array[i][6])
    coordenada_x.append(array[i][7])
    coordenada_y.append(array[i][8])
    coordenada_z.append(array[i][9])
