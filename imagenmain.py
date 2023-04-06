# Author: Jose Angel Garcia Gomez
# Date: 29/10/2020
# Description: This program read images and applies different transform
# functions to it such as: convert to black and white, gray scale, convolution
# and padding

import cv2
import numpy as np
import black_white 
import grayescale 
import padding
import convolucion

imagen = cv2.imread("imagen.jpg")
imagen_gray = grayescale.escala(imagen)
valor = 127
cv2.imwrite("grayScale.jpg", imagen_gray)

imagen_black_white = black_white.black_white(imagen_gray, valor)
cv2.imwrite("BlackWhite.jpg", imagen_black_white)

filtro = [[3, 4, 2], [1, 0, 1], [2, 3, 1]]
B = np.array(filtro)
imagen_convolucion = convolucion.convolucion(imagen_gray, B)

cv2.imwrite("ImagenConvolucion.jpg", imagen_convolucion)

imagen_padd = padding.padding(imagen_gray)
imagen_convolucion_padding = convolucion.convolucion(imagen_padd, B)
cv2.imwrite("ImagenConvolucionPadding.jpg", imagen_convolucion_padding)

filtro2 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
B2 = np.array(filtro2)
imagen_convolucion2 = convolucion.convolucion(imagen_gray, B2)

cv2.imwrite("ImagenConvolucion2.jpg", imagen_convolucion2)

imagen_padd2 = padding.padding(imagen_gray)
imagen_convolucion_padding2 = convolucion.convolucion(imagen_padd, B2)
cv2.imwrite("ImagenConvolucionPadding2.jpg", imagen_convolucion_padding2)
