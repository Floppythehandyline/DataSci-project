import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  #standardize the features
df = pd.read_csv('data.csv', names=['m','d','target']) #read data from csv file

#------ graphical representation of data ------
print(df.head(2),'\n')  #print first 2 rows of the dataframe
print(df.sample(4, replace=True, random_state=1),'\n')  #print 4 random rows of the dataframe

print(df.target.unique()) #unique target values
np.array([0, 1], dtype=np.int64)

sns.scatterplot(x='m',y='d',data=df,hue='target',style='target',s=100) #scatter plot of data points
plt.show()  #display the plot
