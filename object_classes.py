
# External imports
from dataclasses import dataclass
import numpy as np


@dataclass
class Sphere:
    x: int
    y: int
    r: int

@dataclass
class Camera:
    x: int
    y: int
    z: int

    @property
    def pos(self):
        return np.array([self.x, self.y, self.z])

@dataclass
class Screen:
    x: int
    y: int
    z: int
    width: int
    height: int
