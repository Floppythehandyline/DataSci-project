import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')
# print(df.head())
# print(df.sample(5),'\n')

# print(df.isnull().sum(),'\n')
# print(pd.unique(df.species),'\n')

y, class_names = pd.factorize(df.species, sort=True)
# print(class_names, '\n')
#print(y[:5])
# print(y[40:60])
# print(pd.unique(y), '\n')

sns.scatterplot(x='petal_length', y='petal_width', data=df, hue='species', style='species')
# sns.pairplot(df, hue='species')
# plt.show()

X = df.drop('species', axis=1)
# print(X.head())

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_sc = sc.fit_transform(X)
# print(X_sc[:5])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_sc, y, test_size=0.25, random_state=1)
# print(len(X_train), len(X_test))

from sklearn.neural_network import MLPClassifier
# hidden = 30
# iter = 2500
model = MLPClassifier(hidden_layer_sizes=(4), max_iter=2000, random_state=1)
model.fit(X_train, y_train)

from sklearn.metrics import classification_report, confusion_matrix
y_predict = model.predict(X_test)
# print('Score: {:.4f}'.format(model.score(X_test, y_test)))
# print(classification_report(y_test, y_predict, target_names=class_names))
# print(confusion_matrix(y_test, y_predict),'\n')

# print([coef.shape for coef in model.coefs_])

X_new = [[5.1,3.5,3.4,1.4]]
X_new = [[6.1,3.,3.9,1.6]]

X_new_sc = sc.transform(X_new)
# print(X_new_sc)

y_pred = model.predict(X_new_sc)
# print(class_names[y_pred][0])

from mlxtend.plotting import plot_decision_regions
value = 0
width = 3.5

ax = plot_decision_regions(X_test, np.array(y_test), clf=model, feature_index=[2, 3], 
                           filler_feature_values={0: value, 1: value},
                           filler_feature_ranges={0: width, 1: width},
                           legend=2)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, class_names, framealpha=0.5)

plt.title("MLP: Iris Prediction")
plt.xticks([])
plt.yticks([])
plt.xlabel('petal_length')
plt.ylabel('petal_width')
plt.scatter(X_new_sc[:,2], X_new_sc[:,3], marker='o', s=130, c='b')
plt.show()

