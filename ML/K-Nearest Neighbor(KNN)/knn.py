import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

dataf = pd.read_csv('knn.csv')
print(dataf)

features = dataf[['height', 'weight']]
label = dataf['gender']

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(features, label)
pred = knn.predict([[190, 70], [170, 65], [600, 10]])
print(pred)
