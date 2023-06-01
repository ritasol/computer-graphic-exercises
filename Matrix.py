import numpy as np
def show_determinant(A):
    determinant = A[0,0:1] * A[1,1:2] - A[0,1:] * A[1,0:1]
    return determinant

def decompose_matrices(arr):
    U,D,VT = np.linalg.svd(arr)

    return U,D,VT
