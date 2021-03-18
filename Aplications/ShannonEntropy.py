import numpy as np
from scipy.stats import entropy
from math import log, e
import pandas as pd
import matplotlib.pyplot as plt

vector = []


def SubEntropy(data, Px, base):
    Px = Px/len(data)
    H = (Px * log(Px, base)) * (-1)
    return H


def totalEntropy(data, data2):
    a = len(data2)
    sum = 0
    for a in data2:
        sum = SubEntropy(data, a, 10) + sum
    return sum
