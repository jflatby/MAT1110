import numpy as np

M = np.array([[1, 0, 1],
             [1, 1, 0],
             [0, 1, 1]])

x0 = np.array([[100],
               [0],
               [0]])

print np.linalg.matrix_power(M, 1000)