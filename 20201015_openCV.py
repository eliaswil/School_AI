
import os

# opencv: computer vision
import cv2
# numpy: best math library
import numpy as np
import time

file_name = 'wald.jpg'
title = 'picture title'
folder = '4dHIF'



image = cv2.imread(file_name)
cv2.imshow(title, image)

key = cv2.waitKey(0) & 0xFF

if key == 27: #ESC
    cv2.destroyAllWindows()
    pass

if key == ord('s'): # ASCII Table converter ord()
    os.chdir(folder)
    print("Files before saving")
    print(os.listdir('.')) # current folder

    cv2.imwrite(f'new_{file_name}', image)
    cv2.destroyAllWindows()

    print("Files after saving")
    print(os.listdir('.')) # current folder

    pass





