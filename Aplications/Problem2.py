import csv
import numpy as np
from scipy.stats import entropy
from math import log, e
import matplotlib.pyplot as plt
import pandas as pd
from KLDivergence import subKLDivergence, KLDivergence, Probability

df = pd.read_csv("StudentsPerformance.csv")


def Personalized(data, category):
    vector = []
    y = np.unique(df[category])
    for i in y:
        vector.append(i)
    return vector


def selectCategoryU(category):
    return len(Personalized(df[category], category))


def selectCategory(category):
    return Personalized(df[category], category)


print(KLDivergence(selectCategory("math score"),
                   df["math score"], selectCategoryU("math score")))


def Graphic(data):
    vector = []
    vector2 = []
    selectCategoryU("math score")
    for a in selectCategory("math score"):
        vector2.append(a)
        vector.append(subKLDivergence(
            a, selectCategoryU("math score"), df["math score"]))
    return vector, vector2


vector, vector2 = Graphic("math score")


#xpoints = np.array(selectCategory("math score"))
#ypoints = np.array([vector])

plt.plot(vector2, vector)
plt.xlabel('Individuos', fontsize=18)
plt.ylabel('KL divergence', fontsize=18)
plt.show()
