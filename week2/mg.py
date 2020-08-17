import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#by magege
ma_data = pd.read_csv('seeds_dataset.csv',names = ['面积','周长','紧凑度', '籽粒长度','籽粒宽度','不对称系数','核槽的长度','种类'])
print(ma_data)
print(ma_data.shape)

is_seed_1 = ma_data ['种类'] == 1
#print(is_seed_1)
seed_1 = ma_data.loc[is_seed_1]
print(seed_1)
is_seed_2 = ma_data ['种类'] == 2
#print(is_seed_1)
seed_2 = ma_data.loc[is_seed_2]
print(seed_2)
is_seed_3 = ma_data ['种类'] == 3
#print(is_seed_1)
seed_3 = ma_data.loc[is_seed_3]
#print(seed_3)
plt.plot(seed_1['面积'],seed_1['不对称系数'],'bo',seed_2['面积'],seed_2['不对称系数'],'go',seed_3['面积'],seed_3['不对称系数'],'co',)
plt.show()

xmin = min (ma_data['面积'])#获取面积中最小值
xmax = max (ma_data['面积'])#获取面积中最大值
plt.subplot(311)
plt.hist(seed_1['面积'],color = 'pink',alpha = 0.7)
plt.xlim(xmin,xmax)#设置x轴的数值显示范围。
plt.subplot(312)
plt.hist(seed_2['面积'],color = 'm',alpha = 0.7)
plt.xlim(xmin,xmax)
plt.subplot(313)
plt.hist(seed_3['面积'],color = 'c',alpha = 0.7)
plt.xlim(xmin,xmax)
plt.show()


mg = np.arange(seed_1.shape[0])
print(mg)
plt.plot(mg,seed_1['核槽的长度'],'pink')
plt.plot(mg,seed_2['核槽的长度'],'m')
plt.plot(mg,seed_3['核槽的长度'],'c')
plt.show()

plt.subplot(311)
plt.plot(mg,seed_1['核槽的长度'],'pink')
plt.subplot(312)
plt.plot(mg,seed_2['核槽的长度'],'m')
plt.subplot(313)
plt.plot(mg,seed_3['核槽的长度'],'c')
plt.show()


