import os
import utils
import video_processing as vp

if not os.path.exists('results'):
    os.makedirs('results')

#### Background substraction, frame differencing and MHI ####

# each element is a list with two arrays:
#   - the first array contains the names of the sequences to be compared
#   - the second array contains the functions to be applied to the sequences
comparisons = [
    [['course', 'neige'], [vp.background_substraction]],
    [['action', 'pirate'], [vp.background_substraction]],
    [['action', 'femme'], [vp.frame_differencing]],
    [['course', 'neige'], [vp.frame_differencing]],
    [['action', 'course', 'femme'], [vp.mhi]],
    [['pirate'], [vp.mhi]],
    [['diplome', 'homme'], [vp.mhi, vp.background_substraction, vp.frame_differencing]],
    [['toupie'], [vp.mhi, vp.background_substraction, vp.frame_differencing]],
    [['lumiere'], [vp.mhi, vp.background_substraction, vp.frame_differencing]],
]

# for each comparison, apply the functions to the sequences
for sequence_names, functions in comparisons:
    for fn in functions:
        sequences = utils.retrieve_frames(sequence_names)
        for sequence in sequences:
            # Apply the function to the sequence
            result = fn(sequences)
            utils.display(result, sequence_names, fn.__name__)
            utils.store(result, sequence_names, fn.__name__)


#### Optical flow and frame differencing ####

# the sequences with the corresponding frames to work with
frames = {
    "femme": ['sequences/femme/frame12.png', 'sequences/femme/frame13.png'],
    "action": ['sequences/action/seq2_008.png', 'sequences/action/seq2_009.png'],
    "course": ['sequences/course/frame9.png', 'sequences/course/frame10.png'],
    "neige": ['sequences/neige/frame14.png', 'sequences/neige/frame15.png'],
    "homme": ['sequences/homme/frame10.png', 'sequences/homme/frame11.png'],
    "lumiere": ['sequences/lumiere/frame8.png', 'sequences/lumiere/frame9.png'],
    "pirate": ['sequences/pirate/frame8.png', 'sequences/pirate/frame9.png'],
    "diplome": ['sequences/diplome/frame8.png', 'sequences/diplome/frame9.png'],
}

lk_params = dict(step=15, win_size=(21, 21), max_level=8)
for name in frames:
    path_frame_1, path_frame_1 = frames[name]
    
    frame1 = utils.grayscaled_image(path_frame_1)
    frame2 = utils.grayscaled_image(path_frame_1)

    ### optical flow ###
    points1, points2 = vp.optical_flow_LK(frame1, frame2, **lk_params)
    # points2 = utils.normalize_flow_vectors(points1, points2)
    flow_image = utils.draw_flow(frame2, points1, points2)
    utils.display(flow_image, name, 'LK')
    utils.store(flow_image, name, 'LK')

    ### frame differencing ###
    diff = utils.abs_diff(frame1, frame2)
    diff = utils.normalize(diff)
    utils.display(diff, name, 'FD')
    utils.store(diff, name, 'FD')


