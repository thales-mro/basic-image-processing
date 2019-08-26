import numpy as np
import cv2

def save_image(img, name):
    cv2.imwrite(name, img.astype(np.uint8), [int(cv2.IMWRITE_PNG_COMPRESSION), 100])


baboon = cv2.imread('../baboon.png')
height = baboon.shape[0]
width = baboon.shape[1]

slices = np.zeros(shape=(16, height//4, width//4, 3))

height = height//4
width = width//4

slices_counter = 0
for i in range(0, 4):
    for j in range(0, 4):
        slices[slices_counter] = baboon[height*i:height*(i+1), width*j:width*(j+1)]
        slices_counter += 1

block_orders = [5, 10, 12, 2, 7, 15, 0, 8, 11, 13, 1, 6, 3, 14, 9, 4]

block_counter = 0
for i in range(0, 4):
    for j in range(0, 4):
        baboon[height*i:height*(i+1), width*j:width*(j+1)] = slices[block_orders[block_counter]]
        block_counter += 1

save_image(baboon, "mosaic.png")