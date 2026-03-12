from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv('fruit3class.csv', names=['m','d','target'])
# print(df.sample(6, replace=True, random_state=1),'\n')  #print 6 random rows of the dataframe
# print("Unique target values:", df.target.unique())

X = df.drop("target", axis=1).values
y = df.target
sc = StandardScaler()
X_train = sc.fit_transform(X)
y_train = y
# df_sc = pd.DataFrame(X_train, columns=['d','m'])
# df_sc['target'] = y_train
# print(df_sc.head(8))
# print(df_sc.sample(6, replace=True, random_state=1))

# sns.scatterplot(x='m',y='d',data=df ,hue='target',style='target', s=140)
# plt.show()

#-----usinge MLPClassifier-----
hidden = 30
iter = 2500
model = MLPClassifier(hidden_layer_sizes=(hidden,), max_iter=iter, random_state=1)
model.fit(X_train, y_train)
print('score: {:.4f}'.format(model.score(X_train, y_train)))
print('score:', round(model.score(X_train, y_train), 4))
print('actual y:', np.array(y))
print('predicted:', model.predict(X_train))

plt.figure(figsize=(5,3))

from mlxtend.plotting import plot_decision_regions
plot_decision_regions(X_train, np.array(y_train), clf=model, legend=2)
plt.title('MLP: 3 Classes (hidden: {}, iter: {})'.format(hidden, iter))
plt.xticks([])
plt.yticks([])
plt.xlabel('m (gram)')
plt.ylabel('d (diameter)')
plt.show()

plt.title('Loss curve')
plt.xlabel('Iterations')
plt.plot(model.loss_curve_)
plt.tight_layout()
plt.show()
print([coef.shape for coef in model.coefs_])
