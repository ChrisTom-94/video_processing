import os
import cv2
import background_substraction as bs

path = 'sequences/'
frames = []

full_path = path + 'course/'

# list all files in the directory
files = os.listdir(full_path)

for file in files:
    # read the image
    img = cv2.imread(full_path + file)
    # convert to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # append to the list
    frames.append(img)

result = bs.background_substraction(frames)

cv2.imshow('result', result)
cv2.waitKey(0)

