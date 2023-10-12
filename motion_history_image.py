import cv2
import numpy as np
import utils

def mhi(frames):
    tau = len(frames)

    rows, cols = frames[0].shape
    MHI = np.zeros((rows, cols))
    prev_frame = frames[0]

    for frame in frames:
        diff = utils.frames_difference(prev_frame, frame)
        ret, diff = cv2.threshold(diff, tau, 1, cv2.THRESH_BINARY)
        MHI += diff
        prev_frame = frame

    M = np.max(np.max(MHI))
    return np.uint8(255 * MHI / M)