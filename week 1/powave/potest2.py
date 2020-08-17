import csv
import numpy as np
import math
f = open("维基百科数据.csv",'r')
csvreader = csv.reader(f)
new = list (csvreader)
news =  new [1:]#原列表保留
print(news)
#转换分数并相加
sums = []
for i in news:
    score = int(i[3]) + int(i[4]) + int(i[5]) + int(i[6]) + int(i[7])
    i.append(score)
    sums.append(i)
print(sums)
a = sums
a = sorted(a,key = lambda x:x[8])
print(a)
#替换括号和岁
replaces = []
for i in a:
    for b in i:
        b = str(b).replace("（","")
        b = str(b).replace("）","")
        b = str(b).replace("岁","")
        print(b)
        replaces.append(b)
print (replaces)
w = replaces
step = 9
new_n = [w[i:i + step]for i in range(0,len(w),step)]
print(new_n)
#根据岁数找到年龄

#进行《维基百科数据》与《百度百科数据合并》百度百科选手工作信息.csv

#使用ndarray统计演员和歌手的舞台表现和声乐表现均值 ，看演员和歌手是否哪个职业在个人选秀舞台上更有优势？？

#使用ndarray求解成团潜力的中位数和标准差

#使用ndarray计算个人特质和成团潜力的相关系数