import numpy as np
cimport numpy as np

# multiply square matrix
def compute(double[:,:] m1, double[:,:] m2):
    cdef Py_ssize_t order = m1.shape[0]

    result = np.zeros((order, order), dtype=np.double)

    cdef double[:,:] result_view = result

    cdef Py_ssize_t x, y

    for x in range(order):
        for y in range(order):
            result_view[x, y] += m1[x, y] * m2[y, x] 

    return result

