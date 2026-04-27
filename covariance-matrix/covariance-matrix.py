import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    N = X.shape[0]
    dim = X.ndim

    if (N<2 or dim !=2):
        return None
    else:
        X_centered = X - np.mean(X,axis=0,keepdims = True)
        Cov_matrix = X_centered.T@X_centered/(N-1)
        return Cov_matrix
    
    pass