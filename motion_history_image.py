import cv2
import numpy as np

def mhi(sequence):
    tau = len(sequence)

    rows, cols = sequence[0].shape
    MHI = np.zeros((rows, cols))
    prev_frame = sequence[0]

    for frame in sequence:
        diff = cv2.absdiff(frame, prev_frame)
        ret, diff = cv2.threshold(diff, tau, 1, cv2.THRESH_BINARY)
        MHI += diff
        prev_frame = frame

    M = np.max(np.max(MHI))
    return np.uint8(255 * MHI / M)