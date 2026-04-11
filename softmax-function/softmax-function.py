import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    x_max = np.max(x, axis=x.ndim-1, keepdims=True)
    return np.exp(x-x_max)/np.sum(np.exp(x-x_max), axis=x.ndim-1,
    keepdims=True)
    pass