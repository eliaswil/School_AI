
import os
import cv2
import numpy as np
import time

file_name = 'images/image.png'
title = 'picture title'
folder = '4dHIF'




image = cv2.imread(file_name)


red, green, blue = cv2.split(image)

cv2.imshow('orig', image)
cv2.waitKey(0)
cv2.imshow('blue', blue)
cv2.waitKey(0)
cv2.imshow('green', green)
cv2.waitKey(0)
cv2.imshow('red', red)
cv2.waitKey(0)

cv2.destroyAllWindows()









