import numpy as np
import utils


def frame_differencing_average(frames):
    # print(frames[0].shape)
    avg = np.zeros(frames[0].shape, dtype=np.double)
    print(avg.shape)
    last_frame = frames[0]
    for frame in frames[1:]:
        avg += np.double(utils.frames_difference(last_frame, frame))
        last_frame = frame

    M = np.max(np.max(avg))
    return np.uint8(255 * avg / M)