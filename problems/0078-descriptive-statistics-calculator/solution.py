import numpy as np
from scipy import stats

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    mean = np.mean(data, dtype=float)
    median = np.median(data)
    vals, counts = np.unique(data, return_counts=True)
    mode = int(vals[np.argmax(counts)])
    # mode = stats.mode(data)
    variance = np.var(data, dtype=float)
    # std = np.sqrt(variance, dtype=float)
    std = np.std(data, dtype=float)
    p25, p50, p75 = (float(v) for v in np.percentile(data, [25, 50, 75]))
    iqr = float(p75 - p25)
    return {
        'mean': mean, 
        'median': median, 
        'mode': mode, 
        'variance': variance, 
        'standard_deviation': std, 
        '25th_percentile': p25, 
        '50th_percentile': p50, 
        '75th_percentile': p75, 
        'interquartile_range': iqr
    }
