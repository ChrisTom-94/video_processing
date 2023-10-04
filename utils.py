import numpy as np
import cv2

def compute_average_background(frames):
    average_background = np.zeros(frames[0].shape, dtype=np.double)

    np.add.reduce(frames, out=average_background)

    return average_background / len(frames)

def grayscaled_image(path):
    return cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2GRAY)
