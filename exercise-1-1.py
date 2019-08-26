import numpy as np
import cv2

image = cv2.imread('../baboon.png')

negative_baboon = np.subtract(255, image)

cv2.imwrite('1-1-negative-baboon.png', negative_baboon, [int(cv2.IMWRITE_PNG_COMPRESSION), 100])

print(image.max())
transformed_baboon = np.add(np.multiply(image, (100/255)), 100).astype(np.uint8)
print(transformed_baboon)
cv2.imwrite('1-2-transformed-baboon.png', transformed_baboon, [int(cv2.IMWRITE_PNG_COMPRESSION), 100])

