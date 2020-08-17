import pandas as pd
df=pd.read_excel('seeds_dataset (1).xlsx')
print(df.shape)
df
import matplotlib.pyplot as plt
import numpy as np
a=df['种子类别']==1
seed1=df.loc[a]
b=df['种子类别']==2
seed2=df.loc[b]
c=df['种子类别']==3
seed3=df.loc[c]
plt.plot(seed1['面积'],seed1['不对称系数'],'ro',seed2['面积'],seed2['不对称系数'],'yo',seed3['面积'],seed3['不对称系数'],'bo')
plt.hist(seed1['面积'],color='r',alpha=0.7)
plt.hist(seed2['面积'],color='y',alpha=0.7)
plt.hist(seed3['面积'],color='b',alpha=0.7)
plt.plot(seed1['核槽的长度'],'r',seed2['核槽的长度'],'y',seed3['核槽的长度'],'b')
plt.plot(seed1['核槽的长度'],'r')
plt.show()
plt.plot(seed2['核槽的长度'],'y')
plt.show()
plt.plot(seed3['核槽的长度'],'b')
plt.show()