import numpy as np
import cv2
import os

DIR = 'sequences/'

def abs_diff(frame1, frame2):
    return np.double(cv2.absdiff(frame1, frame2))

def normalize(input):
    M = np.max(input)
    return np.uint8(255 * input / M)

def compute_average_background(frames):
    average_background = np.zeros(frames[0].shape, dtype=np.double)
    np.add.reduce(frames, out=average_background)
    return average_background / len(frames)

def grayscaled_image(path):
    return cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2GRAY)

def retrieve_frames(paths):
    return [[grayscaled_image(full_path + '/' + file) for file in files] 
                for full_path, _, files in os.walk(DIR) 
                    if len(files) > 0 and full_path.split('/')[-1] in paths]

def compareSequences(fn, sequences):
    return [fn(np.array(sequence)) for sequence in sequences]

def show_results(results, sequence_names, fn_name):
    for i in range(len(results)):
        name = sequence_names[i] + " - " + fn_name
        cv2.imshow(name, results[i])
        
        #if file don't exist, create it
        if not os.path.exists("./results/" + name + ".jpg"):
            cv2.imwrite("./results/" + name + ".jpg", results[i])
    cv2.waitKey(0)
    cv2.destroyAllWindows()