import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    dp = float(np.dot(np.array(a), np.array(b)))
    print(dp)
    aNorm = float(np.linalg.norm(a))
    print(aNorm)
    bNorm = float(np.linalg.norm(b))
    print(bNorm)

    e = .000000001
    return float(dp/((aNorm * bNorm) + e))
