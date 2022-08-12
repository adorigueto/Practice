import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


df = pd.read_csv('data1.csv')
columns=['q1', 'q2', 'label']
df1 = df.rename(columns={'Years of experience?': columns[0], 'Manager at previous position?': columns[1], 'Passed hiring process?': columns[2]})
cat_q2 = pd.Categorical(df1['q2'])
codes_1, uniques_1 = pd.factorize(cat_q2)
cat_label = pd.Categorical(df1['label'])
codes_2, uniques_2 = pd.factorize(cat_label)
df1.drop(['q2', 'label'], axis=1, inplace=True)
df1['q2'] = codes_1
df1['label'] = codes_2
df1

X = df1[['q1', 'q2']]
y = df1[['label']]
y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
clf = DecisionTreeClassifier(max_depth=2)
clf.fit(X_train, y_train)
clf.score(X, y)

