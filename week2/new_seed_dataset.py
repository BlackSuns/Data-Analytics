import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#by xujintao
xu_data = pd.read_csv('seeds_dataset.csv',names = ['面积','周长','紧凑度', '籽粒长度','籽粒宽度','不对称系数','核槽的长度','种类'])
print(xu_data)
print(xu_data.shape)

is_seed_1 = xu_data ['种类'] == 1
#print(is_seed_1)
seed_1 = xu_data.loc[is_seed_1]
print(seed_1)
is_seed_2 = xu_data ['种类'] == 2
#print(is_seed_1)
seed_2 = xu_data.loc[is_seed_2]
print(seed_2)
is_seed_3 = xu_data ['种类'] == 3
#print(is_seed_1)
seed_3 = xu_data.loc[is_seed_3]
#print(seed_3)
plt.plot(seed_1['面积'],seed_1['不对称系数'],'bo',seed_2['面积'],seed_2['不对称系数'],'go',seed_3['面积'],seed_3['不对称系数'],'co',)
plt.show()

xmin = min (xu_data['面积'])#获取面积中最小值
xmax = max (xu_data['面积'])#获取面积中最大值
plt.subplot(321)#行数、列数和索引值
plt.hist(seed_1['面积'],color = 'r',alpha = 0.7)
plt.xlim(xmin,xmax)#设置x轴的数值显示范围。
plt.subplot(322)
plt.hist(seed_2['面积'],color = 'k',alpha = 0.7)
plt.xlim(xmin,xmax)
plt.subplot(323)
plt.hist(seed_3['面积'],color = 'c',alpha = 0.7)
plt.xlim(xmin,xmax)
plt.show()


xjt = np.arange(seed_1.shape[0])
print(xjt)
plt.plot(xjt,seed_1['核槽的长度'],'r')
plt.plot(xjt,seed_2['核槽的长度'],'k')
plt.plot(xjt,seed_3['核槽的长度'],'c')
plt.show()

plt.subplot(311)
plt.plot(xjt,seed_1['核槽的长度'],'r')
plt.subplot(312)
plt.plot(xjt,seed_2['核槽的长度'],'k')
plt.subplot(313)
plt.plot(xjt,seed_3['核槽的长度'],'c')
plt.show()


