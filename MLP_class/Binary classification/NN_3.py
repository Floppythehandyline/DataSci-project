from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

sc = StandardScaler()  #standardize the features
df = pd.read_csv('data.csv', names=['m','d','target']) #read data from csv file

X = df.drop('target', axis=1).values  #features
y = df.target

X_train = sc.fit_transform(X)  #fit and transform the features
y_train = y

hidden = 10 #number of neurons in the hidden layer
iter = 2000 #number of iterations
model = MLPClassifier(hidden_layer_sizes=(hidden,), max_iter=iter, random_state=1) #random_state กำหนดการสุ่มค่าเหมือนเดิมตลอด

model.fit(X_train, y_train)  #train the model
print("score: {:.4f}".format(model.score(X_train, y_train)))  #print the accuracy score of the model on training data
print("score:", round(model.score(X_train, y_train), 4))  #print the accuracy score of the model on training data
print("actual y: ", np.array(y))
print("predictedd:", model.predict(X_train))

#-------mlextend-------
from mlxtend.plotting import plot_decision_regions
plt.figure(figsize=(4.5,3.5))
plot_decision_regions(X_train, np.array(y_train), clf=model, legend=2)

plt.title("MLP: 2 Classes (hidden layer: {})".format(hidden))
plt.xticks([])
plt.yticks([])
plt.xlabel("m (gram)")
plt.ylabel("d (diameter)")
plt.show()

#---loss curve---
# plt.figure(figsize=(5,3))
# plt.title("Loss Curve")
# plt.xlabel("Iterations")
# plt.plot(model.loss_curve_)
# plt.show()
