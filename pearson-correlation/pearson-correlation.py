import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    X_centered = X - np.mean(X, axis=0, keepdims=True)
    N = X.shape[0]
    Cov = (X_centered.T@X_centered)/(N-1)
    
    std = np.sqrt(np.diag(Cov))
    denom = np.outer(std, std)

    return Cov/denom

    pass