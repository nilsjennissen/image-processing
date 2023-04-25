#  Script to convert a colour image to greyscale

import numpy as np
import matplotlib.pyplot as plt
import pathlib

#%%
# Convert all images in image folder to individual greyscale images with name suffix grey
images = pathlib.Path('images').glob('*.jpg')
def convert_to_gray(image):
    # Y = red * 0.3 + green * 0.59 + blue * 0.11
    red = image[:,:,0]
    green = image[:,:,1]
    blue = image[:,:,2]
    Y = red * 0.3 + green * 0.59 + blue * 0.11
    return Y

for image in images:
    img = plt.imread(image)
    gray = convert_to_gray(img)
    plt.imsave('images/grey_' + image.name, gray, cmap='gray')
