import utils
import numpy as np
import cv2

def background_substraction(frames): 
    
    background = utils.compute_average_background(frames)

    [height, width] = background.shape

    result = np.zeros((height, width), dtype=np.uint8)

    for frame in frames:
        result = result + np.double(np.abs(background - frame))

    M = np.max(np.max(result))
    return np.uint8(255 * result / M)