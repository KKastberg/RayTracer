
# External imports
from dataclasses import dataclass
import numpy as np
from numpy.linalg import norm

@dataclass
class Light:
    x: int
    y: int
    z: int

    @property
    def origin(self):
        return np.array([self.x, self.y, self.z])


@dataclass
class Camera:
    x: int
    y: int
    z: int

    @property
    def origin(self):
        return np.array([self.x, self.y, self.z])

@dataclass
class Ray:
    _origin: list
    _direction: list
    _vector: list

    def __init__(self, origin, pixel_origin):
        self.origin = origin
        self.vector = pixel_origin - origin
        self.direction = self.vector / norm(self.vector)

    @property
    def origin(self):
        return np.array(self._origin)

    @origin.setter
    def origin(self, value):
        self._origin = value

    @property
    def direction(self):
        return np.array(self._direction)

    @direction.setter
    def direction(self, value):
        self._direction = value

    @property
    def vector(self):
        return self._vector

    @vector.setter
    def vector(self, value):
        self._vector = value


    @property
    def length(self):
        return norm(self.vector)


@dataclass
class Sphere:
    x: int
    y: int
    z: int
    r: int

    @property
    def origin(self):
        return np.array([self.x, self.y, self.z])

    def ray_intersection(self, ray: Ray):
        vector_w = ray.direction - self.origin
        vector_t_norm = np.dot(ray.direction, vector_w)
        point_t = ray.direction * vector_t_norm + ray.origin
        length_y = norm(point_t - self.origin)
        if length_y < self.r:
            x = np.sqrt(self.r**2 - length_y**2)
            intersection1 = (vector_t_norm - x) * ray.direction + ray.origin
            return  intersection1
        else:
            return False

@dataclass
class Screen:
    x: int
    y: int
    z: int
    width: int
    height: int

    @property
    def xspan(self):
        return np.arange(self.x, self.x + self.width, 1)

    @property
    def yspan(self):
        return np.arange(self.y, self.y + self.height, 1)
