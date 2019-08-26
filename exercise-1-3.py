import numpy as np
import cv2

def save_image(img, name):
    cv2.imwrite(name, img.astype(np.uint8), [int(cv2.IMWRITE_PNG_COMPRESSION), 100])

def bit_plane(img, bit):
    imge =  np.where(img & (2**bit) > 0, 255, 0)
    print(imge)
    return imge

image = cv2.imread('../baboon.png')
plane_img = bit_plane(image, 7)
save_image(plane_img, "plane-7.png")
plane_img = bit_plane(image, 6)
save_image(plane_img, "plane-6.png")
plane_img = bit_plane(image, 5)
save_image(plane_img, "plane-5.png")
plane_img = bit_plane(image, 4)
save_image(plane_img, "plane-4.png")
plane_img = bit_plane(image, 3)
save_image(plane_img, "plane-3.png")
plane_img = bit_plane(image, 2)
save_image(plane_img, "plane-2.png")
plane_img = bit_plane(image, 1)
save_image(plane_img, "plane-1.png")
plane_img = bit_plane(image, 0)
save_image(plane_img, "plane-0.png")
