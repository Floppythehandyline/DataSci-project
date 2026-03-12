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

#print(df.sample(10, replace=True, random_state=1),'\n')  #print 4 random rows of the dataframe

df_sc = pd.DataFrame(X_train, columns=['d','m'])  #create a new dataframe with standardized features
df_sc['target'] = y_train  #add the target column to the new dataframe
#print(df_sc.sample(10, replace=True, random_state=1))  #print 4 random rows of the new dataframe

hidden = 100 #number of neurons in the hidden layer
model = MLPClassifier(random_state=1) #random_state กำหนดการสุ่มค่าเหมือนเดิมตลอด
model.fit(X_train, y_train)  #train the model

print("score: {:.4f}".format(model.score(X_train, y_train)))  #print the accuracy score of the model on training data
# print("score", model.score(X_test, y_test))  #print the accuracy score of the model on test data
print("actual y: ", np.array(y))
print("predicted: ", model.predict(X_train),2*"\n")

#-------using confusion matrix-------
from sklearn.metrics import classification_report, confusion_matrix
y_predict = model.predict(X_train)
print('Score -> {:.4f}'.format(model.score(X_train, y_train)))
#print(classification_report(y_train, y_predict))
print(confusion_matrix(y_train, y_predict),2*"\n")

#-------mlextend-------
from mlxtend.plotting import plot_decision_regions
# plt.figure(figsize=(4.5,3.5))
# plot_decision_regions(X_train, np.array(y_train), clf=model, legend=2)

# plt.title("MLP: 2 Classes (hidden layer: {})".format(hidden))
# plt.xticks([])
# plt.yticks([])
# plt.xlabel("m (gram)")
# plt.ylabel("d (diameter)")
# plt.show()
#---loss curve---
plt.figure(figsize=(5,3))
plt.title("Loss Curve")
plt.xlabel("Iterations")
plt.plot(model.loss_curve_)
plt.show()