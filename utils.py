import numpy as np

def compute_average_background(frames):
    average_background = np.zeros(frames[0].shape, dtype=np.double)

    np.add.reduce(frames, out=average_background)

    return average_background / len(frames)
