import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_matrix = np.loadtxt(open("seeds_dataset.csv", "rb"), delimiter = ",")
print(my_matrix)
print(my_matrix.shape)
one = []
two = []
three = []
for i in my_matrix:
    if int(i[7]) == 1:
        one.append(i)
    if int(i[7]) == 2:
        two.append(i)
    if int(i[7]) == 3:
        three.append(i)
'''
print(one)
print(two)
print(three)
'''
one_s = []
one_b = []
two_s = []
two_b = []
three_s = []
three_b = []
for i in one:
    one_s.append(i[0])
    one_b.append(i[5])
print(one_s)
print(one_b)
plt.scatter(one_s,one_b,color = 'red')
plt.show()
for i in two:
    two_s.append(i[0])
    two_b.append(i[5])
plt.scatter(two_s,two_b,color = 'black')
plt.show()
for i in three:
    three_s.append(i[0])
    three_b.append(i[5])
plt.scatter(three_s,three_b,color = 'green')
plt.show()
'''
plt.show()
plt.scatter(two[:,0],two[:,5])
#plt.scatter(my_matrix[:,0],my_matrix[:,5])
plt.show()
'''