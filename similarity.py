import numpy as np

def similarity_index(cosine_diffs):
    lst  = []
    for i in cosine_diffs:
        lst.append(np.pi - i)
    return lst

def similarity_matrix(vals):
    raise NotImplementedError
