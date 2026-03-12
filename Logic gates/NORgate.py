import numpy as np
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt

X = [[0,0],
     [0,1],
     [1,0],
     [1,1]]

X_train = np.array(X)
y = [1,0,0,0]

hidden = 4
y_train = np.array(y)

model = MLPClassifier(hidden_layer_sizes=(hidden),random_state=1,verbose=True,max_iter=900)

model.fit(X_train,y_train)

print('Score:',model.score(X_train,y_train))
print('predicted',model.predict(X_train))
print('target: ',np.array(y_train))
print([coef.shape for coef in model.coefs_])

from mlxtend.plotting import plot_decision_regions
plt.figure(figsize=(4.5,3.5))
plot_decision_regions(X_train,np.array(y_train),clf = model,legend = 2)
plt.title('MLP: 2 Classes (hidden layer: {})'.format(2))

plt.xticks([])
plt.yticks([])
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()