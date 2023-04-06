# Author: Jose Angel Garcia Gomez
# Date: 29/10/2020
# Description: This function receives a matrix and returns a matrix
# transformed to a gray scale

import cv2
import numpy as np


def escala(M):
    matriz_zeros = np.zeros((M.shape[0], M.shape[1]))
    for i in range(len(M)):
        for a in range(len(M[i])):
            suma = 0
            for b in M[i][a]:
                suma += b
            promedio = suma/len(M[i][a])
            matriz_zeros[i][a] = promedio
    return matriz_zeros
