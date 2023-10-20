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

def display(results, sequence_names, fn_name):
    for i in range(len(results)):
        name = sequence_names[i] + " - " + fn_name
        cv2.imshow(name, results[i])
        
        if not os.path.exists("./results/" + name + ".jpg"):
            cv2.imwrite("./results/" + name + ".jpg", results[i])
    cv2.waitKey(0)
    cv2.destroyAllWindows()