import numpy as np
import cv2


def frame_differencing_average(frames):
    avg = np.zeros(frames[0].shape, dtype=np.double)
    last_frame = frames[0]
    for frame in frames[1:]:
        avg += np.double(cv2.absdiff(last_frame, frame))
        last_frame = frame

    M = np.max(np.max(avg))
    return np.uint8(255 * avg / M)