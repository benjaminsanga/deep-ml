import numpy as np

def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    if not samples:
        return []
    
    vals, counts = np.unique(samples, return_counts=True)
    return list((val, counts[idx] / len(samples)) for idx, val in enumerate(vals))
