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
    [['action', 'femme'], [fd.frame_differencing_average]],
    # (b)
    # ["question", ['course', 'neige'], [fd.frame_differencing_average]],
    # question 1.3
    # (a) (b)
    # ["question", ['action', 'course', 'femme'], [mhi.mhi]],
    # (c)
    # ["question", ['pirate'], [mhi.mhi]],
    # question 1.4
    # ["question", ['homme', 'pirate'], [mhi.mhi, bs.background_substraction, fd.frame_differencing_average]],
    # question 1.5
    # ["question", ['toupie'], [mhi.mhi, bs.background_substraction, fd.frame_differencing_average]],
    # question 1.6
    # ["question", ['lumiere'], [mhi.mhi, bs.background_substraction, fd.frame_differencing_average]],
]

for sequence_names, functions in exercices:
    for fn in functions:
        sequences = utils.retrieve_frames(sequence_names)
        results = utils.compareSequences(fn, sequences)
        for i in range(len(results)):
            name = sequence_names[i] + " - " + fn.__name__
            cv2.imshow(name, results[i])
            
            #if file don't exist, create it
            if not os.path.exists("./results/" + name + ".jpg"):
                cv2.imwrite("./results/" + name + ".jpg", results[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# img = utils.grayscaled_image("sequences/course/frame10.png")
# cv2.imwrite("results/course - grayscale.jpg", img)