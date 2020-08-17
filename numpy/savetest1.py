import numpy as np
import csv
ten2 = []
matrix = np.array([
    [5,10,15],
    [20,25,30],
    [40,25,50]
])
#ten = (vector = 10)
ten2 = matrix [:,2] == 50 |30
print(matrix[ten2,:])