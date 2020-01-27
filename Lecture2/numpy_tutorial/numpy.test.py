# numpy_test.py

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(type(a))
print(a.shape)
print(a)

# create arrays
b = np.zeros((2,2))
print(b)

c = np.eye(3)
print(c)

d = np.random.random((2,2))
print(d)