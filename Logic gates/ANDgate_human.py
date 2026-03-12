import numpy as np # type: ignore

X = np.array([[0, 0, 1, 1],[0, 1, 0, 1]])
Y = np.array([[0, 0, 0, 1]])
W1 = 0.5
W2 = 0.5
W0 = -0.5
sum = X[0]*W1 + X[1]*W2 + W0

def binary_step_function(sum):
    return np.where(sum > 0, 1, 0)

def model(x):
    pre = binary_step_function(x)
    return pre

predict = model(sum)
print("Out label: ", Y)
print("Out predict model: ", predict)
