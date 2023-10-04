import os
import cv2
# import background_substraction as bs
# import frame_differencing as fd
import motion_history_image as mhi

path = 'sequences/'

full_path = path + 'action/'

# list all files in the directory
files = os.listdir(full_path)

def grayscaled_image(file):
    return cv2.cvtColor(cv2.imread(full_path + file), cv2.COLOR_BGR2GRAY)

frames = [grayscaled_image(file) for file in files]

# result = bs.background_substraction(frames)
# result = fd.frame_differencing_average(frames)
result = mhi.mhi(frames)

cv2.imshow('result', result)
cv2.waitKey(0)



