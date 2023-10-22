import cv2

import utils
import video_processing as vp

DIR = "results/"

comparisons = [
    # [['course', 'neige'], [vp.background_substraction]],
    # [['action', 'pirate'], [vp.background_substraction]],
    # [['action', 'femme'], [vp.frame_differencing]],
    # [['course', 'neige'], [vp.frame_differencing]],
    # [['action', 'course', 'femme'], [vp.mhi]],
    # [['pirate'], [vp.mhi]],
    # [['homme', 'pirate'], [vp.mhi, vp.background_substraction, vp.frame_differencing]],
    # [['toupie'], [vp.mhi, vp.background_substraction, vp.frame_differencing]],
    # [['lumiere'], [vp.mhi, vp.background_substraction, vp.frame_differencing]],
]

# for sequence_names, functions in comparisons:
#     for fn in functions:
#         sequences = utils.retrieve_frames(sequence_names)
#         results = [fn(sequence) for sequence in sequences]
#         utils.display(results, sequence_names, fn.__name__)


frame1 = utils.grayscaled_image('sequences/femme/frame5.png')
frame2 = utils.grayscaled_image('sequences/femme/frame6.png')

params = dict(step=20, win_size=(21, 21), max_level=2)
points1, points2 = vp.optical_flow_LK(frame1, frame2, **params)
points2 = utils.normalize_flow_vectors(points1, points2)
flow_image = utils.draw_flow(frame2, points1, points2)
cv2.imshow('Optical flow', flow_image)
cv2.waitKey(0)



