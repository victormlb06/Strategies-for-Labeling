import csv
import numpy as np

gender = []
race_ethnicity = []
education_level = []
lunch = []
test_preparation = []
math_score = []
reading_score = []
writing_score = []

with open('StudentsPerformance.csv') as archive:

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

print(len(gender))


def StructedData(data, x):
    i = 0
    counts = len(data)
    for counts in data:
        if counts == x:
            i = i+1
    return i


print(StructedData(gender, 'male'))
