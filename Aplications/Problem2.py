import csv
import numpy as np
from scipy.stats import entropy
from math import log, e
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
df.head()
