from math import log


def subKLDivergence(Px, data):
    Pq = len(data)
    Px = Px/Pq
    kl = Px * log(Px, 10)
    return kl


def KLDivergence(data):
    for i in range(len(data)):
        sum = subKLDivergence(i, data) + sum
    return sum
