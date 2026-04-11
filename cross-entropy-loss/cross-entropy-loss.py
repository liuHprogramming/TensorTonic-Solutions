import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    rows = np.arange(len(y_true))
    probs = y_pred[rows, y_true]
    return -np.mean(np.log(probs))
    pass