
# External imports
from dataclasses import dataclass
import numpy as np
from numpy.linalg import norm


@dataclass
class Sphere:
    x: int
    y: int
    z: int
    r: int

    @property
    def center(self):
        return np.array([self.x, self.y, self.z])

    def ray_intersection(self, vector_d, d_origin):
        vector_w = d_origin - self.center
        vector_t_norm = np.dot(vector_d, vector_w)
        point_t = vector_d * vector_t_norm - d_origin
        length_y = norm(point_t - self.center)
        if length_y < self.r:
            x = np.sqrt(self.r**2 - length_y**2)
            intersection1 = (vector_t_norm - x) * vector_d - d_origin
            return  intersection1
        else:
            return False

@dataclass
class Camera:
    x: int
    y: int
    z: int

    @property
    def origin(self):
        return np.array([self.x, self.y, self.z])

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
