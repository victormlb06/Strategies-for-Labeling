import csv
import numpy as np
from scipy.stats import entropy
from math import log, e
import pandas as pd
from ShannonEntropy import SubEntropy, totalEntropy

df = pd.read_csv("StudentsPerformance.csv")
df.head()
df.index
x = df[df.gender == "male"].groupby('gender').size()

k = x.loc['male']

print(SubEntropy(df["gender"], k, 10))
