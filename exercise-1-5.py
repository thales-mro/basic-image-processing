import numpy as np
import cv2

def save_image(img, name):
    cv2.imwrite(name, img.astype(np.uint8), [int(cv2.IMWRITE_PNG_COMPRESSION), 100])

def combine_images(img1, img2, alfa):
    return img1*alfa + img2*(1 - alfa)

baboon = cv2.imread('../baboon.png')
bfly = cv2.imread('../butterfly.png')

comb1 = combine_images(baboon, bfly, 0.2)
save_image(comb1, 'alfa20.png')

comb2 = combine_images(baboon, bfly, 0.5)
save_image(comb2, 'alfa50.png')

comb3 = combine_images(baboon, bfly, 0.8)
save_image(comb3, 'alfa80.png')