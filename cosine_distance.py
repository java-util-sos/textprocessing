import cohere
import numpy as np
from api_keys import cohere_key

print(cohere_key)

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

def process_text(text_input):
    """
    Processes the text and returns the embeddings
    """
    co = cohere.Client(f'{cohere_key}')
    response = co.embed(
        model='large',
        texts=text_input)
    return response.embeddings
    