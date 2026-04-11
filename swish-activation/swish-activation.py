import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.array(x)
    x_sigmoid = 1/ (1+np.exp(-x))
    return x*x_sigmoid
    
    pass