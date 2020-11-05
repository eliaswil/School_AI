
import os
import cv2
import numpy as np
import time

file_name = 'images/image.png'
title = 'picture title'
folder = '4dHIF'


cursed = cv2.imread('images/image.png')
wald = cv2.imread('images/wald_edit.jpg')

print(cursed.shape)



def show_image(description, img):
    cv2.imshow(description, img)
    cv2.waitKey(0)

def show_scaled_image(img, factor):
    scale_factor = factor #percent
    scaled_width = int(img.shape[1] * scale_factor/100)
    scaled_height = int(img.shape[0] * scale_factor/100)
    dim = (scaled_width, scaled_height)

    # default: INTER_LINEAR
    # INTER_CUBIC
    # INTER_AREA
    # INTER_NEAREST
    # INTER_LANCZOS4
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    cv2.imshow('resized', resized)
    cv2.waitKey(0)


def edge_detection(img):
    try:
        img_sw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edge = cv2.Canny(img_sw, 100, 200)
        show_image('sw', img_sw)
        show_image('edge', edge)

    except IOError:
        print('Exception!')


def video():
    video = cv2.VideoCapture(0)
    fbground_sub = cv2.createBackgroundSubtractorMOG2()

    
    is_running = True
    while is_running:
        ret, img = video.read()

        fore_ground_mask = fbground_sub.apply(img)

        cv2.imshow('fg', fore_ground_mask)


        key = cv2.waitKey(5) & 0xFF
        if (key == 27):
            is_running = False
            pass

    video.release()

# show_scaled_image(cursed, 50)
# edge_detection(cursed)
video()

cv2.destroyAllWindows()









