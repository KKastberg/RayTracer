
# External imports
import itertools
import matplotlib.pyplot as plt


# Internal imports
import numpy as np

from scene_objects import objects, screen, camera

def main():

    # Generate a black image
    image = np.zeros((screen.height, screen.width, 3))

    # Loop through every coordinate on the screen
    for x, y in itertools.product(range(screen.width), range(screen.height)):
        print(x,y)

    # Display the image
    plt.imshow(image, interpolation='nearest')
    plt.show()


if __name__ == '__main__':
    main()