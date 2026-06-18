import cv2
import numpy as np

def analyze_thermal(path):

    img = cv2.imread(
        path,
        cv2.IMREAD_GRAYSCALE
    )

    mean_temp = np.mean(img)

    if mean_temp > 180:
        return "Hotspot"

    return "Normal"