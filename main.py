#!/usr/bin/env python3
# main.py

# External imports
import itertools
import matplotlib.pyplot as plt
import numpy as np

# Internal imports
from scene_objects import *
from utils import *


def closest_intersection(ray_vector:Ray, objects:[]):
    shortest_distance = None
    closest_object = None
    for object in objects:
        intersection = object.ray_intersection(ray_vector)
        distance = norm(intersection - ray_vector.origin)
        if not shortest_distance or distance < shortest_distance:
            closest_object = object
            shortest_distance = distance
    if closest_object:
        return closest_object, shortest_distance, intersection
    else:
        return None, None, None



def main():

    # Generate a black image
    image = np.zeros((screen.height, screen.width, 3))

    # Loop through every coordinate on the screen
    z = screen.z
    for x, y in itertools.product(screen.xspan, screen.yspan):
        # Calculate ray vector
        ray_vector = Ray(camera.origin, np.array([x,y,z]))

        # Look for first intersection
        closest_object, distance, intersection = closest_intersection(ray_vector, objects)

        if intersection:
            pass

        # Create ray aiming for the light source
        object_normal = normalize(intersection - closest_object.origin)
        offset_origin = intersection + object_normal * 1e-5
        light_source_ray = Ray(offset_origin, lights[0].origin)

        # Check if anything blocks the light source ray
        _, distance, _ = closest_intersection(light_source_ray, objects)
        shadowed = distance < light_source_ray.length

        if shadowed:
            continue


        print(closest_object, distance, intersection)
        print(x,y,z)


    # Display the image
    plt.imshow(image, interpolation='nearest')
    plt.show()


if __name__ == '__main__':
    main()
