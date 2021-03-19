import numpy as np
from scipy.stats import entropy
from math import log, e
import pandas as pd
import matplotlib.pyplot as plt

vector = []


def SubEntropy(data, item, base):
    Px = Probability(item, data)
    H = (Px * log(Px, base)) * (-1)
    return H


def Probability(a, data):
    count = np.count_nonzero(data == a)
    Px = count/len(data)
    return Px


def totalEntropy(data, data2):
    sum = 0
    for a in data:
        sum = SubEntropy(data2, a, 10) + sum
    return sum
