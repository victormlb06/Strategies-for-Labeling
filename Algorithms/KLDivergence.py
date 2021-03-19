from math import log
import numpy as np


def subKLDivergence(Px, data):
    Pq = len(data)
    Px = Px/Pq
    kl = Px * log(Px, 10)
    return kl


def Probability(a, data):
    count = np.count_nonzero(data == a)
    Px = count/len(data)
    return Px


def KLDivergence(data):
    for i in range(len(data)):
        sum = subKLDivergence(i, data) + sum
    return sum
