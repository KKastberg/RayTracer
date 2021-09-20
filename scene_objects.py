import numpy as np
from object_classes import *

objects = [
    Sphere(x=0, y=-1, z=8, r=3)
]

lights = [
    Light(x=0, y=100, z=0)
]

camera = Camera(x=0, y=0, z=0)
screen = Screen(x=0, y=0, z=4, width=1, height=1)



if __name__ == '__main__':
    s = objects[0]

    i = s.ray_intersection(np.array([1,0,0]), np.array([-5,0,0]))
    print(i)

