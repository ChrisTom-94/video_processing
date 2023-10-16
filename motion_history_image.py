import cv2
import numpy as np

def mhi(frames, tau = None):
    tau = len(frames) if tau is None else tau

    frames_array = np.stack(frames, axis=-1)

    diffs = cv2.absdiff(frames_array[:, :, 1:], frames_array[:, :, :-1])
    thresh_diffs = np.where(diffs >= tau, 1, 0)

    MHI = np.cumsum(thresh_diffs, axis=-1)
    MHI = MHI[:, :, -1]  # Take the last slice

    # Normalize
    M = np.max(MHI)
    return np.uint8(255 * MHI / M)