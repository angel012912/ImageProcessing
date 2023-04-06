# Author: Jose Angel Garcia Gomez
# Date: 29/10/2020
# Description: This function receives a matrix and a value and returns a
# matrix transofrmed to black and white

import numpy as np


def black_white(M, valor):
    matriz_zeros = np.zeros((M.shape[0], M.shape[1]))
    for i in range(len(M)):
        for a in range(len(M[i])):
            if M[i][a] < valor:
                matriz_zeros[i][a] = 0
            elif M[i][a] >= valor:
                matriz_zeros[i][a] = 255
    return matriz_zeros
