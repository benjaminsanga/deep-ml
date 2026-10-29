import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
   
    flat = np.absolute(arr.flatten())
    if norm_type == 'l1':
        return float(np.sum(flat))
    if norm_type == 'l2':
        return float(np.sqrt(np.sum([num ** 2 for num in flat])))
    if norm_type == 'linf':
        return float(flat.max())
    if norm_type == 'frobenius':
        if not (arr.ndim > 1):
            raise ValueError
        return float(np.sqrt(np.sum([num ** 2 for num in flat])))
    raise ValueError
    
