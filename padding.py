# Author: Jose Angel Garcia Gomez
# Date: 29/10/2020
# Description: This function receives a matrix and returns a matrix with a
# padding transformation

import numpy as np


def padding(A):
    A = A.tolist()
    D = []
    for i in A:
        D.append([0]+i+[0])
    ceros = [0]*(len(A[0])+2)
    return np.array([ceros]+D+[ceros])
