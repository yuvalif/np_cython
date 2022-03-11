import numpy as np
cimport numpy as np

# multiply square matrix
def compute(m1, m2):
    order = m1.shape[0]

    assert m1.shape[0] == m1.shape[1]
    assert m1.shape == m2.shape

    result = np.zeros((order, order))

    for x in range(order):
        for y in range(order):
            result[x, y] += m1[x, y] * m2[y, x] 

    return result

