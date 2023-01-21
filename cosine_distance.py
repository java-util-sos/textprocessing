import cohere
import numpy as np

def get_angle(a, b):
    """
    Gets the distance between vector a and b
    """

    ab_dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    cos_theta = ab_dot/(norm_a * norm_b)

    theta = np.arccos(cos_theta)
    return theta
