import numpy as np
from object_classes import *

objects = [
    Sphere(x=0, y=1, z=0, r=2)
]

camera = Camera(x=0, y=0, z=-1)
screen = Screen(x=20, y=40, z=0, width=300, height=200)



if __name__ == '__main__':
    s = objects[0]

    i = s.ray_intersection(np.array([1,0,0]), np.array([-5,0,0]))
    print(i)

