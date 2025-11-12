import matplotlib.pyplot as plt

wieght = [10, 30, 50, 70, 90]
price = [10, 20, 30, 40, 100]

plt.plot(wieght, price, 'o')
plt.xlabel('weight')
plt.ylabel('price')
plt.grid(True)

# plt.show()

from sklearn.linear_model import LinearRegression
X = [[10], [30], [50], [70], [90]]
Y = [10, 20, 30, 40, 100]

model = LinearRegression()
model.fit(X, Y)

predicted_price = model.predict([[60],[100], [120]])
print("Predicted prices for 60, 100, 120:", predicted_price)