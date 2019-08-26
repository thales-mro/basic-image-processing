import numpy as np
import cv2

def change_scale(img, original_min, original_max, tmin, tmax):
    print((tmax - tmin)/(original_max - original_min), tmin)
    transf_image = np.add(np.multiply(img, ((tmax - tmin)/(original_max - original_min))), tmin)
    print(transf_image)
    return transf_image

def save_image(img, name):
    cv2.imwrite(name, img.astype(np.uint8), [int(cv2.IMWRITE_PNG_COMPRESSION), 100])

def gamma_correction(img, gamma):
    corr = 1/gamma
    ti = img**corr
    return ti

image = cv2.imread('../baboon.png')
scaled_image = change_scale(image, 0, 255, 0, 1)
gamma15 = gamma_correction(scaled_image, 1.5)
gamma15 = change_scale(gamma15, 0, 1, 0, 255)
save_image(gamma15, "gamma1-5.png")
gamma25 = gamma_correction(scaled_image, 2.5)
gamma25 = change_scale(gamma25, 0, 1, 0, 255)
save_image(gamma25, "gamma2-5.png")
gamma35 = gamma_correction(scaled_image, 3.5)
gamma35 = change_scale(gamma35, 0, 1, 0, 255)
save_image(gamma35, "gamma3-5.png")