# utils.py

# External imports
from numpy.linalg import norm

# Normalize vector
def normalize(vector):
    return vector/norm(vector)