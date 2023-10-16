import os
import cv2

import utils
import background_substraction as bs
import frame_differencing as fd
import motion_history_image as mhi

DIR = "results/"

exercices = [
    # question 1.1
    # (a)
    # [['course', 'neige'], [bs.background_substraction]],
    # (b)
    # [['action', 'pirate'], [bs.background_substraction]],
    # question 1.2
    # (a)
    # [['action', 'femme'], [fd.frame_differencing_average]],
    # (b)
    # [['course', 'neige'], [fd.frame_differencing_average]],
    # question 1.3
    # (a) (b)
    [['action', 'course', 'femme'], [mhi.mhi]],
    # (c)
    # [['pirate'], [mhi.mhi]],
    # question 1.4
    # [['homme', 'pirate'], [mhi.mhi, bs.background_substraction, fd.frame_differencing_average]],
    # question 1.5
    # [['toupie'], [mhi.mhi, bs.background_substraction, fd.frame_differencing_average]],
    # question 1.6
    # [['lumiere'], [mhi.mhi, bs.background_substraction, fd.frame_differencing_average]],
]

for sequence_names, functions in exercices:
    for fn in functions:
        sequences = utils.retrieve_frames(sequence_names)
        results = utils.compareSequences(fn, sequences)
        utils.show_results(results, sequence_names, fn.__name__)

# img = utils.grayscaled_image("sequences/course/frame10.png")
# cv2.imwrite("results/course - grayscale.jpg", img)