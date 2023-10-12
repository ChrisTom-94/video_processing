import utils
import numpy as np

def background_substraction(frames): 
    background = utils.compute_average_background(frames)

    result = np.zeros(frames[0].shape, dtype=np.double)
    for frame in frames:
        result += np.double(np.abs(background - frame))

    M = np.max(np.max(result))
    return np.uint8(255 * result / M)