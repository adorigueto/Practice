import pandas as pd
import numpy as np

def class_grades(students):
    """
    :param students: (list) Each element of the list is another list with the 
      following elements: Student name (string), class name (string), student grade (int).
    :returns: (list) Each element is a list with the following 
      elements: Class name (string), median grade for students in the class (float).
    """
    df = pd.DataFrame(students, columns=['name', 'class', 'grade'])
    cat = pd.Categorical(df['class'])
    codes, uniques = pd.factorize(cat)
    result = [[uniques[0], df['grade'].groupby(df['class']).mean()[0].round()], uniques[1], df['grade'].groupby(df['class']).mean()[1].round()]
    return result

students = [["Ana Stevens", "1a", 5], ["Mark Stevens", "1a", 4], ["Jon Jones", "1b", 2], ["Bob Kent", "1c", 4]]
print(class_grades(students))

df = pd.DataFrame(students, columns=['name', 'class', 'grade'])
cat = pd.Categorical(df['class'])
codes, uniques = pd.factorize(cat)
result = [[uniques[0], df['grade'].groupby(df['class']).mean()[0].round()], uniques[1], df['grade'].groupby(df['class']).mean()[1].round()]
result

i = 0
result = []
while i in range(len(uniques)):
    print([uniques[i], df['grade'].groupby(df['class']).mean()[i].round()])
    i = i +1


for i in range(uniques):
    result_partial = [uniques[i], df['grade'].groupby(df['class']).mean()[i].round()]
    result




