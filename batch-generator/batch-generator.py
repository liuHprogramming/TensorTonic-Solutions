import numpy as np

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    """
    Randomly shuffle a dataset and yield mini-batches (X_batch, y_batch).
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    N=X.shape[0]
    indices = np.arange(N)

    if rng is not None:
        rng.shuffle(indices)
    else:
        np.random.shuffle(indices)

    X_shuffled = X[indices]
    y_shuffled = y[indices]

    for start in range(0,N,batch_size):
        end = start+batch_size

        if drop_last and end>N:
            break

        yield X_shuffled[start:end], y_shuffled[start:end]
    pass