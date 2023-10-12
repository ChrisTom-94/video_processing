import utils

import background_substraction as bs
import frame_differencing as fd
import motion_history_image as mhi


# question 1.1
paths = ['course', 'neige']
sequences = utils.retrieve_frames(paths)
utils.compare(bs.background_substraction, sequences, paths)
currents = ['pirate', 'action']
sequences = utils.retrieve_frames(currents)
utils.compare(bs.background_substraction, sequences, currents)

# question 1.2
# utils.compare(fd.frame_differencing, sequences, currents)