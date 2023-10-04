import os
import cv2
import utils
import background_substraction as bs
import frame_differencing as fd
import motion_history_image as mhi

path = 'sequences/'

full_path = path + 'action/'

# list all files in the directory
files = os.listdir(full_path)

frames = [utils.grayscaled_image(full_path + file) for file in files]

functions = [bs.background_substraction, fd.frame_differencing_average, mhi.mhi]

results = [function(frames) for function in functions]

for i in range(len(results)):
    cv2.imshow('result', results[i])
    cv2.setWindowTitle('result', functions[i].__name__)

cv2.waitKey(0)



