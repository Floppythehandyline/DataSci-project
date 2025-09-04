import numpy as np

oneD = np.array([2,3,5,7]) # 1 มิติ
twoD = np.array([[11,13,17],[19,23,29],[31,37,41]]) # 2 มิติ
treeD = np.array([[[43,47],[53,59]],[[61,67],[71,73]],[[79,83],[89,97]]]) # 3 มิติ
print(oneD.shape,twoD.shape,treeD.shape)