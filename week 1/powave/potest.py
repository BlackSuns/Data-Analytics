'''
import csv
import numpy as np
import math
f = open("维基百科数据.csv",'r')
csvreader = csv.reader(f)
new = list (csvreader)
new =  new [1:]
print(new)
sums = []
for i in new:
    #score = int(i[3]) + int(i[4]) + int(i[5]) + int(i[6]) + int(i[7])
    score = int(i[3]) + int(i[4]) + int(i[5]) + int(i[6]) + int(i[7])
    i.append(score)
    sums.append(i)
print(sums)
'''
import csv
import numpy as np
import math

f = open("维基百科数据.csv", 'r')
csvreader = csv.reader(f)
new = list(csvreader)
new = new[1:]
print(new)
sums = []
for i in new:
    score = i[3] + i[4] + i[5] + i[6] + i[7]

    i.append(score)
    sums.append(i)
print(sums)