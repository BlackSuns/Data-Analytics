import csv
import numpy as np
import math
#读取文件
f = open("维基百科数据.csv",'r')
csvreader = csv.reader(f)
new = list (csvreader)
news =  new [1:]#原列表保留
#print(news)
l = open("百度百科选手工作信息.csv",'r')
csvreader2 = csv.reader(l)
new2 = list (csvreader2)
news2 =  new2 [1:]#原列表保留
#print(news2)
#转换分数并相加
sums = []
qianli = []
tezhi = []
wutai = []
shenyue = []
for i in news:
    score = int(i[3]) + int(i[4]) + int(i[5]) + int(i[6]) + int(i[7])
    b=int(i[5])
    f=int(i[4])
    h=int(i[6])
    j=int(i[7])
    qianli.append(b)
    tezhi.append(f)
    wutai.append(h)
    shenyue.append(j)
    i.append(score)
    sums.append(i)
#print(sums)
a = sums
a = sorted(a,key = lambda x:x[8] , reverse=True)
print(a)
#替换括号和岁
replaces = []
for i in a:
    for b in i:
        b = str(b).replace("（","")
        b = str(b).replace("）","")
        b = str(b).replace("岁","")
        #print(b)
        replaces.append(b)
#print (replaces)
w = replaces
step = 9
new_n = [w[i:i + step]for i in range(0,len(w),step)]
print(new_n)
#根据岁数找到年龄
old = {}
for i in new_n:
    old [i[0]] = 2020 - int(i[2])
print(old)
#进行《维基百科数据》与《百度百科数据合并》百度百科选手工作信息.csv
#如果列表中姓名相等，则将news2添加到new_n
space= []

'''
    for i in new_n:
        for row in i:
            #print(row)
            if row in j:
                new_n.append(j)
                print(row)
'''
hebing = []
for i in news2:
    for j in i:
        a = j.split(" ")
    space.append(a)
print(space)
for i in space:
    for j in new_n:
        if j[0] == i[0]:
            i.remove(i[0])
            j = j + i
            hebing.append(j)
print(hebing)
'''b = hebing
for i in b:
b = sorted(b,key = lambda x:x[8] , reverse=True)
print(b)
'''
#hebing.sort(,reverse = True)
#使用ndarray统计演员和歌手的舞台表现和声乐表现均值 ，看演员和歌手是否哪个职业在个人选秀舞台上更有优势？？
qianlis = np.array(qianli)
tezhis = np.array(tezhi)
wutais = np.array(wutai)
shenyues = np.array(shenyue)
medians = np.median(qianli)
stds = np.std(qianlis)
corrcoefs = np.corrcoef(qianlis,tezhis)
averages = np.average(wutais)
averages_wu = np.average(shenyues)
#使用ndarray求解成团潜力的中位数和标准差
#使用ndarray计算个人特质和成团潜力的相关系数
print("成团潜力的中位数为：")
print(medians)
print("成团潜力的标准差为：")
print(stds)
print("个人特质和成团潜力的相关系数为：")
print(corrcoefs)
print("演员和歌手声乐平均分为：")
print(averages)
print("演员和歌手舞台平均分为：")
print(averages_wu)
if averages < averages_wu:
    print("演员和歌手在舞台表现上更占优势")
else:
    print("演员和歌手在声乐表现上更占优势")