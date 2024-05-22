import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1.0, 2.0, 3.0],[4.0, 5.0, 6.0]])

print(a.nbytes)      # a.nbytes = a.size * a.itemsize
print(b.nbytes)      # b.nbytes = b.size * b.itemsize
