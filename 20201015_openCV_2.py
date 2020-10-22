
import os
import cv2
import numpy as np
import time

file_name = 'images/image.png'
title = 'picture title'
folder = '4dHIF'


cursed = cv2.imread('images/image.png')
wald = cv2.imread('images/wald_edit.jpg')


# cv2.imshow('cursed', cursed)
# cv2.imshow('wald', wald)


cv2.imshow('add', cv2.add(wald, cursed))
cv2.waitKey(0)

weight_add = cv2.addWeighted(cursed, 0.8, wald, 0.2, 0)
cv2.imshow('weight_add', weight_add)
cv2.waitKey(0)


substracted = cv2.subtract(wald, cursed)
cv2.imshow('substracted', substracted)
cv2.waitKey(0)

cv2.destroyAllWindows()









