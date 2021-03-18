import csv
import numpy as np
from scipy.stats import entropy
from math import log, e
import pandas as pd
from ShannonEntropy import SubEntropy, totalEntropy, Probabilite

df = pd.read_csv("StudentsPerformance.csv")
df.head()
df.index
x = df[df.gender == "male"].groupby('gender').size()
k = x.loc['male']


def Personalized(data, category):
    vector = []
    y = np.unique(df[category])
    for i in y:
        vector.append(i)
    return vector


# print(len(df["gender"]))


print(SubEntropy(df["gender"], 'female', 10))
print(totalEntropy(Personalized(
    df["math score"], "math score"), df["math score"]))
