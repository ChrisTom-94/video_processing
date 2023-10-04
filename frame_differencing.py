import cv2
import numpy as np

def frame_differencing(frame1, frame2):
    return cv2.absdiff(frame1, frame2)


def frame_differencing_average(sequence):
    avg = np.zeros(sequence[0].shape, dtype=np.double)
    last_frame = sequence[0]
    for frame in list(sequence)[1:]:
        avg += np.double(frame_differencing(frame, last_frame))
        last_frame = frame

    M = np.max(np.max(avg))
    return np.uint8(255 * avg / M)