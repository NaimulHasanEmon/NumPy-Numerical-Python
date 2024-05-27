import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1.0, 2.0, 3.0],[4.0, 5.0, 6.0]])
c = np.array([[[1,2],[3,4]],[[5,6], [7,8]]])

print(f'{a.size} * {a.itemsize} = {a.nbytes}')      # a.nbytes = a.size * a.itemsize
print(f'{b.size} * {b.itemsize} = {b.nbytes}')      # b.nbytes = b.size * b.itemsize
print(f'{c.size} * {c.itemsize} = {c.nbytes}')      # c.nbytes = c.size * c.itemsize
