import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix:
        return []
    
    means = np.mean(matrix, axis=1 if mode == 'row' else 0)
    return means