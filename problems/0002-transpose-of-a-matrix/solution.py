def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    if len(a) == 0:
        return -1
    # result = [[0] * len(a)] * len(a[0])
    result = []
    for row_item_index in range(len(a[0])):
        result.append([row[row_item_index] for row in a])
    
    return result