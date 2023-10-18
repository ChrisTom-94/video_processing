import utils
import video_processing as vp

DIR = "results/"

exercices = [
    # question 1.1
    # (a)
    # [['course', 'neige'], [vp.background_substraction]],
    # (b)
    # [['action', 'pirate'], [vp.background_substraction]],
    # question 1.2
    # (a)
    # [['action', 'femme'], [vp.frame_differencing]],
    # (b)
    # [['course', 'neige'], [vp.frame_differencing]],
    # question 1.3
    # (a) (b)
    [['action', 'course', 'femme'], [vp.mhi]],
    # (c)
    # [['pirate'], [vp.mhi]],
    # question 1.4
    # [['homme', 'pirate'], [vp.mhi, vp.background_substraction, vp.frame_differencing]],
    # question 1.5
    # [['toupie'], [vp.mhi, vp.background_substraction, vp.frame_differencing]],
    # question 1.6
    # [['lumiere'], [vp.mhi, vp.background_substraction, vp.frame_differencing]],
]

for sequence_names, functions in exercices:
    for fn in functions:
        sequences = utils.retrieve_frames(sequence_names)
        results = utils.compareSequences(fn, sequences)
        utils.show_results(results, sequence_names, fn.__name__)
