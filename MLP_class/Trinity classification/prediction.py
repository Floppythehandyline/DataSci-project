from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

sc = StandardScaler()  #standardize the features
df = pd.read_csv('fruit3class.csv', names=['m','d','target']) #read data from csv file

X = df.drop('target', axis=1).values  #features
y = df.target

X_train = sc.fit_transform(X)  #fit and transform the features
y_train = y

hidden = 10 #number of neurons in the hidden layer
iter = 2000 #number of iterations
model = MLPClassifier(hidden_layer_sizes=(hidden,), max_iter=iter, random_state=1) #random_state กำหนดการสุ่มค่าเหมือนเดิมตลอด

model.fit(X_train, y_train)  #train the model

# X_new = [8.4, 5] #predict ข้อมูล 1 ตัว
X_new = [[8.4, 5.2],
         [6.8,4.2]]
X_new_sc = sc.transform(X_new) #standardize the new data
print(X_new_sc)
print(model.predict(X_new_sc))

from mlxtend.plotting import plot_decision_regions
plt.figure(figsize=(4.5,3.5))
plot_decision_regions(X_train, np.array(y_train), clf=model, legend=2)
plt.title("MLP: prediction)")
plt.xticks([])
plt.yticks([])
plt.xlabel("m (gram)")
plt.ylabel("d (diameter)")

#พล็อตจุดใหม่ที่เราต้องการทำนาย
plt.scatter(X_new_sc[:,0], X_new_sc[:,1], marker='o', s=120, c='r')
plt.show()