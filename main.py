#!/usr/bin/env python3
# main.py

# External imports
import itertools
import matplotlib.pyplot as plt
import numpy as np

# Internal imports
from scene_objects import objects, screen, camera
from utils import *

def main():

    # Generate a black image
    image = np.zeros((screen.height, screen.width, 3))

    # Loop through every coordinate on the screen
    z = screen.z
    for x, y in itertools.product(screen.xspan, screen.yspan):
        pixel_origin = np.array([x,y,z])

        direction_vector = normalize(pixel_origin - camera.origin)
        print(x,y,z)


    # Display the image
    plt.imshow(image, interpolation='nearest')
    plt.show()


if __name__ == '__main__':
    main()
