import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here
    y = np.asarray(y, dtype=int)
    
    if y.ndim != 1:
        return None

    if num_classes is None:
        num_classes = np.max(y) + 1

    if np.any(y>=num_classes) or np.any(y<0):
        return None

    N = y.shape[0]

    Y = np.zeros((N, num_classes), dtype = float)
    Y[np.arange(N), y] = 1

    return Y
    pass