import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix
from mlxtend.plotting import plot_decision_regions

df = sns.load_dataset('iris')
df.loc[0, 'sepal_length'] = None
sns.scatterplot(x='petal_length', y='petal_width', data=df, hue='species', style='species', s=80)
# plt.show()

# print(df.describe())
# print(df.head(4))
# print(df.isnull().sum())

y, class_names = pd.factorize(df.species, sort=True)
# print(class_names, '\n')
# print(y[40:60])
# print(pd.unique(y), '\n')

X = df.drop('species', axis=1)
# print(X.head())

sc = StandardScaler()
X_sc = sc.fit_transform(X)
# print(X_sc[:5])

X_train, X_test, y_train, y_test = train_test_split(X_sc, y, test_size=0.25, random_state=1)
# print(len(X_train), len(X_test))

model = MLPClassifier(hidden_layer_sizes=(4), max_iter=2000, random_state=1)
model.fit(X_train, y_train)




