from math import log
import numpy as np


def subKLDivergence(item, probQ, data):
    Px = Probability(item, data)
    kl = Px * log(Px/probQ, 10) * (-1)
    return kl


def Probability(a, data):
    count = np.count_nonzero(data == a)
    Px = count/len(data)
    return Px


def KLDivergence(selectData, allData, probQ):
    sum = 0
    for i in selectData:
        sum = subKLDivergence(i, probQ,  allData) + sum
    return sum
