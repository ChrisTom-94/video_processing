import numpy as np
import utils
import cv2


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


def optical_flow_LK(frame1, frame2, **kwargs):
    if len(frame1.shape) == 3:
        frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    step = kwargs.get('step', 10)
    win_size = kwargs.get('win_size', (15, 15))
    max_level = kwargs.get('max_level', 2)

    # Define a grid of points to track
    h, w = frame1.shape
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2, -1).astype(np.float32)
    points1 = np.array([x, y]).T

    # Use Lucas-Kanade optical flow method to track the grid points
    lk_params = dict(winSize=win_size, maxLevel=max_level, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.3e-6))
    points2, status, err = cv2.calcOpticalFlowPyrLK(frame1, frame2, points1, None, **lk_params)
    
    return points1, points2
    