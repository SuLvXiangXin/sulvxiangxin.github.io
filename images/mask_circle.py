import cv2
import numpy as np


def extract_circle(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read image.")
        return

    center_x, center_y = image.shape[1] // 2, image.shape[0] // 2
    radius = min(center_x, center_y)

    mask = np.zeros_like(image)
    cv2.circle(mask, (center_x, center_y), radius, (255, 255, 255), -1)

    result = np.where(mask == np.array([255, 255, 255]), image, 255)

    cv2.imwrite("photo_circle.jpg", result)

extract_circle('photo.jpg')
