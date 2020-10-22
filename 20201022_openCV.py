
import os
import cv2
import numpy as np
import time

file_name = 'images/image.png'
title = 'picture title'
folder = '4dHIF'


cursed = cv2.imread('images/image.png')
wald = cv2.imread('images/wald_edit.jpg')

bit_1 = cv2.imread('images/bit-1.png')
bit_2 = cv2.imread('images/bit-2.png')



# bitwise AND
and_image = cv2.bitwise_and(bit_1, bit_2, mask=None)

cv2.imshow('bitwise AND', and_image)
cv2.waitKey(0)



cv2.destroyAllWindows()









