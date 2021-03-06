import csv
import numpy as np
from scipy.stats import entropy
from math import log, e
import pandas as pd

gender = []
race_ethnicity = []
education_level = []
lunch = []
test_preparation = []
math_score = []
reading_score = []
writing_score = []


with open('StudentsPerformance.csv') as archive:
    next(archive)

    # 2. ler a tabela
    table = csv.reader(archive, delimiter=',')

    # 3. navegar pela tabela
    for l in table:
        gender.append(l[0])
        race_ethnicity.append(l[1])
        education_level.append(l[2])
        lunch.append(l[3])
        test_preparation.append(l[4])
        math_score.append(l[5])
        reading_score.append(l[6])
        writing_score.append(l[7])


def SubEntropy(data, Px, base):
    Px = Px/len(data)
    H = (Px * log(Px, base)) * (-1)
    return H


def frequencyDataSeparation(data):
    aux = []
    qtd = len(data)
    var = isinstance(data[1], str)
    if var:
        for qtd in data:
            if aux:
                y = len(aux)
                cont = 0
                for y in aux:
                    if qtd == y:
                        cont = cont+1
                if cont == 0:
                    aux.append(qtd)
            if not aux:
                aux.append(qtd)
    return aux


def totalEntropy(data, data2):
    a = len(data2)
    b = len(data)
    sum = 0
    for a in data2:
        sum = SubEntropy(data, StructedData(data, a), 10) + sum
    return sum


def StructedData(data, x):
    i = 0
    counts = len(data)
    for counts in data:
        if counts == x:
            i = i+1
    return i


print(SubEntropy(gender, StructedData(gender, 'male'), 10))
print(SubEntropy(gender, StructedData(gender, 'female'), 10))
print(totalEntropy(math_score, frequencyDataSeparation(math_score)))
