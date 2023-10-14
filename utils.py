import numpy as np
import cv2
import os

DIR = 'sequences/'

def compute_average_background(frames):
    average_background = np.zeros(frames[0].shape, dtype=np.double)

    np.add.reduce(frames, out=average_background)

    return average_background / len(frames)

def frames_difference(frame1, frame2):
    return cv2.absdiff(frame2, frame1)

def grayscaled_image(path):
    return cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2GRAY)

def id_generator():
    i = 0
    while True:
        yield i
        i += 1

def retrieve_frames(paths):
    return [[grayscaled_image(full_path + '/' + file) for file in files] 
                for full_path, _, files in os.walk(DIR) 
                    if len(files) > 0 and full_path.split('/')[-1] in paths]

def compareSequences(fn, sequences, sequence_names):
    results = [fn(sequence) for sequence in sequences]

    for i in range(len(results)):
        cv2.imshow(sequence_names[i], results[i])