import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import random
import math

housings = pd.read_csv("housing2.csv",low_memory=False)
#print(housings)
housings_2 = housings [1:]#去除第一天无用数据
#print(housings_2)
MEDV2 = housings_2['MEDV1']
print(MEDV2)
MEDV2 = MEDV2.reset_index(drop=True)
#MEDV2.index = range (0,len(MEDV2))#重建索引并合并数据
print(MEDV2)
housings['MEDV2'] = MEDV2
housings = housings.iloc[:-1]#删除多余的最后一行
print(housings)
housings['MEDV1'] = housings['MEDV1'].astype(float)#转换数据为float类型
housings['MEDV2'] = housings['MEDV2'].astype(float)
#rint(housings['MEDV1'].dtype)#转换数据格式
#2
np.random.seed(1)#seed( ) 用于指定随机数生成时所用算法开始的整数值，如果使用相同的seed( )值，则每次生成的随即数都相同
random.seed(1)
#随机重排housing数据
housings = housings.loc[np.random.permutation(housings.index)]
#对data数据进行随机重排之后将数据分为训练数据和测试数据，比例为7:3；
print(housings.shape[0])
hight_train_row = int (housings.shape[0]*.7)#shape函数的功能是读取矩阵的长度，比如shape[0]就是读取矩阵第一维度的长度,相当于行数。它的输入参数可以是一个整数表示维度，也可以是一个矩阵。
print(hight_train_row)
train = housings.loc[:hight_train_row,:]
test = housings.loc[hight_train_row:,:]
regressor = LinearRegression()
#predictor，变量需要一个dataframe而不能是一个series
predictors = train[['MEDV1']]
to_predictors = train ['MEDV2']
regressor.fit(predictors,to_predictors)
#根据模型生产预测值
MEDV2_predictor = regressor.predict(test[['MEDV1']])
print(MEDV2_predictor)
#均方差
mse = sum((MEDV2_predictor - test['MEDV2'])**2)/len(MEDV2_predictor)
print("均方差")
print(mse)
mae = sum(abs(MEDV2_predictor-test['MEDV2']))/len(predictors)
print("平均绝对误差")
print(mae)
plt.scatter(housings['MEDV1'],housings['MEDV2'])
plt.plot(test['MEDV1'],MEDV2_predictor)
plt.show()