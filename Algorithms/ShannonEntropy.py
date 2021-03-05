import numpy as np
from scipy.stats import entropy
from math import log, e
import pandas as pd
import matplotlib.pyplot as plt

vector = []


def entropy2(data, base=10):
    """ Computes entropy of label distribution. """
    n_data = len(data)

    if n_data <= 1:
        return 0

    counts = np.unique(data, return_counts=True)
    probs = counts / n_data
    n_classes = np.count_nonzero(probs)

    if n_classes <= 1:
        return 0

    ent = 0.

    # Compute entropy

    base = e if base is None else base
    for i in probs:
        x = i*log(i, base)*(-1)
        vector.append(x)

    for i in probs:
        ent -= i * log(i, base)

    return ent


def entropy4(data, base=10):  # Total Entropy #
    counts = np.unique(data, return_counts=True)
    print(counts)
    norm_counts = counts / counts.sum()
    print(norm_counts)
    base = e if base is None else base
    return -(norm_counts * np.log(norm_counts)/np.log(base)).sum()


data = [0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4]
data2 = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 4]
print(entropy2(data))
print(entropy4(data))
