import numpy as np
import csv
f1=open("维基百科数据.csv",'r')
csvreader=csv.reader(f1)
nf1=list(csvreader)
f2=open("百度百科选手工作信息.csv",'r')
csvreader=csv.reader(f2)
nf2=list(csvreader)
nf1=nf1[1:]
nf2=nf2[1:]
print(nf2)
xy={}
qianli=[]
tezhi=[]
wutai=[]
shenyue=[]
for row in nf1:
    xy[row[0]]=int(row[4])+int(row[5])+int(row[6])+int(row[7])
    b=int(row[5])
    f=int(row[4])
    h=int(row[6])
    j=int(row[7])
    qianli.append(b)
    tezhi.append(f)
    wutai.append(h)
    shenyue.append(j)
print(xy)
p=np.array(qianli)
e=np.array(tezhi)
k=np.array(wutai)
i=np.array(shenyue)
cjpm=sorted(xy.items(),key=lambda x:x[1],reverse=False)
print(cjpm)
for row in nf1:
    row[2]=row[2].replace("（","")
    row[2]=row[2].replace("）","")
    row[2]=row[2].replace("岁","")
print(nf1)





c=np.median(p)
d=np.std(p)
g=np.corrcoef(p,e)
n=np.average(k)
m=np.average(i)
print("成团潜力的中位数为：")
print(c)
print("成团潜力的标准差为：")
print(d)
print("个人特质和成团潜力的相关系数为：")
print(g)
print("演员和歌手声乐平均分为：")
print(m)
print("演员和歌手舞台平均分为：")
print(n)
if m < n:
    print("演员和歌手在舞台表现上更占优势")
else:
    print("演员和歌手在声乐表现上更占优势")