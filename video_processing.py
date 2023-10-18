import numpy as np
import utils

def background_substraction(frames): 
    background = np.array(utils.compute_average_background(frames))
    result = np.sum(np.abs(frames - background), axis=0)
    return utils.normalize(result)

def frame_differencing(frames):
    diffs = np.double(utils.abs_diff(frames[:-1], frames[1:]))
    result = np.sum(diffs, axis=0)
    return utils.normalize(result)

def mhi(frames, tau = None):
    tau = len(frames) if tau is None else tau
    frames_array = np.stack(frames, axis=-1)
    diffs = utils.abs_diff(frames_array[:, :, 1:], frames_array[:, :, :-1])
    thresh_diffs = np.where(diffs >= tau, 1, 0)

    MHI = np.cumsum(thresh_diffs, axis=-1)
    MHI = MHI[:, :, -1]  # Take the last slice
    return utils.normalize(MHI)