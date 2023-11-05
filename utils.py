import numpy as np
import cv2
import os
import re

DIR = 'sequences/'

def abs_diff(frame1, frame2):
    return np.double(cv2.absdiff(frame1, frame2))

def normalize(input):
    M = np.max(np.max(input))
    return np.uint8(255 * input / M)

def compute_average_background(frames):
    average_background = np.zeros(frames[0].shape, dtype=np.double)
    np.add.reduce(frames, out=average_background)
    return average_background / len(frames)

def grayscaled_image(path):
    return cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2GRAY)

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

def retrieve_frames(paths):
    return [np.array([grayscaled_image(full_path + '/' + file) for file in sorted_alphanumeric(files)]) 
                for full_path, _, files in os.walk(DIR) 
                    if len(files) > 0 and full_path.split('/')[-1] in paths]

def display(result, sequence_name, fn_name):
    name = sequence_name + "-" + fn_name
    cv2.imshow(name, result)
    cv2.waitKey(0)

def store(result, sequence_name, fn_name):
        name = sequence_name + "-" + fn_name
        cv2.imwrite("./results/" + name + ".jpg", result)

def draw_flow(img, points1, points2, vector_color=(255, 200, 0)):
    vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    for i, (new, old) in enumerate(zip(points2, points1)):
        a, b = map(int, new.ravel())
        c, d = map(int, old.ravel())
        vis = cv2.arrowedLine(vis, (c, d), (a, b), vector_color, 2, tipLength=0.2)
        
    return vis


def normalize_flow_vectors(points1, points2, max_len=10):
    displacements = np.abs(points2 - points1)
    magnitudes = np.sqrt((displacements**2).sum(axis=1))
    normalized_displacements = displacements / (magnitudes[..., np.newaxis] + 1e-10) * max_len
    return points1 + normalized_displacements
