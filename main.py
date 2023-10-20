import utils
import video_processing as vp

DIR = "results/"

comparisons = [
    [['course', 'neige'], [vp.background_substraction]],
    # [['action', 'pirate'], [vp.background_substraction]],
    # [['action', 'femme'], [vp.frame_differencing]],
    # [['course', 'neige'], [vp.frame_differencing]],
    # [['action', 'course', 'femme'], [vp.mhi]],
    # [['pirate'], [vp.mhi]],
    # [['homme', 'pirate'], [vp.mhi, vp.background_substraction, vp.frame_differencing]],
    # [['toupie'], [vp.mhi, vp.background_substraction, vp.frame_differencing]],
    # [['lumiere'], [vp.mhi, vp.background_substraction, vp.frame_differencing]],
]

for sequence_names, functions in comparisons:
    for fn in functions:
        sequences = utils.retrieve_frames(sequence_names)
        results = [fn(sequence) for sequence in sequences]
        utils.display(results, sequence_names, fn.__name__)
