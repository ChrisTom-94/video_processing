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


def mhi(frames, tau=None, threshold=40):
    tau = len(frames) if tau is None else tau
    MHI = np.zeros_like(frames[0], dtype=np.double)

    for i in range(1, len(frames)):
        diff = utils.abs_diff(frames[i], frames[i-1])
        
        MHI[diff > threshold] = tau
        MHI[diff <= threshold] = np.maximum(0, MHI[diff <= threshold] - 1)

    return utils.normalize(MHI)