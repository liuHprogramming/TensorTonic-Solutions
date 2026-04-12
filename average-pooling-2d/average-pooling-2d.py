import numpy as np

def average_pooling_2d(X, pool_size):
    """
    Apply 2D average pooling with non-overlapping windows.
    """
    # Write code here
    H = len(X)
    W = len(X[0])
    k = pool_size
    out_h = H // k
    out_w = W // k

    output = []

    for i in range(out_h):
        row = []
        for j in range(out_w):
            total = 0
            for m in range(k):
                for n in range(k):
                    total += X[i*k+m][j*k+n]
                    avg = total / pool_size**2

            row.append(avg)

        output.append(row)

    return output

    