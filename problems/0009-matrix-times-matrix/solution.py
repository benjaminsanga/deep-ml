import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
    if len(a) == 0 or len(b) == 0:
        return -1
    if not (len(a[0]) == len(b)):
        return -1
    
    np_a = np.array(a)
    np_b = np.array(b)
    c = np.dot(np_a, np_b)

    return c